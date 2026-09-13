import re
import json

TOP_7_KEYS = [
    "portfolio-dark-gold",          # 1. Personal Portfolio Template
    "funnel-dark-gold",             # 2. Sales Funnel Template
    "realstate-dark-gold",          # 3. Real Estate Landing Page Template
    "single-product-white-gold",    # 4. Single Product E-Commerce Template
    "funnel-white-gold",            # 5. B2B Sales Funnel Template
    "ecommerce-dark-gold",          # 6. E-Commerce Store Template
    "course-white-gold",            # 7. Online Course Template
]

# Remaining 37 templates
REMAINING_TEMPLATES = [
    # Gold
    {"key": "saas-dark-gold", "cat": "saas", "badge": "SaaS Platform", "title": "SaaS Landing Page Template", "sub": "Enterprise AI & Software Platform"},
    {"key": "ecommerce-white-gold", "cat": "ecom", "badge": "E-Commerce", "title": "Fashion E-Commerce Template", "sub": "Designer Apparel & Minimalist Boutique"},
    {"key": "portfolio-white-gold", "cat": "portfolio", "badge": "Portfolio", "title": "Agency Portfolio Template", "sub": "Architecture & Modern Interior Studio"},
    {"key": "single-product-dark-gold", "cat": "single", "badge": "Single Product", "title": "Single Product E-Commerce Template", "sub": "Smart Ring & Luxury Wearable Gadget"},

    # Emerald
    {"key": "funnel-dark-emerald", "cat": "funnel", "badge": "Sales Funnel", "title": "Fintech Sales Funnel Template", "sub": "Wealth Advisory & High-Ticket Investment"},
    {"key": "funnel-white-emerald", "cat": "funnel", "badge": "Sales Funnel", "title": "Healthcare Sales Funnel Template", "sub": "Clinic & Doctor Appointment Booking"},
    {"key": "course-dark-green", "cat": "course", "badge": "Online Course", "title": "Coding Bootcamp Template", "sub": "Full-Stack Dev & DevOps Learning Platform"},
    {"key": "course-white-green", "cat": "course", "badge": "Online Course", "title": "Online Course Template", "sub": "Organic Agriculture & Clean-Tech Academy"},
    {"key": "ecommerce-dark-emerald", "cat": "ecom", "badge": "E-Commerce", "title": "Skincare E-Commerce Template", "sub": "Organic Cosmetics & Herbal Beauty Store"},
    {"key": "ecommerce-white-emerald", "cat": "ecom", "badge": "E-Commerce", "title": "E-Commerce Store Template", "sub": "Eco-Friendly Bamboo Home Goods & DTC"},
    {"key": "portfolio-dark-emerald", "cat": "portfolio", "badge": "Portfolio", "title": "Cybersecurity Portfolio Template", "sub": "Security Auditor & Pentesting Consultant"},
    {"key": "portfolio-white-emerald", "cat": "portfolio", "badge": "Portfolio", "title": "Creative Portfolio Template", "sub": "Landscape Architect & Sustainable Planner"},
    {"key": "single-product-dark-emerald", "cat": "single", "badge": "Single Product", "title": "Single Product E-Commerce Template", "sub": "Cold-Pressed Smart Kitchen Appliance"},
    {"key": "single-product-white-emerald", "cat": "single", "badge": "Single Product", "title": "Single Product E-Commerce Template", "sub": "Hydroponic Indoor Smart Garden System"},

    # Purple
    {"key": "funnel-dark-purple", "cat": "funnel", "badge": "Sales Funnel", "title": "Web3 & Crypto Funnel Template", "sub": "Token Pre-Sale & Launchpad Platform"},
    {"key": "funnel-white-purple", "cat": "funnel", "badge": "Sales Funnel", "title": "Creative Agency Funnel Template", "sub": "Branding Studio & Client Discovery Call"},
    {"key": "course-white-purple", "cat": "course", "badge": "Online Course", "title": "UI/UX Course Template", "sub": "Figma Design Systems & Mentorship"},
    {"key": "ecommerce-dark-purple", "cat": "ecom", "badge": "E-Commerce", "title": "Gaming E-Commerce Template", "sub": "Pro Gaming Gear & RGB PC Peripherals"},
    {"key": "ecommerce-white-purple", "cat": "ecom", "badge": "E-Commerce", "title": "Perfume E-Commerce Template", "sub": "Artisan Luxury Fragrance & Scent House"},
    {"key": "portfolio-dark-purple", "cat": "portfolio", "badge": "Portfolio", "title": "Video & 3D Portfolio Template", "sub": "Motion Graphics & VFX Director Showreel"},
    {"key": "portfolio-white-purple", "cat": "portfolio", "badge": "Portfolio", "title": "Fashion Stylist Portfolio Template", "sub": "Editorial Art Director & Fashion Bio"},
    {"key": "single-product-dark-purple", "cat": "single", "badge": "Single Product", "title": "Single Product E-Commerce Template", "sub": "Studio Wireless Audiophile Headphones"},
    {"key": "single-product-white-purple", "cat": "single", "badge": "Single Product", "title": "Single Product E-Commerce Template", "sub": "Circadian Sunrise Smart Sleep Lamp"},

    # Blue
    {"key": "funnel-white-blue", "cat": "funnel", "badge": "Sales Funnel", "title": "Dental Clinic Funnel Template", "sub": "Medical Practice Patient Acquisition"},
    {"key": "course-white-blue", "cat": "course", "badge": "Online Course", "title": "Cloud Certification Course Template", "sub": "AWS Solutions Architect Video Training"},
    {"key": "ecommerce-white-blue", "cat": "ecom", "badge": "E-Commerce", "title": "Medical Supply E-Commerce Template", "sub": "Clinical Equipment & Healthcare Store"},
    {"key": "portfolio-white-blue", "cat": "portfolio", "badge": "Portfolio", "title": "Lawyer & Attorney Portfolio Template", "sub": "Corporate Legal Firm & Retainer Booking"},
    {"key": "single-product-white-blue", "cat": "single", "badge": "Single Product", "title": "Single Product E-Commerce Template", "sub": "Alkaline Multi-Stage Home Water Purifier"},

    # Classic
    {"key": "funnel-dark", "cat": "funnel", "badge": "Sales Funnel", "title": "Private Equity Funnel Template", "sub": "M&A Advisory & Investor Deal Room Pitch"},
    {"key": "funnel-white", "cat": "funnel", "badge": "Sales Funnel", "title": "Coaching & Mastermind Funnel Template", "sub": "Executive 1-on-1 Mentorship & VSL Lander"},
    {"key": "course-dark", "cat": "course", "badge": "Online Course", "title": "Trading & Finance Course Template", "sub": "Quantitative Trading & Algo Finance"},
    {"key": "ecommerce-dark", "cat": "ecom", "badge": "E-Commerce", "title": "Leather Goods E-Commerce Template", "sub": "Handcrafted Leather Luggage & Accessories"},
    {"key": "ecommerce-white", "cat": "ecom", "badge": "E-Commerce", "title": "Eyewear E-Commerce Template", "sub": "Italian Acetate Sunglasses & Frames Store"},
    {"key": "portfolio-dark", "cat": "portfolio", "badge": "Portfolio", "title": "Filmmaker Portfolio Template", "sub": "Commercial Cinematographer & Director Wall"},
    {"key": "portfolio-white", "cat": "portfolio", "badge": "Portfolio", "title": "Consultant Portfolio Template", "sub": "Chartered Accountant & Corporate Tax Strategist"},
    {"key": "single-product-dark", "cat": "single", "badge": "Single Product", "title": "Single Product E-Commerce Template", "sub": "Automatic Mechanical Luxury Watch"},
    {"key": "single-product-white", "cat": "single", "badge": "Single Product", "title": "Single Product E-Commerce Template", "sub": "Ceramic Pour-Over French Press Brewer"}
]

