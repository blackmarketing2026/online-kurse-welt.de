# Affiliate-Agent für online-kurse-welt.de

## Aufruf

In Codex im geöffneten Projektordner schreiben:

`Affiliate-Agent starten. Produkt-URL: https://… Affiliate-Link: https://…`

Codex liest `AGENTS.md` als Projektanweisung und startet mit diesem Aufruf den folgenden Arbeitsablauf. Der Agent ist ein wiederverwendbarer Codex-Arbeitsablauf, kein Hintergrunddienst. Er läuft nur nach ausdrücklichem Aufruf. Keine zusätzliche KI-API, Agentenplattform, Docker- oder Serverinstallation ist nötig.

## Projektkarte (Stand: 19. Oktober 2026)

- Statische Website aus HTML, CSS und JavaScript ohne Framework oder Build-Schritt. `index.html` und `styles.css` sind technische Referenz für allgemeine Seiten. Neue Produktseiten werden individuell gestaltet; `funnel-cockpit.html` und `funnel-cockpit.css` sind ein Beispiel für eine eigenständige Seite, keine Designvorlage.
- `script.js` filtert die Produktkarten auf der Startseite über `data-category`. Kategorien und Karten stehen in `index.html` im Bereich `#kategorien` beziehungsweise `#kurse`. Bestehende Kategorien: Online-Business (`business`), Persönliche Finanzen (`persoenlich`), Reisen & Familie (`reisen`). Eine neue Kategorie erfordert passende Filter-/Layoutprüfung.
- `generate_product_pages.py` erzeugt drei ältere Produktseiten. Neue individuell gestaltete Seiten werden nicht darüber erzeugt, solange das Skript dafür nicht ausdrücklich angepasst wurde. Bestehende generierte Seiten nicht versehentlich überschreiben.
- `sitemap.xml`, `robots.txt` und `<link rel="canonical">` verwenden `https://www.online-kurse-welt.de/`. `vercel.json` enthält `cleanUrls: true`: Datei `slug.html` wird öffentlich unter `/slug` verlinkt.
- `consent-config.js`, `consent.js` und `consent.css` steuern die Einwilligung. Neue Tracking-IDs nur nach `TRACKING-SETUP.md`. Partnerlinks allein erfordern kein zusätzliches Tracking-Skript.
- Git-Branch `main`, Remote `origin` auf GitHub; Vercel veröffentlicht über den vorhandenen GitHub-Prozess. Keine lokale Vercel-CLI oder neue Deployment-Automation voraussetzen. Verfügbarkeit und Zuordnung vor dem Push prüfen.
- `DESIGN.md` enthält die aktuelle Gestaltungsvorgabe. `impressum.html` und `datenschutz.html` enthalten die Rechtstexte. `Digistore24.md`, `Produktliste.md` und `SEO-Produktseite-Briefing-Vorlage.md` liefern bei Bedarf redaktionellen Kontext, aber keine automatisch aktuellen Produktdaten.

## 1. Eingaben und Ausgangslage prüfen

1. Beide URLs vollständig erfassen und syntaktisch prüfen. Fehlt eine, gezielt danach fragen. Nur HTTPS-Ziele verwenden. Ein vom Nutzer ausdrücklich bereitgestellter Affiliate-Link gilt für die Verwendung als freigegeben. Ihn unverändert einschließlich Reihenfolge, Schreibweise, Query-Parametern und URL-Fragment übernehmen; nicht eigenmächtig umschreiben oder Parameter entfernen.
2. `git status --short --branch`, Branch, Remote, `vercel.json` und relevante Dateien prüfen. Fremde Änderungen nicht committen oder überschreiben.
3. Vor jeder Website-Änderung `DESIGN.md`, `AGENTS.md`, `index.html` und `styles.css` lesen. Bestehende Produktnamen, Slugs, Canonicals, Sitemap-Einträge und interne Links nach Duplikaten durchsuchen. Bei vorhandenem Produkt die passende Seite aktualisieren, statt eine zweite URL anzulegen.

## 2. Produkt und Suchintention recherchieren

