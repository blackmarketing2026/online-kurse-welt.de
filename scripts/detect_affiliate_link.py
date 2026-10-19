"""Recognize a standalone, user-supplied affiliate URL without changing it."""

import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote_plus, urlsplit


AFFILIATE_ID = "mysticmarketing"
AFFILIATE_KEYS = {"aff", "affiliate"}
MARKDOWN_LINK = re.compile(r"\[(https://[^\s\]]+)\]\((https://[^\s)]+)\)\Z")


def valid_https_url(url):
    if not url or any(char.isspace() or ord(char) < 32 for char in url):
        return False
    if re.search(r"%(?![0-9A-Fa-f]{2})", url) or any(char in url for char in '<>"\\'):
        return False
    try:
        parts = urlsplit(url)
        return (
            parts.scheme == "https"
            and bool(parts.netloc and parts.hostname)
            and parts.username is None
            and parts.password is None
            and parts.port != 0
        )
    except ValueError:
        return False


def standalone_url(message):
    """Accept one bare URL or a Markdown link with identical label and target."""
    value = message.strip()
    match = MARKDOWN_LINK.fullmatch(value)
    if match:
        if match.group(1) != match.group(2):
            return None
        value = match.group(2)
    if not valid_https_url(value):
        return None
    return value


def strip_affiliate_parameters(url):
    """Return the product URL only for an unambiguous matching affiliate ID."""
    before_fragment, fragment_mark, fragment = url.partition("#")
    base, query_mark, query = before_fragment.partition("?")
    matched = False
    conflict = False

    def filter_parts(raw):
        nonlocal matched, conflict
        kept = []
        for part in raw.split("&"):
            name, separator, value = part.partition("=")
            if separator and name.lower() in AFFILIATE_KEYS:
                if unquote_plus(value) == AFFILIATE_ID:
                    matched = True
                    continue
                conflict = True
            kept.append(part)
        return "&".join(kept)

    clean_query = filter_parts(query) if query_mark else ""
    clean_fragment = filter_parts(fragment) if fragment_mark else ""
    if not matched or conflict:
        return None
    product_url = base
    if query_mark and clean_query:
        product_url += "?" + clean_query
    if fragment_mark and clean_fragment:
        product_url += "#" + clean_fragment
    return product_url if valid_https_url(product_url) else None


def detect_standalone_affiliate_link(message):
    """Return URLs for a link-only message; otherwise return None."""
    affiliate_url = standalone_url(message)
    if affiliate_url is None:
        return None
    product_url = strip_affiliate_parameters(affiliate_url)
    if product_url is None:
        return None
    return {"affiliate_url": affiliate_url, "product_url": product_url}


def self_test():
    positive = {
        "https://umfragen-system.de/komplettpaket-start-2/#aff=mysticmarketing":
            "https://umfragen-system.de/komplettpaket-start-2/",
        "https://example.de/kurs?aff=mysticmarketing&cam=oktober#details":
            "https://example.de/kurs?cam=oktober#details",
        "https://example.de/kurs?x=1&affiliate=mysticmarketing&x=2":
            "https://example.de/kurs?x=1&x=2",
        "https://example.de/kurs#kapitel&aff=mysticmarketing&cam=1":
            "https://example.de/kurs#kapitel&cam=1",
        "[https://example.de/kurs#aff=mysticmarketing](https://example.de/kurs#aff=mysticmarketing)":
            "https://example.de/kurs",
    }
    negative = [
        "https://example.de/kurs?aff=fremde-id",
        "https://example.de/kurs?aff=mysticmarketing2",
        "https://example.de/kurs?ref=aff=mysticmarketing",
        "https://example.de/kurs?aff=mysticmarketing&affiliate=fremde-id",
        "https://example.de/mysticmarketing/kurs",
        "http://example.de/kurs#aff=mysticmarketing",
        "Bitte nur analysieren: https://example.de/kurs#aff=mysticmarketing",
        "Beispiel: https://example.de/kurs#aff=mysticmarketing",
        "`https://example.de/kurs#aff=mysticmarketing`",
        "> https://example.de/kurs#aff=mysticmarketing",
        "[Beispiel](https://example.de/kurs#aff=mysticmarketing)",
        "https://example.de/kurs#aff=mysticmarketing\nhttps://example.de/zweiter-kurs#aff=mysticmarketing",
    ]
    for message, product_url in positive.items():
        result = detect_standalone_affiliate_link(message)
        assert result is not None, message
        expected_affiliate = standalone_url(message)
        assert result == {"affiliate_url": expected_affiliate, "product_url": product_url}, message
    for message in negative:
        assert detect_standalone_affiliate_link(message) is None, message
    print(f"OK: {len(positive)} positive und {len(negative)} negative Erkennungsfälle.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="Erkennungsregeln ohne Veröffentlichung testen")
    parser.add_argument("--message-file", type=Path, help="UTF-8-Datei mit genau einer Nutzernachricht")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if args.message_file:
        result = detect_standalone_affiliate_link(args.message_file.read_text(encoding="utf-8-sig"))
        print(json.dumps(result, ensure_ascii=False))
        return
    parser.error("--self-test oder --message-file angeben")


if __name__ == "__main__":
    main()