THEME_DATA = {
    "portfolio-dark-gold": {
        "title": "Personal Portfolio Template",
        "subtitle": "Developer, Consultant & Architect Profile",
        "badge": "Portfolio",
        "btn": "Personal Portfolio Template"
    },
    "funnel-dark-gold": {
        "title": "Sales Funnel Template",
        "subtitle": "Meta Ads & Performance Agency Lander",
        "badge": "Sales Funnel",
        "btn": "Meta Ads Sales Funnel Template"
    },
    "realstate-dark-gold": {
        "title": "Real Estate Landing Page Template",
        "subtitle": "Luxury Properties, Penthouse & Sky Villas",
        "badge": "Real Estate",
        "btn": "Real Estate Landing Page Template"
    },
    "single-product-white-gold": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Ergonomic Workspace & DTC Product Lander",
        "badge": "Single Product",
        "btn": "Single Product E-Commerce Template"
    },
    "funnel-white-gold": {
        "title": "B2B Sales Funnel Template",
        "subtitle": "Growth Agency & High-Ticket Retainers",
        "badge": "Sales Funnel",
        "btn": "B2B Sales Funnel Template"
    },
    "ecommerce-dark-gold": {
        "title": "E-Commerce Store Template",
        "subtitle": "Luxury Watches & High-End Jewelry",
        "badge": "E-Commerce",
        "btn": "Luxury E-Commerce Store Template"
    },
    "course-white-gold": {
        "title": "Online Course Template",
        "subtitle": "Tech Academy & AI Masterclass Platform",
        "badge": "Course / EdTech",
        "btn": "Online Course & Academy Template"
    }
}

