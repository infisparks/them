import os, re

with open('index.source.html', 'r', encoding='utf-8') as f:
    source = f.read()

# 1. Update relative links: './' -> '../' for subfolder 'purchase/'
processed = re.sub(r'href="\./', 'href="../', source)
processed = re.sub(r'src="\./', 'src="../', processed)
processed = re.sub(r'data-src="\./', 'data-src="../', processed)

# 2. Fix openPreviewModal calls so they reference '../'
processed = re.sub(r'openPreviewModal\(\'([^\']+)\'', r"openPreviewModal('../\1'", processed)

# 3. Replace card action bars: Preview button becomes Download ZIP button + Live Demo
def replace_card_footer(match):
    full = match.group(0)
    m_url = re.search(r'openPreviewModal\(\'([^\']+)\',\s*\'([^\']+)\'\)', full)
    if not m_url:
        return full
    path = m_url.group(1)
    title = m_url.group(2)
    clean_folder = path.replace('../', '').split('/')[0]
    zip_url = f'../downloads/{clean_folder}.zip'

    return f'''<div class="flex items-center gap-1 pt-1.5 border-t border-slate-100 mt-1">
            <a href="{zip_url}" download class="flex-1 bg-emerald-600 hover:bg-emerald-700 text-white text-[9.5px] sm:text-[11px] font-black py-1.5 px-1.5 rounded-lg flex items-center justify-center gap-1 shadow-xs transition-colors">
              <i class="fa-solid fa-download text-[9px]"></i>
              <span>Download ZIP</span>
            </a>
            <button onclick="openPreviewModal('{path}', '{title}')" class="bg-slate-100 hover:bg-slate-200 text-slate-700 text-[9.5px] sm:text-[11px] font-bold py-1.5 px-2 rounded-lg" title="Live Preview">
              <i class="fa-solid fa-eye text-[8.5px]"></i>
            </button>
            <a href="{path}" target="_blank" class="bg-slate-100 hover:bg-slate-200 text-slate-700 text-[9.5px] sm:text-[11px] font-bold py-1.5 px-2 rounded-lg" title="Open in New Tab">
              ↗
            </a>
          </div>'''

processed = re.sub(r'<div class="flex items-center gap-1 pt-1\.5 border-t border-slate-100 mt-1">.*?</div>\s*</div>\s*(?=<!--|<div class="card-phone-unit|\n\s*</div>)', replace_card_footer, processed, flags=re.DOTALL)

# 4. Title & Header adjustments
processed = processed.replace(
    '<title>45+ Ultimate Landing Page Bundle | Just ₹299 (Live Mobile Screens)</title>',
    '<title>Customer License Vault &amp; Downloads | 45+ Ultimate Landing Page Bundle</title>'
)

