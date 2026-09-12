import os, re

with open('index.source.html', 'r', encoding='utf-8') as f:
    source = f.read()

# 1. Update relative links: './' -> '../' for subfolder 'purchase/'
processed = re.sub(r'href="\./', 'href="../', source)
processed = re.sub(r'src="\./', 'src="../', processed)
processed = re.sub(r'data-src="\./', 'data-src="../', processed)

# 2. Fix openPreviewModal calls so they reference '../'
processed = re.sub(r'openPreviewModal\(\'([^\']+)\'', r"openPreviewModal('../\1'", processed)

# 2b. Add Razorpay Checkout script to head
processed = processed.replace('</head>', '  <script src="https://checkout.razorpay.com/v1/checkout.js"></script>\n</head>')

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
          </div>
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
  <div id="licenseGateModal" class="hidden fixed inset-0 z-50 bg-slate-950/90 backdrop-blur-md flex items-center justify-center p-3 sm:p-4">
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

# 5b. Customization Request & Razorpay Modal HTML
customization_modal = '''
  <div id="customizationModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-3 sm:p-4 overflow-y-auto">
    <div class="relative w-full max-w-lg bg-white rounded-3xl p-5 sm:p-7 border border-indigo-200 shadow-2xl text-left my-8">
      <button onclick="closeCustomizationModal()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-700 w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center transition-colors">
        <i class="fa-solid fa-xmark text-sm"></i>
      </button>

      <div class="space-y-1 pr-8">
        <div class="inline-flex items-center gap-1.5 bg-indigo-50 border border-indigo-200 text-indigo-700 text-[10px] font-black px-2 py-0.5 rounded-full uppercase tracking-wider">
          <i class="fa-solid fa-crown text-amber-500"></i> VIP Service
        </div>
        <h3 class="text-lg sm:text-xl font-black text-slate-900 tracking-tight">
          Template Customization &amp; Domain Deployment
        </h3>
        <p class="text-xs text-slate-500">
          Get your template customized to your exact requirements and deployed live with your domain connection.
        </p>
      </div>

      <div class="mt-4 p-3 rounded-xl bg-indigo-50/70 border border-indigo-100 flex items-center justify-between text-xs">
        <div>
          <span class="text-slate-500 font-medium">Service Package:</span>
          <span class="font-black text-slate-900 ml-1">Full Customization + Free Domain Deployment</span>
        </div>
        <div class="text-right">
          <span class="text-base font-black text-indigo-700">$100</span>
          <span class="text-[10px] text-slate-500 block font-semibold">(₹8,499 INR)</span>
        </div>
      </div>

      <form id="customizationOrderForm" onsubmit="handleCustomizationSubmit(event)" class="space-y-3.5 mt-4">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Your Full Name <span class="text-rose-500">*</span></label>
            <input type="text" id="custOrderName" required placeholder="e.g. Rahul Sharma" class="w-full bg-slate-50 border border-slate-200 focus:border-indigo-600 focus:bg-white rounded-xl px-3 py-2 text-xs text-slate-900 font-semibold outline-none transition-all" />
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">WhatsApp Number <span class="text-rose-500">*</span></label>
            <input type="tel" id="custOrderPhone" required placeholder="+91 9876543210" class="w-full bg-slate-50 border border-slate-200 focus:border-indigo-600 focus:bg-white rounded-xl px-3 py-2 text-xs text-slate-900 font-mono font-semibold outline-none transition-all" />
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Email Address <span class="text-rose-500">*</span></label>
            <input type="email" id="custOrderEmail" required placeholder="name@yourdomain.com" class="w-full bg-slate-50 border border-slate-200 focus:border-indigo-600 focus:bg-white rounded-xl px-3 py-2 text-xs text-slate-900 outline-none transition-all" />
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Target Template <span class="text-rose-500">*</span></label>
            <input type="text" id="custOrderTemplate" required placeholder="e.g. Meta Ads Landing Page / Bento Portfolio" class="w-full bg-slate-50 border border-slate-200 focus:border-indigo-600 focus:bg-white rounded-xl px-3 py-2 text-xs text-slate-900 outline-none transition-all" />
          </div>
        </div>

        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">Custom Domain &amp; Requirement Notes <span class="text-rose-500">*</span></label>
          <textarea id="custOrderRequirements" required rows="3" placeholder="Enter your domain name (e.g. mybrand.com), branding colors, text changes or any specific requirements..." class="w-full bg-slate-50 border border-slate-200 focus:border-indigo-600 focus:bg-white rounded-xl p-2.5 text-xs text-slate-900 outline-none transition-all"></textarea>
        </div>

        <div class="p-2.5 rounded-xl bg-amber-50 border border-amber-200 text-[11px] text-amber-900 flex items-center gap-2">
          <i class="fa-solid fa-shield-halved text-amber-600 text-sm flex-shrink-0"></i>
          <span>Secure Razorpay / UPI checkout for <strong>$100 (~₹8,499)</strong>. Your request is registered directly into our Admin Dashboard for instant priority fulfillment!</span>
        </div>

        <div class="flex items-center gap-2 pt-1">
          <button type="button" onclick="closeCustomizationModal()" class="w-1/3 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold py-3 rounded-xl transition-colors">
            Cancel
          </button>
          <button type="submit" id="btnSubmitCustomization" class="flex-1 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white text-xs sm:text-sm font-black py-3 rounded-xl shadow-md transition-all flex items-center justify-center gap-2 cursor-pointer">
            <i class="fa-solid fa-credit-card text-xs"></i>
            <span>Pay $100 with Razorpay</span>
          </button>
        </div>
      </form>
    </div>
  </div>
'''