def render_top_card(theme_key, index):
    d = THEME_DATA[theme_key]
    badge_bg = "bg-white/95 text-amber-900 border-amber-400" if "white" in theme_key else "bg-black/85 text-gold-400 border-gold-400/40"
    
    # First 4 are loaded eager, next 3 are lazy
    loading_attr = 'loading="eager"' if index < 4 else 'loading="lazy"'
    
    return f'''        <!-- #{index+1}: {d["title"]} ({theme_key}) -->
        <div class="card-phone-unit rounded-2xl p-1.5 sm:p-3 text-left flex flex-col justify-between border-gold-300/80">
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
              <iframe src="./{theme_key}/index.html" class="live-scaled-iframe hero-iframe" onload="handleIframeLoaded(this)" title="{d["title"]}" {loading_attr}></iframe>
              <div class="absolute top-1.5 left-1.5 z-20">
                <span class="{badge_bg} border text-[7.5px] sm:text-[9px] font-black px-1.5 py-0.2 rounded shadow">
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
            <button onclick="openPreviewModal('{theme_key}/index.html', '{d["btn"]}')" class="flex-1 btn-gold-main text-[9.5px] sm:text-[11px] font-black py-1 px-1.5 rounded-lg flex items-center justify-center gap-1 shadow-2xs">
              <i class="fa-solid fa-eye text-[8px]"></i>
              <span>Preview</span>
            </button>
            <a href="./{theme_key}/index.html" target="_blank" class="bg-slate-100 hover:bg-slate-200 text-slate-700 text-[9.5px] sm:text-[11px] font-black py-1 px-2 rounded-lg" title="Open in New Tab">
              ↗
            </a>
          </div>
        </div>'''

