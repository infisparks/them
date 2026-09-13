import re

THEME_DATA = {
    # =========================================================================
    # GOLD THEMES
    # =========================================================================
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
    },
    "saas-dark-gold": {
        "title": "SaaS Landing Page Template",
        "subtitle": "Enterprise AI & Software Platform",
        "badge": "SaaS Platform",
        "btn": "SaaS Landing Page Template"
    },
    "ecommerce-white-gold": {
        "title": "Fashion E-Commerce Template",
        "subtitle": "Designer Apparel & Minimalist Boutique",
        "badge": "E-Commerce",
        "btn": "Fashion E-Commerce Template"
    },
    "portfolio-white-gold": {
        "title": "Agency Portfolio Template",
        "subtitle": "Architecture & Modern Interior Studio",
        "badge": "Portfolio",
        "btn": "Agency Portfolio Template"
    },
    "single-product-dark-gold": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Smart Ring & Luxury Wearable Gadget",
        "badge": "Single Product",
        "btn": "Single Product E-Commerce Template"
    },

    # =========================================================================
    # EMERALD & GREEN THEMES
    # =========================================================================
    "funnel-dark-emerald": {
        "title": "Fintech Sales Funnel Template",
        "subtitle": "Wealth Advisory & High-Ticket Investment",
        "badge": "Sales Funnel",
        "btn": "Fintech Sales Funnel Template"
    },
    "funnel-white-emerald": {
        "title": "Healthcare Sales Funnel Template",
        "subtitle": "Clinic & Doctor Appointment Booking",
        "badge": "Sales Funnel",
        "btn": "Healthcare Sales Funnel Template"
    },
    "course-dark-green": {
        "title": "Coding Bootcamp Template",
        "subtitle": "Full-Stack Dev & DevOps Learning Platform",
        "badge": "Online Course",
        "btn": "Coding Bootcamp Template"
    },
    "course-white-green": {
        "title": "Online Course Template",
        "subtitle": "Organic Agriculture & Clean-Tech Academy",
        "badge": "Online Course",
        "btn": "Online Course Template"
    },
    "ecommerce-dark-emerald": {
        "title": "Skincare E-Commerce Template",
        "subtitle": "Organic Cosmetics & Herbal Beauty Store",
        "badge": "E-Commerce",
        "btn": "Organic Skincare E-Commerce Template"
    },
    "ecommerce-white-emerald": {
        "title": "E-Commerce Store Template",
        "subtitle": "Eco-Friendly Bamboo Home Goods & DTC",
        "badge": "E-Commerce",
        "btn": "Eco E-Commerce Store Template"
    },
    "portfolio-dark-emerald": {
        "title": "Cybersecurity Portfolio Template",
        "subtitle": "Security Auditor & Pentesting Consultant",
        "badge": "Portfolio",
        "btn": "Cybersecurity Portfolio Template"
    },
    "portfolio-white-emerald": {
        "title": "Creative Portfolio Template",
        "subtitle": "Landscape Architect & Sustainable Planner",
        "badge": "Portfolio",
        "btn": "Creative Portfolio Template"
    },
    "single-product-dark-emerald": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Cold-Pressed Smart Kitchen Appliance",
        "badge": "Single Product",
        "btn": "Single Product E-Commerce Template"
    },
    "single-product-white-emerald": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Hydroponic Indoor Smart Garden System",
        "badge": "Single Product",
        "btn": "Single Product E-Commerce Template"
    },

    # =========================================================================
    # PURPLE THEMES
    # =========================================================================
    "funnel-dark-purple": {
        "title": "Web3 & Crypto Funnel Template",
        "subtitle": "Token Pre-Sale & Launchpad Platform",
        "badge": "Sales Funnel",
        "btn": "Crypto Sales Funnel Template"
    },
    "funnel-white-purple": {
        "title": "Creative Agency Funnel Template",
        "subtitle": "Branding Studio & Client Discovery Call",
        "badge": "Sales Funnel",
        "btn": "Creative Agency Funnel Template"
    },
    "course-white-purple": {
        "title": "UI/UX Course Template",
        "subtitle": "Figma Design Systems & Mentorship",
        "badge": "Online Course",
        "btn": "UI/UX Design Course Template"
    },
    "ecommerce-dark-purple": {
        "title": "Gaming E-Commerce Template",
        "subtitle": "Pro Gaming Gear & RGB PC Peripherals",
        "badge": "E-Commerce",
        "btn": "Gaming E-Commerce Template"
    },
    "ecommerce-white-purple": {
        "title": "Perfume E-Commerce Template",
        "subtitle": "Artisan Luxury Fragrance & Scent House",
        "badge": "E-Commerce",
        "btn": "Luxury Perfume E-Commerce Template"
    },
    "portfolio-dark-purple": {
        "title": "Video & 3D Portfolio Template",
        "subtitle": "Motion Graphics & VFX Director Showreel",
        "badge": "Portfolio",
        "btn": "Motion Graphics Portfolio Template"
    },
    "portfolio-white-purple": {
        "title": "Fashion Stylist Portfolio Template",
        "subtitle": "Editorial Art Director & Fashion Bio",
        "badge": "Portfolio",
        "btn": "Fashion Stylist Portfolio Template"
    },
    "single-product-dark-purple": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Studio Wireless Audiophile Headphones",
        "badge": "Single Product",
        "btn": "Single Product E-Commerce Template"
    },
    "single-product-white-purple": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Circadian Sunrise Smart Sleep Lamp",
        "badge": "Single Product",
        "btn": "Single Product E-Commerce Template"
    },

    # =========================================================================
    # BLUE THEMES
    # =========================================================================
    "funnel-white-blue": {
        "title": "Dental Clinic Funnel Template",
        "subtitle": "Medical Practice Patient Acquisition",
        "badge": "Sales Funnel",
        "btn": "Dental Clinic Funnel Template"
    },
    "course-white-blue": {
        "title": "Cloud Certification Course Template",
        "subtitle": "AWS Solutions Architect Video Training",
        "badge": "Online Course",
        "btn": "Cloud Course Template"
    },
    "ecommerce-white-blue": {
        "title": "Medical Supply E-Commerce Template",
        "subtitle": "Clinical Equipment & Healthcare Store",
        "badge": "E-Commerce",
        "btn": "Medical Supply E-Commerce Template"
    },
    "portfolio-white-blue": {
        "title": "Lawyer & Attorney Portfolio Template",
        "subtitle": "Corporate Legal Firm & Retainer Booking",
        "badge": "Portfolio",
        "btn": "Lawyer Portfolio Template"
    },
    "single-product-white-blue": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Alkaline Multi-Stage Home Water Purifier",
        "badge": "Single Product",
        "btn": "Single Product E-Commerce Template"
    },

    # =========================================================================
    # CLASSIC THEMES
    # =========================================================================
    "funnel-dark": {
        "title": "Private Equity Funnel Template",
        "subtitle": "M&A Advisory & Investor Deal Room Pitch",
        "badge": "Sales Funnel",
        "btn": "Private Equity Funnel Template"
    },
    "funnel-white": {
        "title": "Coaching & Mastermind Funnel Template",
        "subtitle": "Executive 1-on-1 Mentorship & VSL Lander",
        "badge": "Sales Funnel",
        "btn": "Coaching Funnel Template"
    },
    "course-dark": {
        "title": "Trading & Finance Course Template",
        "subtitle": "Quantitative Trading & Algo Finance",
        "badge": "Online Course",
        "btn": "Trading Course Template"
    },
    "ecommerce-dark": {
        "title": "Leather Goods E-Commerce Template",
        "subtitle": "Handcrafted Leather Luggage & Accessories",
        "badge": "E-Commerce",
        "btn": "Leather Goods E-Commerce Template"
    },
    "ecommerce-white": {
        "title": "Eyewear E-Commerce Template",
        "subtitle": "Italian Acetate Sunglasses & Frames Store",
        "badge": "E-Commerce",
        "btn": "Eyewear E-Commerce Template"
    },
    "portfolio-dark": {
        "title": "Filmmaker Portfolio Template",
        "subtitle": "Commercial Cinematographer & Director Wall",
        "badge": "Portfolio",
        "btn": "Filmmaker Portfolio Template"
    },
    "portfolio-white": {
        "title": "Consultant Portfolio Template",
        "subtitle": "Chartered Accountant & Corporate Tax Strategist",
        "badge": "Portfolio",
        "btn": "Consultant Portfolio Template"
    },
    "single-product-dark": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Automatic Mechanical Luxury Watch",
        "badge": "Single Product",
        "btn": "Single Product E-Commerce Template"
    },
    "single-product-white": {
        "title": "Single Product E-Commerce Template",
        "subtitle": "Ceramic Pour-Over French Press Brewer",
        "badge": "Single Product",
        "btn": "Single Product E-Commerce Template"
    }
}

