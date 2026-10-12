/* IDs erst eintragen, wenn die jeweiligen Konten und Datenschutzhinweise bereit sind.
 * Entweder Tags direkt über die IDs unten ODER über GTM einbinden, nicht doppelt.
 * GTM erst nach Prüfung sämtlicher Trigger und zusätzlicher Consent Checks freigeben.
 */
window.ONLINE_KURSE_TRACKING = Object.freeze({
  googleAnalyticsId: '',  // G-XXXXXXXXXX
  microsoftClarityId: '', // Clarity-Projekt-ID
  metaPixelId: '',        // numerische Pixel-ID
  googleTagManagerId: '', // GTM-XXXXXXX
  googleTagManagerAudited: false
});