def render_unlock_card():
    return '''        <!-- #8: VIP LOCK CARD (+38 MORE TEMPLATES UNLOCKED FREE) -->
        <div class="card-phone-unit rounded-2xl p-1.5 sm:p-3 text-left flex flex-col justify-between border-2 border-dashed border-amber-400/90 bg-gradient-to-br from-amber-500/15 via-slate-900 to-black text-white relative overflow-hidden shadow-xl group">
          
          <div class="space-y-2">
            <!-- Simulated Phone Mockup with Luxury Lock Experience -->
            <div class="phone-mockup-frame group border border-amber-400/40 bg-slate-950 flex flex-col items-center justify-between p-3 sm:p-4 text-center relative overflow-hidden">
              <div class="phone-notch"></div>
              
              <!-- Subtle Background Light Beam -->
              <div class="absolute -top-12 -right-12 w-32 h-32 bg-amber-500/20 rounded-full blur-2xl pointer-events-none"></div>

              <!-- Top Badge -->
              <div class="pt-2 z-10">
                <span class="inline-flex items-center gap-1 bg-amber-500/20 border border-amber-400/60 text-amber-300 text-[8px] sm:text-[9.5px] font-black px-2 py-0.5 rounded-full uppercase tracking-wider animate-pulse">
                  <i class="fa-solid fa-crown text-amber-400 text-[9px]"></i> +38 More Included
                </span>
              </div>

              <!-- Center Big Lock & Value Punch -->
              <div class="my-auto space-y-2 z-10">
                <div class="w-12 h-12 sm:w-14 sm:h-14 mx-auto rounded-2xl bg-gradient-to-tr from-amber-600 to-yellow-400 flex items-center justify-center text-slate-950 shadow-lg shadow-amber-500/30">
                  <i class="fa-solid fa-lock text-lg sm:text-xl"></i>
                </div>
                <div>
                  <h4 class="text-xs sm:text-sm font-black text-white leading-tight">
                    Unlock All 45+ Templates
                  </h4>
                  <p class="text-[8.5px] sm:text-[9.5px] text-amber-200/90 font-medium mt-0.5">
                    1-Time ₹999 Payment • No Monthly Fees
                  </p>
                </div>

                <!-- Feature Mini Bullets -->
                <div class="space-y-1 text-left bg-white/5 border border-white/10 rounded-xl p-2 text-[8px] sm:text-[9px] text-slate-300">
                  <div class="flex items-center gap-1 text-amber-300 font-bold">
                    <i class="fa-solid fa-circle-check text-[7.5px] text-emerald-400"></i> SaaS, Ecom, Funnels &amp; Portfolios
                  </div>
                  <div class="flex items-center gap-1">
                    <i class="fa-solid fa-circle-check text-[7.5px] text-emerald-400"></i> Full Clean HTML, Tailwind &amp; CSS
                  </div>
                  <div class="flex items-center gap-1">
                    <i class="fa-solid fa-circle-check text-[7.5px] text-emerald-400"></i> Commercial Unlimited License
                  </div>
                </div>
              </div>

              <!-- CTA Inside Phone Screen -->
              <div class="w-full z-10 pt-1">
                <button onclick="openCheckoutModal()" class="w-full py-2 px-2 rounded-xl bg-gradient-to-r from-amber-500 via-amber-400 to-yellow-500 text-slate-950 font-black text-[10px] sm:text-xs uppercase tracking-tight shadow-md hover:brightness-110 active:scale-95 transition-all flex items-center justify-center gap-1.5 cursor-pointer">
                  <span>Unlock Everything (₹999)</span>
                  <i class="fa-solid fa-bolt text-[10px]"></i>
                </button>
              </div>
            </div>

            <!-- Card Bottom Info -->
            <div class="px-0.5">
              <h3 class="text-[11px] sm:text-xs font-black text-slate-900 truncate flex items-center gap-1">
                <span class="text-amber-600">⚡</span> +38 More Premium Templates
              </h3>
              <p class="text-[8.5px] sm:text-[10px] text-slate-500 truncate">
                Get All 45 Themes In One Instant ZIP Download
              </p>
            </div>
          </div>

          <!-- Card Actions -->
          <div class="flex items-center gap-1 pt-1.5 border-t border-slate-100 mt-1">
            <button onclick="openCheckoutModal()" class="flex-1 py-1.5 px-2 rounded-lg bg-slate-900 hover:bg-slate-800 text-amber-400 text-[10px] sm:text-[11px] font-black flex items-center justify-center gap-1.5 shadow-sm transition-all cursor-pointer">
              <i class="fa-solid fa-key text-[9px]"></i>
              <span>Buy ₹999 &amp; Unlock All 45+</span>
            </button>
          </div>
        </div>'''