1. Produkt-URL und nach Möglichkeit die tatsächliche Weiterleitung beziehungsweise Affiliate-Zuordnung prüfen. Offizielle Verkaufsseite, Anbieterinformationen und gegebenenfalls Checkout prüfen. Bei dynamischen Seiten vorhandene Browserwerkzeuge nutzen. Kein Kauf und keine Eingabe persönlicher Daten. HTTP 429, Captcha und Bot-Schutz nicht umgehen. Verhindern sie die externe Prüfung, dies als Warnung „Affiliate-Zuordnung nicht verifiziert“ festhalten; es ist allein kein Veröffentlichungsblocker.
2. Produktname, Anbieter, Kategorie, Zielgruppe, Format, Inhalte, Nutzen, Grenzen, Voraussetzungen, Preis und Vertragsmodell nur festhalten, soweit belegt. Datum und konkrete Quell-URLs in der Arbeitsnotiz beziehungsweise im Abschlussbericht nennen. Widersprüche und nicht verifizierbare Angaben offen kennzeichnen. Keine erfundenen Bewertungen, Zahlen, Garantien oder Erfolgsversprechen.
3. Reale Suchergebnisse und passende Seiten als Hinweise auf Suchintention und Sprache prüfen. Hauptkeyword, Nebenkeywords und typische Käuferfragen daraus ableiten; keine Suchvolumen oder Rankings erfinden.
4. Originale, eigenständige Texte schreiben. Die Verkaufsseite nicht kopieren. Eine hilfreiche Kaufentscheidung ermöglichen: Für wen geeignet, Leistungsumfang, Kosten soweit belegt, Grenzen, Vergleichsaspekte, FAQ und klare Weiterleitung zum Anbieter.
5. Ist die Produktseite nicht zuverlässig lesbar, andere offizielle Quellen und den Checkout versuchen. Wenn wesentliche Fakten danach fehlen, nur die fehlenden Angaben erfragen. Keine erfundene Produktseite veröffentlichen.

## 3. Seite erstellen und integrieren

1. Einen eindeutigen, kurzen Slug wählen. Datei `<slug>.html`, bei Bedarf eigene `<slug>.css` und lokale Assets anlegen. Öffentlich ausschließlich `/slug` verwenden, auch in Canonical, Open-Graph-URL, internen Links und Sitemap.
2. Für jedes Produkt grundsätzlich ein neues, produktgerechtes Design entwickeln: eigene Farb- und Schriftidee, Bildsprache, Hero, Abschnittsfolge und CTA-Gestaltung. Verlangt der aktuelle Auftrag ausdrücklich das bestehende Website-Design, diese Einzelanweisung befolgen. `DESIGN.md` beachten und eine solche Ausnahme dort dokumentieren. Die Startseite und allgemeinen Seiten nicht umgestalten.
3. Semantisches HTML mit genau einer H1, sinnvoller H2/H3-Folge, eindeutigen Linktexten, sichtbaren Fokussen und funktionierender Mobilansicht bauen. Title, Meta-Description, Canonical, Sprache, sinnvolle Social-Metadaten und bei belegbarer Eignung strukturierte Daten ergänzen. FAQ-Markup nur für tatsächlich sichtbare Fragen und Antworten verwenden.
4. Produktbilder nur mit nachprüfbarer Berechtigung zur Verwendung in der Partnerwerbung übernehmen; Quelle und Rechteprüfung dokumentieren. Bilder lokal speichern, optimieren und mit passenden Alternativtexten versehen. Sonst eigene CSS/SVG-Grafik oder zulässig erzeugte Illustration verwenden. Keine irreführenden Produktabbildungen und keine ungeprüften externen Fonts/Skripte einbinden.
5. Affiliate-CTAs mit dem übergebenen exakten Link setzen und direkt sichtbar mit „Werbung“ oder „Anzeige“ kennzeichnen. Externe Links mit `rel="sponsored noopener noreferrer"` versehen; bei `target="_blank"` eine neue Registerkarte kenntlich machen. Footer mit Impressum, Datenschutz, Cookie-Einstellungen und Werbehinweis erreichbar halten.
6. Passende bestehende Kategorie wählen oder eine sinnvolle neue Kategorie samt Filterlogik anlegen. Eine gekennzeichnete Produktkarte in `index.html` ergänzen und weitere thematisch sinnvolle interne Links setzen. `sitemap.xml` mit eindeutiger sauberer URL und aktuellem `lastmod` aktualisieren; `robots.txt` nur bei echtem Bedarf ändern.
7. Vor Veröffentlichung Impressum und Datenschutz gegen tatsächlich verwendete Dienste, Partnerziele, Assets und Hosting abgleichen und bei Bedarf aktualisieren. Vor jeder Tracking-ID zusätzlich `TRACKING-SETUP.md` abarbeiten.