GOLD_ORDER = [
    "portfolio-dark-gold",          # #1 Portfolio Template
    "funnel-dark-gold",             # #2 Sales Funnel Template
    "realstate-dark-gold",          # #3 Real Estate Template
    "single-product-white-gold",    # #4 Single Product E-Commerce Template
    "funnel-white-gold",            # #5 B2B Sales Funnel Template
    "ecommerce-dark-gold",          # #6 E-Commerce Store Template
    "course-white-gold",            # #7 Online Course Template
    "saas-dark-gold",               # #8 SaaS Landing Page Template
    "ecommerce-white-gold",         # #9 Fashion E-Commerce Template
    "portfolio-white-gold",         # #10 Agency Portfolio Template
    "single-product-dark-gold"      # #11 Single Product E-Commerce Template
]

EMERALD_ORDER = [
    "funnel-dark-emerald",
    "funnel-white-emerald",
    "course-dark-green",
    "course-white-green",
    "ecommerce-dark-emerald",
    "ecommerce-white-emerald",
    "portfolio-dark-emerald",
    "portfolio-white-emerald",
    "single-product-dark-emerald",
    "single-product-white-emerald"
]

PURPLE_ORDER = [
    "funnel-dark-purple",
    "funnel-white-purple",
    "course-white-purple",
    "ecommerce-dark-purple",
    "ecommerce-white-purple",
    "portfolio-dark-purple",
    "portfolio-white-purple",
    "single-product-dark-purple",
    "single-product-white-purple"
]