# 5. Verification Modal HTML
verification_modal = '''
  <!-- License Verification Gate Modal -->
  <div id="licenseGateModal" class="fixed inset-0 z-50 bg-slate-950/90 backdrop-blur-md flex items-center justify-center p-3 sm:p-4">
    <div class="relative w-full max-w-md bg-white rounded-3xl p-6 sm:p-7 border border-amber-300 shadow-2xl text-center space-y-4">
      <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-amber-400 to-amber-600 flex items-center justify-center mx-auto text-slate-950 text-2xl shadow-md">
        <i class="fa-solid fa-crown"></i>
      </div>
      <div>
        <div class="inline-flex items-center gap-1.5 bg-amber-50 border border-amber-300 text-amber-900 text-[10px] font-black px-2.5 py-0.5 rounded-full uppercase tracking-wider mb-2">
          <span>Official Customer Download Vault</span>
        </div>
        <h2 class="text-xl font-black text-slate-950 tracking-tight">Customer License Verification</h2>
        <p class="text-xs text-slate-600 mt-1.5 leading-relaxed">
          Please enter your registered WhatsApp number and License Key to access and download all 45+ template source codes.
        </p>
      </div>

      <form id="licenseGateForm" onsubmit="handleVerifyLicense(event)" class="space-y-3 pt-1 text-left">
        <div>
          <label class="block text-[11px] font-bold text-slate-800 mb-1">
            Registered WhatsApp Number <span class="text-rose-500">*</span>
          </label>
          <input 
            type="tel" 
            id="verifyPhoneInput" 
            required 
            placeholder="e.g. +91 9876543210" 
            class="w-full bg-slate-50 border border-slate-300 focus:border-amber-500 focus:bg-white rounded-xl px-3.5 py-2.5 text-xs font-bold text-slate-900 outline-none transition-all"
          />
        </div>

        <div>
          <label class="block text-[11px] font-bold text-slate-800 mb-1">
            License Key <span class="text-rose-500">*</span>
          </label>
          <input 
            type="text" 
            id="verifyKeyInput" 
            required 
            placeholder="e.g. LIC-45LP-XXXX-XXXX" 
            class="w-full bg-slate-50 border border-slate-300 focus:border-amber-500 focus:bg-white rounded-xl px-3.5 py-2.5 text-xs font-mono font-bold text-amber-700 uppercase outline-none transition-all"
          />
        </div>

        <div id="verifyErrorAlert" class="hidden p-2.5 rounded-xl bg-rose-50 border border-rose-200 text-rose-800 text-xs flex items-center gap-2">
          <i class="fa-solid fa-circle-exclamation text-rose-600 flex-shrink-0"></i>
          <span id="verifyErrorText">Invalid license key or WhatsApp number.</span>
        </div>

        <button 
          type="submit" 
          id="btnVerifyLicenseSubmit"
          class="w-full btn-gold-main text-xs sm:text-sm py-3.5 rounded-xl font-black shadow-md flex items-center justify-center gap-2 mt-2"
        >
          <i class="fa-solid fa-key text-xs"></i>
          <span>Verify &amp; Unlock All 45+ Downloads ⚡</span>
        </button>

        <p class="text-[10.5px] text-slate-500 text-center pt-1">
          Need assistance? WhatsApp Support: <a href="https://wa.me/919951231231?text=Hi,%20I%20need%20help%20with%20my%20license%20key" target="_blank" class="font-bold text-amber-700 underline">Chat with Us</a>
        </p>
      </form>
    </div>
  </div>
'''

# 6. Header replacement
new_header = '''
  <!-- 1. Customer Portal Header -->
  <header class="sticky top-0 z-40 backdrop-blur-xl bg-white/95 border-b border-gold-500/20 shadow-2xs">
    <div class="max-w-7xl mx-auto px-3 sm:px-6 h-12 sm:h-14 flex items-center justify-between">
      <a href="#" class="flex items-center space-x-2 group">
        <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg bg-gradient-to-br from-gold-400 to-amber-600 p-0.5 shadow-sm flex items-center justify-center">
          <div class="w-full h-full bg-white rounded-[6px] flex items-center justify-center">
            <i class="fa-solid fa-crown text-gold-600 text-xs sm:text-sm"></i>
          </div>
        </div>
        <div class="flex flex-col text-left">
          <span class="text-xs sm:text-sm font-black tracking-tight text-slate-900 leading-none">
            DigitalTheme<span class="text-gold-600">.Store</span>
          </span>
          <span class="text-[8px] sm:text-[9px] text-emerald-700 font-bold uppercase tracking-wider flex items-center gap-1">
            <i class="fa-solid fa-shield-check text-[8px]"></i> Licensed Download Vault
          </span>
        </div>
      </a>

      <div class="flex items-center space-x-2 sm:space-x-3">
        <div id="customerHeaderBadge" class="hidden sm:flex items-center gap-2 bg-amber-50 border border-amber-300/80 px-2.5 py-1 rounded-lg text-xs">
          <i class="fa-solid fa-user-check text-amber-600 text-xs"></i>
          <span id="headerCustomerName" class="font-black text-slate-900">Customer</span>
          <span id="headerCustomerKey" class="font-mono text-[11px] font-bold text-amber-800 bg-amber-200/60 px-1.5 py-0.2 rounded">KEY</span>
        </div>
        <a href="../downloads/complete-45-landing-pages-bundle.zip" download class="btn-gold-main text-[10px] sm:text-xs py-1.5 px-2.5 sm:px-3.5 rounded-lg flex items-center space-x-1.5 shadow-xs">
          <i class="fa-solid fa-file-zipper text-[10px]"></i>
          <span>Bundle ZIP (128 MB)</span>
        </a>
        <button onclick="lockPortalSession()" class="text-slate-400 hover:text-rose-600 text-xs p-1.5" title="Lock / Change License">
          <i class="fa-solid fa-arrow-right-from-bracket"></i>
        </button>
      </div>
    </div>
  </header>
'''