## 4. Qualitätssicherung

1. `python scripts/check_affiliate_site.py --page <slug>.html --product-url "<Produkt-URL>" --affiliate-link "<exakter Link>"` ausführen. Das Skript prüft beide HTTPS-URLs syntaktisch und die exakte Übernahme des Affiliate-Links samt Query und Fragment. Alle gemeldeten internen Fehler beheben und erneut ausführen. Das Projekt hat keinen Build; die HTML-/Link-/Sitemap-Prüfung ist der technische Ersatz, ergänzt um Browserprüfung. Jeder Partnerlink braucht einen zugänglichen Linknamen mit „Werbung“ oder „Anzeige“ und eine direkt sichtbare Kennzeichnung.
2. Seite lokal oder in einer Vorschau auf Desktop und schmalem Mobilbildschirm öffnen. Layout, Bilder, Tastaturfokus, Cookie-Dialog, interne Links und CTA-Ziel prüfen. Keine horizontal abgeschnittenen Inhalte oder defekten Assets.
3. `git diff --check`, `git diff`, `git status` prüfen. Keine doppelten URLs, fremden Änderungen, Zugangsdaten oder versehentlich generierten Dateien veröffentlichen. Bei relevanten Korrekturen erneut prüfen.
4. Bei fehlerhaftem Build beziehungsweise statischer Prüfung, beschädigten bestehenden Seiten, fehlender Affiliate-Kennzeichnung, fehlenden Berechtigungen, nicht autorisierten Änderungen oder anderen Sicherheits-/Rechtsproblemen nicht pushen; Grund und nächsten Schritt berichten. Ein nur extern blockierter Attributionstest ist als Warnung zu dokumentieren und sperrt die Veröffentlichung bei ausdrücklichem Auftrag nicht. Sind wesentliche Produktfakten unbelegt, keine Behauptungen dazu veröffentlichen; fehlen die Grundlagen für eine sachliche Seite, den Auftrag anhalten.

## 5. Veröffentlichen und live prüfen

Bei ausdrücklichem Veröffentlichungsauftrag nach bestandenen internen Prüfungen automatisch committen und pushen, auch wenn die externe Affiliate-Zuordnung wegen Schutzmaßnahmen nicht verifiziert werden konnte. Nur auftragsbezogene Dateien einzeln stagen. Aussagekräftigen Commit erstellen. Vor Push sicherstellen, dass `main` aktuell und der Remote der erwartete ist; bei Divergenz sauber integrieren, nie Force-Push. `git push origin main` löst den bestehenden Vercel-Workflow aus. Deployment-Status über verfügbare Vercel-/GitHub-Oberfläche oder die Live-Site prüfen; keinen Erfolg aus dem Git-Push allein ableiten. Die öffentliche URL `/slug` abrufen und Status, Title, H1, exakten CTA-Link einschließlich Fragment, CSS/Assets und interne Verlinkung kontrollieren. Bei Verzögerung erneut prüfen und einen noch offenen Status ausdrücklich melden.

## 6. Bericht

Mit `AFFILIATE-AGENT – AUFTRAG ABGESCHLOSSEN` abschließen und Produktname, Kategorie, Hauptkeyword, Landingpage-URL, Affiliate-Link integriert (Ja/Nein), Affiliate-Zuordnung nachgewiesen (Ja/Nein/nicht verifiziert), SEO eingerichtet (Ja/Nein), Produktübersicht aktualisiert (Ja/Nein), technische Prüfung erfolgreich (Ja/Nein; kein Build vorhanden), Deployment erfolgreich (Ja/Nein), Live-Website geprüft (Ja/Nein), Commit und relevante Quellen angeben. Externe Schutzmaßnahmen als Warnung nennen und nie eine nicht nachgewiesene Affiliate-Zuordnung als erfolgreich getestet darstellen. Bei Abbruch `AFFILIATE-AGENT – NICHT VERÖFFENTLICHT` mit genauem Fehler und erforderlichem nächsten Schritt verwenden; keinen Erfolg behaupten.

## Probelauf dieses Agenten

Die bestehende reale Seite `funnel-cockpit.html` kann als Prüfobjekt für das Hilfsskript dienen. Dadurch werden weder ein erfundenes Produkt noch neue Dateien auf der Live-Site veröffentlicht. Eine tatsächliche neue Veröffentlichung wird erst mit einem künftigen Aufruf mit Produkt-URL und Affiliate-Link vollständig durchlaufen.