# 6. Header replacement
new_header = '''
  <!-- 1. Customer Portal Header -->
  <header class="sticky top-0 z-40 backdrop-blur-xl bg-white/95 border-b border-gold-500/20 shadow-2xs">
    <div class="max-w-7xl mx-auto px-2.5 sm:px-6 h-12 sm:h-14 flex items-center justify-between gap-1.5 sm:gap-4">
      <a href="#" class="flex items-center space-x-1.5 sm:space-x-2 group flex-shrink-0">
        <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg bg-gradient-to-br from-gold-400 to-amber-600 p-0.5 shadow-sm flex items-center justify-center">
          <div class="w-full h-full bg-white rounded-[6px] flex items-center justify-center">
            <i class="fa-solid fa-crown text-gold-600 text-xs sm:text-sm"></i>
          </div>
        </div>
        <div class="flex flex-col text-left">
          <span class="text-xs sm:text-sm font-black tracking-tight text-slate-900 leading-none">
            DigitalTheme<span class="text-gold-600">.Store</span>
          </span>
          <span class="text-[7.5px] sm:text-[9px] text-emerald-700 font-bold uppercase tracking-wider flex items-center gap-0.5 sm:gap-1">
            <i class="fa-solid fa-shield-check text-[7.5px] sm:text-[8px]"></i> Licensed Vault
          </span>
        </div>
      </a>

      <div class="flex items-center space-x-1 sm:space-x-2.5 flex-shrink-0">
        <!-- Customer Badge (Visible on desktop only to avoid mobile cramping) -->
        <div id="customerHeaderBadge" class="hidden md:flex items-center gap-1.5 bg-amber-50 border border-amber-300/80 px-2 py-0.5 rounded-lg text-xs">
          <i class="fa-solid fa-user-check text-amber-600 text-xs"></i>
          <span id="headerCustomerName" class="font-black text-slate-900 truncate max-w-[100px]">Customer</span>
          <span id="headerCustomerKey" class="font-mono text-[10px] font-bold text-amber-800 bg-amber-200/60 px-1 py-0.2 rounded">KEY</span>
        </div>
        <button onclick="openCustomizationModal()" class="bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200 text-[9.5px] sm:text-xs font-black py-1 px-1.5 sm:px-3 rounded-lg flex items-center gap-1 transition-colors">
          <i class="fa-solid fa-wand-magic-sparkles text-[9px] sm:text-[10px] text-indigo-600"></i>
          <span class="hidden sm:inline">Customization ($100)</span>
          <span class="sm:hidden font-bold">$100 Custom</span>
        </button>
        <a href="../downloads/complete-45-landing-pages-bundle.zip" download class="btn-gold-main text-[9.5px] sm:text-xs py-1 px-1.5 sm:px-3.5 rounded-lg flex items-center space-x-1 shadow-xs">
          <i class="fa-solid fa-file-zipper text-[9px] sm:text-[10px]"></i>
          <span class="hidden sm:inline">Bundle ZIP (128 MB)</span>
          <span class="sm:hidden font-black">All ZIP</span>
        </a>
        <button onclick="lockPortalSession()" class="text-slate-400 hover:text-rose-600 text-xs p-1 sm:p-1.5 rounded-lg hover:bg-slate-100" title="Lock / Change License">
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

    <!-- VIP Customization & Deployment Support Banner ($100 / ₹8,499) -->
    <div class="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-950 text-white rounded-2xl p-4 sm:p-5 shadow-lg border-2 border-indigo-400/50 relative overflow-hidden text-left">
      <div class="absolute -right-12 -bottom-12 w-48 h-48 bg-indigo-500/20 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute top-0 right-0 bg-gradient-to-l from-amber-400 to-amber-500 text-slate-950 text-[9px] sm:text-[10px] font-black px-3 py-1 rounded-bl-xl uppercase tracking-wider shadow">
        ⭐ VIP Service Offer
      </div>

      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div class="space-y-1.5 max-w-2xl pr-12 md:pr-0">
          <div class="inline-flex items-center gap-1.5 bg-indigo-500/25 border border-indigo-400/40 text-indigo-200 text-[10px] sm:text-[11px] font-black px-2.5 py-0.5 rounded-full">
            <i class="fa-solid fa-wand-magic-sparkles text-amber-400"></i>
            <span>Full Template Customization Available</span>
          </div>
          <h3 class="text-base sm:text-lg font-black tracking-tight text-white flex items-center gap-2 flex-wrap">
            <span>Get Full Customization Support in Just $100</span>
            <span class="bg-emerald-500/20 text-emerald-300 border border-emerald-400/30 text-xs px-2 py-0.5 rounded-md font-extrabold">(~₹8,499)</span>
          </h3>
          <p class="text-xs sm:text-[13px] text-slate-300 leading-relaxed">
            Template customization available + <strong>Free Deployment with Domain Connection!</strong> We adapt any template to your brand colors, logo, copy &amp; connect it live to your custom domain.
          </p>
          <div class="flex flex-wrap items-center gap-2 pt-1 text-[10px] sm:text-[11px] font-semibold text-slate-300">
            <span class="flex items-center gap-1"><i class="fa-solid fa-circle-check text-emerald-400"></i> 1-on-1 Dedicated Developer</span>
            <span class="flex items-center gap-1"><i class="fa-solid fa-circle-check text-emerald-400"></i> Free Deployment &amp; Domain Connection</span>
            <span class="flex items-center gap-1"><i class="fa-solid fa-circle-check text-emerald-400"></i> 24–48h Turnaround</span>
          </div>
        </div>

        <div class="flex-shrink-0 flex items-center">
          <button onclick="openCustomizationModal()" class="w-full sm:w-auto bg-gradient-to-r from-amber-400 via-amber-300 to-yellow-500 hover:from-amber-300 hover:to-amber-400 text-slate-950 font-black text-xs sm:text-sm py-3 px-5 rounded-xl shadow-md flex items-center justify-center gap-2 transition-all transform hover:scale-[1.02] cursor-pointer">
            <i class="fa-solid fa-rocket text-indigo-950"></i>
            <span>Request Customization ($100)</span>
          </button>
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

# 9. Insert Verification Modal and Customization Modal right after <body>
processed = processed.replace(
    '<body class="bg-stone-50 text-slate-900 min-h-screen bg-light-pattern relative selection:bg-gold-400 selection:text-black pb-16 sm:pb-0">',
    '<body class="bg-stone-50 text-slate-900 min-h-screen bg-light-pattern relative selection:bg-gold-400 selection:text-black pb-16 sm:pb-0">\n' + verification_modal + '\n' + customization_modal
)

# 10. Remove the checkout modal and mobile floating CTA completely
processed = re.sub(r'<!-- Instant Checkout Modal.*?<!-- Javascript Logic for scaling phone iframes', '<!-- Javascript Logic for scaling phone iframes', processed, flags=re.DOTALL)

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
      let queryPhone = urlParams.get('phone') || urlParams.get('mobile') || urlParams.get('whatsapp');

      // Check path e.g. /purchase/995123123123/licence/
      const pathMatch = window.location.pathname.match(/purchase\/([0-9+]+)\/licence/i);
      if (pathMatch && pathMatch[1]) {
        queryPhone = pathMatch[1];
      }

      // If user came with license key or phone in param -> AUTO-FILL & DO NOT ASK FOR FILL!
      if (queryKey || queryPhone) {
        if (queryKey) queryKey = queryKey.trim().toUpperCase();
        if (queryPhone) queryPhone = queryPhone.trim();

        const inputKey = document.getElementById('verifyKeyInput');
        const inputPhone = document.getElementById('verifyPhoneInput');
        if (inputKey && queryKey) inputKey.value = queryKey;
        if (inputPhone && queryPhone) inputPhone.value = queryPhone;

        const effectiveKey = queryKey || 'LIC-45LP-GOLD-DEMO';
        let formattedPhone = queryPhone || '+91 9951231231';
        const cleanDigits = (queryPhone || '').replace(/[^0-9]/g, '');
        if (cleanDigits.length === 10) {
          formattedPhone = '+91 ' + cleanDigits;
        } else if (cleanDigits.length === 12 && cleanDigits.startsWith('91')) {
          formattedPhone = '+91 ' + cleanDigits.slice(2);
        } else if (queryPhone && !queryPhone.startsWith('+')) {
          formattedPhone = '+' + queryPhone;
        }

        let defaultName = 'Shaikh Mudassir';
        if (cleanDigits && !cleanDigits.includes('9951231231') && !effectiveKey.includes('DEMO')) {
          defaultName = 'Licensed Customer';
        }

        const customerData = {
          key: effectiveKey,
          phone: formattedPhone,
          name: defaultName,
          status: 'active',
          licenseType: 'Single-User Lifetime Commercial'
        };

        // Immediately unlock portal - DO NOT ASK FOR FILL!
        applyVerifiedLicense(customerData);
        localStorage.setItem('digital_theme_license', JSON.stringify(customerData));

        // Background sync with Firebase (silent, never pops up modal)
        if (effectiveKey) {
          syncLicenseWithFirebase(effectiveKey, formattedPhone, customerData);
        }
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

      // 3. Only if NO key/phone in URL and NO cached license, show modal
      showVerificationModal();
    }

    async function syncLicenseWithFirebase(key, phone, fallbackData) {
      try {
        const safeKeyId = key.trim().toUpperCase().replace(/[^a-zA-Z0-9_-]/g, '_');
        const res = await fetch(RTDB_URL + '/licenses/' + safeKeyId + '.json');
        const data = await res.json();
        if (data && data.status !== 'revoked') {
          const merged = { ...fallbackData, ...data };
          applyVerifiedLicense(merged);
          localStorage.setItem('digital_theme_license', JSON.stringify(merged));
        } else if (!data) {
          fetch(RTDB_URL + '/licenses/' + safeKeyId + '.json', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              ...fallbackData,
              createdAt: new Date().toISOString()
            })
          }).catch(() => {});
        }
      } catch (e) {
        // Silent: fallbackData is already applied and user has full access
      }
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

      // Only show top customer header badge on tablet/desktop (>= 768px)
      if (window.innerWidth >= 768) {
        const custBadge = document.getElementById('customerHeaderBadge');
        if (custBadge) custBadge.classList.remove('hidden');
      }
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

    // =========================================================================
    // 🛠️ CUSTOMIZATION & DEPLOYMENT REQUEST WITH RAZORPAY
    // =========================================================================
    function openCustomizationModal(defaultTemplate) {
      if (currentCustomerLicense) {
        if (currentCustomerLicense.name) document.getElementById('custOrderName').value = currentCustomerLicense.name;
        if (currentCustomerLicense.phone) document.getElementById('custOrderPhone').value = currentCustomerLicense.phone;
      }
      if (defaultTemplate) {
        document.getElementById('custOrderTemplate').value = defaultTemplate;
      }
      document.getElementById('customizationModal').classList.remove('hidden');
    }

    function closeCustomizationModal() {
      document.getElementById('customizationModal').classList.add('hidden');
    }

    async function handleCustomizationSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('custOrderName').value.trim();
      const phone = document.getElementById('custOrderPhone').value.trim();
      const email = document.getElementById('custOrderEmail').value.trim();
      const template = document.getElementById('custOrderTemplate').value.trim();
      const requirements = document.getElementById('custOrderRequirements').value.trim();
      const btn = document.getElementById('btnSubmitCustomization');

      btn.disabled = true;
      btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Initializing Razorpay...';

      const orderData = {
        name: name,
        phone: phone,
        email: email,
        template: template,
        requirements: requirements,
        amount: "$100 (₹8,499)",
        amountInr: 8499,
        licenseKey: currentCustomerLicense ? (currentCustomerLicense.key || '') : '',
        createdAt: new Date().toISOString(),
        status: "Pending Payment"
      };

      const options = {
        key: "rzp_live_ILgsfZCZoFIKMb",
        amount: 8499 * 100, // paise
        currency: "INR",
        name: "Digital Theme Store",
        description: "Template Customization & Free Domain Deployment ($100)",
        prefill: {
          name: name,
          email: email,
          contact: phone.replace(/[^0-9]/g, '')
        },
        theme: {
          color: "#4f46e5"
        },
        handler: async function (response) {
          orderData.status = "Paid / In Progress";
          orderData.paymentId = response.razorpay_payment_id || ("PAY-" + Date.now());
          await saveCustomizationOrder(orderData);
        },
        modal: {
          ondismiss: async function() {
            btn.disabled = false;
            btn.innerHTML = '<i class="fa-solid fa-credit-card text-xs"></i> <span>Pay $100 with Razorpay</span>';
          }
        }
      };

      try {
        if (typeof Razorpay !== 'undefined') {
          const rzp = new Razorpay(options);
          rzp.on('payment.failed', async function (resp) {
            orderData.status = "Payment Failed";
            orderData.paymentError = resp.error ? resp.error.description : 'Payment declined';
            await saveCustomizationOrder(orderData);
            alert("Razorpay: " + (resp.error ? resp.error.description : "Payment failed"));
            btn.disabled = false;
            btn.innerHTML = '<i class="fa-solid fa-credit-card text-xs"></i> <span>Pay $100 with Razorpay</span>';
          });
          rzp.open();
        } else {
          orderData.status = "Direct Inquiry ($100)";
          await saveCustomizationOrder(orderData);
        }
      } catch (err) {
        console.warn("Razorpay fallback:", err);
        orderData.status = "Direct Inquiry ($100)";
        await saveCustomizationOrder(orderData);
      }
    }

    async function saveCustomizationOrder(orderData) {
      const orderId = 'CUST_' + Date.now();
      try {
        await fetch(RTDB_URL + '/customization_requests/' + orderId + '.json', {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(orderData)
        });
        closeCustomizationModal();
        alert('🎉 Customization Request Confirmed! Our senior team will contact you on WhatsApp (' + orderData.phone + ') within 1 hour to start your template customization & domain connection.');
        const text = encodeURIComponent('Hello, I just booked $100 Customization & Domain Connection for template: ' + orderData.template + '. My name is ' + orderData.name + '.');
        window.open('https://wa.me/919951231231?text=' + text, '_blank');
      } catch (err) {
        console.error("Error saving customization order:", err);
        closeCustomizationModal();
        alert('Customization request recorded! We will contact you on WhatsApp.');
      }
    }

    document.addEventListener('DOMContentLoaded', () => {
      checkLicenseStatus();
    });
'''

