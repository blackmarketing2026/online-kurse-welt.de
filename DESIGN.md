# Designregeln für online-kurse-welt.de

Dieses Dokument beschreibt die Gestaltung der Startseite und der allgemeinen Seiten. Ausgangspunkt sind die mitgelieferte Bildvorlage und die umgesetzte Startseite in `index.html` und `styles.css`. **Produkt-Landingpages sind ausdrücklich eigenständig gestaltet** und folgen den Regeln im Abschnitt „Produkt-Landingpages“. Konkrete spätere Wünsche des Nutzers haben Vorrang; nach einer abgestimmten Designänderung wird diese Datei mitgepflegt.

## Leitbild

- Die Seite wirkt hell, freundlich, ruhig und vertrauenswürdig. Viel Weißraum, zarte Blautöne und klare dunkelblaue Überschriften prägen das Bild.
- Inhalt und Navigation sind sofort verständlich. Jede Seite hat eine eindeutige Hauptüberschrift, kurze Absätze und klare nächste Schritte.
- Allgemeine Seiten übernehmen das Erscheinungsbild der Startseite. Produkt-Landingpages bekommen jeweils ein neues, zum Produkt passendes Design.
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

Die CSS-Variablen in `styles.css` sind die technische Quelle für die Grundfarben der Startseite und allgemeinen Seiten. Affiliate-Landingpages verwenden jeweils ein eigenes Farb- und Schriftkonzept.

## Schrift und Abstände

- Schriftfamilie für allgemeine Seiten: lokal eingebundenes `Inter`, ersatzweise `Arial, sans-serif`. Affiliate-Landingpages wählen eine eigene, zum Produkt passende Typografie; Schriften werden lokal eingebunden.
- Fließtext: 16 px auf Desktop; dunkelblau oder gedämpftes Blau, gut lesbare Zeilenhöhe.
- Überschriften: kräftig (`font-weight: 800`), dunkelblau, mit enger Laufweite. Die Startseite nutzt etwa 52 px für die Hero-Überschrift und 30 px für Abschnittsüberschriften; mobil etwa 36 px und 25 px.
- Maximalbreite des Inhalts: 1162 px. Auf Desktop mindestens 24 px Seitenabstand, mobil 16 px und höchstens 440 px Inhaltsbreite.
- Abschnitte erhalten großzügige, gleichmäßige vertikale Abstände. Karten haben 8 bis 9 px Radius, feine hellblaue Ränder und nur einen dezenten Schatten.
- Text wird für Mobilansichten umgebrochen, nicht abgeschnitten. Kein horizontaler Scrollbalken.

## Header und Navigation

- Allgemeine Seiten nutzen den weißen Header mit dem blauen Buchsymbol und dem Schriftzug `online-kurse-welt.de`. Auf Produkt-Landingpages darf der Header anders gestaltet sein; ein klarer Link zur Startseite bleibt erhalten.
- Desktop: Logo links, die Hauptnavigation in einer waagerechten Zeile. Die Startseite zeigt `Produkte entdecken`, `Kategorien`, `Ratgeber`.
- Mobil: Logo oben, Navigation darunter; alle Punkte bleiben ohne Menüzwang sichtbar und erreichbar.
- Navigationspunkte führen zu einem echten Abschnitt oder einer fertigen Seite. Solange ein Ziel noch fehlt, wird der Platzhalterzustand klar angezeigt; keine leeren Links verwenden.
- Hover und Tastaturfokus sind sichtbar. Interaktive Elemente erhalten verständliche Beschriftungen.

## Seitenaufbau

- Pro Seite genau eine `h1`; darunter eine logische Überschriftenfolge.
- Die Startseite behält ihre Abfolge: Hero mit Hauptaussage und primärem Button, Kategorien, Kursübersicht, schmales Abschlussband, Footer.
- Allgemeine Innenseiten verwenden denselben Header und Footer. Produkt-Landingpages gestalten Aufbau und Seitenrhythmus eigenständig.
- Primäre Buttons sind blau mit weißer Schrift und abgerundeten Ecken. Sekundäre Aktionen sind blaue Textlinks. Gleiche Aktionen erhalten auf allen Seiten die gleiche Darstellung.
- Kategoriekacheln und Kurskarten folgen dem Muster der Startseite: weißer Hintergrund, heller Rand, klares Icon beziehungsweise Bild, kurze Texte und eine eindeutige Aktion.
- Bilder sollen zum Lernen und zum jeweiligen Kursthema passen. Die aktuelle Startseite verwendet Ausschnitte der gelieferten Bildvorlage. Für spätere echte Kurse eigene passende Bilder einsetzen und Bildbeschreibungen pflegen.

