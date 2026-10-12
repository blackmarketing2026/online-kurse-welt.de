# Designregeln für online-kurse-welt.de

Dieses Dokument ist die verbindliche Gestaltungsgrundlage für neue Seiten und Änderungen an bestehenden Seiten. Ausgangspunkt sind die mitgelieferte Bildvorlage und die umgesetzte Startseite in `index.html` und `styles.css`. Konkrete spätere Wünsche des Nutzers haben Vorrang; nach einer abgestimmten Designänderung wird diese Datei mitgepflegt.

## Leitbild

- Die Seite wirkt hell, freundlich, ruhig und vertrauenswürdig. Viel Weißraum, zarte Blautöne und klare dunkelblaue Überschriften prägen das Bild.
- Inhalt und Navigation sind sofort verständlich. Jede Seite hat eine eindeutige Hauptüberschrift, kurze Absätze und klare nächste Schritte.
- Neue Seiten übernehmen das Erscheinungsbild der Startseite. Sie müssen nicht deren Hero oder Kurskarten kopieren, wenn der Inhalt eine andere Struktur braucht.
- Keine erfundenen Bewertungen, Kennzahlen, Anbieterinformationen oder Kursversprechen einsetzen. Beispielinhalte bleiben als solche erkennbar, bis echte Daten vorliegen.

## Farben

| Zweck | Wert | Verwendung |
| --- | --- | --- |
| Dunkelblau | `#082650` | Haupttext, Überschriften, Logo-Schrift |
| Primärblau | `#249ff5` | Buttons, Icons, aktive Elemente |
| Button-Blau | `#2b9ff2` | Primäre Handlungsaufforderung |
| Button-Hover | `#0a85df` | Hover-Zustand des primären Buttons |
| Link-Blau | `#0079e9` | Textlinks und Kursaktionen |
| Gedämpftes Blau | `#496185` | Fließtext und Hinweise |
| Helles Blau | `#eaf7ff` | Hero und sanfte Flächen |
| Abschlussband | `#e5f5fd` | Schmaler Akzent vor dem Footer |
| Linienblau | `#d7e7f4` | Karten- und Feldränder |
| Weiß | `#ffffff` | Seitenhintergrund und Karten |

Die CSS-Variablen in `styles.css` sind die technische Quelle für die Grundfarben. Neue Farben nur ergänzen, wenn ein konkreter Anwendungsfall fehlt; sie sollen zu dieser Palette passen.

## Schrift und Abstände

- Schriftfamilie: lokal eingebundenes `Inter`, ersatzweise `Arial, sans-serif`. Neue Seiten laden `fonts.css` und keine Schrift von externen Servern.
- Fließtext: 16 px auf Desktop; dunkelblau oder gedämpftes Blau, gut lesbare Zeilenhöhe.
- Überschriften: kräftig (`font-weight: 800`), dunkelblau, mit enger Laufweite. Die Startseite nutzt etwa 52 px für die Hero-Überschrift und 30 px für Abschnittsüberschriften; mobil etwa 36 px und 25 px.
- Maximalbreite des Inhalts: 1162 px. Auf Desktop mindestens 24 px Seitenabstand, mobil 16 px und höchstens 440 px Inhaltsbreite.
- Abschnitte erhalten großzügige, gleichmäßige vertikale Abstände. Karten haben 8 bis 9 px Radius, feine hellblaue Ränder und nur einen dezenten Schatten.
- Text wird für Mobilansichten umgebrochen, nicht abgeschnitten. Kein horizontaler Scrollbalken.

## Header und Navigation

- Jede Seite nutzt den weißen Header mit dem blauen Buchsymbol und dem Schriftzug `online-kurse-welt.de`. Das Logo führt zur Startseite.
- Desktop: Logo links, die Hauptnavigation in einer waagerechten Zeile. Die Startseite zeigt `Produkte entdecken`, `Kategorien`, `Ratgeber`.
- Mobil: Logo oben, Navigation darunter; alle Punkte bleiben ohne Menüzwang sichtbar und erreichbar.
- Navigationspunkte führen zu einem echten Abschnitt oder einer fertigen Seite. Solange ein Ziel noch fehlt, wird der Platzhalterzustand klar angezeigt; keine leeren Links verwenden.
- Hover und Tastaturfokus sind sichtbar. Interaktive Elemente erhalten verständliche Beschriftungen.

## Seitenaufbau