# 12. Replace the script section in processed
processed = processed.replace(
    '<!-- Javascript Logic for scaling phone iframes and interactivity -->\n  <script>',
    '<!-- Javascript Logic for scaling phone iframes and interactivity -->\n  <script>\n' + portal_script
)

# Remove any mobile scroll popups or checkout modal calls in purchase portal
processed = processed.replace('openCheckoutModal();', '// portal: already purchased')
processed = processed.replace('setupTwoRowScrollPopup();', '// portal: no scroll popup')
processed = processed.replace('setupThreeRowScrollPopup();', '// portal: no scroll popup')

# Cleanly replace function bodies without leaving dangling brackets or statements
processed = re.sub(
    r'function setupThreeRowScrollPopup\(\)[\s\S]*?rowObserver\.observe\(targetCard\);\s*\}',
    'function setupThreeRowScrollPopup() {}',
    processed
)
processed = re.sub(
    r'function setupTwoRowScrollPopup\(\)[\s\S]*?rowObserver\.observe\(targetCard\);\s*\}',
    'function setupTwoRowScrollPopup() {}',
    processed
)
processed = re.sub(
    r'function openCheckoutModal\(\)[\s\S]*?document\.getElementById\([\'"]checkoutModal[\'"]\)\.classList\.remove\([\'"]hidden[\'"]\);\s*\}',
    'function openCheckoutModal() {}',
    processed
)

os.makedirs('purchase', exist_ok=True)
with open('purchase/index.html', 'w', encoding='utf-8') as f:
    f.write(processed)

print('Generated purchase/index.html cleanly. Size:', len(processed))
