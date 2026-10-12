"""Generate the four verified static product pages and their research briefs."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
TODAY = "12.10.2026"

PRODUCTS = [
    {
        "slug": "digitales-produkt-in-fuenf-tagen",
        "name": "Five-day digital product launch challenge",
        "title": "Digitales Produkt in fünf Tagen starten: Was die Challenge bietet",
        "description": "Die Five-day digital product launch challenge im Überblick: fünf Schritte, Grenzen und Fragen vor dem Kauf. Anbieterangaben geprüft am 12.10.2026.",
        "category": "Business & Marketing",
        "keyword": "digitales Produkt in fünf Tagen starten",
        "link": "https://fivedaylaunch-j2m.plannerpack.fun/#aff=mysticmarketing",
        "source": "https://fivedaylaunch-j2m.plannerpack.fun/",
        "image": "",
        "alt": "",
        "intro": "Die englischsprachige Challenge gliedert den Start eines kleinen digitalen Produkts in fünf Tagesaufgaben. Sie richtet sich an Menschen, die eine erste Idee in ein konkretes Angebot und einen einfachen Verkaufsstart übersetzen möchten.",
        "facts": [
            "Tag 1: ein konkretes Problem und eine Zielgruppe eingrenzen.",
            "Tag 2: eine kleine, schnell nutzbare Lösung ausarbeiten.",
            "Tag 3: Nutzen und Angebot verständlich formulieren.",
            "Tag 4: mit möglichen Interessenten ins Gespräch kommen.",
            "Tag 5: das Angebot veröffentlichen und erste Reaktionen sammeln.",
        ],
        "fit": "Passend, wenn du bereits ein Thema oder eine grobe Produktidee hast und eine kurze Arbeitsstruktur suchst. Für eine umfassende technische Ausbildung zu Shop, Zahlungsabwicklung oder rechtlichen Pflichten ist die Challenge nach der sichtbaren Beschreibung nicht ausgelegt.",
        "decision": "Schreibe vor dem Start einen Satz auf: Für wen löst mein Produkt welches Problem? Wenn du das nicht beantworten kannst, nutze die ersten beiden Tage zur Recherche statt sofort zur Produktion. Prüfe außerdem, welches Dateiformat du am Ende anbieten willst und wie du Rückmeldungen einsammelst.",
        "limits": "Die Verkaufsseite nennt an verschiedenen Stellen abweichende Preisangaben. Ein verbindlicher Endpreis lässt sich daraus nicht ableiten; prüfe ihn im Bestellschritt. Kurszugang, Support und konkrete Rückgabebedingungen sind auf der sichtbaren Seite nicht ausreichend klar. Wir haben die Challenge nicht selbst absolviert.",
        "faq": [
            ("Ist die Challenge auf Deutsch?", "Die eingesehene Angebotsseite ist auf Englisch. Eine deutsche Produktfassung ist dort nicht belegt."),
            ("Brauche ich schon ein fertiges Produkt?", "Laut Anbieter führt der Ablauf von der Idee über eine kleine Lösung bis zum Start. Eine erste Themenidee ist trotzdem hilfreich."),
            ("Garantiert der Fünf-Tage-Plan Verkäufe?", "Nein. Der Plan strukturiert Aufgaben; ob ein Angebot Nachfrage findet, hängt unter anderem von Zielgruppe, Produkt und Reichweite ab."),
        ],
        "related": ("nupem-money-reset.html", "Money Reset Program"),
        "price": "Angebotsseite mit widersprüchlichen Preisangaben; Endpreis vor Kauf prüfen",
        "audience": "Einsteigerinnen und Einsteiger mit einer ersten Idee für ein digitales Produkt",
        "search": "digitales Produkt starten; Fünf-Tage-Challenge; erstes digitales Produkt erstellen; digitales Angebot verkaufen",
        "image_note": "Die Angebotsseite zeigt ein Bild mit der Aufschrift „PUT YOUR IMAGE HERE“. Das ist ein Platzhalter und wird bewusst nicht übernommen.",
        "serp": [
            ("Udemy: 5-day digital product guide", "https://www.udemy.com/frontends-course-landing-page/en/course/2026-ai-digital-product-guide-from-0-to-profit-in-5-days/"),
            ("Create and Launch Challenge", "https://www.createandlaunchchallenge.com/"),
            ("5-Tage-Miniprodukt-Challenge", "https://sarahgernhoefer.de/5-tage-miniprodukt-challenge-original/"),
        ],
        "resources": [],
    },
    {
        "slug": "nupem-money-reset",
        "name": "Nupem.finance Money Reset Program",
        "title": "Nupem.finance Money Reset Program: Inhalt und Kauf-Check",
        "description": "Was das Money Reset Program laut Anbieter enthält, für wen es gedacht ist und welche Fragen vor dem Kauf offenbleiben. Stand 12.10.2026.",
        "category": "Persönliche Finanzen",
        "keyword": "Nupem.finance Money Reset Program",
        "link": "https://nupemfinancemoney-fj3.plannerpack.co/#aff=mysticmarketing",
        "source": "https://nupemfinancemoney-fj3.plannerpack.co/",
        "image": "assets/products/nupem-money-reset.webp",
        "alt": "Produktcover The Personal Finance Reset von Nupem",
        "intro": "Das englischsprachige, selbstgesteuerte Programm will helfen, Ausgabenmuster zu erkennen, ein ruhigeres Budget aufzubauen und kleine Finanzroutinen festzulegen. Die Angebotsseite beschreibt Reflexionsfragen und praktische Schritte; ein persönlicher Beratungstermin ist dort nicht belegt.",
        "facts": [
            "Ausgaben und wiederkehrende Kosten anhand eigener Unterlagen betrachten.",
            "Mögliche Geldlecks identifizieren und Prioritäten für ein Budget setzen.",
            "Mit kleinen wiederholbaren Schritten eine Budgetroutine aufbauen.",
            "Laut Anbieter erfolgt der digitale Zugang nach dem Bestellschritt.",
        ],
        "fit": "Sinnvoll kann es für Menschen sein, die ihre privaten Einnahmen und Ausgaben selbst ordnen möchten und englische Arbeitsmaterialien nutzen. Wer individuelle Schuldner-, Steuer- oder Anlageberatung braucht, sollte eine dafür qualifizierte Beratungsstelle wählen.",
        "decision": "Prüfe zuerst, ob du bereits eine Übersicht über Einnahmen, feste Kosten und variable Ausgaben hast. Lege ein realistisches Monatsbudget fest, ohne sensible Kontodaten auf unbekannte Seiten hochzuladen. Vergleiche den verlangten Preis mit kostenlosen Haushaltsbuch-Vorlagen und unabhängiger Beratung.",
        "limits": "Die Angebotsseite zeigt widersprüchliche Beträge; der in der Produktliste genannte Europreis ist dort nicht verifizierbar. Der genaue Umfang, Support und Aktualisierungsrhythmus sind nicht eindeutig dokumentiert. Wir haben das Programm nicht gekauft oder getestet. Diese Seite ersetzt keine Finanzberatung.",
        "faq": [
            ("Muss ich Kontoauszüge hochladen?", "Die sichtbare Angebotsseite belegt keine Pflicht zum Upload. Kläre vor dem Kauf, welche Daten du tatsächlich eingeben oder teilen sollst."),
            ("Ist das Programm eine individuelle Finanzberatung?", "Die Angebotsseite beschreibt ein selbstgesteuertes Programm, keine persönliche Beratung."),
            ("Wie hoch ist der Preis?", "Die sichtbaren Preisfelder widersprechen einander. Maßgeblich ist der Endbetrag im Bestellschritt; prüfe ihn vor Zahlung."),
        ],
        "related": ("digitales-produkt-in-fuenf-tagen.html", "Fünf-Tage-Challenge"),
        "price": "widersprüchliche Angaben auf der Angebotsseite; Endbetrag prüfen",
        "audience": "Menschen, die ihr privates Budget selbst strukturieren wollen",
        "search": "Budget ordnen; Ausgabenmuster erkennen; Money Reset Program Erfahrungen; Haushaltsbudget planen",
        "image_note": "Cover von der Angebotsseite lokal als WebP gespeichert. Das Motiv nennt „The Personal Finance Reset“; die Verbindung zum Programm ergibt sich aus der Einbettung auf dessen Verkaufsseite. Eigenständige Nutzungsrechte wurden nicht bestätigt.",
        "serp": [
            ("Verbraucherzentrale: Haushaltsbuch führen", "https://www.verbraucherzentrale.de/wissen/geld-versicherungen/sparen-und-anlegen/haushaltsbuch-fuehren-ueberblick-ueber-ihre-finanzen-52179"),
            ("Verbraucherzentrale: Das Haushaltsbuch", "https://www.verbraucherzentrale.de/buecher-und-ebooks/haushaltsbuch"),
            ("Verbraucherzentrale: Budgetplaner", "https://www.verbraucherzentrale.de/baustein-3-was-kostet-das-leben-31784"),
        ],
        "resources": [("Kostenlose Anleitung zum Haushaltsbuch bei der Verbraucherzentrale", "https://www.verbraucherzentrale.de/wissen/geld-versicherungen/sparen-und-anlegen/haushaltsbuch-fuehren-ueberblick-ueber-ihre-finanzen-52179")],
    },
    {
        "slug": "teneriffa-wandern-mit-kindern",
        "name": "Wandern auf Teneriffa mit Kindern für Anfänger",
        "title": "Teneriffa mit Kindern wandern: Was der digitale Guide enthält",
        "description": "Der Familien-Wanderführer für Teneriffa: 80 angekündigte Wanderideen, Planungskriterien und wichtige Grenzen vor dem Kauf. Stand 12.10.2026.",
        "category": "Reisen & Familie",
        "keyword": "Teneriffa wandern mit Kindern",
        "link": "https://www.checkout-ds24.com/redir/743903/mysticmarketing/okw-teneriffa-wandern",
        "source": "https://www.checkout-ds24.com/product/743903",
        "image": "assets/products/teneriffa-wandern-kinder.webp",
        "alt": "Cover des digitalen Wanderführers Wandern auf Teneriffa mit Kindern für Anfänger",
        "intro": "Der deutschsprachige digitale Wanderführer kündigt 80 Wanderideen für Familien an. Die Verkaufsseite nennt Waldwege, Küstenpfade und Vulkanlandschaften sowie Hinweise zu Ausrüstung, Pausen und Wetter. Die einzelnen Routen konnten wir ohne Kauf nicht prüfen.",
        "facts": [
            "Laut Anbieter 80 Wanderideen für Familien auf Teneriffa.",
            "Themen: Küstenwege, Wälder, Vulkanlandschaften und Aussichtspunkte.",
            "Hinweise zur Auswahl passender Strecken sowie zu Wasser, Sonnenschutz und Wetter.",
            "Digitaler Download; kein physischer Versand.",
        ],
        "fit": "Geeignet als Ideensammlung für Eltern, die ihre Ausflüge selbst planen. Eine Route ist erst dann familiengeeignet, wenn Länge, Höhenmeter, Untergrund, Wetter und Tagesform zum jüngsten Kind passen. Für verbindliche aktuelle Wegdaten brauchst du zusätzlich offizielle lokale Informationen.",
        "decision": "Prüfe jede geplante Strecke kurz vor dem Start: Wegsperrungen, Wetterwarnungen, Höhenlage, Schatten und Rückweg. Plane ausreichend Wasser, Sonnenschutz und eine Abbruchmöglichkeit ein. Ein Guide kann die aktuelle Prüfung vor Ort nicht ersetzen.",
        "limits": "Die 80 Routen und ihre Eignung wurden von uns nicht einzeln geprüft. Die Bestellseite nennt 12,99 € Produktpreis zuzüglich 19 % MwSt. und zeigt 15,46 € als Gesamtbetrag (Stand 12.10.2026); der angezeigte Endbetrag im Checkout ist maßgeblich. Angaben zu Updates und konkreten Dateiformaten bleiben offen.",
        "faq": [
            ("Sind alle 80 Touren für jedes Alter geeignet?", "Das lässt sich aus der Verkaufsseite nicht ableiten. Wähle jede Tour nach Kondition, Wegbeschaffenheit und aktuellem Wetter aus."),
            ("Bekomme ich ein gedrucktes Buch?", "Die Bestellseite beschreibt einen digitalen Download und keinen Versand."),
            ("Reicht der Guide für die Sicherheit unterwegs?", "Nein. Aktuelle Sperrungen, Warnungen und örtliche Regeln solltest du zusätzlich vor jeder Tour prüfen."),
        ],
        "related": ("bali-reisefuehrer.html", "Bali-Reiseführer"),
        "price": "12,99 € Produktpreis; Checkout zeigt 15,46 € inkl. 19 % MwSt. (12.10.2026)",
        "audience": "Familien mit Kindern und wenig Wandererfahrung auf Teneriffa",
        "search": "Teneriffa Familienwanderungen; Kinderwanderungen Teneriffa; Teneriffa Wanderführer E-Book; Wandern mit Kindern Sicherheit",
        "image_note": "Produktcover aus der Digistore24-Bestellseite lokal als WebP gespeichert; eigenständige Nutzungsrechte wurden nicht bestätigt.",
        "serp": [
            ("Tenerife Tourism: Wanderwege", "https://www.webtenerife.de/aktivitaten/natur/wandern/wanderwege/?tab=1"),
            ("Tenerife ON: FAQ und Wegsperrungen", "https://www.tenerifeon.es/faq"),
            ("Tenerife Tourism: Wandern", "https://www.webtenerife.de/aktivitaten/natur/vulkane/legendare-vulkane/erleben-und-sehen/senderismo-caminatas/"),
        ],
        "resources": [("Offizielle Wanderwege nach Schwierigkeit und Dauer", "https://www.webtenerife.de/aktivitaten/natur/wandern/wanderwege/?tab=1"), ("Tenerife ON: aktuelle Wegwarnungen", "https://www.tenerifeon.es/faq")],
    },
    {
        "slug": "bali-reisefuehrer",
        "name": "Bali Reiseführer",
        "title": "Bali Reiseführer von Indojunkie: Umfang und Planungshilfe",
        "description": "Was der digitale Bali-Reiseführer laut Verkaufsseite enthält: 122 Tipps, 12 Kapitel und Fragen zur Aktualität. Stand 12.10.2026.",
        "category": "Reisen",
        "keyword": "Bali Reiseführer digital",
        "link": "https://www.checkout-ds24.com/redir/743944/mysticmarketing/okw-bali-reisefuehrer",
        "source": "https://www.checkout-ds24.com/product/743944",
        "image": "assets/products/bali-reisefuehrer.webp",
        "alt": "Cover des digitalen Bali Reiseführers mit 122 Unternehmungen",
        "intro": "Die Digistore24-Seite beschreibt einen deutschsprachigen digitalen Reiseführer von Indojunkie. Genannt werden 122 Tipps in 12 Kapiteln auf knapp 400 Seiten, einschließlich Bali, Nusa Penida, Lombok und der Gili-Inseln. Der konkrete Inhalt wurde von uns nicht selbst gelesen.",
        "facts": [
            "Angekündigt sind 122 Aktivitäten und Reisetipps in 12 Kapiteln.",
            "Die Verkaufsseite nennt Strände, Tempel, Wasserfälle, Märkte, Unterkünfte und Restaurants.",
            "Hinweise zu Regionen, Kartenmaterial und nachhaltiger Reiseplanung werden beworben.",
            "Deutschsprachiges E-Book mit digitalem Zugriff; zusätzlich wird eine druckbare PDF-Datei genannt.",
        ],
        "fit": "Für Reisende, die Anregungen für eine eigene Bali-Route suchen und auch Ausflüge nach Nusa Penida, Lombok oder zu den Gilis erwägen. Wer aktuelle Öffnungszeiten, Einreisebestimmungen oder Buchbarkeit benötigt, muss diese vor Ort beziehungsweise bei offiziellen Stellen nachprüfen.",
        "decision": "Lege zuerst Reisedauer und Regionen fest. Markiere nur so viele Orte, wie mit realistischen Fahrzeiten erreichbar sind. Kontrolliere anschließend Öffnungszeiten, Zugangsregeln und Transportmöglichkeiten aktuell; Reiseführer können hier schnell veralten.",
        "limits": "Die Aktualität einzelner Tipps, Karten und Unterkünfte wurde nicht geprüft. Die Bestellseite nennt 12,99 € Produktpreis zuzüglich 19 % MwSt. und 15,46 € als Gesamtbetrag (Stand 12.10.2026). Der endgültige Checkout-Betrag gilt. Ein gedrucktes Buch wird nicht angeboten.",
        "faq": [
            ("Ist der Reiseführer auf Deutsch?", "Ja, die Digistore24-Bestellseite nennt ein deutsches E-Book."),
            ("Geht es nur um Bali?", "Die Angebotsseite nennt zusätzlich Tipps für Nusa Penida, Lombok und die Gili-Inseln."),
            ("Sind die Informationen immer aktuell?", "Das kann ein E-Book nicht garantieren. Prüfe Einreise, Öffnungszeiten und lokale Regeln kurz vor Reiseantritt."),
        ],
        "related": ("teneriffa-wandern-mit-kindern.html", "Teneriffa mit Kindern wandern"),
        "price": "12,99 € Produktpreis; Checkout zeigt 15,46 € inkl. 19 % MwSt. (12.10.2026)",
        "audience": "Deutschsprachige Individualreisende mit Bali-Reiseplänen",
        "search": "Bali E-Book Reiseführer; Bali 122 Things to Do; Bali Reisetipps; Nusa Penida Lombok Gilis Reiseführer",
        "image_note": "Produktcover aus der Digistore24-Bestellseite lokal als WebP gespeichert; eigenständige Nutzungsrechte wurden nicht bestätigt.",
        "serp": [
            ("Indojunkie: Verlagsseite des Reiseführers", "https://indojunkie.com/bali-reisefuehrer-122-things-to-do-in-bali-2-auflage/"),
            ("Indojunkie: Inhaltsverzeichnis als PDF", "https://indojunkie.com/wp-content/uploads/bali-reisefuehrer-inhaltsverzeichnis.pdf"),
            ("Bali.info: Reiseführer und Bücher", "https://www.bali.info/buch/"),
        ],
        "resources": [("Inhaltsverzeichnis beim Verlag ansehen", "https://indojunkie.com/wp-content/uploads/bali-reisefuehrer-inhaltsverzeichnis.pdf")],
    },
]


def p(value):
    return escape(value, quote=True)


def make_page(item):
    image = (
        f'<img class="product-cover" src="{p(item["image"])}" alt="{p(item["alt"])}" width="420" height="560">'
        if item["image"]
        else '<div class="product-cover-missing" role="img" aria-label="Kein verifiziertes Produktbild verfügbar">Produktbild derzeit nicht verfügbar</div>'
    )
    facts = "".join(f"<li>{p(fact)}</li>" for fact in item["facts"])
    faqs = "".join(f"<h3>{p(q)}</h3><p>{p(a)}</p>" for q, a in item["faq"])
    resources = (
        '<section><h2>Weitere Informationen</h2><ul>'
        + "".join(f'<li><a href="{p(url)}" rel="noopener" target="_blank">{p(label)}</a></li>' for label, url in item["resources"])
        + '</ul></section>'
        if item["resources"] else ""
    )
    return f'''<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#eaf7ff">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="canonical" href="https://www.online-kurse-welt.de/{p(item["slug"])}.html">
  <meta name="description" content="{p(item["description"])}">
  <title>{p(item["title"])} | online-kurse-welt.de</title>
  <link rel="stylesheet" href="fonts.css">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="consent.css">
  <script src="consent-config.js" defer></script>
  <script src="consent.js" defer></script>
</head>
<body>
  <header class="site-header"><div class="container header-inner">
    <a class="brand" href="index.html" aria-label="online-kurse-welt.de – Startseite"><svg class="brand-mark" viewBox="0 0 46 36" aria-hidden="true"><path d="M22 5.5C15.7 1.5 8.2 1.1 1 3v27.4c7.3-1.9 14.8-1.5 21 2.5V5.5Z" fill="#27a7ff"/><path d="M24 5.5c6.3-4 13.8-4.4 21-2.5v27.4c-7.3-1.9-14.8-1.5-21 2.5V5.5Z" fill="#27a7ff"/><path d="M23 5v29" stroke="white" stroke-width="1.7"/></svg><span>online-kurse-welt.de</span></a>
    <nav class="main-nav" aria-label="Hauptnavigation"><a href="index.html#kurse">Produkte entdecken</a><a href="index.html#kategorien">Kategorien</a><a href="index.html">Startseite</a></nav>
  </div></header>
  <main>
    <div class="product-hero"><div class="container product-hero-grid">
      <div><p class="eyebrow">{p(item["category"])} · Werbung</p><h1>{p(item["title"])}</h1><p class="product-lead">{p(item["intro"])}</p>
      <p class="product-meta">Redaktion: online-kurse-welt.de · Anbieterangaben geprüft am {TODAY} · Nicht selbst getestet</p>
      <a class="primary-button" href="{p(item["link"])}" rel="sponsored noopener" target="_blank" aria-label="{p(item["name"])} beim Anbieter ansehen (Werbung)">Angebot ansehen <span aria-hidden="true">→</span></a>
      <p class="affiliate-inline">Werbung: Bei einem Kauf über diesen Link erhalten wir eine Provision. Der Preis ändert sich dadurch nicht.</p></div>
      <div class="product-visual">{image}</div>
    </div></div>
    <div class="container product-content">
      <nav class="breadcrumbs" aria-label="Brotkrumennavigation"><a href="index.html">Startseite</a> / {p(item["name"])}</nav>
      <section><h2>Das ist laut Anbieter enthalten</h2><ul class="check-list">{facts}</ul><p class="source-note">Quelle: <a href="{p(item["source"])}" rel="noopener" target="_blank">Angebots- und Bestellseite des Anbieters</a>, abgerufen am {TODAY}.</p></section>
      <section><h2>Für wen passt das Angebot?</h2><p>{p(item["fit"])}</p></section>
      <section class="decision-box"><h2>Unser praktischer Kauf-Check</h2><p>{p(item["decision"])}</p></section>
      <section><h2>Grenzen und offene Fragen</h2><p>{p(item["limits"])}</p><p>Preis und Leistungsumfang können sich ändern. Prüfe die Angaben vor einer Bestellung direkt beim Anbieter.</p></section>
      <section><h2>Häufige Fragen</h2>{faqs}</section>
      {resources}
      <section class="product-cta"><h2>Details beim Anbieter prüfen</h2><p>Sieh dir Produktumfang, aktuellen Endpreis und Vertragsbedingungen vor der Bestellung selbst an.</p><a class="primary-button" href="{p(item["link"])}" rel="sponsored noopener" target="_blank" aria-label="{p(item["name"])} beim Anbieter ansehen (Werbung)">Zum Anbieter <span aria-hidden="true">→</span></a><p class="affiliate-inline">Werbung · Partnerlink</p></section>
      <p class="related-link">Weitere Seite: <a href="{p(item["related"][0])}">{p(item["related"][1])}</a></p>
    </div>
  </main>
  <div class="closing-line">Wissen entdecken. Möglichkeiten erweitern.</div>
  <footer class="site-footer"><div class="container footer-inner"><a class="brand brand-footer" href="index.html" aria-label="online-kurse-welt.de – Startseite"><svg class="brand-mark" viewBox="0 0 46 36" aria-hidden="true"><path d="M22 5.5C15.7 1.5 8.2 1.1 1 3v27.4c7.3-1.9 14.8-1.5 21 2.5V5.5Z" fill="#27a7ff"/><path d="M24 5.5c6.3-4 13.8-4.4 21-2.5v27.4c-7.3-1.9-14.8-1.5-21 2.5V5.5Z" fill="#27a7ff"/><path d="M23 5v29" stroke="white" stroke-width="1.7"/></svg><span>online-kurse-welt.de</span></a><div class="footer-right"><nav aria-label="Footer-Navigation"><a href="index.html">Startseite</a><span aria-hidden="true">·</span><a href="impressum.html">Impressum</a><span aria-hidden="true">·</span><a href="datenschutz.html">Datenschutz</a><span aria-hidden="true">·</span><button class="cookie-settings-button" type="button" data-cookie-settings>Cookie-Einstellungen</button></nav><p class="affiliate-disclaimer"><strong>Werbehinweis:</strong> Diese Website ist eine Affiliate-Seite. Links zu Kursen und Produkten sind Partnerlinks (Werbung). Bei einem Kauf über diese Links erhalten wir eine Provision. Der Preis ändert sich dadurch nicht.</p></div></div></footer>
</body></html>
'''


def make_brief(item):
    other = " · ".join(x["slug"] + ".html" for x in PRODUCTS if x is not item)
    serp = "<br>".join(f"[{label}]({url})" for label, url in item["serp"])
    return f"""# SEO-Briefing: {item['name']}

