"""Build the verified product briefs first, then their static HTML pages.

Source of truth for the page copy. Run: python generate_product_pages.py
"""

from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
CHECKED = "12.10.2026"

PRODUCTS = [
    {
        "slug": "nupem-money-reset",
        "name": "Nupem.finance Money Reset Program",
        "provider": "Nupem.finance (Eigenbezeichnung auf der Angebotsseite); rechtlicher Verkäufer nicht klar benannt",
        "category": "Persönliche Finanzen",
        "keyword": "Nupem.finance Money Reset Program",
        "title": "Nupem Money Reset: Inhalt, Preis & Grenzen",
        "description": "Nupem Money Reset Program: Budget-Routine, Eignung und der Preiswiderspruch von $580 zu $0. Kauf-Check und Quellen, Stand 12.10.2026.",
        "h1": "Nupem.finance Money Reset Program: Was steckt hinter dem Budget-Neustart?",
        "lead": "Du willst deine Ausgaben verstehen und einen Plan für den nächsten Monat finden? Das englischsprachige Money Reset Program setzt laut Anbieter bei Ausgabenmustern, Budgetplanung und kleinen Alltagsroutinen an.",
        "problem": "Wenn am Monatsende unklar bleibt, wohin das Geld geflossen ist, hilft eine Übersicht oft mehr als ein weiterer Vorsatz. Der Anbieter verspricht dafür ein selbstgesteuertes Material. Wie detailliert die Übungen sind, lässt sich ohne Zugang nicht prüfen.",
        "steps": [
            ("Ausgabenmuster erkennen", "Laut Verkaufsseite nutzt das Programm einfache Fragen, um wiederkehrende Ausgaben und mögliche Geldlecks sichtbar zu machen."),
            ("Budget ordnen", "Anschließend soll ein überschaubarer Plan für Einnahmen und Ausgaben entstehen. Konkrete Vorlagen oder Module werden öffentlich nicht aufgelistet."),
            ("Routine aufbauen", "Kleine tägliche Handlungen sollen helfen, die Planung fortzuführen. Ein messbarer finanzieller Erfolg ist dadurch nicht belegt."),
        ],
        "facts": [
            "Selbstgesteuertes, herunterladbares digitales Programm in englischer Sprache.",
            "Die Verkaufsseite nennt Fragen zu Ausgabenmustern, Budgetplanung und täglichen Schritten.",
            "Laut FAQ dürfen für den persönlichen Gebrauch mehrere Kopien ausgedruckt werden.",
            "Der Anbieter nennt unmittelbaren Zugang nach Anmeldung beziehungsweise Zahlung.",
        ],
        "price_short": "$580 laut Angebot · $0 im Formular",
        "price_detail": "Auf der Angebotsseite stehen zweimal $580. Im eingebetteten Zahlungsformular steht für dasselbe Produkt $0. Der tatsächlich zahlbare Endbetrag und eine Umrechnung in Euro sind damit nicht verlässlich feststellbar. Vor einer Zahlung Preis und Vertragsbedingungen direkt im Bestellschritt klären.",
        "payment": "Eine einmalige Bestellung wird dargestellt; ein Abo oder Ratenplan ist auf der sichtbaren Seite nicht belegt.",
        "extras": "Zusatzkosten oder Upsells sind im sichtbaren Formular nicht aufgeführt; spätere Schritte wurden nicht geprüft.",
        "returns": "Die Angebotsseite bewirbt eine 60-Tage-Geld-zurück-Garantie und verweist für die Erstattung auf Kontaktaufnahme. Die vollständigen Bedingungen wurden nicht unabhängig geprüft.",
        "fit": [
            "Du möchtest Ausgaben selbst sortieren und kannst englische Materialien nutzen.",
            "Du suchst eine eigenständig nutzbare Struktur für dein Haushaltsbudget.",
        ],
        "notfit": [
            "Du brauchst individuelle Schuldner-, Steuer- oder Anlageberatung.",
            "Du willst den genauen Leistungsumfang und Endpreis kennen, bevor du eine Kaufentscheidung triffst; beides bleibt hier teilweise offen.",
        ],
        "check": [
            "Notiere Einnahmen, feste Kosten und variable Ausgaben. Die Verbraucherzentrale bietet dafür auch eine kostenlose Anleitung.",
            "Frage vor der Bestellung nach konkreten Dateien, Seitenzahl, Betreuung und dem tatsächlich zahlbaren Preis.",
            "Gib keine Kontoauszüge oder Zugangsdaten weiter, bevor der Anbieter und die erforderlichen Daten klar benannt sind.",
        ],
        "limits": "Wir haben das Programm nicht gekauft oder getestet. Der rechtliche Verkäufer, die genaue Anzahl der Materialien, Aktualisierungen, technische Voraussetzungen und der Endpreis sind auf der sichtbaren Seite nicht eindeutig. Die frühere Angabe einer 90-Tage-Kontoauszugsanalyse aus der Produktliste ist dort nicht belegt und wird nicht übernommen. Diese Seite ist keine Finanzberatung.",
        "faq": [
            ("Was kostet das Nupem.finance Money Reset Program?", "Auf der Angebotsseite stehen $580, im eingebetteten Formular $0 (geprüft am 12.10.2026). Der Widerspruch lässt keinen sicheren Endbetrag zu. Prüfe den Preis vor jeder Zahlung direkt im Bestellschritt."),
            ("Für wen ist das Programm geeignet?", "Es richtet sich laut Anbieter an Menschen, die Ausgabenmuster erkennen und eine eigene Budgetroutine entwickeln wollen. Für persönliche Finanz- oder Schuldnerberatung ist es kein belegter Ersatz."),
            ("In welcher Sprache und in welchem Format bekomme ich es?", "Die Verkaufsseite ist englischsprachig und beschreibt ein herunterladbares, selbstgesteuertes digitales Programm. Die genaue Zahl und Art der Dateien ist öffentlich nicht angegeben."),
            ("Gibt es eine Rückgabe oder Garantie?", "Der Anbieter nennt eine 60-Tage-Geld-zurück-Garantie. Prüfe vor dem Kauf die vollständigen Bedingungen und den zuständigen Kontakt."),
            ("Garantiert das Programm, dass ich Geld spare?", "Nein. Die sichtbare Beschreibung belegt weder einen festen Sparbetrag noch einen persönlichen Erfolg."),
            ("Muss ich Kontoauszüge hochladen?", "Eine Upload-Pflicht steht auf der eingesehenen Angebotsseite nicht. Kläre vor dem Kauf, ob und welche persönlichen Daten im Programm benötigt werden."),
        ],
        "source": "https://nupemfinancemoney-fj3.plannerpack.co/",
        "checkout": "https://nupemfinancemoney-fj3.plannerpack.co/",
        "link": "https://nupemfinancemoney-fj3.plannerpack.co/#aff=mysticmarketing",
        "program": "Plannerpack",
        "product_id": "entfällt",
        "campaign": "okw-nupem-money-reset",
        "campaign_note": "Intern vergeben und in Produktliste.md dokumentiert; Plannerpack übernimmt über #aff=mysticmarketing keinen nachweisbaren Campaign Key im Link.",
        "image": "Kein Cover ohne belegtes Nutzungsrecht. Ein früher heruntergeladenes Cover wurde von der Veröffentlichung entfernt.",
        "image_meaning": "Ein Produktcover könnte den geplanten Budget-Neustart veranschaulichen; derzeit neutraler Platzhalter.",
        "alt": "Kein freigegebenes Produktbild für das Nupem.finance Money Reset Program",
        "serp": [
            ("Verbraucherzentrale: Haushaltsbuch führen", "https://www.verbraucherzentrale.de/wissen/geld-versicherungen/sparen-und-anlegen/haushaltsbuch-fuehren-ueberblick-ueber-ihre-finanzen-52179", "kostenlose Grundanleitung und Vorlagen"),
            ("Verbraucherzentrale: Das Haushaltsbuch", "https://www.verbraucherzentrale.de/buecher-und-ebooks/haushaltsbuch", "gedruckter Ratgeber als Alternative"),
            ("Verbraucherzentrale: Budgetplanung", "https://www.verbraucherzentrale.de/baustein-3-was-kostet-das-leben-31784", "Lernmaterial zur Budgetplanung"),
        ],
        "resources": [
            ("Kostenlose Haushaltsbuch-Anleitung der Verbraucherzentrale", "https://www.verbraucherzentrale.de/wissen/geld-versicherungen/sparen-und-anlegen/haushaltsbuch-fuehren-ueberblick-ueber-ihre-finanzen-52179"),
        ],
        "wish": "Mehr Überblick über das eigene Geld und weniger Ungewissheit vor dem nächsten Monatsende.",
        "scene": "Die regelmäßigen Abbuchungen liegen vor; eine verständliche Übersicht soll zeigen, wo Geld bleibt.",
        "obstacle": "Verteilte Ausgaben, fehlende Routine und unklare Produktdetails.",
        "awareness": "4 – produktbewusst: Suchende kennen das Programm und prüfen Nutzen und Preis.",
        "market": "3 – viele allgemeine Budgetversprechen; die Überschrift zeigt das konkrete Programm und die Preisfrage.",
        "mechanism": "Ausgabenmuster per Fragen erkennen, Budget ordnen, kleine Schritte wiederholen – nur soweit auf der Verkaufsseite beschrieben.",
        "identity": "Du weißt, dass du deine Ausgaben ordnen willst, aber noch nicht, ob dieses Programm genug konkrete Hilfe bietet.",
        "related": [
            ("/teneriffa-wandern-mit-kindern", "Familienwanderungen auf Teneriffa planen"),
            ("/bali-reisefuehrer", "Bali-Reiseführer prüfen"),
        ],
    },
    {
        "slug": "teneriffa-wandern-mit-kindern",
        "name": "Wandern auf Teneriffa mit Kindern für Anfänger",
        "provider": "Digistore24 GmbH als Verkäufer und Vertragspartner laut Bestellformular; Urheber des E-Books dort nicht eindeutig benannt",
        "category": "Reisen & Familie",
        "keyword": "Teneriffa wandern mit Kindern",
        "title": "Teneriffa mit Kindern wandern: E-Book & Preis",
        "description": "Teneriffa mit Kindern wandern: Das E-Book nennt 80 Wanderideen. Inhalt, Kauf-Check und Checkout-Preis von 15,46 € (Stand 12.10.2026).",
        "h1": "Teneriffa mit Kindern wandern: 80 Tourideen im E-Book",
        "lead": "Du möchtest mit deinen Kindern Teneriffas Natur entdecken und Touren auswählen, die zu eurer Familie passen? Der digitale Wanderführer kündigt 80 Ideen sowie Hinweise zu Vorbereitung, Wetter und Ausrüstung an.",
        "problem": "Eine schöne Aussicht allein macht eine Route noch nicht kindgerecht. Länge, Höhenmeter, Untergrund und die Tagesform müssen zusammenpassen. Das E-Book kann Ideen liefern; die aktuelle Eignung jeder Strecke musst du selbst prüfen.",
        "steps": [
            ("Ideen auswählen", "Die Verkaufsseite nennt 80 Wanderungen in unterschiedlichen Landschaften, darunter Wald-, Küsten- und Vulkanwege."),
            ("Tour eingrenzen", "Laut Anbieter helfen Hinweise, Strecken nach Alter, Kondition und Interessen der Kinder auszuwählen."),
            ("Aktuell prüfen", "Vor der Wanderung kontrollierst du selbst Wetter, Wegstatus und örtliche Regeln; ein statisches E-Book ersetzt diese Prüfung nicht."),
        ],
        "facts": [
            "Deutschsprachiges E-Book mit laut Anbieter 80 Wanderideen auf Teneriffa.",
            "Beschrieben werden Waldwege, Küstenpfade, Vulkanlandschaften und Aussichtspunkte.",
            "Die Verkaufsseite nennt Hinweise zu Ausrüstung, Wasser, Sonnenschutz und Wetterwechsel.",
            "Digitaler Zugriff über den Digistore24 Download Vault; kein physischer Versand. Eine druckbare PDF-Datei wird als Bonus genannt.",
        ],
        "price_short": "12,99 € Produktpreis · 15,46 € im Checkout",
        "price_detail": "Das Bestellformular zeigt 12,99 € Produktpreis, 2,47 € MwSt. (19 %) und 15,46 € Gesamtbetrag. Diese Angaben wurden am 12.10.2026 geprüft. Maßgeblich ist der Endbetrag im Bestellschritt.",
        "payment": "Einmalige Bestellung von einem digitalen Produkt laut sichtbarem Bestellformular; kein Abo erkennbar.",
        "extras": "Keine weiteren Zusatzkosten im sichtbaren Formular; mögliche spätere Angebote wurden nicht geprüft.",
        "returns": "Die Bestellseite bewirbt eine 60-Tage-Geld-zurück-Garantie. Bedingungen und Verfahren vor der Bestellung bei Digistore24 prüfen.",
        "fit": [
            "Du planst Familienausflüge auf Teneriffa und suchst eine Sammlung von Wanderideen.",
            "Du möchtest Hinweise zur Vorbereitung, wählst Routen aber selbst anhand aktueller Daten aus.",
        ],
        "notfit": [
            "Du brauchst eine persönlich geführte Tour oder eine verbindliche Sicherheitsfreigabe für jedes Kind.",
            "Du erwartest ein gedrucktes Buch oder garantiert tagesaktuelle Wegsperrungen.",
        ],
        "check": [
            "Prüfe vor jeder Tour die offizielle Routenbeschreibung: Schwierigkeit, Dauer, Höhenlage und Rückweg.",
            "Kontrolliere am selben Tag Sperrungen und Warnungen, etwa bei Tenerife ON, sowie die Wetterlage.",
            "Plane Wasser, Sonnenschutz, Pausen und eine Abbruchmöglichkeit nach dem jüngsten Kind.",
        ],
        "limits": "Wir haben das E-Book und die 80 Routen nicht selbst geprüft. Die Verkaufsseite zeigt keine vollständige Routenliste, keine detaillierten Höhenprofile und keinen belegten Aktualisierungsrhythmus. Das Bestellformular enthält einen Hinweis auf eine nicht öffentliche Version; prüfe, ob der Bestellschritt bei dir ordnungsgemäß funktioniert.",
        "faq": [
            ("Was kostet der Wanderführer?", "Am 12.10.2026 zeigte der Checkout 12,99 € Produktpreis zuzüglich 2,47 € MwSt., insgesamt 15,46 €. Der aktuelle Endbetrag im Bestellschritt ist maßgeblich."),
            ("Für wen ist das E-Book geeignet?", "Laut Anbieter richtet es sich an Familien und Wanderanfänger, die auf Teneriffa Tourideen suchen. Ob eine einzelne Route für dein Kind geeignet ist, musst du anhand aktueller Daten prüfen."),
            ("In welcher Sprache und in welchem Format erhalte ich es?", "Die Bestellseite nennt ein deutsches E-Book mit digitalem Zugriff und eine druckbare PDF-Datei als Bonus. Ein gedrucktes Buch wird nicht versendet."),
            ("Gibt es eine Rückgabe oder Garantie?", "Die Bestellseite bewirbt eine 60-Tage-Geld-zurück-Garantie. Prüfe die geltenden Bedingungen direkt vor der Bestellung."),
            ("Garantiert der Guide sichere Familienwanderungen?", "Nein. Wetter, Wegzustand und Fähigkeiten der Kinder ändern sich. Prüfe jede Tour selbst und beachte offizielle Warnungen."),
            ("Sind alle 80 Touren für jedes Alter geeignet?", "Das lässt sich aus der Verkaufsseite nicht ableiten. Sie nennt keine allgemeingültigen Altersgrenzen für alle Routen."),
            ("Wo prüfe ich aktuelle Wegsperrungen?", "Tenerife ON informiert über Warnungen und Einschränkungen; ergänzend bietet die offizielle Tourismus-Seite Routendaten."),
        ],
        "source": "https://www.checkout-ds24.com/product/743903",
        "checkout": "https://www.checkout-ds24.com/product/743903?aff=mysticmarketing&cam=okw-teneriffa-wandern",
        "link": "https://www.checkout-ds24.com/redir/743903/mysticmarketing/okw-teneriffa-wandern",
        "program": "Digistore24",
        "product_id": "743903",
        "campaign": "okw-teneriffa-wandern",
        "campaign_note": "Im Digistore24-Link und in Digistore24.md dokumentiert; Weiterleitung mit cam=okw-teneriffa-wandern geprüft.",
        "image": "Produktcover auf der Bestellseite vorhanden, aber kein belegtes Recht zur eigenen Veröffentlichung; deshalb Platzhalter.",
        "image_meaning": "Ein freigegebenes Cover könnte den familienbezogenen Wanderführer zeigen; derzeit neutraler Platzhalter.",
        "alt": "Kein freigegebenes Produktbild für den Teneriffa-Wanderführer",
        "serp": [
            ("Tenerife Tourism: Wanderwege", "https://www.webtenerife.de/aktivitaten/natur/wandern/wanderwege/?tab=1", "offizielle Routen nach Dauer und Schwierigkeit"),
            ("Tenerife ON: FAQ und Wegstatus", "https://www.tenerifeon.es/faq", "aktuelle Warnungen und Sperrungen"),
            ("Tenerife Tourism: Wandern", "https://www.webtenerife.de/aktivitaten/natur/vulkane/legendare-vulkane/erleben-und-sehen/senderismo-caminatas/", "allgemeine Wanderinspiration"),
        ],
        "resources": [
            ("Offizielle Wanderwege nach Schwierigkeit und Dauer", "https://www.webtenerife.de/aktivitaten/natur/wandern/wanderwege/?tab=1"),
            ("Tenerife ON: aktuelle Warnungen und Sperrungen", "https://www.tenerifeon.es/faq"),
        ],
        "wish": "Gemeinsame Naturerlebnisse auf Teneriffa, die die Kinder nicht überfordern.",
        "scene": "Die Familie steht vor der Tourenauswahl und möchte Aussicht, Pausen und einen passenden Rückweg verbinden.",
        "obstacle": "Viele Routen, unklare Eignung für Kinder und wechselnde Bedingungen.",
        "awareness": "3 – lösungsbewusst: Familien suchen einen passenden Wanderführer und konkrete Routenideen.",
        "market": "3 – viele Wanderlisten; die Überschrift nennt die belegten 80 Ideen und das Format.",
        "mechanism": "80 angekündigte Tourideen plus Hinweise zu Streckenauswahl und Vorbereitung.",
        "identity": "Du willst mit Kindern wandern, ohne eine Tour allein nach schönen Bildern auszuwählen.",
        "related": [("/bali-reisefuehrer", "Bali-Reise planen")],
    },
    {
        "slug": "bali-reisefuehrer",
        "name": "Bali Reiseführer",
        "provider": "Indojunkie als genannter Herausgeber; Digistore24 GmbH als Verkäufer und Vertragspartner im Checkout",
        "category": "Reisen",
        "keyword": "Bali Reiseführer",
        "title": "Bali Reiseführer: 122 Tipps, E-Book & Preis",
        "description": "Bali Reiseführer von Indojunkie: 122 Tipps in 12 Kapiteln, Format, Grenzen und 15,46 € Checkout-Preis. Kauf-Check, Stand 12.10.2026.",
        "h1": "Bali Reiseführer: 122 Tipps für deine Reiseplanung",
        "lead": "Du möchtest aus vielen Bali-Ideen eine Reise zusammenstellen, die zu deiner Zeit und deinen Interessen passt? Der digitale Reiseführer von Indojunkie ordnet laut Anbieter 122 Tipps in 12 Kapitel und bezieht Nachbarinseln ein.",
        "problem": "Strände, Tempel, Wasserfälle und weitere Inseln klingen nach einer vollen Route. Ohne Prioritäten werden Fahrtzeiten und Ortswechsel schnell unterschätzt. Ein Reiseführer kann Ideen sortieren; die tatsächliche Machbarkeit musst du für deine Reisedaten prüfen.",
        "steps": [
            ("Regionen auswählen", "Der Anbieter beschreibt 12 Kapitel mit regional geordneten Tipps für Bali sowie Hinweise zu Nusa Penida, Lombok und den Gilis."),
            ("Aktivitäten priorisieren", "Aus 122 angekündigten Ideen wählst du passend zu Reisedauer und Interessen eine kleinere Auswahl."),
            ("Details aktualisieren", "Öffnungszeiten, Transport, Einreise und lokale Regeln kontrollierst du vor Ort beziehungsweise bei offiziellen Stellen neu."),
        ],
        "facts": [
            "Indojunkie beschreibt die zweite Auflage mit 122 Tipps in 12 Kapiteln auf knapp 400 Seiten.",
            "Genannt werden Strände, Tempel, Wasserfälle, Märkte, Unterkünfte, Restaurants und weitere Aktivitäten.",
            "Die Verkaufsseite nennt Kartenmaterial, Illustrationen, Fotos und Anregungen zu nachhaltigem Reisen.",
            "Deutschsprachiges E-Book mit digitalem Zugang über Digistore24; eine druckbare PDF-Datei wird zusätzlich genannt.",
        ],
        "price_short": "12,99 € Produktpreis · 15,46 € im Checkout",
        "price_detail": "Das Bestellformular zeigt 12,99 € Produktpreis, 2,47 € MwSt. (19 %) und 15,46 € Gesamtbetrag. Diese Angaben wurden am 12.10.2026 geprüft. Maßgeblich ist der Endbetrag im Bestellschritt.",
        "payment": "Einmalige Bestellung von einem digitalen Produkt laut sichtbarem Bestellformular; kein Abo erkennbar.",
        "extras": "Keine weiteren Zusatzkosten im sichtbaren Formular; mögliche spätere Angebote wurden nicht geprüft.",
        "returns": "Die Bestellseite bewirbt eine 60-Tage-Geld-zurück-Garantie. Bedingungen und Verfahren vor der Bestellung bei Digistore24 prüfen.",
        "fit": [
            "Du suchst Ideen für eine selbst geplante Reise durch Bali und eventuell zu Nachbarinseln.",
            "Du möchtest einen deutschsprachigen digitalen Guide mit regional gegliederten Anregungen.",
        ],
        "notfit": [
            "Du brauchst tagesaktuelle Öffnungszeiten, Einreisevorgaben oder verbindlich buchbare Touren.",
            "Du erwartest ein gedrucktes Buch von diesem Bestelllink.",
        ],
        "check": [
            "Markiere zuerst die Regionen, die du bei deiner Reisedauer wirklich erreichen kannst.",
            "Sieh dir das öffentlich verfügbare Inhaltsverzeichnis beim Verlag an, bevor du kaufst.",
            "Prüfe aktuelle Einreise-, Transport- und Öffnungszeiten separat; das E-Book ersetzt keine aktuelle amtliche Auskunft.",
        ],
        "limits": "Wir haben das E-Book nicht vollständig gelesen oder die 122 Tipps überprüft. Erscheinungsdatum und Aktualisierungsrhythmus einzelner Empfehlungen sind im Checkout nicht klar. Das Bestellformular enthält einen Hinweis auf eine nicht öffentliche Version; prüfe, ob der Bestellschritt bei dir ordnungsgemäß funktioniert.",
        "faq": [
            ("Was kostet der Bali Reiseführer?", "Am 12.10.2026 zeigte der Checkout 12,99 € Produktpreis zuzüglich 2,47 € MwSt., insgesamt 15,46 €. Der aktuelle Endbetrag im Bestellschritt ist maßgeblich."),
            ("Für wen ist der Reiseführer geeignet?", "Er richtet sich an Reisende, die Bali selbst planen und Ideen für Orte und Aktivitäten suchen. Für verbindliche aktuelle Reiseauskünfte ist er kein Ersatz."),
            ("In welcher Sprache und in welchem Format erhalte ich ihn?", "Der Checkout nennt ein deutsches E-Book mit digitalem Zugriff und eine druckbare PDF-Datei. Ein gedrucktes Buch wird über diesen Link nicht versendet."),
            ("Gibt es eine Rückgabe oder Garantie?", "Die Bestellseite bewirbt eine 60-Tage-Geld-zurück-Garantie. Prüfe die geltenden Bedingungen direkt vor der Bestellung."),
            ("Garantiert der Guide eine gelungene Reise?", "Nein. Ob Tipps zu deinen Interessen, deinem Budget und den aktuellen Bedingungen passen, lässt sich nicht garantieren."),
            ("Behandelt der Guide auch Nusa Penida, Lombok und die Gilis?", "Ja, die Verkaufsseite nennt zusätzliche Tipps für diese Inseln. Den genauen Kapitelumfang kannst du im Inhaltsverzeichnis des Verlags nachsehen."),
            ("Sind Öffnungszeiten und Einreiseinfos aktuell?", "Das wurde nicht geprüft. Kontrolliere solche Angaben kurz vor der Reise bei offiziellen Stellen."),
        ],
        "source": "https://www.checkout-ds24.com/product/743944",
        "checkout": "https://www.checkout-ds24.com/product/743944?aff=mysticmarketing&cam=okw-bali-reisefuehrer",
        "link": "https://www.checkout-ds24.com/redir/743944/mysticmarketing/okw-bali-reisefuehrer",
        "program": "Digistore24",
        "product_id": "743944",
        "campaign": "okw-bali-reisefuehrer",
        "campaign_note": "Im Digistore24-Link und in Digistore24.md dokumentiert; Weiterleitung mit cam=okw-bali-reisefuehrer geprüft.",
        "image": "Produktcover auf der Bestellseite vorhanden, aber kein belegtes Recht zur eigenen Veröffentlichung; deshalb Platzhalter.",
        "image_meaning": "Ein freigegebenes Cover könnte die Reiseideen visuell verorten; derzeit neutraler Platzhalter.",
        "alt": "Kein freigegebenes Produktbild für den Bali Reiseführer",
        "serp": [
            ("Indojunkie: Verlagsseite", "https://indojunkie.com/bali-reisefuehrer-122-things-to-do-in-bali-2-auflage/", "Herausgeber und Produktbeschreibung"),
            ("Indojunkie: Inhaltsverzeichnis", "https://indojunkie.com/wp-content/uploads/bali-reisefuehrer-inhaltsverzeichnis.pdf", "öffentlicher Einblick in Kapitel"),
            ("Bali.info: Reiseführer", "https://www.bali.info/buch/", "Vergleich verschiedener Reiseführer"),
        ],
        "resources": [
            ("Öffentliches Inhaltsverzeichnis beim Verlag", "https://indojunkie.com/wp-content/uploads/bali-reisefuehrer-inhaltsverzeichnis.pdf"),
        ],
        "wish": "Eine Reise mit passenden Erlebnissen planen, ohne sich in einer endlosen Ideensammlung zu verlieren.",
        "scene": "Vor der Reise liegen viele Bali-Orte auf einer Karte; einige sollen zu einer machbaren Route werden.",
        "obstacle": "Zu viele Optionen, knappe Reisetage und wechselnde Angaben vor Ort.",
        "awareness": "3 – lösungsbewusst: Suchende vergleichen Reiseführer und möchten den Umfang kennen.",
        "market": "3 – viele ähnliche Reiseversprechen; die Überschrift nennt belegte 122 Tipps als konkreten Umfang.",
        "mechanism": "Regional gegliederte Kapitel mit 122 angekündigten Tipps und begleitendem Kartenmaterial.",
        "identity": "Du hast viele Bali-Ideen gesammelt und möchtest wissen, ob dieser Guide bei der Auswahl hilft.",
        "related": [("/teneriffa-wandern-mit-kindern", "Familienwanderungen auf Teneriffa")],
    },
]


