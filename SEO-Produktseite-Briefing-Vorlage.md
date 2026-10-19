# SEO-Produktseite: Briefing-Vorlage

Diese Vorlage wird **vor jeder neuen Produktseite einmal vollständig ausgefüllt** und als eigene Datei unter `produkt-briefings/<seitenpfad>.md` gespeichert. Erst danach wird die HTML-Seite gebaut.

Die Landingpage folgt **AIDA**: Attention, Interest, Desire, Action. Die Methode von **Eugene M. Schwartz** („Breakthrough Advertising“) hilft innerhalb dieser Struktur bei Blickwinkel und Formulierung: Wir greifen einen bereits vorhandenen Wunsch der Zielgruppe auf. **Weder AIDA noch Schwartz bestimmen die Fakten.** Jede Aussage muss belegt sein. Keine erfundenen Ergebnisse, Bewertungen, Knappheit oder Garantien.

**Ablauf:** 1. Fakten sammeln → 2. Preis und Link prüfen → 3. Suchintention klären → 4. Schwartz-Analyse → 5. AIDA-Struktur, Produktbilder und Video/VSL planen → 6. Seitentexte schreiben → 7. FAQ → 8. Freigabe-Check.

---

## 1. Stammdaten

| Angabe | Eintrag |
|---|---|
| Produktname (exakt wie beim Anbieter) | [eintragen] |
| Anbieter / Verkäufer | [eintragen] |
| Seitenpfad (Kleinbuchstaben, Bindestriche, Hauptkeyword) | `/[kurzname]` (Datei intern: `[kurzname].html`) |
| Kategorie auf der Website | Business & Marketing · Persönliche Entwicklung · Gesundheit & Fitness · Kreativität · [andere] |
| Sprache des Produkts | [eintragen; Quelle] |
| Status in `Produktliste.md` | ❌ Nicht eingebaut → nach Veröffentlichung ✅ Eingebaut |
| Verantwortlich für Prüfung und Freigabe | [Name] |
| Stand des Briefings | [TT.MM.JJJJ] |

## 2. Nachprüfbare Produktfakten

Nur Angaben, die auf der Verkaufsseite oder in einer anderen Quelle belegt sind. Unbelegtes bleibt leer und wird auf der Seite als offene Frage genannt.

| Angabe | Eintrag | Quelle / Abrufdatum |
|---|---|---|
| Offizielle Verkaufsseite | [URL] | |
| Produktart und Format (E-Book, Kurs, Challenge, Planer …) | [eintragen] | |
| Inhalt: Module, Kapitel, Dateien, Umfang | [eintragen] | |
| Zugang und Lieferung (Download, Login, Dauer) | [eintragen] | |
| Technische Voraussetzungen | [eintragen] | |
| Support, Updates, Rückgabe / Widerruf | [eintragen] | |
| Für wen geeignet | [eintragen, begründet] | |
| Für wen **nicht** geeignet | [eintragen, begründet] | |
| Selbst getestet? | Ja (Datum, Umfang) / **Nicht selbst getestet** | |

**Regel:** Keine Eigenschaften, Ergebnisse, Rabatte oder Garantien aus dem Produktnamen oder Werbeversprechen ableiten.

## 3. Preis

Der Preis steht **immer** auf der Seite: im Hero als Preisbox, im Abschnitt „Preis und Konditionen“ und in einer FAQ.

| Angabe | Eintrag |
|---|---|
| Produktpreis laut Verkaufsseite | [z. B. 12,99 €] |
| Endbetrag im Checkout (inkl. MwSt.) | [z. B. 15,46 € inkl. 19 % MwSt.] |
| Zahlungsmodell | Einmalzahlung / Abo (Intervall, Kündigung) / Ratenzahlung |
| Währung | [EUR / USD …] – bei Fremdwährung Hinweis auf Umrechnung |
| Zusatzkosten / Upsells im Checkout | [eintragen oder „keine sichtbar“] |
| Prüftag | [TT.MM.JJJJ] |
| Quelle | [URL des Checkouts] |
| Widersprüche zwischen Angaben? | [beschreiben oder „keine“] |

