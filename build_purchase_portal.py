import os, re, json

# All 44 Theme Data definitions with categories & color tagging
THEME_DATA = {
    # =========================================================================
    # GOLD THEMES (11)
    # =========================================================================
    "portfolio-dark-gold": {
        "title": "Personal Portfolio Template",
        "subtitle": "Developer, Consultant & Architect Profile",
        "badge": "Portfolio",
        "color": "gold"
    },
    "funnel-dark-gold": {
        "title": "Sales Funnel Template",
        "subtitle": "Meta Ads & Performance Agency Lander",
        "badge": "Sales Funnel",
        "color": "gold"
    },
    "realstate-dark-gold": {
        "title": "Real Estate Landing Page Template",
        "subtitle": "Luxury Properties, Penthouse & Sky Villas",
        "badge": "Real Estate",
        "color": "gold"
    },
    "single-product-white-gold": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Ergonomic Workspace & DTC Product Lander",
        "badge": "Single Product",
        "color": "gold"
    },
    "funnel-white-gold": {
        "title": "B2B Sales Funnel Template",
        "subtitle": "Growth Agency & High-Ticket Retainers",
        "badge": "Sales Funnel",
        "color": "gold"
    },
    "ecommerce-dark-gold": {
        "title": "E-Commerce Store Template",
        "subtitle": "Luxury Watches & High-End Jewelry",
        "badge": "E-Commerce",
        "color": "gold"
    },
    "course-white-gold": {
        "title": "Online Course Template",
        "subtitle": "Tech Academy & AI Masterclass Platform",
        "badge": "Course / EdTech",
        "color": "gold"
    },
    "saas-dark-gold": {
        "title": "SaaS Landing Page Template",
        "subtitle": "Enterprise AI & Software Platform",
        "badge": "SaaS Platform",
        "color": "gold"
    },
    "ecommerce-white-gold": {
        "title": "Fashion E-Commerce Template",
        "subtitle": "Designer Apparel & Minimalist Boutique",
        "badge": "E-Commerce",
        "color": "gold"
    },
    "portfolio-white-gold": {
        "title": "Agency Portfolio Template",
        "subtitle": "Architecture & Modern Interior Studio",
        "badge": "Portfolio",
        "color": "gold"
    },
    "single-product-dark-gold": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Smart Ring & Luxury Wearable Gadget",
        "badge": "Single Product",
        "color": "gold"
    },

    # =========================================================================
    # EMERALD & GREEN THEMES (10)
    # =========================================================================
    "funnel-dark-emerald": {
        "title": "Fintech Sales Funnel Template",
        "subtitle": "Wealth Advisory & High-Ticket Investment",
        "badge": "Sales Funnel",
        "color": "emerald"
    },
    "funnel-white-emerald": {
        "title": "Healthcare Sales Funnel Template",
        "subtitle": "Clinic & Doctor Appointment Booking",
        "badge": "Sales Funnel",
        "color": "emerald"
    },
    "course-dark-green": {
        "title": "Coding Bootcamp Template",
        "subtitle": "Full-Stack Dev & DevOps Learning Platform",
        "badge": "Online Course",
        "color": "emerald"
    },
    "course-white-green": {
        "title": "Online Course Template",
        "subtitle": "Organic Agriculture & Clean-Tech Academy",
        "badge": "Online Course",
        "color": "emerald"
    },
    "ecommerce-dark-emerald": {
        "title": "Skincare E-Commerce Template",
        "subtitle": "Organic Cosmetics & Herbal Beauty Store",
        "badge": "E-Commerce",
        "color": "emerald"
    },
    "ecommerce-white-emerald": {
        "title": "E-Commerce Store Template",
        "subtitle": "Eco-Friendly Bamboo Home Goods & DTC",
        "badge": "E-Commerce",
        "color": "emerald"
    },
    "portfolio-dark-emerald": {
        "title": "Cybersecurity Portfolio Template",
        "subtitle": "Security Auditor & Pentesting Consultant",
        "badge": "Portfolio",
        "color": "emerald"
    },
    "portfolio-white-emerald": {
        "title": "Creative Portfolio Template",
        "subtitle": "Landscape Architect & Sustainable Planner",
        "badge": "Portfolio",
        "color": "emerald"
    },
    "single-product-dark-emerald": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Cold-Pressed Smart Kitchen Appliance",
        "badge": "Single Product",
        "color": "emerald"
    },
    "single-product-white-emerald": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Hydroponic Indoor Smart Garden System",
        "badge": "Single Product",
        "color": "emerald"
    },

    # =========================================================================
    # PURPLE THEMES (9)
    # =========================================================================
    "funnel-dark-purple": {
        "title": "Web3 & Crypto Funnel Template",
        "subtitle": "Token Pre-Sale & Launchpad Platform",
        "badge": "Sales Funnel",
        "color": "purple"
    },
    "funnel-white-purple": {
        "title": "Creative Agency Funnel Template",
        "subtitle": "Branding Studio & Client Discovery Call",
        "badge": "Sales Funnel",
        "color": "purple"
    },
    "course-white-purple": {
        "title": "UI/UX Course Template",
        "subtitle": "Figma Design Systems & Mentorship",
        "badge": "Online Course",
        "color": "purple"
    },
    "ecommerce-dark-purple": {
        "title": "Gaming E-Commerce Template",
        "subtitle": "Pro Gaming Gear & RGB PC Peripherals",
        "badge": "E-Commerce",
        "color": "purple"
    },
    "ecommerce-white-purple": {
        "title": "Perfume E-Commerce Template",
        "subtitle": "Artisan Luxury Fragrance & Scent House",
        "badge": "E-Commerce",
        "color": "purple"
    },
    "portfolio-dark-purple": {
        "title": "Video & 3D Portfolio Template",
        "subtitle": "Motion Graphics & VFX Director Showreel",
        "badge": "Portfolio",
        "color": "purple"
    },
    "portfolio-white-purple": {
        "title": "Fashion Stylist Portfolio Template",
        "subtitle": "Editorial Art Director & Fashion Bio",
        "badge": "Portfolio",
        "color": "purple"
    },
    "single-product-dark-purple": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Studio Wireless Audiophile Headphones",
        "badge": "Single Product",
        "color": "purple"
    },
    "single-product-white-purple": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Circadian Sunrise Smart Sleep Lamp",
        "badge": "Single Product",
        "color": "purple"
    },

    # =========================================================================
    # BLUE THEMES (5)
    # =========================================================================
    "funnel-white-blue": {
        "title": "Dental Clinic Funnel Template",
        "subtitle": "Medical Practice Patient Acquisition",
        "badge": "Sales Funnel",
        "color": "blue"
    },
    "course-white-blue": {
        "title": "Cloud Certification Course Template",
        "subtitle": "AWS Solutions Architect Video Training",
        "badge": "Online Course",
        "color": "blue"
    },
    "ecommerce-white-blue": {
        "title": "Medical Supply E-Commerce Template",
        "subtitle": "Clinical Equipment & Healthcare Store",
        "badge": "E-Commerce",
        "color": "blue"
    },
    "portfolio-white-blue": {
        "title": "Lawyer & Attorney Portfolio Template",
        "subtitle": "Corporate Legal Firm & Retainer Booking",
        "badge": "Portfolio",
        "color": "blue"
    },
    "single-product-white-blue": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Alkaline Multi-Stage Home Water Purifier",
        "badge": "Single Product",
        "color": "blue"
    },

    # =========================================================================
    # CLASSIC THEMES (9)
    # =========================================================================
    "funnel-dark": {
        "title": "Private Equity Funnel Template",
        "subtitle": "M&A Advisory & Investor Deal Room Pitch",
        "badge": "Sales Funnel",
        "color": "classic"
    },
    "funnel-white": {
        "title": "Coaching & Mastermind Funnel Template",
        "subtitle": "Executive 1-on-1 Mentorship & VSL Lander",
        "badge": "Sales Funnel",
        "color": "classic"
    },
    "course-dark": {
        "title": "Trading & Finance Course Template",
        "subtitle": "Quantitative Trading & Algo Finance",
        "badge": "Online Course",
        "color": "classic"
    },
    "ecommerce-dark": {
        "title": "Leather Goods E-Commerce Template",
        "subtitle": "Handcrafted Leather Luggage & Accessories",
        "badge": "E-Commerce",
        "color": "classic"
    },
    "ecommerce-white": {
        "title": "Eyewear E-Commerce Template",
        "subtitle": "Italian Acetate Sunglasses & Frames Store",
        "badge": "E-Commerce",
        "color": "classic"
    },
    "portfolio-dark": {
        "title": "Filmmaker Portfolio Template",
        "subtitle": "Commercial Cinematographer & Director Wall",
        "badge": "Portfolio",
        "color": "classic"
    },
    "portfolio-white": {
        "title": "Consultant Portfolio Template",
        "subtitle": "Chartered Accountant & Corporate Tax Strategist",
        "badge": "Portfolio",
        "color": "classic"
    },
    "single-product-dark": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Automatic Mechanical Luxury Watch",
        "badge": "Single Product",
        "color": "classic"
    },
    "single-product-white": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Ceramic Pour-Over French Press Brewer",
        "badge": "Single Product",
        "color": "classic"
    }
}