def render_catalog_items():
    items = []
    for item in REMAINING_TEMPLATES:
        items.append(f'''        <!-- {item["title"]} ({item["key"]}) -->
        <div class="catalog-item bg-white rounded-xl p-3 border border-slate-200 hover:border-amber-400 shadow-2xs hover:shadow-md transition-all flex flex-col justify-between text-left group" data-cat="{item["cat"]}">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="text-[8px] font-black uppercase tracking-wider px-2 py-0.5 rounded-full bg-slate-100 text-slate-700 border border-slate-200">
                {item["badge"]}
              </span>
              <span class="text-[9px] font-bold text-amber-600 flex items-center gap-1">
                <i class="fa-solid fa-check-circle text-emerald-500"></i> Included Free
              </span>
            </div>
            <div>
              <h4 class="text-xs font-extrabold text-slate-900 group-hover:text-amber-600 transition-colors line-clamp-1">
                {item["title"]}
              </h4>
              <p class="text-[10px] text-slate-500 line-clamp-1 mt-0.5">
                {item["sub"]}
              </p>
            </div>
          </div>
          <div class="flex items-center gap-1.5 pt-2.5 mt-2 border-t border-slate-100">
            <button onclick="openPreviewModal('{item["key"]}/index.html', '{item["title"]}')" class="flex-1 py-1 px-2 rounded-lg bg-slate-100 hover:bg-amber-100 text-slate-800 hover:text-amber-900 text-[10px] font-bold flex items-center justify-center gap-1 transition-colors cursor-pointer">
              <i class="fa-solid fa-eye text-[8.5px]"></i> Preview
            </button>
            <button onclick="openCheckoutModal()" class="py-1 px-2 rounded-lg bg-amber-500 hover:bg-amber-600 text-slate-950 text-[10px] font-black flex items-center justify-center gap-1 transition-colors cursor-pointer" title="Unlock With ₹999 Bundle">
              <i class="fa-solid fa-download text-[8.5px]"></i>
            </button>
          </div>
        </div>''')
    return "\n".join(items)