# 7. Hero & Verified Banner
new_hero = '''
  <!-- 2. Customer Hero Banner & License Rights -->
  <section class="pt-3 pb-2 sm:pt-4 sm:pb-3 px-3 sm:px-6 max-w-7xl mx-auto text-center space-y-3">
    
    <!-- Verified License Rights Box -->
    <div id="verifiedLicenseCard" class="bg-white border-2 border-amber-300 rounded-2xl p-3 sm:p-5 text-left shadow-md space-y-2.5 relative overflow-hidden">
      <div class="absolute top-0 right-0 bg-gradient-to-l from-amber-400 to-amber-500 text-slate-950 font-black text-[9px] sm:text-[10px] uppercase px-3 py-1 rounded-bl-xl tracking-wider shadow-2xs">
        Official Single-User Commercial License
      </div>
      
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pr-28 sm:pr-0">
        <div class="flex items-center gap-2.5">
          <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center text-lg flex-shrink-0">
            <i class="fa-solid fa-certificate"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <h2 id="licenseCardName" class="text-sm sm:text-base font-black text-slate-950">Licensed Customer</h2>
              <span id="licenseCardBadge" class="bg-emerald-100 text-emerald-800 text-[10px] font-extrabold px-2 py-0.5 rounded-full">ACTIVE</span>
            </div>
            <p class="text-[11px] text-slate-500 font-mono">
              WhatsApp: <span id="licenseCardPhone" class="font-bold text-slate-800">--</span> • Key: <span id="licenseCardKey" class="font-bold text-amber-700">--</span>
            </p>
          </div>
        </div>

        <div class="flex items-center gap-2">
          <a href="../downloads/complete-45-landing-pages-bundle.zip" download class="btn-gold-main text-xs sm:text-sm font-black py-2.5 px-4 rounded-xl shadow flex items-center gap-2 flex-shrink-0">
            <i class="fa-solid fa-cloud-arrow-down text-sm"></i>
            <span>Download All 45+ Themes (Full ZIP)</span>
          </a>
        </div>
      </div>

      <!-- Legal Protection Terms: strictly no resale -->
      <div class="bg-amber-50/80 border border-amber-200/90 rounded-xl p-2.5 text-xs text-amber-950 flex items-start gap-2">
        <i class="fa-solid fa-shield-halved text-amber-600 text-sm mt-0.5 flex-shrink-0"></i>
        <div class="text-[11px] leading-relaxed">
          <strong class="font-black text-slate-900">LEGAL NOTICE &amp; NON-RESALE COVENANT:</strong>
          This license grants the registered phone holder lifetime permission to use, customize, and publish these 45+ landing pages for unlimited personal and client projects. 
          <span class="text-rose-700 font-extrabold">Re-selling, sub-licensing, sharing, or publishing the raw source code files in digital stores or repositories is strictly prohibited and subject to DMCA copyright enforcement.</span>
        </div>
      </div>
    </div>

    <!-- Color Filter Strip -->
    <div class="flex items-center gap-1 overflow-x-auto w-full max-w-3xl mx-auto pb-0.5 no-scrollbar justify-start sm:justify-center text-[10px] sm:text-xs font-bold">
      <button onclick="filterColor('all')" id="filter-all" class="color-btn active py-1 px-2.5 rounded-lg bg-gold-500 text-slate-950 font-black shadow-xs flex-shrink-0">
        All 45+
      </button>
      <button onclick="filterColor('gold')" id="filter-gold" class="color-btn py-1 px-2.5 rounded-lg bg-white border border-gold-400 text-gold-900 hover:bg-gold-50 font-black flex-shrink-0">
        🏆 Top Featured (12)
      </button>
      <button onclick="filterColor('emerald')" id="filter-emerald" class="color-btn py-1 px-2.5 rounded-lg bg-white border border-slate-200 text-emerald-800 hover:bg-emerald-50 flex-shrink-0">
        💚 Emerald (10)
      </button>
      <button onclick="filterColor('purple')" id="filter-purple" class="color-btn py-1 px-2.5 rounded-lg bg-white border border-slate-200 text-purple-800 hover:bg-purple-50 flex-shrink-0">
        💜 Purple (9)
      </button>
      <button onclick="filterColor('blue')" id="filter-blue" class="color-btn py-1 px-2.5 rounded-lg bg-white border border-slate-200 text-blue-800 hover:bg-blue-50 flex-shrink-0">
        💙 Blue (5)
      </button>
      <button onclick="filterColor('classic')" id="filter-classic" class="color-btn py-1 px-2.5 rounded-lg bg-white border border-slate-200 text-slate-700 hover:bg-slate-100 flex-shrink-0">
        🖤 Classic (10)
      </button>
    </div>
  </section>
'''

