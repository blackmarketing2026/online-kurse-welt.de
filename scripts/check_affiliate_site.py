"""Dependency-free pre-publication checks for a static affiliate product page."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlparse, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "www.online-kurse-welt.de"


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.headings = []
        self.title = ""
        self.description = ""
        self.canonical = ""
        self.links = []
        self.assets = []
        self.html_lang = ""
        self._capture = None

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if tag == "html":
            self.html_lang = attr.get("lang", "")
        if tag in ("title", "h1"):
            self._capture = tag
            if tag == "h1":
                self.headings.append("")
        if tag == "meta" and attr.get("name", "").lower() == "description":
            self.description = attr.get("content", "")
        if tag == "link" and attr.get("rel") == "canonical":
            self.canonical = attr.get("href", "")
        if tag == "a":
            self.links.append(attr)
        if tag in ("script", "img") and attr.get("src"):
            self.assets.append(attr["src"])
        if tag == "link" and attr.get("rel") in ("stylesheet", "icon") and attr.get("href"):
            self.assets.append(attr["href"])

    def handle_endtag(self, tag):
        if tag == self._capture:
            self._capture = None

    def handle_data(self, data):
        if self._capture == "title":
            self.title += data
        elif self._capture == "h1":
            self.headings[-1] += data


def local_target(url):
    parsed = urlparse(url)
    if parsed.scheme or parsed.netloc or url.startswith(("mailto:", "tel:", "#")):
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    relative = path.lstrip("/")
    target = ROOT / relative if relative else ROOT / "index.html"
    if path.endswith("/") and relative:
        target /= "index.html"
    elif not target.suffix:
        target = target.with_suffix(".html")
    target = target.resolve()
    if not target.is_relative_to(ROOT):
        return False
    return target


def parse_page(path):
    page = Page()
    page.feed(path.read_text(encoding="utf-8"))
    return page


def valid_https_url(url):
    """Check syntax without normalizing the user-provided URL."""
    if not url or any(char.isspace() or ord(char) < 32 for char in url):
        return False
    if re.search(r"%(?![0-9A-Fa-f]{2})", url) or any(char in url for char in '<>"\\'):
        return False
    try:
        parsed = urlsplit(url)
        return (
            parsed.scheme == "https"
            and bool(parsed.netloc and parsed.hostname)
            and parsed.username is None
            and parsed.password is None
            and parsed.port != 0
        )
    except ValueError:
        return False


def check(page_file, affiliate_link, product_url=None):
    errors = []
    if not page_file.is_file() or page_file.suffix != ".html" or page_file.parent != ROOT:
        return ["Produktseite muss eine vorhandene HTML-Datei im Projektwurzelverzeichnis sein."]
    if not valid_https_url(affiliate_link):
        errors.append("Affiliate-Link ist keine gültige HTTPS-URL.")
    if product_url is not None and not valid_https_url(product_url):
        errors.append("Produkt-URL ist keine gültige HTTPS-URL.")

    slug = page_file.stem
    clean_url = f"https://{DOMAIN}/{slug}"
    product = parse_page(page_file)
    home = parse_page(ROOT / "index.html")
    source = page_file.read_text(encoding="utf-8")

    if product.html_lang != "de":
        errors.append("HTML-Sprachattribut lang=de fehlt.")
    if not product.title.strip():
        errors.append("SEO-Titel fehlt.")
    if not product.description.strip():
        errors.append("Meta-Description fehlt.")
    if len(product.headings) != 1 or not product.headings[0].strip():
        errors.append("Genau eine nichtleere H1 ist erforderlich.")
    if product.canonical != clean_url:
        errors.append(f"Canonical muss {clean_url} sein.")
    if "Werbung" not in source and "Anzeige" not in source:
        errors.append("Sichtbare Werbekennzeichnung fehlt.")
    for required in ("/impressum", "/datenschutz"):
        if not any(a.get("href") == required for a in product.links):
            errors.append(f"Footer-Link {required} fehlt.")
    if "data-cookie-settings" not in source:
        errors.append("Cookie-Einstellungen fehlen.")

    affiliates = [a for a in product.links if a.get("href") == affiliate_link]
    if not affiliates:
        errors.append("Der exakte Affiliate-Link ist nicht eingebaut.")
    for a in affiliates:
        if "sponsored" not in a.get("rel", "").split():
            errors.append("Affiliate-Link ohne rel=sponsored.")
        if not any(label in a.get("aria-label", "").lower() for label in ("werbung", "anzeige")):
            errors.append("Affiliate-Link ohne Werbekennzeichnung im zugänglichen Linknamen.")
        if a.get("target") == "_blank" and "noopener" not in a.get("rel", "").split():
            errors.append("Affiliate-Link mit target=_blank ohne rel=noopener.")
    for a in product.links:
        if "sponsored" in a.get("rel", "").split() and a.get("href") != affiliate_link:
            errors.append(f"Anderer Partnerlink als der freigegebene Link: {a.get('href', '')}")

    if not any(a.get("href") == f"/{slug}" for a in home.links):
        errors.append("Interner Produktlink auf der Startseite fehlt.")
    if not any(a.get("href") == "/" for a in product.links):
        errors.append("Rücklink zur Startseite fehlt.")
    for name, parsed in ((page_file.name, product), ("index.html", home)):
        for url in [a.get("href", "") for a in parsed.links] + parsed.assets:
            target = local_target(url)
            if target is False or (target is not None and not target.is_file()):
                errors.append(f"Defekter lokaler Link/Asset in {name}: {url}")
            if url.startswith("/") and urlparse(url).path.endswith(".html"):
                errors.append(f"Öffentliche URL mit .html in {name}: {url}")

    try:
        sitemap = ET.parse(ROOT / "sitemap.xml")
        locations = [node.text for node in sitemap.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        if locations.count(clean_url) != 1:
            errors.append("Produkt-URL muss genau einmal in sitemap.xml stehen.")
        if len(locations) != len(set(locations)):
            errors.append("Sitemap enthält doppelte URLs.")
        if any(urlparse(url or "").path.endswith(".html") for url in locations):
            errors.append("Sitemap enthält eine .html-URL.")
    except (OSError, ET.ParseError) as exc:
        errors.append(f"Sitemap nicht lesbar: {exc}")

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page", required=True, help="Dateiname der Produktseite, z. B. funnel-cockpit.html")
    parser.add_argument("--affiliate-link", required=True, help="Exakter Affiliate-Link des Auftrags")
    parser.add_argument("--product-url", help="Optionale Produkt-URL für die Syntaxprüfung")
    args = parser.parse_args()
    page_file = (ROOT / args.page).resolve()
    errors = check(page_file, args.affiliate_link, args.product_url)
    if errors:
        for error in errors:
            print(f"FEHLER: {error}")
        raise SystemExit(1)
    print(f"OK: {page_file.name}, interne Links/Assets, Affiliate-Link, SEO und Sitemap geprüft.")


if __name__ == "__main__":
    main()
