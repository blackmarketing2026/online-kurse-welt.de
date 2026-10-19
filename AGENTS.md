# Projektanweisungen

- Lies vor jeder Änderung an dieser Website `DESIGN.md` und halte die dort beschriebenen Gestaltungsregeln ein.
- Nutze `index.html` und `styles.css` als aktuelle technische Referenz. Bei ausdrücklich gewünschten Designänderungen aktualisiere `DESIGN.md` zusammen mit der Umsetzung.
- Prüfe vor einer Veröffentlichung, ob Impressum und Datenschutz die tatsächlich eingesetzten Dienste, Partnerlinks und Hosting-Einstellungen korrekt beschreiben.
- Vor dem Eintragen oder Aktivieren von Tracking-IDs `TRACKING-SETUP.md` lesen, die Dienstekonfiguration prüfen und die Datenschutzerklärung aktualisieren.

## Affiliate-Agent

- Bei einem Auftrag der Form `Affiliate-Agent starten. Produkt-URL: … Affiliate-Link: …` lies `AFFILIATE-AGENT.md` vollständig und führe den dort beschriebenen Ablauf für genau dieses Produkt aus. Die beiden URLs sind die Eingaben; weitere Angaben nur erfragen, wenn eine wesentliche Tatsache nicht zuverlässig recherchierbar ist.
- Ein vom Nutzer ausdrücklich bereitgestellter Affiliate-Link ist für die Verwendung freigegeben. Prüfe seine Syntax und übernimm ihn unverändert einschließlich Query-Parametern und Fragment. Ein nicht nachweisbarer externer Attributionstest, etwa wegen HTTP 429, Captcha oder Bot-Schutz, ist als „nicht verifiziert“ zu dokumentieren und allein kein Veröffentlichungsblocker. Behaupte in diesem Fall keinen erfolgreichen Attributionstest; umgehe keine Zugangssperren.
- Ein ausdrücklicher Veröffentlichungsauftrag autorisiert nach bestandenen internen Prüfungen Commit und Push der auftragsbezogenen Änderungen über den bestehenden GitHub-/Vercel-Weg. Kein Force-Push und kein Löschen bestehender Inhalte. Fehlgeschlagener Build beziehungsweise statische Prüfung, beschädigte bestehende Seiten, fehlende Affiliate-Kennzeichnung, fehlende Berechtigungen, nicht autorisierte Änderungen sowie sonstige Sicherheits- oder Rechtsprobleme sperren die Veröffentlichung.
- Jede neue Produkt-Landingpage erhält gemäß `DESIGN.md` grundsätzlich ein eigenes, zum Produkt passendes Design. Wenn der aktuelle Auftrag ausdrücklich das bestehende Website-Design verlangt, gilt diese konkrete Vorgabe für die betroffene Seite. Die Startseite und allgemeine Seiten behalten ihr bestehendes Design.
- Ein Dateiname darf `.html` enthalten; öffentliche URLs, Canonicals, interne Links und Sitemap-Einträge dürfen es nicht. Die bestehende Vercel-Konfiguration mit `cleanUrls` bleibt maßgeblich.