# 8. Replace Header and Hero in html
processed = re.sub(r'<!-- 1\. Ultra-Compact Top Sticky Header -->.*?<!-- 2\. Mobile Top 30% Compact Banner & Hook', new_header + '\n  <!-- 2. Mobile Top 30% Compact Banner & Hook', processed, flags=re.DOTALL)
processed = re.sub(r'<!-- 2\. Mobile Top 30% Compact Banner & Hook.*?<!-- 3\. MAIN LIVE SHOWCASE', new_hero + '\n  <!-- 3. MAIN LIVE SHOWCASE', processed, flags=re.DOTALL)

# 9. Insert Verification Modal right after <body>
processed = processed.replace(
    '<body class="bg-stone-50 text-slate-900 min-h-screen bg-light-pattern relative selection:bg-gold-400 selection:text-black pb-16 sm:pb-0">',
    '<body class="bg-stone-50 text-slate-900 min-h-screen bg-light-pattern relative selection:bg-gold-400 selection:text-black pb-16 sm:pb-0">\n' + verification_modal
)

# 10. Remove the checkout modal and mobile floating CTA
processed = re.sub(r'<!-- Instant Checkout Modal.*?<!-- Mobile Floating Sticky Bottom CTA.*?</div>\s*</div>\s*(?=<!-- Javascript Logic)', '', processed, flags=re.DOTALL)