ORDERED_KEYS = [
    # Gold (11)
    "portfolio-dark-gold",
    "funnel-dark-gold",
    "realstate-dark-gold",
    "single-product-white-gold",
    "funnel-white-gold",
    "ecommerce-dark-gold",
    "course-white-gold",
    "saas-dark-gold",
    "ecommerce-white-gold",
    "portfolio-white-gold",
    "single-product-dark-gold",

    # Emerald (10)
    "funnel-dark-emerald",
    "funnel-white-emerald",
    "course-dark-green",
    "course-white-green",
    "ecommerce-dark-emerald",
    "ecommerce-white-emerald",
    "portfolio-dark-emerald",
    "portfolio-white-emerald",
    "single-product-dark-emerald",
    "single-product-white-emerald",

    # Purple (9)
    "funnel-dark-purple",
    "funnel-white-purple",
    "course-white-purple",
    "ecommerce-dark-purple",
    "ecommerce-white-purple",
    "portfolio-dark-purple",
    "portfolio-white-purple",
    "single-product-dark-purple",
    "single-product-white-purple",

    # Blue (5)
    "funnel-white-blue",
    "course-white-blue",
    "ecommerce-white-blue",
    "portfolio-white-blue",
    "single-product-white-blue",

    # Classic (9)
    "funnel-dark",
    "funnel-white",
    "course-dark",
    "ecommerce-dark",
    "ecommerce-white",
    "portfolio-dark",
    "portfolio-white",
    "single-product-dark",
    "single-product-white"
]