**So steht der Preis auf der Seite:** „Preis: 12,99 € (Endbetrag im Checkout: 15,46 € inkl. MwSt.) · Stand: TT.MM.JJJJ. Maßgeblich ist der Preis im Bestellschritt.“ Sind die Angaben widersprüchlich, wird das offen gesagt, statt einen Preis zu wählen.

## 4. Partnerlink mit Campaign Key (Pflicht)

Jedes Produkt bekommt **einen eigenen Campaign Key**. Regeln und Schema: siehe [Digistore24.md](Digistore24.md).

| Angabe | Eintrag |
|---|---|
| Partnerprogramm | Digistore24 / Plannerpack / [anderes] |
| Produkt-ID (bei Digistore24) | [z. B. 743903] |
| Campaign Key | `okw-[kurzname]` |
| Fertiger Partnerlink | [vollständige URL] |
| Key eingetragen in | ☐ `Digistore24.md` (bei Digistore24) ☐ `Produktliste.md` |
| Link getestet (Zielseite lädt, Key bleibt erhalten) | ☐ Ja, am [TT.MM.JJJJ] |

**Linkaufbau Digistore24:**

```
https://www.checkout-ds24.com/redir/<PRODUKT-ID>/mysticmarketing/<CAMPAIGN-KEY>
```

**Andere Partnerprogramme:** Den Campaign Key trotzdem vergeben und dokumentieren. Kann das Programm ihn nicht im Link übertragen (z. B. Plannerpack mit `#aff=mysticmarketing`), im Briefing „Key intern vergeben, im Link nicht übertragbar“ vermerken.

Auf der Seite: jeder Partnerlink mit `rel="sponsored noopener"` und `target="_blank"`, sichtbar als „Werbung“ gekennzeichnet; das `aria-label` endet auf „(Werbung)“.

## 5. Suchintention und Keywords

| Angabe | Eintrag |
|---|---|
| Hauptfrage, die die Seite beantwortet | [ein Satz] |
| Hauptkeyword | [eintragen] |
| 3–5 verwandte Suchbegriffe / Fragen | [eintragen – liefern Stoff für die FAQ] |
| Suchintention | Information · Vergleich · Kaufentscheidung |
| Suchergebnis-Check (Datum, 3–5 URLs, Beobachtung) | [eintragen] |
| Eigener Mehrwert gegenüber diesen Seiten | [konkret benennen] |
| Interne Links (passende Produkt- oder Ratgeberseiten) | [eintragen] |

