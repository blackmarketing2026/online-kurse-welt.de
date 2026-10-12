# Digistore24 – Affiliate-Daten und Link-Aufbau

## Affiliate-ID

**Digistore24-Affiliate-ID:** `mysticmarketing`

## Link-Aufbau (Promolink)

```
https://www.checkout-ds24.com/redir/<PRODUKT-ID>/<AFFILIATE-ID>/<CAMPAIGN-KEY>
```

| Teil | Bedeutung | Beispiel |
|---|---|---|
| `<PRODUKT-ID>` | Digistore24-Produkt-ID des Anbieters | `743903` |
| `<AFFILIATE-ID>` | Eigene Affiliate-ID | `mysticmarketing` |
| `<CAMPAIGN-KEY>` | Optionales Kampagnen-Kennzeichen (frei wählbar) | `okw-teneriffa-wandern` |

**Beispiel:**

- Ohne Campaign Key: `https://www.checkout-ds24.com/redir/743903/mysticmarketing/`
- Mit Campaign Key: `https://www.checkout-ds24.com/redir/743903/mysticmarketing/okw-teneriffa-wandern`

Der Campaign Key wird in Digistore24 unter **Berichte → Transaktionen** bei jedem vermittelten Kauf angezeigt. So lässt sich auswerten, welches Produkt bzw. welche Platzierung den Verkauf gebracht hat.

## Regeln für Campaign Keys

1. **Jedes Produkt bekommt einen eigenen Campaign Key.** Nie einen Key für zwei Produkte verwenden.
2. Nur Kleinbuchstaben, Ziffern und Bindestriche, keine Leerzeichen, Umlaute oder Sonderzeichen.
3. Schema: `okw-<kurzname-des-produkts>` (z. B. `okw-bali-reisefuehrer`). Bei Bedarf eine Platzierung anhängen, z. B. `okw-bali-reisefuehrer-startseite`.
4. Einmal vergebene Keys nicht mehr ändern, sonst werden die Auswertungen unvollständig.
5. Vergebene Keys in der Tabelle unten eintragen und den fertigen Link auf der Website einbauen.
6. Keine Linkkürzer (bit.ly o. ä.) verwenden, da diese das Affiliate-Tracking stören können.
7. Der Klick setzt ein Cookie (laut Digistore24 180 Tage gültig). Das muss im [Datenschutz](datenschutz.html) erwähnt sein.

## Campaign Keys je Produkt

Nur Digistore24-Produkte (Links über `checkout-ds24.com`). Die übrigen Produkte stehen in [Produktliste.md](Produktliste.md).

| Produkt | Produkt-ID | Campaign Key | Fertiger Link |
|---|---|---|---|
| Wandern auf Teneriffa mit Kindern für Anfänger | 743903 | `okw-teneriffa-wandern` | `https://www.checkout-ds24.com/redir/743903/mysticmarketing/okw-teneriffa-wandern` |
| Bali Reiseführer | 743944 | `okw-bali-reisefuehrer` | `https://www.checkout-ds24.com/redir/743944/mysticmarketing/okw-bali-reisefuehrer` |

## Quellen

- [Digistore24 Hilfe: Getting started as an affiliate](https://help.digistore24.com/hc/en-us/articles/24291871025553-Getting-started-as-an-affiliate)