def render_portal_card(key, idx):
    d = THEME_DATA[key]
    color = d["color"]
    is_white = "white" in key
    
    if color == "gold":
        badge_style = "bg-white/95 text-amber-900 border-amber-400" if is_white else "bg-black/85 text-gold-400 border-gold-400/40"
        card_border = "border-gold-300/80 hover:border-gold-500"
    elif color == "emerald":
        badge_style = "bg-white/95 text-emerald-900 border-emerald-400" if is_white else "bg-black/85 text-emerald-400 border-emerald-400/40"
        card_border = "border-emerald-200/80 hover:border-emerald-400"
    elif color == "purple":
        badge_style = "bg-white/95 text-purple-900 border-purple-400" if is_white else "bg-black/85 text-purple-400 border-purple-400/40"
        card_border = "border-purple-200/80 hover:border-purple-400"
    elif color == "blue":
        badge_style = "bg-white/95 text-blue-900 border-blue-400" if is_white else "bg-black/85 text-blue-400 border-blue-400/40"
        card_border = "border-blue-200/80 hover:border-blue-400"
    else:
        badge_style = "bg-white/95 text-slate-900 border-slate-300" if is_white else "bg-black/85 text-slate-200 border-slate-700"
        card_border = "border-slate-200 hover:border-slate-400"

    # Eager load first 4 cards for instant visual punch, lazy load the rest
    if idx < 4:
        iframe_tag = f'<iframe src="../{key}/preview.html" class="live-scaled-iframe hero-iframe" onload="handleIframeLoaded(this)" title="{d["title"]}" loading="eager"></iframe>'
    else:
        iframe_tag = f'<iframe src="about:blank" data-src="../{key}/preview.html" class="live-scaled-iframe" onload="handleIframeLoaded(this)" title="{d["title"]}" loading="lazy"></iframe>'

    zip_url = f'../downloads/{key}.zip'

    return f'''        <!-- #{idx+1}: {d["title"]} ({key}) -->
        <div class="card-phone-unit rounded-2xl p-1.5 sm:p-3 text-left flex flex-col justify-between {card_border} transition-all shadow-2xs" data-color="{color}">
          <div class="space-y-1.5">
            <div class="phone-mockup-frame group">
              <div class="phone-notch"></div>
              <div class="phone-skeleton">
                <div class="skeleton-spinner"></div>
                <div class="w-16 space-y-1.5">
                  <div class="skeleton-line w-full"></div>
                  <div class="skeleton-line w-3/4 mx-auto"></div>
                </div>
              </div>
              {iframe_tag}
              <div class="absolute top-1.5 left-1.5 z-20">
                <span class="{badge_style} border text-[7.5px] sm:text-[9px] font-black px-1.5 py-0.2 rounded shadow">
                  {d["badge"]}
                </span>
              </div>
            </div>
            <div>
              <h3 class="text-[11px] sm:text-xs font-black text-slate-900 truncate">{d["title"]}</h3>
              <p class="text-[8.5px] sm:text-[10px] text-slate-500 truncate">{d["subtitle"]}</p>
            </div>
          </div>
          <div class="flex items-center gap-1 pt-1.5 border-t border-slate-100 mt-1">
            <a href="{zip_url}" download class="flex-1 bg-emerald-600 hover:bg-emerald-700 text-white text-[9.5px] sm:text-[11px] font-black py-1.5 px-1.5 rounded-lg flex items-center justify-center gap-1 shadow-xs transition-colors">
              <i class="fa-solid fa-download text-[9px]"></i>
              <span>Download ZIP</span>
            </a>
            <button onclick="openPreviewModal('../{key}/index.html', '{d["title"]}')" class="bg-slate-100 hover:bg-slate-200 text-slate-700 text-[9.5px] sm:text-[11px] font-bold py-1.5 px-2 rounded-lg" title="Live Preview">
              <i class="fa-solid fa-eye text-[8.5px]"></i>
            </button>
            <a href="../{key}/index.html" target="_blank" class="bg-slate-100 hover:bg-slate-200 text-slate-700 text-[9.5px] sm:text-[11px] font-bold py-1.5 px-2 rounded-lg" title="Open in New Tab">
              ↗
            </a>
          </div>
        </div>'''