### Produkt-Landingpages

- **Jede neu erstellte oder gestalterisch überarbeitete Affiliate-Landingpage erhält ein vollständig eigenes Design, das zu Produkt, Zielgruppe und Angebot passt.** Farben, Typografie, Bildsprache, Hero, Karten, Abschnittsfolge und CTA-Gestaltung werden dafür neu entwickelt. Die Startseite, die frühere FunnelCockpit-Seite und die KI-Training-Seite sind keine Gestaltungsvorlagen.
- Die Leserführung folgt **AIDA**: Attention im Hero mit einer belegbaren, zur Suchintention passenden Aussage; Interest durch verständliche Produkt- und Inhaltsinformationen; Desire durch konkreten belegten Nutzen, Eignung, Preis, Grenzen und Kauf-Check; Action durch einen klaren Weg zur Anbieter-Seite. Die visuelle Umsetzung und die Reihenfolge einzelner Informationsblöcke bleiben produktspezifisch. AIDA darf keine unbelegten Erfolgsversprechen, Druck oder künstliche Knappheit erzeugen.
- Primäre Affiliate-Buttons heißen bei einem belegten Kursformat **„Jetzt zum Online-Kurs“**, bei einem anderen Online-Produkt **„Jetzt zum Online-Produkt“**. Das Buttonziel bleibt der vom Nutzer gelieferte vollständige Affiliate-Link. Die unmittelbar zugeordnete Kennzeichnung „Werbung“ oder „Anzeige“ und der zugängliche Linkname erklären Produkt, Ziel und gegebenenfalls die neue Registerkarte.
- Jede Affiliate-Landingpage verwendet eine eigene CSS-Datei und lädt `styles.css` nicht als visuelle Basis. Technische Konventionen wie saubere URLs, Einwilligung und erreichbare Rechtsseiten bleiben erhalten. Eine klare Seitenstruktur, gute Lesbarkeit, mobile Bedienbarkeit und sichtbare Tastaturfokusse sind Pflicht.
- Produktinformationen werden mit Quellen belegt. Preis, Vertragsmodell, Eignung, Grenzen, FAQ und ein eigener Kauf-Check sind sinnvoll, aber ihre Reihenfolge und visuelle Form richten sich nach dem jeweiligen Produkt. Anbieterangaben bleiben von redaktioneller Einordnung getrennt.
- Produktbilder und Markenmaterial von der offiziellen Landingpage dürfen lokal importiert und passend eingesetzt werden. Quelle und Nutzungsrecht beziehungsweise Freigabe für die Partnerwerbung werden geprüft und dokumentiert; Bilder erhalten aussagekräftige Alternativtexte. Wenn kein verwendbares Bild vorliegt, wird ein eigenes grafisches Element gestaltet.
- Passende Originalbilder der verlinkten Anbieter-Website beziehungsweise offizielle Partner-Werbemittel werden bevorzugt. Die konkrete Quelle und die Grundlage der werblichen Nutzung stehen in `BILDQUELLEN.md`. Enthält ein Cover Einkommens- oder Garantieaussagen, wird es unmittelbar als Anbieterwerbung eingeordnet.
- Partnerlinks und werbliche Bereiche werden direkt sichtbar als „Werbung“ oder „Anzeige“ gekennzeichnet. Preis- und Leistungsversprechen werden nicht erfunden.
- Die Startseite zeigt aktuelle Produkte als weiße Karten mit freigegebenem Cover oder Textfläche. Jede Karte trägt sichtbar „Werbung“ und führt zur internen Produktseite.
- Die Kategorien der Startseite können auch Softwareprodukte für Online-Business aufnehmen. Drei Kacheln stehen auf Desktop nebeneinander, auf kleinen Bildschirmen zweispaltig.
- Bestehende statische Produktseiten können aus `generate_product_pages.py` erzeugt werden; neue Landingpages dürfen individuell umgesetzt werden. Interne Links, Canonicals und die Sitemap verwenden die URLs ohne `.html`; Vercel liefert die HTML-Dateien über diese URLs aus.