def h(value):
    return escape(value, quote=True)


def bullets(items):
    return "".join(f"<li>{h(item)}</li>" for item in items)


def brief(item):
    rows = lambda pairs: "\n".join(f"| {key} | {value} |" for key, value in pairs)
    facts = "; ".join(point.rstrip(".") for point in item["facts"]) + "."
    faq = "\n".join(f"| {q} | {a} |" for q, a in item["faq"])
    serp = "<br>".join(f"[{name}]({url}) – {observation}" for name, url, observation in item["serp"])
    related = ", ".join(f"[{label}](https://www.online-kurse-welt.de{path})" for path, label in item["related"])
    return f"""# SEO-Produktbriefing: {item['name']}

Ausgefüllt am {CHECKED} nach [SEO-Produktseite-Briefing-Vorlage.md](../SEO-Produktseite-Briefing-Vorlage.md). Fakten, Anbieterbehauptungen und redaktionelle Einordnung sind getrennt. Freigabe durch den Betreiber steht aus.

## 1. Stammdaten

| Angabe | Eintrag |
|---|---|
{rows([
("Produktname", item["name"]),
("Anbieter / Verkäufer", item["provider"]),
("Seitenpfad", "/" + item["slug"]),
("Kategorie", item["category"]),
("Sprache", "Englisch laut Angebotsseite" if item["slug"] == "nupem-money-reset" else "Deutsch laut Bestellseite"),
("Status", "✅ Eingebaut in Produktliste.md"),
("Verantwortlich für Prüfung und Freigabe", "Steven Jesse / Betreiber; persönliche Freigabe nicht dokumentiert"),
("Stand", CHECKED),
])}

## 2. Nachprüfbare Produktfakten

| Angabe | Eintrag | Quelle / Abrufdatum |
|---|---|---|
{rows([
("Verkaufsseite", item["source"] + " | " + CHECKED),
("Produktart und Format", ("Herunterladbares, selbstgesteuertes Digitalprogramm" if item["slug"] == "nupem-money-reset" else "Digitales E-Book mit zusätzlich genannter druckbarer PDF-Datei") + " | " + item["source"] + " · " + CHECKED),
("Inhalt / Umfang", facts + " | " + item["source"] + " · " + CHECKED),
("Zugang / Lieferung", ("Digital nach Anmeldung/Zahlung laut Anbieter; genaue Zugangsdauer offen" if item["slug"] == "nupem-money-reset" else "Digital über Digistore24 Download Vault, kein Versand; Zugangsdauer offen") + " | " + item["source"] + " · " + CHECKED),
("Technische Voraussetzungen", "Nicht klar angegeben; Gerät zum Öffnen der digitalen Dateien erforderlich | " + item["source"] + " · " + CHECKED),
("Support / Updates / Rückgabe", item["returns"] + " Support und Updates nicht klar angegeben. | " + item["source"] + " · " + CHECKED),
("Geeignet", "; ".join(item["fit"]) + " | redaktionelle Einordnung auf Basis der Verkaufsseite · " + CHECKED),
("Nicht geeignet", "; ".join(item["notfit"]) + " | redaktionelle Einordnung · " + CHECKED),
("Selbst getestet", "**Nicht selbst getestet** | redaktioneller Prüfstatus · " + CHECKED),
])}

## 3. Preis

| Angabe | Eintrag |
|---|---|
{rows([
("Produktpreis laut Verkaufsseite", "$580" if item["slug"] == "nupem-money-reset" else "12,99 €"),
("Endbetrag im Checkout", "$0 im eingebetteten Formular; Widerspruch, Endpreis ungeklärt" if item["slug"] == "nupem-money-reset" else "15,46 € einschließlich 2,47 € MwSt. (19 %)"),
("Zahlungsmodell", item["payment"]),
("Währung", "USD; keine belastbare EUR-Umrechnung" if item["slug"] == "nupem-money-reset" else "EUR"),
("Zusatzkosten / Upsells", item["extras"]),
("Prüftag / Quelle", CHECKED + " · " + item["checkout"]),
("Widersprüche", item["price_detail"] if item["slug"] == "nupem-money-reset" else "Keine zwischen Produktpreis, ausgewiesener MwSt. und Gesamtbetrag erkennbar; aktueller Endbetrag vor Kauf erneut prüfen."),
])}

## 4. Partnerlink und Campaign Key

| Angabe | Eintrag |
|---|---|
{rows([
("Partnerprogramm / Produkt-ID", item["program"] + " / " + item["product_id"]),
("Campaign Key", "`" + item["campaign"] + "`"),
("Fertiger Partnerlink", item["link"]),
("Dokumentation", item["campaign_note"]),
("Linktest", "Zielseite lädt; " + ("Key nicht im Plannerpack-Link übertragbar" if item["slug"] == "nupem-money-reset" else "Key nach Weiterleitung als cam-Parameter vorhanden") + " · " + CHECKED),
])}

## 5. Suchintention und Keywords

| Angabe | Eintrag |
|---|---|
{rows([
("Hauptfrage", "Was bietet " + item["name"] + ", für wen passt es und was kostet es wirklich?"),
("Hauptkeyword", item["keyword"]),
("Verwandte Fragen", "; ".join(q for q, _ in item["faq"][:5])),
("Suchintention", "Information, Vergleich und Kaufentscheidung"),
("Suchergebnis-Check", CHECKED + ": " + serp + ". Relevante Suchergebnisse und Quellen, keine behauptete feste Rangfolge."),
("Eigener Mehrwert", "Belegte Fakten, Preisprüfung, konkreter Kauf-Check, Eignung und Grenzen statt einer bloßen Anbieterumschreibung."),
("Interne Links", "[Startseite](https://www.online-kurse-welt.de/), " + related),
])}

## 6. Schwartz-Analyse

| Element | Eintrag |
|---|---|
{rows([
("Vorhandener Wunsch", item["wish"]),
("Konkretes Bild", item["scene"]),
("Hindernis", item["obstacle"]),
("Stärke / Dringlichkeit", "mittel bis hoch; redaktionelle Annahme, keine gemessene Marktforschung"),
("Bewusstseinsstufe", item["awareness"]),
("Marktreife", item["market"]),
("Mechanismus", item["mechanism"]),
("Identifikationssatz", item["identity"]),
("Beleg / Steigerung", facts + " Quelle: " + item["source"]),
("H1", item["h1"]),
("Lead", item["lead"]),
("Title-Tag", item["title"]),
("Meta-Description", item["description"]),
])}

## 7. Produktbild

| Angabe | Eintrag |
|---|---|
{rows([
("Bildquelle und Recht", item["image"]),
("Nutzungsrecht geklärt?", "Nein. Deshalb wird kein fremdes Cover veröffentlicht."),
("Bildaussage", item["image_meaning"]),
("Alt-Text", item["alt"]),
("Datei", "Keine veröffentlichte Produktbilddatei; CSS-Platzhalter auf Seite und Startseite."),
])}

## 8. Seitenaufbau und eigener Mehrwert

Die HTML-Seite folgt der Reihenfolge Hero mit Preisbox → Brotkrumen → Worum es geht → So funktioniert es → belegter Umfang → Preis und Konditionen → Eignung → Kauf-Check → Grenzen → FAQ → Abschluss-CTA → weitere Seiten. Der Kauf-Check ist redaktioneller Mehrwert:

{chr(10).join("- " + point for point in item["check"])}

## 9. FAQ

| Frage | Antwort |
|---|---|
{faq}

## 10. Pflichtangaben

Werbung im Eyebrow und direkt an beiden Partnerlinks; `rel="sponsored noopener"`; Prüfdatum und „Nicht selbst getestet“; Leistungsumfang mit Anbieterquelle; keine erfundenen Bewertungen, Garantien oder strukturierten Produktdaten.

## 11. Freigabe-Check

- [x] Fakten und Preis mit Quelle und Prüftag dokumentiert; Widersprüche offen genannt.
- [x] Campaign Key vergeben, Link getestet und dokumentiert.
- [x] H1 und Lead anhand der festgehaltenen Suchintention formuliert.
- [x] Kein ungeklärtes Produktbild veröffentlicht.
- [x] Preis in Hero, Konditionen und FAQ.
- [x] FAQ mit Pflichtfragen vor Abschluss-CTA.
- [x] Partnerlinks gekennzeichnet; Sitemap und Produktliste gepflegt.
- [x] Desktop und Mobil technisch geprüft.
- [ ] Persönliche redaktionelle und rechtliche Freigabe durch den Betreiber.
"""