with open('index.source.html', 'r', encoding='utf-8') as f:
    source = f.read()

# 1. Update relative links: './' -> '../' for subfolder 'purchase/'
processed = re.sub(r'href="\./', 'href="../', source)
processed = re.sub(r'src="\./', 'src="../', processed)
processed = re.sub(r'data-src="\./', 'data-src="../', processed)

# 2. Add Razorpay Checkout script to head
processed = processed.replace('</head>', '  <script src="https://checkout.razorpay.com/v1/checkout.js"></script>\n</head>')

# 3. Title & Header adjustments
processed = processed.replace(
    '<title>45+ Ultimate Landing Page Bundle | Just ₹399 (Live Mobile Screens)</title>',
    '<title>Customer License Vault &amp; Downloads | 45+ Ultimate Landing Page Bundle</title>'
)
processed = processed.replace(
    '<title>45+ Ultimate Landing Page Bundle | Just ₹999 (Live Mobile Screens)</title>',
    '<title>Customer License Vault &amp; Downloads | 45+ Ultimate Landing Page Bundle</title>'
)

# 4. Modals HTML
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

customization_modal = '''
  <!-- 1-Click VIP Customization Checkout Modal -->
  <div id="customizationModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-3 sm:p-4 overflow-y-auto">
    <div class="relative w-full max-w-md bg-white rounded-3xl p-5 sm:p-6 border border-indigo-200 shadow-2xl text-left my-8 space-y-4">
      <button onclick="closeCustomizationModal()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-700 w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center transition-colors">
        <i class="fa-solid fa-xmark text-sm"></i>
      </button>

      <div class="space-y-1 pr-8">
        <div class="inline-flex items-center gap-1.5 bg-indigo-50 border border-indigo-200 text-indigo-700 text-[10px] font-black px-2 py-0.5 rounded-full uppercase tracking-wider">
          <i class="fa-solid fa-crown text-amber-500"></i> VIP Service
        </div>
        <h3 class="text-lg font-black text-slate-900 tracking-tight">
          Template Customization &amp; Database Setup
        </h3>
        <p class="text-xs text-slate-500">
          Full business customization, database connection with Admin Panel, free hosting, free cloud storage &amp; custom domain connection.
        </p>
      </div>

      <!-- Package Pricing Box -->
      <div class="p-3.5 rounded-2xl bg-indigo-50/80 border border-indigo-200 flex items-center justify-between text-xs">
        <div>
          <span class="text-slate-500 font-medium block">All-In-One Package:</span>
          <span class="font-black text-slate-900 text-xs">Full Customization + Database + Hosting</span>
        </div>
        <div class="text-right flex-shrink-0 ml-2">
          <span class="text-xl font-black text-indigo-700">₹3,999</span>
          <span class="text-[9.5px] text-emerald-700 block font-bold">1-Time Fee</span>
        </div>
      </div>

      <!-- Auto-Fetched Customer Profile Box -->
      <div class="bg-slate-50 border border-slate-200 rounded-2xl p-3.5 space-y-2">
        <div class="flex items-center justify-between text-xs">
          <span class="text-slate-500 font-medium">Customer Name:</span>
          <span id="custAutoName" class="font-bold text-slate-900">--</span>
        </div>
        <div class="flex items-center justify-between text-xs border-t border-slate-200/60 pt-1.5">
          <span class="text-slate-500 font-medium">WhatsApp Number:</span>
          <span id="custAutoPhone" class="font-bold text-indigo-700 font-mono">--</span>
        </div>
        <div class="flex flex-col sm:flex-row sm:items-center justify-between text-xs border-t border-slate-200/60 pt-1.5 gap-1">
          <span class="text-slate-500 font-medium">License Key:</span>
          <span id="custAutoKey" class="font-mono text-amber-900 bg-amber-100 border border-amber-300 px-2 py-0.5 rounded font-bold text-[11px] select-all break-all self-start sm:self-auto">--</span>
        </div>
      </div>

      <!-- Informational Feature Checklist -->
      <div class="p-3 rounded-xl bg-amber-50/80 border border-amber-200 text-xs text-amber-950 space-y-1.5">
        <div class="flex items-start gap-1.5">
          <i class="fa-solid fa-circle-check text-emerald-600 text-xs mt-0.5 flex-shrink-0"></i>
          <span><strong>Direct WhatsApp Setup:</strong> No forms needed! Right after checkout, our dedicated support team will contact your WhatsApp to get your custom domain &amp; requirements.</span>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex items-center gap-2 pt-1">
        <button type="button" onclick="closeCustomizationModal()" class="w-1/3 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold py-3.5 rounded-xl transition-colors">
          Cancel
        </button>
        <button type="button" id="btnSubmitCustomization" onclick="startCustomizationPayment()" class="flex-1 bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white text-xs sm:text-sm font-black py-3.5 rounded-xl shadow-md transition-all flex items-center justify-center gap-2 cursor-pointer">
          <i class="fa-solid fa-bolt text-amber-300"></i>
          <span>Pay ₹3,999 with Razorpay</span>
        </button>
      </div>
    </div>
  </div>
'''