Eine umformulierte Anbieterbeschreibung mit Partnerlink ist nach den [Google-Spamrichtlinien](https://developers.google.com/search/docs/essentials/spam-policies) „Thin Affiliation“. Mindestens ein eigener Mehrwert ist Pflicht: Kauf-Check, Eignung und Grenzen, Vergleich, beantwortete Fragen oder eigener Test.

## 6. Schwartz-Analyse

Diese Analyse entscheidet, **womit die Seite beginnt** und **wie die Überschrift klingt**.

### 6.1 Der vorhandene Massenwunsch

| Frage | Eintrag |
|---|---|
| Welchen Wunsch hat die Zielgruppe schon, bevor sie die Seite sieht? | [z. B. „entspannter Urlaub mit Kindern ohne Überforderung“] |
| Welches konkrete Bild hat sie dabei im Kopf? | [Szene in einem Satz] |
| Welches Hindernis steht diesem Wunsch im Weg? | [eintragen] |
| Wie stark und dringend ist der Wunsch? | gering · mittel · hoch |

### 6.2 Bewusstseinsstufe der Besucher

Die Stufe bestimmt den Einstieg. Bei Suchtraffic meist Stufe 3 oder 4.

| Stufe | Besucher weiß … | Einstieg der Seite | Gewählt |
|---|---|---|:---:|
| 1 Unbewusst | nichts vom Problem | mit Geschichte oder Szene, die sich wiedererkennt | ☐ |
| 2 Problembewusst | um das Problem, kennt keine Lösung | mit dem Problem und seinen Folgen | ☐ |
| 3 Lösungsbewusst | dass es Lösungen gibt, nicht dieses Produkt | mit dem Wunschergebnis und dem Weg dorthin | ☐ |
| 4 Produktbewusst | vom Produkt, ist unsicher | mit dem, was das Produkt konkret leistet und für wen | ☐ |
| 5 Vollständig bewusst | alles, braucht nur Preis und Link | mit Produktname, Preis und Link | ☐ |

### 6.3 Marktreife (wie viele ähnliche Versprechen kennt die Zielgruppe schon?)

| Stufe | Situation | Strategie für die Überschrift | Gewählt |
|---|---|---|:---:|
| 1 | Neues Thema | Wunsch direkt und einfach benennen | ☐ |
| 2 | Erste Konkurrenz | Versprechen konkreter machen (Zahlen, Umfang – nur belegt) | ☐ |
| 3 | Viele gleiche Versprechen | den **Mechanismus** zeigen: wie das Produkt es erreicht | ☐ |
| 4 | Mechanismen bekannt | Mechanismus präzisieren, einfacher oder vollständiger | ☐ |
| 5 | Zielgruppe ist übersättigt | über **Identifikation** einsteigen: „für wen“ statt „was“ | ☐ |

### 6.4 Mechanismus, Identifikation, Beleg

| Element | Eintrag |
|---|---|
| Mechanismus: Wie bringt das Produkt den Leser zum Ziel? (aus den Produktfakten, Abschnitt 2) | [z. B. „fünf Tagesaufgaben von der Idee bis zum Start“] |
| Identifikation: In welchem Satz erkennt sich der Leser wieder? | [z. B. „Du hast eine Idee, aber noch kein Angebot.“] |
| Belege, die es wirklich gibt (Inhaltsverzeichnis, Umfang, eigener Test) | [eintragen] |
| Steigerung: welche belegten Details machen den Nutzen greifbar? | [konkrete Kapitel, Beispiele, Zahlen] |

**Grenzen der Methode auf dieser Website:** kein Druck durch erfundene Knappheit oder Countdown, keine Einkommens-, Heil- oder Erfolgsversprechen, keine abwertenden Aussagen über Alternativen. Bei Finanz- und Gesundheitsthemen besonders zurückhaltend formulieren.

### 6.5 Überschrift und Kernaussage

| Element | Entwurf |
|---|---|
| H1 (aus Wunsch + Stufe + Marktreife, mit Hauptkeyword) | [eintragen] |
| Lead (2 Sätze: Wunsch aufgreifen, Mechanismus nennen) | [eintragen] |
| Title-Tag (max. ca. 60 Zeichen) | [eintragen] |
| Meta-Description (max. ca. 155 Zeichen, mit Preis-/Nutzenhinweis) | [eintragen] |

## 7. Produktbilder und Video/VSL

Auch das Bild folgt Schwartz: Es zeigt **das Produkt im Zusammenhang mit dem Wunsch**, nicht nur eine Datei.

| Angabe | Eintrag |
|---|---|
| Bildquelle | echtes Produktcover / eigener Screenshot / Anbieter-Pressebild |
| Nutzungsrecht geklärt? | ☐ Ja (Nachweis: [eintragen]) – ohne Nachweis Platzhalter „Produktbild derzeit nicht verfügbar“ |
| Bildaussage (welchen Teil des Wunsches zeigt es?) | [z. B. „Cover des Reiseführers vor Strandmotiv“] |
| Alt-Text (Produkt + Format + Wunschbezug, sachlich, max. ca. 125 Zeichen) | [z. B. „Cover des E-Books ‚Bali Reiseführer‘ mit 122 Tipps für die Reiseplanung“] |
| Bildunterschrift (optional, ein Satz, belegt) | [eintragen] |
| Datei | `assets/produkte/[kurzname].webp`, max. ca. 1200 px Breite, komprimiert |

**Nicht erlaubt:** Mockups, die Inhalte, Formate oder Ergebnisse zeigen, die es nicht gibt (z. B. ein gedrucktes Buch bei einem reinen E-Book), erfundene Personen mit Erfolgsergebnis, Sterne oder Siegel.

### Video Sales Letter (VSL) und weitere Videos

Prüfe die verlinkte Anbieter-Seite und offizielle Partner-Werbemittel auf passendes Videomaterial. Ist eine VSL vorhanden, plane auf der Landingpage einen sichtbaren Videobereich mit Vorschaubild oder Play-Element und einem Link zur offiziellen VSL. Wenn der vom Nutzer bereitgestellte Affiliate-Link direkt zur Seite mit der VSL führt, ist genau dieser unveränderte Link zugleich das Video-Ziel. Eine separate offizielle VSL-URL darf als Video-Link dienen; die primären Kauf-CTAs behalten den bereitgestellten Affiliate-Link. Eine bloß vermutete VSL wird nicht als vorhanden dargestellt.

| Angabe | Eintrag |
|---|---|
| VSL vorhanden und erreichbar? | Ja / Nein / nicht verifiziert; Prüftag |
| Offizielle VSL- oder Angebots-URL | [vollständige URL] |
| Ziel des Video-Links | [unveränderter Affiliate-Link oder separate offizielle VSL-URL] |
| Vorschaubild / weitere Videos | [Quelle, Produktbezug, Alt-Text beziehungsweise Beschriftung] |
| Recht zur Übernahme/Einbettung geklärt? | [Nachweis oder nur externer Video-Link] |
| Drittanbieter-Player und Einwilligung | [nicht eingebettet / geprüfter Dienst, Lade-Sperre und Datenschutzhinweis] |

Video-Dateien ohne geklärte Nutzungserlaubnis nicht herunterladen oder selbst hosten. Einen externen Player nur nach Prüfung der Einbettungserlaubnis, Einwilligung und Datenschutzerklärung laden; sonst den Video-Link nutzen. Das Video als Anbieterinhalt kennzeichnen und darin gezeigte Ergebnisse nicht als eigene Prüfung darstellen. Videoquelle, Ziel-URL, Prüfdatum und Nutzungsgrundlage in `BILDQUELLEN.md` dokumentieren. Ist die externe Seite durch HTTP 429 oder Bot-Schutz nicht prüfbar, dies als „nicht verifiziert“ festhalten.

## 8. Seitenaufbau

Die vier AIDA-Phasen bilden die Leserführung. Die Tabelle zeigt eine sinnvolle Standardreihenfolge; einzelne Informationsblöcke dürfen zum Produkt passend angeordnet werden, solange alle vier Phasen erkennbar bleiben. Schwartz bestimmt den Blickwinkel innerhalb der Phasen. Gestaltung nach [DESIGN.md](DESIGN.md).

| # | Abschnitt | Inhalt | AIDA-Aufgabe |
|---|---|---|---|
| 1 | **Hero** | Eyebrow „Kategorie · Werbung“, H1, Lead, Meta-Zeile („Redaktion: online-kurse-welt.de · Anbieterangaben geprüft am … · Selbst getestet / Nicht selbst getestet“), **Preisbox** mit Prüftag, Button mit dem unveränderten Partnerlink, Werbehinweis, Produktbild | **Attention:** Suchintention und vorhandenen Wunsch wahrheitsgemäß aufgreifen |
| 2 | Brotkrumen | Startseite / Produktname | – |
| 3 | **Worum es geht** | Ausgangslage des Lesers und Hindernis, 2–4 Sätze | **Interest:** Relevanz und Produktart erklären |
| 4 | **So funktioniert es** | Ablauf bzw. Aufbau des Produkts in Schritten | **Interest:** Funktionsweise verständlich machen |
| 5 | **Das ist laut Anbieter enthalten** | Liste des Leistungsumfangs, Quelle mit Abrufdatum | **Interest:** belegte Details zeigen |
| 5a | **Video/VSL**, falls vorhanden | Sichtbarer Videobereich mit Link zur offiziellen VSL, Quellen- und Werbehinweis; bei separater VSL-URL bleiben Kauf-CTAs auf dem freigegebenen Affiliate-Link | **Interest:** Anbietererklärung zugänglich machen, ohne Ergebnisse zu übernehmen |
| 6 | **Preis und Konditionen** | Preis, Endbetrag, Zahlungsmodell, Zusatzkosten, Rückgabe, Prüftag | **Desire:** Nutzen und Kosten ehrlich abwägen |
| 7 | **Für wen passt es – und für wen nicht** | zwei kurze Listen | **Desire:** Eignung und Grenzen konkretisieren |
| 8 | **Unser Kauf-Check** | eigener Mehrwert: Prüffragen oder Test | **Desire:** Entscheidung mit Belegen unterstützen |
| 9 | **Grenzen und offene Fragen** | was nicht belegt oder nicht getestet ist | **Desire:** Unsicherheit transparent machen |
| 10 | **Häufige Fragen** | FAQ, siehe Abschnitt 9 | **Desire:** entscheidungsrelevante Fragen beantworten |
| 11 | **Abschluss-CTA** | Aufforderung zur eigenen Prüfung, Button „Jetzt zum Online-Kurs“ oder „Jetzt zum Online-Produkt“ mit demselben unveränderten Partnerlink, „Werbung · Partnerlink“ | **Action:** klar zum Anbieter führen |
| 12 | Weitere Seiten | 1–3 interne Links | – |

**CTA-Regel:** Bei einem tatsächlich belegten Online-Kurs lautet der Text jedes primären Affiliate-Buttons exakt **„Jetzt zum Online-Kurs“**; bei einem anderen Online-Produkt exakt **„Jetzt zum Online-Produkt“**. Bei unklarem Format zunächst recherchieren. Die Werbekennzeichnung steht direkt am Button. Der zugängliche Linkname nennt zusätzlich Produkt, Anbieterziel und gegebenenfalls das Öffnen in einem neuen Tab. Sekundäre interne Navigationslinks dürfen beschreibende Texte tragen.

**Stil:** Du-Form wie auf der Startseite, kurze Sätze, aktive Verben, konkrete Bilder statt Superlative. Jeder Absatz beantwortet eine Frage, die der Leser an dieser Stelle hat.

## 9. FAQ (immer am Ende der Seite, vor dem Abschluss-CTA)

5–8 Fragen. Quellen: verwandte Suchbegriffe aus Abschnitt 5, Einwände aus der Schwartz-Analyse, offene Punkte der Verkaufsseite.

**Pflichtfragen:**

1. **Was kostet [Produkt]?** – Preis, Endbetrag, Zahlungsmodell, Prüftag.
2. **Für wen ist [Produkt] geeignet?**
3. **In welcher Sprache und in welchem Format erhalte ich [Produkt]?**
4. **Gibt es eine Rückgabe oder Garantie?** – nur mit Beleg, sonst „auf der Verkaufsseite nicht klar angegeben“.
5. **Garantiert [Produkt] ein bestimmtes Ergebnis?** – ehrliche Antwort.

| Frage | Antwort (2–4 Sätze, belegt) |
|---|---|
| [Pflichtfrage 1] | [eintragen] |
| [Pflichtfrage 2] | [eintragen] |
| [Pflichtfrage 3] | [eintragen] |
| [Pflichtfrage 4] | [eintragen] |
| [Pflichtfrage 5] | [eintragen] |
| [Zusatzfrage aus Suchbegriffen] | [eintragen] |

Umsetzung: Frage als `h3`, Antwort als `p`. Strukturierte Daten (`FAQPage`) sind erlaubt, wenn Fragen und Antworten sichtbar auf der Seite stehen. Google zeigt FAQ-Rich-Results allerdings nur noch für wenige behördliche und Gesundheitsseiten an: [Google zu FAQ-Daten](https://developers.google.com/search/docs/appearance/structured-data/faqpage).

## 10. Pflichtangaben auf der fertigen Seite

- **Werbekennzeichnung:** „Werbung“ im Eyebrow und direkt bei jedem Partnerlink; zusätzlich der Werbehinweis im Footer. Partnerlinks mit `rel="sponsored"`: [Google zu bezahlten Links](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links).
- **Preis mit Prüftag** und Hinweis, dass der Preis im Bestellschritt maßgeblich ist.
- **Autorschaft und Prüfstatus** in der Meta-Zeile, inklusive „Nicht selbst getestet“, falls zutreffend: [Google zu hilfreichen Inhalten](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).
- **Quellen** für den Leistungsumfang mit Abrufdatum intern dokumentieren und im Abschlussbericht nennen; keinen gesonderten öffentlichen Abschnitt „Quellen & Prüfstand“ oder ähnlichen Prüfprotokoll-Block auf der Landingpage anlegen. Wesentliche Einschränkungen direkt bei den betreffenden Aussagen erklären.
- **Strukturierte Daten** nur für sichtbare, belegte Angaben. Keine Merchant-Listing-Auszeichnung, da der Kauf extern stattfindet: [Google zu Merchant Listings](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing).
- **Keine erfundenen Bewertungen**, Sterne, Testimonials, Erfolgszahlen oder Knappheit.

## 11. Freigabe-Check

- [ ] Alle Fakten in Abschnitt 2 und 3 haben eine Quelle mit Datum.
- [ ] Campaign Key vergeben, Link getestet, in `Digistore24.md` bzw. `Produktliste.md` eingetragen.
- [ ] H1, Lead und Abschnitte folgen der gewählten Bewusstseinsstufe und Marktreife.
- [ ] Attention, Interest, Desire und Action sind in dieser Reihenfolge erkennbar; Nutzen und Dringlichkeit gehen nicht über die Belege hinaus.
- [ ] Keine Aussage geht über die Belege hinaus.
- [ ] Produktbild mit geklärtem Nutzungsrecht und Alt-Text – oder Platzhalter.
- [ ] Verfügbare Anbieterbilder und Videos geprüft; vorhandene VSL als sichtbarer Video-Link eingebaut, Ziel und Nutzungsgrundlage in `BILDQUELLEN.md` dokumentiert.
- [ ] Bei eingebettetem Drittanbieter-Player Einbettungserlaubnis, Einwilligungssperre und Datenschutzerklärung geprüft; sonst externer Video-Link ohne automatisches Laden.
- [ ] Preis steht im Hero, im Abschnitt „Preis und Konditionen“ und in der FAQ.
- [ ] FAQ mit allen Pflichtfragen am Seitenende.
- [ ] Jeder Partnerlink: `rel="sponsored noopener"`, sichtbar „Werbung“.
- [ ] Alle primären Affiliate-Buttons verwenden passend zum belegten Format exakt „Jetzt zum Online-Kurs“ oder „Jetzt zum Online-Produkt“ und den unveränderten Partnerlink.
- [ ] Seite in `sitemap.xml` eingetragen, Status in `Produktliste.md` auf ✅ gesetzt.
- [ ] Datenschutzerklärung nennt das Partnerprogramm.
- [ ] Desktop- und Mobilansicht geprüft.

---

## Kompakte Übergabe zum Kopieren

```text
Produktname / Anbieter:
Seitenpfad / Kategorie:
Verkaufsseite:
Leistungsumfang (mit Quelle, Abrufdatum):
Sprache / Format / Zugang:
Für wen / nicht für wen:
Selbst getestet:

Preis laut Verkaufsseite:
Endbetrag Checkout / Zahlungsmodell / Zusatzkosten:
Prüftag / Quelle:

Partnerprogramm / Produkt-ID:
Campaign Key:
Fertiger Partnerlink:

Hauptkeyword / verwandte Suchbegriffe:
Suchintention / eigener Mehrwert:

Massenwunsch / Hindernis:
Bewusstseinsstufe (1–5):
Marktreife (1–5):
Mechanismus:
Identifikationssatz:
H1 / Lead:
Attention / Interest / Desire / Action (je ein belegter Kernpunkt):
Title / Meta-Description:

Produktbild (Quelle, Recht, Alt-Text):
VSL/Video (vorhanden, Video-Link, Vorschaubild, Rechte, Einwilligung, Prüfdatum):
FAQ (Pflichtfragen + Zusatzfragen):
Interne Links:
Freigabe durch:
```