## Footer

- Allgemeine Seiten enden mit dem weißen Standard-Footer. Produkt-Landingpages dürfen einen eigenen Footer gestalten; Impressum, Datenschutz, Cookie-Einstellungen und Werbehinweis bleiben erreichbar.
- `Impressum` und `Datenschutz` sind auf jeder Seite erreichbar.
- Unter den Footer-Links steht auf jeder Seite der Werbehinweis (`p.affiliate-disclaimer`): „**Werbehinweis:** Diese Website ist eine Affiliate-Seite. Links zu Kursen und Produkten sind Partnerlinks (Werbung). Bei einem Kauf über diese Links erhalten wir eine Provision. Der Preis ändert sich dadurch nicht.“ Auf allgemeinen Seiten ist er 11 px groß, in gedämpftem Blau, höchstens 520 px breit und auf Desktop rechtsbündig. Produkt-Landingpages dürfen ihn passend zum eigenen Footer gestalten, solange er gut lesbar bleibt.
- Der Footer-Hinweis ersetzt nicht die Kennzeichnung am Link selbst: Jeder Partnerlink und jede Karte oder jeder Teaser mit Partnerlink wird direkt sichtbar als „Werbung“ oder „Anzeige“ gekennzeichnet.
- Auf schmalen Bildschirmen stehen Logo und Links untereinander und sind linksbündig.
- Impressum und Datenschutzhinweise beschreiben den aktuellen Stand der Website. Bei neuen Diensten, Partnerlinks oder technischen Änderungen werden sie vor der Veröffentlichung der Änderung geprüft und aktualisiert.
- „Cookie-Einstellungen“ ist auf jeder Seite im Footer erreichbar. Der Einwilligungsbanner bleibt gut lesbar; Ablehnen und Akzeptieren sind gleich leicht zu finden. Optionale Schalter sind beim ersten Aufruf ausgeschaltet.

## Responsive und Bedienung

- Ab 900 px dürfen mehrspaltige Bereiche dichter werden; bis 900 px werden Kategorien zweispaltig. Bis 650 px stehen Kurskarten einspaltig.
- Hero-Text hat auf kleinen Bildschirmen Vorrang; die Illustration rückt darunter. Buttons und Links bleiben gut antippbar.
- Filter und Dialoge müssen per Tastatur bedienbar sein. Aktive Filter werden sichtbar und mit `aria-pressed` kenntlich gemacht.
- Keine Informationen nur über Farbe vermitteln. Bilder mit inhaltlicher Bedeutung erhalten Alternativtexte oder gleichwertige Beschriftungen.

## Bei jeder neuen Seite prüfen

1. Header, Logo, Footer und rechtliche Links entsprechen dem Seitentyp und diesen Regeln.
2. Allgemeine Seiten passen gestalterisch zur Startseite; Produkt-Landingpages haben ein eigenständiges, zum Produkt passendes Design.
3. Desktop- und Mobilansicht funktionieren ohne abgeschnittene Inhalte.
4. Alle sichtbaren Links und Aktionen haben ein sinnvolles Ziel oder einen klaren Platzhalterzustand.
5. Änderungen am abgestimmten Erscheinungsbild werden hier dokumentiert.
6. Die neue Seite ist mit aktuellem `lastmod` in `sitemap.xml` eingetragen.

## Produktbild-Umsetzung vom 19. Oktober 2026

Die Landingpage „Internet Geld Geheimnis“ zeigt das offizielle Produkt-Mockup im Hero und das Cover des Digistore24-Checkouts im Faktenabschnitt. Die eigenständige grün-cremefarbene Gestaltung bleibt erhalten. Beide Bilder sind lokal eingebunden und mit einer direkt zugeordneten Einordnung der nicht überprüften Werbeaussagen versehen. Quellen und Nutzungsgrundlage sind in `BILDQUELLEN.md` dokumentiert.
