(() => {
  'use strict';

  const config = window.ONLINE_KURSE_TRACKING || {};
  const storageKey = 'online-kurse-welt-consent';
  const validityMs = 180 * 24 * 60 * 60 * 1000;
  const services = ['googleAnalytics', 'microsoftClarity', 'metaPixel'];
  const configured = {
    googleAnalytics: /^G-[A-Z0-9]+$/.test(config.googleAnalyticsId || ''),
    microsoftClarity: /^[a-z0-9]+$/i.test(config.microsoftClarityId || ''),
    metaPixel: /^\d+$/.test(config.metaPixelId || ''),
    googleTagManager: /^GTM-[A-Z0-9]+$/.test(config.googleTagManagerId || '') && config.googleTagManagerAudited === true
  };
  const configurationKey = JSON.stringify(config);
  const none = () => ({ googleAnalytics: false, microsoftClarity: false, metaPixel: false });
  const all = () => ({ googleAnalytics: true, microsoftClarity: true, metaPixel: true });

  function readChoice() {
    try {
      const value = JSON.parse(localStorage.getItem(storageKey) || 'null');
      if (!value || value.configurationKey !== configurationKey || Date.now() - value.savedAt > validityMs) return null;
      if (!services.every(name => typeof value.services?.[name] === 'boolean')) return null;
      return value.services;
    } catch { return null; }
  }

  function writeChoice(choice) {
    try {
      localStorage.setItem(storageKey, JSON.stringify({ configurationKey, savedAt: Date.now(), services: choice }));
      return true;
    } catch { return false; }
  }

  function addScript(url) {
    const script = document.createElement('script');
    script.async = true;
    script.src = url;
    document.head.appendChild(script);
  }

  function initGoogleConsent(choice) {
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    window.gtag('consent', 'default', {
      analytics_storage: 'denied', ad_storage: 'denied',
      ad_user_data: 'denied', ad_personalization: 'denied'
    });
    window.gtag('consent', 'update', {
      analytics_storage: choice.googleAnalytics ? 'granted' : 'denied',
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied'
    });
  }

  function activate(choice) {
    const googleAllowed = (choice.googleAnalytics && configured.googleAnalytics) ||
      (configured.googleTagManager && services.some(name => choice[name]));
    if (googleAllowed) initGoogleConsent(choice);

    if (choice.googleAnalytics && configured.googleAnalytics) {
      window.gtag('js', new Date());
      window.gtag('config', config.googleAnalyticsId);
      addScript('https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(config.googleAnalyticsId));
    }

    if (configured.googleTagManager && services.some(name => choice[name])) {
      window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
      addScript('https://www.googletagmanager.com/gtm.js?id=' + encodeURIComponent(config.googleTagManagerId));
    }

    if (choice.microsoftClarity && configured.microsoftClarity) {
      window.clarity = window.clarity || function () { (window.clarity.q = window.clarity.q || []).push(arguments); };
      window.clarity('consentv2', { ad_Storage: 'denied', analytics_Storage: 'granted' });
      addScript('https://www.clarity.ms/tag/' + encodeURIComponent(config.microsoftClarityId));
    }

    if (choice.metaPixel && configured.metaPixel) {
      if (!window.fbq) {
        const fbq = function () { fbq.callMethod ? fbq.callMethod.apply(fbq, arguments) : fbq.queue.push(arguments); };
        fbq.queue = []; fbq.push = fbq; fbq.loaded = true; fbq.version = '2.0';
        window.fbq = fbq;
      }
      window.fbq('init', config.metaPixelId);
      window.fbq('track', 'PageView');
      addScript('https://connect.facebook.net/en_US/fbevents.js');
    }
  }

  function revokeActive(previous, next) {
    if (previous?.googleAnalytics && !next.googleAnalytics && window.gtag) {
      window.gtag('consent', 'update', { analytics_storage: 'denied' });
    }
    if (previous?.microsoftClarity && !next.microsoftClarity && window.clarity) {
      window.clarity('consentv2', { ad_Storage: 'denied', analytics_Storage: 'denied' });
      window.clarity('consent', false);
    }
    if (previous?.metaPixel && !next.metaPixel && window.fbq) window.fbq('consent', 'revoke');
    const cookieNames = document.cookie.split(';').map(part => part.trim().split('=')[0]);
    const host = window.location.hostname;
    const baseDomain = host.split('.').slice(-2).join('.');
    for (const name of cookieNames) {
      if (/^(_ga(?:_|$)|_gid$|_gat$|_gcl_|_fbp$|_fbc$|_clck$|_clsk$)/.test(name)) {
        document.cookie = name + '=; Max-Age=0; path=/';
        if (host.includes('.')) document.cookie = name + '=; Max-Age=0; path=/; domain=' + host;
        if (baseDomain.includes('.')) document.cookie = name + '=; Max-Age=0; path=/; domain=.' + baseDomain;
      }
    }
  }

  const panel = document.createElement('section');
  panel.className = 'consent-panel';
  panel.hidden = true;
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-modal', 'false');
  panel.setAttribute('aria-labelledby', 'consent-title');
  const inactiveNote = Object.values(configured).every(value => !value)
    ? '<p>Diese optionalen Dienste sind vorbereitet, derzeit aber noch nicht aktiv. Bei ihrer Aktivierung fragen wir Ihre Auswahl erneut ab.</p>' : '';
  panel.innerHTML = `
    <div class="consent-heading"><h2 id="consent-title">Datenschutz-Einstellungen</h2></div>
    <p>Wir möchten mit optionalen Diensten die Nutzung dieser Website auswerten und Werbung messen. Diese Dienste laden erst nach Ihrer Einwilligung. Sie können einzeln wählen oder alles ablehnen. <a href="datenschutz.html">Mehr in der Datenschutzerklärung</a>.</p>
    ${inactiveNote}
    <div class="consent-services" role="group" aria-label="Optionale Dienste">
      <label class="consent-service"><input type="checkbox" data-service="googleAnalytics"><span><strong>Google Analytics</strong><small>Besuche und Nutzung statistisch auswerten · Google Ireland Limited</small></span></label>
      <label class="consent-service"><input type="checkbox" data-service="microsoftClarity"><span><strong>Microsoft Clarity</strong><small>Nutzungsverhalten und Sitzungen analysieren · Microsoft Ireland Operations Limited</small></span></label>
      <label class="consent-service"><input type="checkbox" data-service="metaPixel"><span><strong>Meta Pixel (Facebook)</strong><small>Werbeerfolg messen und Zielgruppen bilden · Meta Platforms Ireland Limited</small></span></label>
    </div>
    <p class="consent-technical">Notwendig: Ihre Auswahl wird für höchstens sechs Monate im Browser gespeichert. Google Tag Manager kann später freigegebene Dienste verwalten und wird ebenfalls erst nach einer passenden Einwilligung geladen. Ihre Auswahl können Sie jederzeit über „Cookie-Einstellungen“ im Footer ändern.</p>
    <div class="consent-actions">
      <button type="button" data-consent-action="reject">Alle ablehnen</button>
      <button type="button" data-consent-action="save">Auswahl speichern</button>
      <button type="button" data-consent-action="accept">Alle akzeptieren</button>
    </div>`;
  document.body.appendChild(panel);

  const inputs = Object.fromEntries(services.map(name => [name, panel.querySelector(`[data-service="${name}"]`)]));
  const saved = readChoice();
  if (saved) activate(saved); else panel.hidden = false;

  document.querySelectorAll('[data-cookie-settings]').forEach(button => button.addEventListener('click', () => {
    const current = readChoice() || none();
    services.forEach(name => { inputs[name].checked = current[name]; });
    panel.hidden = false;
    inputs.googleAnalytics.focus();
  }));

  panel.querySelectorAll('[data-consent-action]').forEach(button => button.addEventListener('click', () => {
    const action = button.dataset.consentAction;
    const choice = action === 'reject' ? none() : action === 'accept' ? all() :
      Object.fromEntries(services.map(name => [name, inputs[name].checked]));
    revokeActive(readChoice(), choice);
    if (writeChoice(choice)) window.location.reload();
    else { panel.hidden = true; activate(choice); }
  }));
})();