def render_showcase_section():
    top_cards = []
    for i, key in enumerate(TOP_7_KEYS):
        top_cards.append(render_top_card(key, i))
    top_cards.append(render_unlock_card())
    grid_html = "\n\n".join(top_cards)

    catalog_html = render_catalog_items()

    return f'''    <!-- ========================================== -->
    <!-- SECTION 1: TOP 7 LIVE MOBILE PREVIEWS + VIP UNLOCK CARD -->
    <!-- ========================================== -->
    <div class="mb-8" id="live-screens">
      <div class="flex items-center justify-between mb-3 px-1">
        <div class="flex items-center space-x-2">
          <span class="w-2.5 h-2.5 rounded-full bg-amber-500 shadow-sm animate-pulse"></span>
          <h2 class="text-xs sm:text-base font-black uppercase tracking-wider text-slate-900">
            🏆 Top Featured Interactive Previews
          </h2>
        </div>
        <span class="text-[9.5px] sm:text-[11px] font-bold bg-amber-100 text-amber-900 border border-amber-300 px-2.5 py-0.5 rounded-full">
          7 Live Previews • 38+ More In Bundle
        </span>
      </div>

      <!-- 2 In 1 Row on Mobile, 4 In 1 Row on Desktop (Exactly 8 Cards = 2 Full Rows) -->
      <div class="grid grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2.5 sm:gap-4 lg:gap-5">
{grid_html}
      </div>
    </div>

    <!-- ========================================== -->
    <!-- SECTION 2: DIRECT COUNT & 1-CLICK BUNDLE UNLOCK (ZERO PREVIEWS, ZERO LAG) -->
    <!-- ========================================== -->
    <div class="mb-10 bg-gradient-to-b from-slate-900 via-slate-950 to-black rounded-3xl p-5 sm:p-8 border border-amber-400/40 shadow-2xl text-white text-center sm:text-left relative overflow-hidden" id="bundle-unlock">
      
      <!-- Subtle Background Glow -->
      <div class="absolute -top-20 -right-20 w-60 h-60 bg-amber-500/15 rounded-full blur-3xl pointer-events-none"></div>

      <div class="relative z-10 flex flex-col lg:flex-row items-center justify-between gap-6">
        
        <!-- Left: Huge Count & Category Breakdown -->
        <div class="space-y-3 max-w-2xl">
          <div class="inline-flex items-center gap-2 text-amber-300 bg-amber-500/20 border border-amber-400/60 px-3 py-1 rounded-full text-xs font-black uppercase tracking-wider">
            <i class="fa-solid fa-crown text-amber-400"></i>
            <span>+38 More Templates Included (45+ Total In Bundle)</span>
          </div>

          <h3 class="text-xl sm:text-3xl font-black text-white tracking-tight leading-tight">
            Buy Today for Just <span class="text-amber-400">₹999</span> &amp; Get All 45+ Templates Free
          </h3>

          <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
            You just saw the top 7 interactive screens above. When you order right now, you instantly unlock the complete collection of <strong>45+ production-ready landing pages</strong> with 100% clean, unencrypted source code:
          </p>

          <!-- Direct Category Counts Grid -->
          <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 pt-1 text-[11px] sm:text-xs">
            <div class="bg-white/5 border border-white/10 rounded-xl p-2.5 text-left flex items-center gap-2">
              <span class="text-base">🛒</span>
              <div>
                <strong class="text-white block font-black">10+ E-Commerce</strong>
                <span class="text-[10px] text-slate-400">Luxury, Fashion &amp; DTC</span>
              </div>
            </div>

            <div class="bg-white/5 border border-white/10 rounded-xl p-2.5 text-left flex items-center gap-2">
              <span class="text-base">⚡</span>
              <div>
                <strong class="text-white block font-black">9+ Sales Funnels</strong>
                <span class="text-[10px] text-slate-400">Meta Ads &amp; High-Ticket</span>
              </div>
            </div>

            <div class="bg-white/5 border border-white/10 rounded-xl p-2.5 text-left flex items-center gap-2">
              <span class="text-base">🎯</span>
              <div>
                <strong class="text-white block font-black">8+ Single Product</strong>
                <span class="text-[10px] text-slate-400">Gadgets, Kitchen &amp; Home</span>
              </div>
            </div>

            <div class="bg-white/5 border border-white/10 rounded-xl p-2.5 text-left flex items-center gap-2">
              <span class="text-base">💼</span>
              <div>
                <strong class="text-white block font-black">7+ Portfolios</strong>
                <span class="text-[10px] text-slate-400">Architects, Devs &amp; Agencies</span>
              </div>
            </div>

            <div class="bg-white/5 border border-white/10 rounded-xl p-2.5 text-left flex items-center gap-2">
              <span class="text-base">🎓</span>
              <div>
                <strong class="text-white block font-black">6+ Online Courses</strong>
                <span class="text-[10px] text-slate-400">Bootcamps &amp; AI Academies</span>
              </div>
            </div>

            <div class="bg-white/5 border border-white/10 rounded-xl p-2.5 text-left flex items-center gap-2">
              <span class="text-base">🤖</span>
              <div>
                <strong class="text-white block font-black">5+ SaaS &amp; AI</strong>
                <span class="text-[10px] text-slate-400">Terminal, ROI &amp; Pricing</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Right: Action Box & Checkout Button -->
        <div class="w-full lg:w-auto flex-shrink-0 bg-white/10 border border-white/15 backdrop-blur-md rounded-2xl p-4 sm:p-6 text-center space-y-3 min-w-[280px]">
          <div class="text-[11px] font-bold text-amber-300 uppercase tracking-wider">
            ⚡ Instant WhatsApp Delivery
          </div>
          <div class="flex items-baseline justify-center gap-2">
            <span class="text-sm text-slate-400 line-through">₹29,999</span>
            <span class="text-3xl sm:text-4xl font-black text-amber-400">₹999</span>
            <span class="text-[10px] font-extrabold bg-emerald-500/30 text-emerald-300 border border-emerald-400/50 px-2 py-0.5 rounded-md">Save 97%</span>
          </div>

          <button onclick="openCheckoutModal()" class="w-full py-3.5 px-6 rounded-xl bg-gradient-to-r from-amber-500 via-amber-400 to-yellow-500 hover:from-amber-400 hover:to-yellow-300 text-slate-950 font-black text-xs sm:text-sm uppercase tracking-tight shadow-xl hover:shadow-amber-500/30 active:scale-95 transition-all flex items-center justify-center gap-2 cursor-pointer">
            <span>Buy Now &amp; Unlock All 45+</span>
            <i class="fa-solid fa-arrow-right text-xs"></i>
          </button>

          <p class="text-[10px] text-slate-400">
            🔒 Commercial License • Unlimited Client Sites
          </p>
        </div>

      </div>
    </div>'''