def html_page(item):
    steps = "".join(f"<li><h3>{h(head)}</h3><p>{h(copy)}</p></li>" for head, copy in item["steps"])
    faq = "".join(f"<h3>{h(q)}</h3><p>{h(a)}</p>" for q, a in item["faq"])
    resources = "".join(f'<li><a href="{h(url)}" rel="noopener" target="_blank">{h(label)}</a></li>' for label, url in item["resources"])
    related = "".join(f'<li><a href="{h(path)}">{h(label)}</a></li>' for path, label in item["related"])
    link = h(item["link"])
    name = h(item["name"])
    return f'''<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#eaf7ff">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="canonical" href="https://www.online-kurse-welt.de/{h(item["slug"])}">
  <meta name="description" content="{h(item["description"])}">
  <title>{h(item["title"])}</title>
  <link rel="stylesheet" href="fonts.css">
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="consent.css">
  <script src="consent-config.js" defer></script>
  <script src="consent.js" defer></script>
</head>
<body>
  <header class="site-header"><div class="container header-inner">
    <a class="brand" href="/" aria-label="online-kurse-welt.de – Startseite"><svg class="brand-mark" viewBox="0 0 46 36" aria-hidden="true"><path d="M22 5.5C15.7 1.5 8.2 1.1 1 3v27.4c7.3-1.9 14.8-1.5 21 2.5V5.5Z" fill="#27a7ff"/><path d="M24 5.5c6.3-4 13.8-4.4 21-2.5v27.4c-7.3-1.9-14.8-1.5-21 2.5V5.5Z" fill="#27a7ff"/><path d="M23 5v29" stroke="white" stroke-width="1.7"/></svg><span>online-kurse-welt.de</span></a>
    <nav class="main-nav" aria-label="Hauptnavigation"><a href="/#kurse">Produkte entdecken</a><a href="/#kategorien">Kategorien</a><a href="/">Startseite</a></nav>
  </div></header>
  <main>
    <section class="product-hero"><div class="container product-hero-grid">
      <div><p class="eyebrow">{h(item["category"])} · Werbung</p><h1>{h(item["h1"])}</h1><p class="product-lead">{h(item["lead"])}</p>
      <p class="product-meta">Redaktion: online-kurse-welt.de · Anbieterangaben geprüft am {CHECKED} · Nicht selbst getestet</p>
      <div class="price-box"><strong>Preis: {h(item["price_short"])}</strong><span>Stand: {CHECKED}. Maßgeblich ist der Preis im Bestellschritt.</span></div>
      <a class="primary-button" href="{link}" rel="sponsored noopener" target="_blank" aria-label="{name} beim Anbieter ansehen (Werbung)">Angebot prüfen <span aria-hidden="true">→</span></a>
      <p class="affiliate-inline">Werbung: Bei einem Kauf über diesen Link erhalten wir eine Provision. Der Preis ändert sich dadurch nicht.</p></div>
      <div class="product-visual"><div class="product-cover-missing" role="img" aria-label="{h(item["alt"])}">Produktbild derzeit nicht verfügbar</div></div>
    </div></section>
    <div class="container product-content">
      <nav class="breadcrumbs" aria-label="Brotkrumennavigation"><a href="/">Startseite</a> / {name}</nav>
      <section><h2>Worum es geht</h2><p>{h(item["problem"])}</p></section>
      <section><h2>So funktioniert es laut Anbieter</h2><ol class="product-steps">{steps}</ol></section>
      <section><h2>Das ist laut Anbieter enthalten</h2><ul class="check-list">{bullets(item["facts"])}</ul><p class="source-note">Quelle: <a href="{h(item["source"])}" rel="noopener" target="_blank">Verkaufs- und Bestellseite</a>, abgerufen am {CHECKED}. Die Angaben sind nicht selbst getestet.</p></section>
      <section><h2>Preis und Konditionen</h2><p>{h(item["price_detail"])}</p><p>{h(item["payment"])} {h(item["extras"])}</p><p>{h(item["returns"])}</p><p class="source-note">Preisquelle: <a href="{h(item["checkout"])}" rel="noopener" target="_blank">Bestellseite</a>, geprüft am {CHECKED}.</p></section>
      <section class="fit-grid"><div><h2>Für wen passt es?</h2><ul>{bullets(item["fit"])}</ul></div><div><h2>Für wen eher nicht?</h2><ul>{bullets(item["notfit"])}</ul></div></section>
      <section class="decision-box"><h2>Unser Kauf-Check</h2><ol>{bullets(item["check"])}</ol><p>Diese Prüffragen sind unsere redaktionelle Einordnung, keine Zusage des Anbieters.</p></section>
      <section><h2>Grenzen und offene Fragen</h2><p>{h(item["limits"])}</p></section>
      <section><h2>Häufige Fragen</h2>{faq}</section>
      <section class="product-cta"><h2>Angaben beim Anbieter prüfen</h2><p>Vergleiche vor dem Kauf den aktuellen Umfang, den Endbetrag und die geltenden Bedingungen.</p><a class="primary-button" href="{link}" rel="sponsored noopener" target="_blank" aria-label="{name} beim Anbieter ansehen (Werbung)">Zum Angebot <span aria-hidden="true">→</span></a><p class="affiliate-inline">Werbung · Partnerlink</p></section>
      <aside class="product-resources"><h2>Weitere Informationen</h2><ul>{resources}</ul><h2>Weitere Seiten</h2><ul>{related}</ul></aside>
    </div>
  </main>
  <div class="closing-line">Wissen entdecken. Möglichkeiten erweitern.</div>
  <footer class="site-footer"><div class="container footer-inner"><a class="brand brand-footer" href="/" aria-label="online-kurse-welt.de – Startseite"><svg class="brand-mark" viewBox="0 0 46 36" aria-hidden="true"><path d="M22 5.5C15.7 1.5 8.2 1.1 1 3v27.4c7.3-1.9 14.8-1.5 21 2.5V5.5Z" fill="#27a7ff"/><path d="M24 5.5c6.3-4 13.8-4.4 21-2.5v27.4c-7.3-1.9-14.8-1.5-21 2.5V5.5Z" fill="#27a7ff"/><path d="M23 5v29" stroke="white" stroke-width="1.7"/></svg><span>online-kurse-welt.de</span></a><div class="footer-right"><nav aria-label="Footer-Navigation"><a href="/">Startseite</a><span aria-hidden="true">·</span><a href="/impressum">Impressum</a><span aria-hidden="true">·</span><a href="/datenschutz">Datenschutz</a><span aria-hidden="true">·</span><button class="cookie-settings-button" type="button" data-cookie-settings>Cookie-Einstellungen</button></nav><p class="affiliate-disclaimer"><strong>Werbehinweis:</strong> Diese Website ist eine Affiliate-Seite. Links zu Kursen und Produkten sind Partnerlinks (Werbung). Bei einem Kauf über diese Links erhalten wir eine Provision. Der Preis ändert sich dadurch nicht.</p></div></div></footer>
</body></html>
'''


def main():
    for item in PRODUCTS:
        (ROOT / f"{item['slug']}.html").write_text(html_page(item), encoding="utf-8")


if __name__ == "__main__":
    main()