# 5. Header replacement
new_header = '''
  <!-- 1. Customer Portal Header -->
  <header class="sticky top-0 z-40 backdrop-blur-xl bg-white/95 border-b border-gold-500/20 shadow-2xs">
    <div class="max-w-7xl mx-auto px-2 sm:px-6 h-12 sm:h-14 flex items-center justify-between gap-1 sm:gap-4">
      <a href="#" class="flex items-center space-x-1 sm:space-x-2 group flex-shrink-0">
        <div class="w-6 h-6 sm:w-8 sm:h-8 rounded-lg bg-gradient-to-br from-gold-400 to-amber-600 p-0.5 shadow-sm flex items-center justify-center">
          <div class="w-full h-full bg-white rounded-[5px] sm:rounded-[6px] flex items-center justify-center">
            <i class="fa-solid fa-crown text-gold-600 text-[10px] sm:text-sm"></i>
          </div>
        </div>
        <div class="flex flex-col text-left">
          <span class="text-xs sm:text-sm font-black tracking-tight text-slate-900 leading-none">
            DigitalTheme<span class="text-gold-600">.Store</span>
          </span>
          <span class="text-[7px] sm:text-[9px] text-emerald-700 font-bold uppercase tracking-wider flex items-center gap-0.5 sm:gap-1">
            <i class="fa-solid fa-shield-check text-[7px] sm:text-[8px]"></i> Licensed Vault
          </span>
        </div>
      </a>

      <div class="flex items-center space-x-1 sm:space-x-2 flex-shrink-0">
        <!-- Customer Badge (Visible on desktop only to avoid mobile cramping) -->
        <div id="customerHeaderBadge" class="hidden md:flex items-center gap-1.5 bg-amber-50 border border-amber-300/80 px-2 py-0.5 rounded-lg text-xs">
          <i class="fa-solid fa-user-check text-amber-600 text-xs"></i>
          <span id="headerCustomerName" class="font-black text-slate-900 truncate max-w-[100px]">Customer</span>
          <span id="headerCustomerKey" class="font-mono text-[10px] font-bold text-amber-800 bg-amber-200/60 px-1 py-0.2 rounded">KEY</span>
        </div>
        <button onclick="openCustomizationModal()" class="bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200 text-[9px] sm:text-xs font-black py-1 px-1.5 sm:px-3 rounded-lg flex items-center gap-1 transition-colors">
          <i class="fa-solid fa-wand-magic-sparkles text-[8.5px] sm:text-[10px] text-indigo-600"></i>
          <span class="hidden sm:inline">Customization (₹3,999)</span>
          <span class="sm:hidden font-bold">₹3,999 Custom</span>
        </button>
        <a href="../downloads/complete-45-landing-pages-bundle.zip" download class="btn-gold-main text-[9px] sm:text-xs py-1 px-1.5 sm:px-3 rounded-lg flex items-center space-x-1 shadow-xs">
          <i class="fa-solid fa-file-zipper text-[8.5px] sm:text-[10px]"></i>
          <span class="hidden sm:inline">Bundle ZIP (128 MB)</span>
          <span class="sm:hidden font-black">All ZIP</span>
        </a>
        <button onclick="lockPortalSession()" class="text-slate-400 hover:text-rose-600 text-xs p-1 rounded-lg hover:bg-slate-100" title="Lock / Change License">
          <i class="fa-solid fa-arrow-right-from-bracket"></i>
        </button>
      </div>
    </div>
  </header>
'''