# 11. Portal Script with Firebase RTDB
portal_script = '''
    // =========================================================================
    // 🔑 FIREBASE REALTIME DATABASE LICENSE VERIFICATION LOGIC
    // =========================================================================
    const RTDB_URL = "https://awdeveloper-f2b8a-default-rtdb.firebaseio.com";
    let currentCustomerLicense = null;

    // Check verification status on load (URL params or localStorage)
    async function checkLicenseStatus() {
      // 1. Check URL parameters (?key=... or ?phone=...&key=... or path regex)
      const urlParams = new URLSearchParams(window.location.search);
      let queryKey = urlParams.get('key') || urlParams.get('licence') || urlParams.get('license');
      let queryPhone = urlParams.get('phone');

      // Check path e.g. /purchase/995123123123/licence/
      const pathMatch = window.location.pathname.match(/purchase\/([0-9+]+)\/licence/i);
      if (pathMatch && pathMatch[1]) {
        queryPhone = pathMatch[1];
      }

      if (queryKey) {
        document.getElementById('verifyKeyInput').value = queryKey;
        if (queryPhone) document.getElementById('verifyPhoneInput').value = queryPhone;
        await verifyLicenseWithFirebase(queryKey, queryPhone);
        return;
      }

      // 2. Check localStorage
      const cached = localStorage.getItem('digital_theme_license');
      if (cached) {
        try {
          const parsed = JSON.parse(cached);
          if (parsed && parsed.key) {
            applyVerifiedLicense(parsed);
            return;
          }
        } catch (e) {}
      }

      // 3. Otherwise show verification modal
      showVerificationModal();
    }

    async function verifyLicenseWithFirebase(key, phone) {
      const btn = document.getElementById('btnVerifyLicenseSubmit');
      const errAlert = document.getElementById('verifyErrorAlert');
      const errText = document.getElementById('verifyErrorText');
      if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Verifying License...';
      }
      if (errAlert) errAlert.classList.add('hidden');

      try {
        const safeKeyId = key.trim().toUpperCase().replace(/[^a-zA-Z0-9_-]/g, '_');
        const res = await fetch(RTDB_URL + '/licenses/' + safeKeyId + '.json');
        const data = await res.json();

        if (!data || data.status === 'revoked') {
          throw new Error("Invalid or revoked license key. Please check your key or contact support.");
        }

        // Check phone if entered
        if (phone && phone.trim() !== '' && data.phone) {
          const cleanInputPhone = phone.replace(/[^0-9]/g, '');
          const cleanLicPhone = data.phone.replace(/[^0-9]/g, '');
          if (cleanInputPhone.length >= 10 && cleanLicPhone.length >= 10) {
            if (!cleanLicPhone.endsWith(cleanInputPhone.slice(-10))) {
              throw new Error("This license key belongs to WhatsApp number ending in ..." + cleanLicPhone.slice(-4) + ".");
            }
          }
        }

        // Successfully verified
        applyVerifiedLicense(data);
        localStorage.setItem('digital_theme_license', JSON.stringify(data));
      } catch (err) {
        if (errText) errText.innerText = err.message;
        if (errAlert) errAlert.classList.remove('hidden');
        showVerificationModal();
      } finally {
        if (btn) {
          btn.disabled = false;
          btn.innerHTML = '<i class="fa-solid fa-key text-xs"></i> <span>Verify &amp; Unlock All 45+ Downloads ⚡</span>';
        }
      }
    }

    function applyVerifiedLicense(data) {
      currentCustomerLicense = data;
      document.getElementById('licenseGateModal').classList.add('hidden');

      // Update UI with customer information
      const name = data.name || 'Verified Customer';
      const phone = data.phone || '';
      const key = data.key || 'LIC-ACTIVE';

      const custBadge = document.getElementById('customerHeaderBadge');
      if (custBadge) custBadge.classList.remove('hidden');
      const headName = document.getElementById('headerCustomerName');
      if (headName) headName.innerText = name;
      const headKey = document.getElementById('headerCustomerKey');
      if (headKey) headKey.innerText = key;

      const cardName = document.getElementById('licenseCardName');
      if (cardName) cardName.innerText = name;
      const cardPhone = document.getElementById('licenseCardPhone');
      if (cardPhone) cardPhone.innerText = phone;
      const cardKey = document.getElementById('licenseCardKey');
      if (cardKey) cardKey.innerText = key;
    }

    function showVerificationModal() {
      document.getElementById('licenseGateModal').classList.remove('hidden');
    }

    function lockPortalSession() {
      if (confirm('Lock session and re-enter license key?')) {
        localStorage.removeItem('digital_theme_license');
        window.location.reload();
      }
    }

    async function handleVerifyLicense(e) {
      e.preventDefault();
      const phone = document.getElementById('verifyPhoneInput').value.trim();
      const key = document.getElementById('verifyKeyInput').value.trim();
      if (!key) return;
      await verifyLicenseWithFirebase(key, phone);
    }

    // Intercept download clicks if unverified
    document.addEventListener('click', (e) => {
      const downloadLink = e.target.closest('a[download]');
      if (downloadLink) {
        if (!currentCustomerLicense) {
          e.preventDefault();
          alert('🔒 Please verify your License Key first to download this source code.');
          showVerificationModal();
        }
      }
    });

    document.addEventListener('DOMContentLoaded', () => {
      checkLicenseStatus();
    });
'''

# 12. Replace the script section in processed
processed = processed.replace(
    '<!-- Javascript Logic for scaling phone iframes and interactivity -->\n  <script>',
    '<!-- Javascript Logic for scaling phone iframes and interactivity -->\n  <script>\n' + portal_script
)

# Remove the checkMobileScrollPopup call if present
processed = processed.replace('setupTwoRowScrollPopup();', '// portal: no scroll popup')

os.makedirs('purchase', exist_ok=True)
with open('purchase/index.html', 'w', encoding='utf-8') as f:
    f.write(processed)

print('Generated purchase/index.html cleanly. Size:', len(processed))