def update_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_showcase = render_showcase_section()

    # Replace the whole main section inside <main class="max-w-7xl mx-auto px-2 sm:px-4 lg:px-6 pb-12"> ... </main>
    pattern = r'(<main class="max-w-7xl mx-auto px-2 sm:px-4 lg:px-6 pb-12">)[\s\S]*?(</main>)'
    content = re.sub(pattern, r'\1\n' + new_showcase + r'\n  \2', content)

    # Add the quick catalog filter JS if not present
    js_func = '''
    // Catalog Filtering for remaining 38+ templates
    function filterCatalog(category) {
      document.querySelectorAll('.cat-tab').forEach(t => {
        t.className = "cat-tab px-3 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-700 border border-slate-200 hover:border-amber-400 flex-shrink-0 cursor-pointer";
      });
      const activeTab = document.getElementById('catTab-' + category);
      if (activeTab) {
        activeTab.className = "cat-tab px-3 py-1.5 rounded-xl text-xs font-black bg-slate-900 text-white shadow-xs flex-shrink-0 cursor-pointer";
      }

      document.querySelectorAll('.catalog-item').forEach(item => {
        const itemCat = item.getAttribute('data-cat');
        if (category === 'all' || itemCat === category || (category === 'course' && itemCat === 'saas')) {
          item.classList.remove('hidden');
        } else {
          item.classList.add('hidden');
        }
      });
    }
'''
    if "function filterCatalog" not in content:
        content = content.replace("function filterColor(color) {", js_func + "\n    function filterColor(color) {")

    # Update top filter buttons to clean navigation
    top_pills_old = r'(<div class="flex items-center justify-start sm:justify-center space-x-1 sm:space-x-1\.5 overflow-x-auto no-scrollbar py-0\.5 text-\[10px\] sm:text-xs">)[\s\S]*?(</div>\s*</section>)'
    top_pills_new = '''<div class="flex items-center justify-start sm:justify-center space-x-1 sm:space-x-1.5 overflow-x-auto no-scrollbar py-0.5 text-[10px] sm:text-xs">
      <a href="#live-screens" class="py-1 px-2.5 rounded-lg bg-gold-500 text-slate-950 font-black shadow-xs flex-shrink-0 flex items-center gap-1">
        <i class="fa-solid fa-mobile-screen"></i> 7 Top Live Previews
      </a>
      <a href="#full-catalog" class="py-1 px-2.5 rounded-lg bg-white border border-amber-300 text-amber-900 hover:bg-amber-50 font-extrabold flex-shrink-0 flex items-center gap-1">
        <i class="fa-solid fa-layer-group text-amber-500"></i> +38 More In Bundle
      </a>
      <button onclick="openCheckoutModal()" class="py-1 px-2.5 rounded-lg bg-white border border-slate-200 text-emerald-800 hover:bg-emerald-50 font-bold flex-shrink-0 flex items-center gap-1 cursor-pointer">
        <i class="fa-solid fa-tag text-emerald-600"></i> Get Everything ₹999
      </button>
      <a href="https://wa.me/919958399157?text=Hi%2C%20I%20want%20custom%20landing%20page%20design" target="_blank" class="py-1 px-2.5 rounded-lg bg-white border border-slate-200 text-slate-700 hover:bg-slate-100 font-bold flex-shrink-0 flex items-center gap-1">
        <i class="fa-brands fa-whatsapp text-emerald-500"></i> Custom Pages
      </a>
    </div>
  </section>'''
    content = re.sub(top_pills_old, top_pills_new, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {filepath} with fast 7-preview showcase + 38 unlock catalog!")

def main():
    update_file("index.html")
    update_file("index.source.html")

if __name__ == "__main__":
    main()