# 6. Hero & Verified Banner
new_hero = '''
  <!-- 2. Customer Hero Banner & License Rights -->
  <section class="pt-2 pb-2 sm:pt-4 sm:pb-3 px-2.5 sm:px-6 max-w-7xl mx-auto text-center space-y-3">
    
    <!-- Verified License Rights Box -->
    <div id="verifiedLicenseCard" class="bg-white border-2 border-amber-300 rounded-2xl sm:rounded-3xl p-3 sm:p-5 text-left shadow-md space-y-3 relative overflow-hidden">
      <!-- Ribbon (In-flow on mobile so it never overlaps, absolute on desktop) -->
      <div class="sm:absolute sm:top-0 sm:right-0 -mx-3 -mt-3 mb-1 sm:m-0 bg-gradient-to-r sm:bg-gradient-to-l from-amber-400 to-amber-500 text-slate-950 font-black text-[9px] sm:text-[10px] uppercase py-1.5 px-2.5 sm:px-3 text-center sm:text-left sm:rounded-bl-xl tracking-wider shadow-2xs flex items-center justify-center sm:justify-start gap-1">
        <i class="fa-solid fa-crown text-[8.5px]"></i>
        <span>Official Single-User Commercial License • ₹29,999 Value (₹399)</span>
      </div>
      
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div class="flex items-start sm:items-center gap-2.5 min-w-0">
          <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center text-lg flex-shrink-0 mt-0.5 sm:mt-0">
            <i class="fa-solid fa-certificate"></i>
          </div>
          <div class="min-w-0 space-y-0.5">
            <div class="flex items-center gap-2 flex-wrap">
              <h2 id="licenseCardName" class="text-sm sm:text-base font-black text-slate-950">Licensed Customer</h2>
              <span id="licenseCardBadge" class="bg-emerald-100 text-emerald-800 text-[10px] font-extrabold px-2 py-0.5 rounded-full flex-shrink-0">ACTIVE</span>
            </div>
            <p class="text-[11px] text-slate-600 font-mono">
              WhatsApp: <span id="licenseCardPhone" class="font-bold text-slate-900">--</span>
            </p>
            <div class="flex items-center gap-1.5 pt-0.5 flex-wrap">
              <span class="text-[11px] text-slate-500 font-mono">License Key:</span>
              <span id="licenseCardKey" class="font-mono font-bold text-amber-900 bg-amber-100 border border-amber-300 px-2 py-0.5 rounded-md text-[11px] sm:text-xs select-all break-all">--</span>
            </div>
          </div>
        </div>

        <div class="flex items-center gap-2 w-full sm:w-auto">
          <a href="../downloads/complete-45-landing-pages-bundle.zip" download class="w-full sm:w-auto btn-gold-main text-xs sm:text-sm font-black py-2.5 px-4 rounded-xl shadow flex items-center justify-center gap-2 flex-shrink-0">
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
          <span class="text-rose-700 font-extrabold">Re-selling, sub-licensing, sharing, or publishing raw source code is strictly prohibited.</span>
        </div>
      </div>
    </div>

    <!-- VIP Customization & Deployment Support Banner (₹3,999) -->
    <div class="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-950 text-white rounded-2xl sm:rounded-3xl p-3.5 sm:p-5 shadow-lg border-2 border-indigo-400/50 relative overflow-hidden text-left space-y-2.5">
      <div class="absolute -right-12 -bottom-12 w-48 h-48 bg-indigo-500/20 rounded-full blur-3xl pointer-events-none"></div>
      
      <!-- Ribbon (In-flow on mobile so it never overlaps, absolute on desktop) -->
      <div class="sm:absolute sm:top-0 sm:right-0 -mx-3.5 -mt-3.5 mb-1 sm:m-0 bg-gradient-to-r sm:bg-gradient-to-l from-amber-400 to-amber-500 text-slate-950 text-[9px] sm:text-[10px] font-black py-1.5 px-3 text-center sm:text-left sm:rounded-bl-xl uppercase tracking-wider shadow flex items-center justify-center sm:justify-start gap-1">
        <i class="fa-solid fa-star text-[8.5px]"></i>
        <span>VIP Business Upgrade</span>
      </div>

      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div class="space-y-1.5 max-w-2xl">
          <div class="inline-flex items-center gap-1.5 bg-indigo-500/25 border border-indigo-400/40 text-indigo-200 text-[10px] sm:text-[11px] font-black px-2.5 py-0.5 rounded-full">
            <i class="fa-solid fa-wand-magic-sparkles text-amber-400"></i>
            <span>Full Customization &amp; Database Package</span>
          </div>
          <h3 class="text-base sm:text-lg font-black tracking-tight text-white flex items-center gap-2 flex-wrap">
            <span>Get Full Customization &amp; Database Setup in Just ₹3,999</span>
            <span class="bg-emerald-500/20 text-emerald-300 border border-emerald-400/30 text-xs px-2 py-0.5 rounded-md font-extrabold">(All-Inclusive)</span>
          </h3>
          <p class="text-xs sm:text-[13px] text-slate-300 leading-relaxed">
            Full template customization tailored to your business needs + <strong>Database Connection with Admin Panel Included!</strong> We provide <strong>Free Hosting &amp; Free Cloud Storage</strong> and connect your custom domain live. Our dedicated support team handles everything for you!
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-1.5 pt-1 text-[10px] sm:text-[11px] font-semibold text-slate-300">
            <span class="flex items-center gap-1"><i class="fa-solid fa-circle-check text-emerald-400"></i> 1-on-1 Dedicated Support Team</span>
            <span class="flex items-center gap-1"><i class="fa-solid fa-circle-check text-emerald-400"></i> Full Customization according to Business</span>
            <span class="flex items-center gap-1"><i class="fa-solid fa-circle-check text-emerald-400"></i> Full Database Connection + Admin Panel</span>
            <span class="flex items-center gap-1"><i class="fa-solid fa-circle-check text-emerald-400"></i> Free Hosting &amp; Free Cloud Storage</span>
            <span class="flex items-center gap-1"><i class="fa-solid fa-circle-check text-emerald-400"></i> Custom Domain Connection (We connect it)</span>
            <span class="flex items-center gap-1"><i class="fa-solid fa-circle-check text-emerald-400"></i> 24–48h Priority Turnaround</span>
          </div>
        </div>

        <div class="flex-shrink-0 flex items-center w-full sm:w-auto">
          <button onclick="openCustomizationModal()" class="w-full sm:w-auto bg-gradient-to-r from-amber-400 via-amber-300 to-yellow-500 hover:from-amber-300 hover:to-amber-400 text-slate-950 font-black text-xs sm:text-sm py-3 px-5 rounded-xl shadow-md flex items-center justify-center gap-2 transition-all transform hover:scale-[1.02] cursor-pointer">
            <i class="fa-solid fa-rocket text-indigo-950"></i>
            <span>Request Customization (₹3,999)</span>
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
        🏆 Top Featured (11)
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
        🖤 Classic (9)
      </button>
    </div>
  </section>
'''

