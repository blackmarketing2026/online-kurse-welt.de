# Tracking vor der Aktivierung

Der Banner und die Lade-Sperre sind in `consent.js` eingebaut. Aktuell sind alle Kennungen in `consent-config.js` leer. Deshalb wird kein optionaler Drittanbieterdienst geladen. Die im Browser gespeicherte Entscheidung wird bei jeder Änderung dieser Konfiguration ungültig und erneut abgefragt.

## Kennungen eintragen

| Dienst | Feld in `consent-config.js` | Vor Aktivierung |
| --- | --- | --- |
| Google Analytics 4 | `googleAnalyticsId` (`G-…`) | Property, Datenaufbewahrung und Ereignisse prüfen. |
| Microsoft Clarity | `microsoftClarityId` | Consent Mode einschalten; sensible Inhalte maskieren. |
| Meta Pixel | `metaPixelId` | Ereignisse und eventuelle Zielgruppenbildung prüfen. |
| Google Tag Manager | `googleTagManagerId` (`GTM-…`) | Alle Tags, Trigger und Consent Checks prüfen; erst dann `googleTagManagerAudited: true` setzen. |

Direkte Einbindung und GTM-Einbindung desselben Dienstes dürfen nicht parallel aktiv sein. Wenn GA4, Clarity oder Meta Pixel im GTM verwaltet werden, bleibt die jeweilige direkte ID leer; die Zustimmung muss dort trotzdem für jeden Dienst einzeln beachtet werden. Der GTM-Container darf keine weiteren Tags ohne eigene passende Einwilligung auslösen. Für Google-Tags sind die vier Consent-Mode-v2-Zustände vor dem ersten Tag und bei jeder Änderung korrekt zu prüfen. Die derzeitige Marketing-Auswahl gilt nur für Meta Pixel und erteilt **keine** Zustimmung zu Google Ads.

## Pflichtprüfung vor Veröffentlichung der aktivierten Dienste

1. Datenschutzerklärung für die tatsächlichen IDs, Anbieter, Zwecke, Ereignisse, Cookie-Laufzeiten, Aufbewahrungsfristen und mögliche Drittlandübermittlungen ergänzen.
2. Ohne Entscheidung und nach „Alle ablehnen“ im Netzwerk prüfen: keine Anfragen an `googletagmanager.com`, `google-analytics.com`, `clarity.ms`, `facebook.net` oder `facebook.com` durch diese Website.
3. Jeden Dienst einzeln erlauben und prüfen, dass ausschließlich dessen Skript und zulässige Ereignisse geladen werden. GTM zusätzlich mit Tag Assistant und den tatsächlichen Container-Tags prüfen.
4. Auswahl im Footer widerrufen und erneut laden: keine weiteren Tracking-Anfragen der abgewählten Dienste. Bereits gesetzte Drittanbieter-Cookies können vom eigenen Skript nicht vollständig entfernt werden; die APIs der Anbieter und deren Einstellungen sind separat zu prüfen.
5. Im privaten Browserfenster, mobil und mit blockiertem Local Storage testen. Ablehnen und Akzeptieren müssen gleich leicht möglich sein.

Eine technische Einwilligungssperre ersetzt keine Prüfung der konkreten Anbieter-Konfiguration und der Rechtstexte vor dem Livegang.