Stand: {TODAY}. Grundlage: [SEO-Produktseite-Briefing-Vorlage.md](../SEO-Produktseite-Briefing-Vorlage.md) und [DESIGN.md](../DESIGN.md).

## 1. Website und Regeln

| Angabe | Eintrag |
|---|---|
| Zieldomain und Pfad | https://www.online-kurse-welt.de/{item['slug']}.html |
| SEO-/Designregeln | ../SEO-Produktseite-Briefing-Vorlage.md; ../DESIGN.md |
| Sprache, Zielland, Zielgruppe | Deutsch; Deutschland; {item['audience']} |
| Themenbereich | {item['category']} |
| Ähnliche Seiten | {other} — andere Produktintentionen, bei Reiseprodukten thematische Querverlinkung |
| Format | Eine H1, Title und Description, lokale Bilder mit Alt-Text, interne Links, belegte Fakten, sichtbar markierte Partnerlinks mit rel=sponsored |
| Fachliche Freigabe | Betreiber von online-kurse-welt.de; noch nicht persönlich freigegeben |

## 2. Nachprüfbare Produktdaten

| Angabe | Eintrag / Beleg |
|---|---|
| Name / Anbieter | {item['name']}; Anbieterbezeichnung auf der verlinkten Angebotsseite prüfen |
| Offizielle Seite | {item['source']} |
| Promo-Link | {item['link']} |
| Preis / Zahlungsmodell | {item['price']}; Stand {TODAY}. Kein Abo belegt. |
| Umfang | {'; '.join(item['facts'])} Quelle: {item['source']} |
| Lieferung / Sprache | Digitale Bereitstellung laut Angebotsseite; die Sprache und technische Voraussetzungen sind nur angegeben, soweit auf der Seite sichtbar. |
| Geeignet / nicht geeignet | {item['fit']} |
| Support / Rückgabe / Zusatzkosten | Nur auf der Angebotsseite erkennbare Bedingungen; offene Punkte auf der fertigen Seite genannt. |
| Bild / Rechte | {item['image_note']} |
| Pflege | Betreiber prüft Link, Endpreis und Umfang vor Veröffentlichung und regelmäßig danach. |