# 7. Render ALL 44 Cards in the Main Section
cards_html_list = []
for idx, key in enumerate(ORDERED_KEYS):
    cards_html_list.append(render_portal_card(key, idx))
all_cards_grid = "\n\n".join(cards_html_list)

new_main = f'''  <!-- 3. MAIN LICENSED VAULT: ALL 45+ UNLOCKED TEMPLATES -->
  <main class="max-w-7xl mx-auto px-2 sm:px-4 lg:px-6 pb-12">
    <div class="mb-4 flex items-center justify-between px-1">
      <div class="flex items-center space-x-2">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 shadow-sm animate-pulse"></span>
        <h2 class="text-xs sm:text-base font-black uppercase tracking-wider text-slate-900">
          All 45+ Unlocked Templates &amp; Source Codes
        </h2>
      </div>
      <span class="text-[9.5px] sm:text-[11px] font-bold bg-emerald-100 text-emerald-900 border border-emerald-300 px-2.5 py-0.5 rounded-full">
        45+ Templates Unlocked
      </span>
    </div>

    <!-- 2 In 1 Row on Mobile, 4 In 1 Row on Desktop -->
    <div id="templatesGrid" class="grid grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2.5 sm:gap-4 lg:gap-5">
{all_cards_grid}
    </div>
  </main>
'''

# 8. Replace Header, Hero and Main in html
processed = re.sub(r'<!-- 1\. Ultra-Compact Top Sticky Header -->.*?<!-- 2\. Mobile Top 30% Compact Banner & Hook', new_header + '\n  <!-- 2. Mobile Top 30% Compact Banner & Hook', processed, flags=re.DOTALL)
processed = re.sub(r'<!-- 2\. Mobile Top 30% Compact Banner & Hook.*?<!-- 3\. MAIN LIVE SHOWCASE', new_hero + '\n  <!-- 3. MAIN LIVE SHOWCASE', processed, flags=re.DOTALL)
processed = re.sub(r'<!-- 3\. MAIN LIVE SHOWCASE.*?<!-- 4\. Pricing / Bundle Checkout Banner', new_main + '\n  <!-- 4. Pricing / Bundle Checkout Banner', processed, flags=re.DOTALL)

# Remove any pricing banner or footer checkout banner in purchase portal
processed = re.sub(r'<!-- 4\. Pricing / Bundle Checkout Banner.*?<!-- 5\. Trust & FAQ', '<!-- 5. Trust & FAQ', processed, flags=re.DOTALL)

# Insert Verification Modal and Customization Modal right after <body>
processed = processed.replace(
    '<body class="bg-stone-50 text-slate-900 min-h-screen bg-light-pattern relative selection:bg-gold-400 selection:text-black pb-16 sm:pb-0">',
    '<body class="bg-stone-50 text-slate-900 min-h-screen bg-light-pattern relative selection:bg-gold-400 selection:text-black pb-16 sm:pb-0">\n' + verification_modal + '\n' + customization_modal
)

# Remove checkout modal and mobile floating CTA
processed = re.sub(r'<!-- Instant Checkout Modal.*?<!-- Javascript Logic for scaling phone iframes', '<!-- Javascript Logic for scaling phone iframes', processed, flags=re.DOTALL)