BLUE_ORDER = [
    "funnel-white-blue",
    "course-white-blue",
    "ecommerce-white-blue",
    "portfolio-white-blue",
    "single-product-white-blue"
]

CLASSIC_ORDER = [
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

def render_card(theme_key, is_hero_row=False, is_purchase_page=False):
    d = THEME_DATA[theme_key]
    prefix = "../" if is_purchase_page else "./"
    
    if is_hero_row:
        iframe_tag = f'<iframe src="{prefix}{theme_key}/index.html" class="live-scaled-iframe hero-iframe" onload="handleIframeLoaded(this)" title="{d["title"]}" loading="eager"></iframe>'
    else:
        iframe_tag = f'<iframe src="about:blank" data-src="{prefix}{theme_key}/index.html" class="live-scaled-iframe" onload="handleIframeLoaded(this)" title="{d["title"]}" loading="lazy"></iframe>'

    badge_bg = "bg-white/95 text-amber-900 border-amber-400" if "white" in theme_key else "bg-black/85 text-gold-400 border-gold-400/40"

    buttons_html = f'''            <button onclick="openPreviewModal('{theme_key}/index.html', '{d["btn"]}')" class="flex-1 btn-gold-main text-[9.5px] sm:text-[11px] font-black py-1 px-1.5 rounded-lg flex items-center justify-center gap-1 shadow-2xs">
              <i class="fa-solid fa-eye text-[8px]"></i>
              <span>Preview</span>
            </button>
            <a href="{prefix}{theme_key}/index.html" target="_blank" class="bg-slate-100 hover:bg-slate-200 text-slate-700 text-[9.5px] sm:text-[11px] font-black py-1 px-2 rounded-lg" title="Open in New Tab">
              ↗
            </a>'''

    return f'''        <!-- {d["title"]} ({theme_key}) -->
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
              {iframe_tag}
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
{buttons_html}
          </div>
        </div>'''

def generate_section_grid(theme_keys, has_hero_eager=False):
    cards = []
    for i, key in enumerate(theme_keys):
        is_hero = has_hero_eager and (i < 4)
        cards.append(render_card(key, is_hero_row=is_hero))
    return "\n\n".join(cards)

def update_html(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Gold Section
    gold_grid = generate_section_grid(GOLD_ORDER, has_hero_eager=True)
    content = re.sub(
        r'(<div class="mb-6 template-group" id="group-gold">[\s\S]*?<div class="grid[^>]*>)([\s\S]*?)(</div>\s*</div>\s*<!-- =+ -->\s*<!-- SECTION 2: EMERALD)',
        r'\1\n' + gold_grid + r'\n      \3',
        content
    )

    # 2. Update Emerald Section
    emerald_grid = generate_section_grid(EMERALD_ORDER)
    content = re.sub(
        r'(<div class="mb-6 template-group" id="group-emerald">[\s\S]*?<div class="grid[^>]*>)([\s\S]*?)(</div>\s*</div>\s*<!-- =+ -->\s*<!-- SECTION 3: PURPLE)',
        r'\1\n' + emerald_grid + r'\n      \3',
        content
    )

    # 3. Update Purple Section
    purple_grid = generate_section_grid(PURPLE_ORDER)
    content = re.sub(
        r'(<div class="mb-6 template-group" id="group-purple">[\s\S]*?<div class="grid[^>]*>)([\s\S]*?)(</div>\s*</div>\s*<!-- =+ -->\s*<!-- SECTION 4: BLUE)',
        r'\1\n' + purple_grid + r'\n      \3',
        content
    )

    # 4. Update Blue Section
    blue_grid = generate_section_grid(BLUE_ORDER)
    content = re.sub(
        r'(<div class="mb-6 template-group" id="group-blue">[\s\S]*?<div class="grid[^>]*>)([\s\S]*?)(</div>\s*</div>\s*<!-- =+ -->\s*<!-- SECTION 5: CLASSIC)',
        r'\1\n' + blue_grid + r'\n      \3',
        content
    )

    # 5. Update Classic Section
    classic_grid = generate_section_grid(CLASSIC_ORDER)
    content = re.sub(
        r'(<div class="mb-6 template-group" id="group-classic">[\s\S]*?<div class="grid[^>]*>)([\s\S]*?)(</div>\s*</div>\s*</main>)',
        r'\1\n' + classic_grid + r'\n      \3',
        content
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {filepath} with explicit Template names!")

def main():
    update_html("index.html")
    update_html("index.source.html")

if __name__ == "__main__":
    main()