- Pro Seite genau eine `h1`; darunter eine logische Überschriftenfolge.
- Die Startseite behält ihre Abfolge: Hero mit Hauptaussage und primärem Button, Kategorien, Kursübersicht, schmales Abschlussband, Footer.
- Innenseiten verwenden denselben Header und Footer. Ihr Hauptinhalt beginnt in einem ruhigen, hellen Bereich und bleibt in einer gut lesbaren Textspalte, sofern der Inhalt kein anderes Layout erfordert.
- Primäre Buttons sind blau mit weißer Schrift und abgerundeten Ecken. Sekundäre Aktionen sind blaue Textlinks. Gleiche Aktionen erhalten auf allen Seiten die gleiche Darstellung.
- Kategoriekacheln und Kurskarten folgen dem Muster der Startseite: weißer Hintergrund, heller Rand, klares Icon beziehungsweise Bild, kurze Texte und eine eindeutige Aktion.
- Bilder sollen zum Lernen und zum jeweiligen Kursthema passen. Die aktuelle Startseite verwendet Ausschnitte der gelieferten Bildvorlage. Für spätere echte Kurse eigene passende Bilder einsetzen und Bildbeschreibungen pflegen.

### Produktseiten

- Produktseiten beginnen mit einem hellblauen Introbereich: Kategorie und Werbekennzeichnung, eine H1, Lead, Prüfdatum, Preisbox, CTA und ein belegtes Produktbild oder einen Platzhalter.
- Der Inhalt folgt der Reihenfolge aus `SEO-Produktseite-Briefing-Vorlage.md`: Worum es geht, Ablauf, belegter Umfang, Preis und Konditionen, Eignung, eigener Kauf-Check, Grenzen, FAQ und Abschluss-CTA. Anbieterangaben bleiben von redaktioneller Einordnung getrennt.
- Produktbilder werden nur bei nachgewiesenem Nutzungsrecht gezeigt. Andernfalls erscheint ein ruhiger Textplatzhalter; generische Anbieter-Platzhalter und irreführende Buch-Mockups bleiben weg.
- Die Startseite zeigt aktuelle Produkte als weiße Karten mit freigegebenem Cover oder Textfläche. Jede Karte trägt sichtbar „Werbung“ und führt zur internen Produktseite.
- Die statischen Produktseiten werden aus `generate_product_pages.py` erzeugt; zu jeder gehört ein ausgefülltes Briefing unter `produkt-briefings/`.

## Footer

- Jede Seite endet mit einem weißen Footer. Links steht die kleine Logo-Variante; rechts stehen die Footer-Links und bei Bedarf ein knapper Hinweis.
- `Impressum` und `Datenschutz` sind auf jeder Seite erreichbar.
- Unter den Footer-Links steht auf jeder Seite der Werbehinweis (`p.affiliate-disclaimer`): „**Werbehinweis:** Diese Website ist eine Affiliate-Seite. Links zu Kursen und Produkten sind Partnerlinks (Werbung). Bei einem Kauf über diese Links erhalten wir eine Provision. Der Preis ändert sich dadurch nicht.“ Er ist 11 px groß, in gedämpftem Blau, höchstens 520 px breit und auf Desktop rechtsbündig.
- Der Footer-Hinweis ersetzt nicht die Kennzeichnung am Link selbst: Jeder Partnerlink und jede Karte oder jeder Teaser mit Partnerlink wird direkt sichtbar als „Werbung“ oder „Anzeige“ gekennzeichnet.
- Auf schmalen Bildschirmen stehen Logo und Links untereinander und sind linksbündig.
- Impressum und Datenschutzhinweise beschreiben den aktuellen Stand der Website. Bei neuen Diensten, Partnerlinks oder technischen Änderungen werden sie vor der Veröffentlichung der Änderung geprüft und aktualisiert.
- „Cookie-Einstellungen“ ist auf jeder Seite im Footer erreichbar. Der Einwilligungsbanner nutzt die vorhandenen Blau- und Weißtöne; Ablehnen und Akzeptieren sind gleich leicht zu finden. Optionale Schalter sind beim ersten Aufruf ausgeschaltet.

## Responsive und Bedienung

- Ab 900 px dürfen mehrspaltige Bereiche dichter werden; bis 900 px werden Kategorien zweispaltig. Bis 650 px stehen Kurskarten einspaltig.
- Hero-Text hat auf kleinen Bildschirmen Vorrang; die Illustration rückt darunter. Buttons und Links bleiben gut antippbar.
- Filter und Dialoge müssen per Tastatur bedienbar sein. Aktive Filter werden sichtbar und mit `aria-pressed` kenntlich gemacht.
- Keine Informationen nur über Farbe vermitteln. Bilder mit inhaltlicher Bedeutung erhalten Alternativtexte oder gleichwertige Beschriftungen.

## Bei jeder neuen Seite prüfen

1. Header, Logo, Footer und rechtliche Links entsprechen diesen Regeln.
2. Farben, Schrift, Containerbreite, Karten und Buttons passen zur Startseite.
3. Desktop- und Mobilansicht funktionieren ohne abgeschnittene Inhalte.
4. Alle sichtbaren Links und Aktionen haben ein sinnvolles Ziel oder einen klaren Platzhalterzustand.
5. Änderungen am abgestimmten Erscheinungsbild werden hier dokumentiert.
6. Die neue Seite ist mit aktuellem `lastmod` in `sitemap.xml` eingetragen.