## 3. Suchintention

| Angabe | Eintrag |
|---|---|
| Hauptfrage | Was bietet {item['name']} tatsächlich, und passt es zu meinem Bedarf? |
| Hauptkeyword | {item['keyword']} |
| Verwandte Suchbegriffe | {item['search']} |
| Intention | Information vor einer möglichen Kaufentscheidung |
| Suchergebnis-Check | Am {TODAY} per Websuche zum Suchthema geprüft. Relevante Seiten: {serp}. Dies sind Suchergebnis-Beispiele, keine behauptete feste Rangfolge. |
| Eigenständiger Nutzen | Eignung, Grenzen, konkrete Prüffragen und transparente Trennung zwischen Anbieterangaben und redaktioneller Einordnung. |
| Interne Links | Startseite; {item['related'][0]} |
| Handlung | Anbieterangaben und Endbetrag selbst prüfen; bei Interesse über gekennzeichneten Partnerlink weiter. |

## 4. Eigener Mehrwert und Quellen

- [x] Konkrete Kauf- und Nutzungsfragen beantwortet, die auf der Verkaufsseite offenbleiben.
- [x] Eignung und Grenzen redaktionell eingeordnet.
- [ ] Produkt selbst getestet. **Nicht selbst getestet.**

Beobachtung: {item['limits']}

Auswahlkriterien: {item['decision']}

Quellen: {item['source']} (abgerufen {TODAY}); Produktliste.md (interne Erfassung); oben verlinkte Suchergebnisse als Vergleich und Kontext. Nutzungsrechte für Anbieterbilder vor Veröffentlichung gesondert klären. Keine Sterne, Testimonials, Erfolgsversprechen oder Produkt-Schema-Daten erfunden.
"""


def main():
    folder = ROOT / "produkt-briefings"
    folder.mkdir(exist_ok=True)
    for item in PRODUCTS:
        (ROOT / f"{item['slug']}.html").write_text(make_page(item), encoding="utf-8")
        (folder / f"{item['slug']}.md").write_text(make_brief(item), encoding="utf-8")


if __name__ == "__main__":
    main()