# 9. Portal Script with Firebase RTDB + Color Filtering
portal_script = '''
    // =========================================================================
    // 🔑 FIREBASE REALTIME DATABASE LICENSE VERIFICATION LOGIC
    // =========================================================================
    const RTDB_URL = "https://awdeveloper-f2b8a-default-rtdb.firebaseio.com";
    let currentCustomerLicense = null;

    // Filter Color Categories
    function filterColor(color) {
      document.querySelectorAll('.color-btn').forEach(btn => {
        btn.classList.remove('active', 'bg-gold-500', 'text-slate-950', 'bg-emerald-600', 'text-white', 'bg-purple-600', 'bg-blue-600', 'bg-slate-900');
        btn.classList.add('bg-white', 'text-slate-700');
      });
      const activeBtn = document.getElementById('filter-' + color);
      if (activeBtn) {
        activeBtn.classList.add('active');
        activeBtn.classList.remove('bg-white', 'text-slate-700');
        if (color === 'gold' || color === 'all') {
          activeBtn.classList.add('bg-gold-500', 'text-slate-950');
        } else if (color === 'emerald') {
          activeBtn.classList.add('bg-emerald-600', 'text-white');
        } else if (color === 'purple') {
          activeBtn.classList.add('bg-purple-600', 'text-white');
        } else if (color === 'blue') {
          activeBtn.classList.add('bg-blue-600', 'text-white');
        } else {
          activeBtn.classList.add('bg-slate-900', 'text-white');
        }
      }

      const cards = document.querySelectorAll('.card-phone-unit');
      cards.forEach(card => {
        const cardColor = card.getAttribute('data-color') || '';
        if (color === 'all' || cardColor === color) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    }

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
    // 🛠️ 1-CLICK CUSTOMIZATION & DEPLOYMENT REQUEST WITH RAZORPAY
    // =========================================================================
    function openCustomizationModal() {
      let name = 'Licensed Customer';
      let phone = '';
      let key = 'LIC-ACTIVE';

      if (currentCustomerLicense) {
        name = currentCustomerLicense.name || name;
        phone = currentCustomerLicense.phone || phone;
        key = currentCustomerLicense.key || key;
      }

      const nameEl = document.getElementById('custAutoName');
      const phoneEl = document.getElementById('custAutoPhone');
      const keyEl = document.getElementById('custAutoKey');
      if (nameEl) nameEl.innerText = name;
      if (phoneEl) phoneEl.innerText = phone || 'Registered WhatsApp';
      if (keyEl) keyEl.innerText = key;

      document.getElementById('customizationModal').classList.remove('hidden');
    }

    function closeCustomizationModal() {
      document.getElementById('customizationModal').classList.add('hidden');
    }

    async function startCustomizationPayment() {
      const btn = document.getElementById('btnSubmitCustomization');
      btn.disabled = true;
      btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Initializing Razorpay...';

      const name = currentCustomerLicense ? (currentCustomerLicense.name || 'Licensed Customer') : 'Licensed Customer';
      const phone = currentCustomerLicense ? (currentCustomerLicense.phone || '') : '';
      const key = currentCustomerLicense ? (currentCustomerLicense.key || '') : '';

      const orderData = {
        name: name,
        phone: phone,
        amount: "₹3,999",
        amountInr: 3999,
        licenseKey: key,
        createdAt: new Date().toISOString(),
        status: "Pending Payment"
      };

      const options = {
        key: "rzp_live_TbySDUVsA57Ndi",
        amount: 3999 * 100, // paise
        currency: "INR",
        name: "Digital Theme Store",
        description: "Template Customization, Database & Admin Panel Setup (₹3,999)",
        prefill: {
          name: name,
          contact: phone.replace(/[^0-9]/g, '')
        },
        theme: {
          color: "#4f46e5"
        },
        handler: async function (response) {
          // Meta Pixel: Track Purchase and Lead ONLY upon confirmed payment success
          if (typeof fbq === 'function') {
            fbq('track', 'Purchase', { value: 3999, currency: 'INR', content_name: 'Template Customization Package' });
            fbq('track', 'Lead', { value: 3999, currency: 'INR', content_name: 'Template Customization Package' });
          }
          orderData.status = "Paid / In Progress";
          orderData.paymentId = response.razorpay_payment_id || ("PAY-" + Date.now());
          await saveCustomizationOrder(orderData);
        },
        modal: {
          ondismiss: async function() {
            btn.disabled = false;
            btn.innerHTML = '<i class="fa-solid fa-bolt text-amber-300"></i> <span>Pay ₹3,999 with Razorpay</span>';
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
            btn.innerHTML = '<i class="fa-solid fa-bolt text-amber-300"></i> <span>Pay ₹3,999 with Razorpay</span>';
          });
          rzp.open();
        } else {
          orderData.status = "Direct Inquiry (₹3,999)";
          await saveCustomizationOrder(orderData);
        }
      } catch (err) {
        console.warn("Razorpay fallback:", err);
        orderData.status = "Direct Inquiry (₹3,999)";
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
        const text = encodeURIComponent('Hello, I just booked ₹3,999 Full Customization & Database Setup. My name is ' + orderData.name + ' (License: ' + orderData.licenseKey + ').');
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

# 10. Replace the script section in processed
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

print('Successfully generated purchase/index.html with ALL 44+ templates unlocked. Size:', len(processed))
