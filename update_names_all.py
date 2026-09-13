import re

THEME_DATA = {
    # Gold Themes
    "portfolio-dark-gold": {
        "title": "Senior Software Architect & Consultant",
        "subtitle": "Skills Radar, Code Demos & Hire Funnel",
        "badge": "Portfolio",
        "btn": "Personal Portfolio - Senior Architect"
    },
    "funnel-dark-gold": {
        "title": "Meta Ads & Performance Agency Sales Funnel",
        "subtitle": "High-Ticket VSL, 12 Video Proofs & Lead Booking",
        "badge": "Meta Ads",
        "btn": "Performance Agency - Meta Ads Funnel"
    },
    "realstate-dark-gold": {
        "title": "Luxury Real Estate & Penthouse Villas",
        "subtitle": "Floor Plans, 3D Virtual Tour & Mortgage Calc",
        "badge": "Real Estate",
        "btn": "Luxury Real Estate - Sky Villas"
    },
    "course-white-gold": {
        "title": "Tech Architect & AI Masterclass Platform",
        "subtitle": "2-in-1 Cards, Video Proofs & Curriculum",
        "badge": "EdTech",
        "btn": "Tech Architect - AI Masterclass"
    },
    "ecommerce-dark-gold": {
        "title": "Luxury Watches & High-End Jewelry Store",
        "subtitle": "Ajax Cart Drawer, 360° Zoom & Fast Checkout",
        "badge": "E-Commerce",
        "btn": "Luxury Jewelry - Dark Gold Boutique"
    },
    "single-product-white-gold": {
        "title": "Ergonomic Workspace & DTC Setup Lander",
        "subtitle": "Conversion Buy Box, Feature Grid & Proofs",
        "badge": "DTC Product",
        "btn": "Ergonomic Desk - DTC Product Lander"
    },
    "saas-dark-gold": {
        "title": "Enterprise AI Platform & Micro-SaaS Lander",
        "subtitle": "Interactive Terminal, Pricing & ROI Calc",
        "badge": "AI & SaaS",
        "btn": "Enterprise AI - Micro-SaaS Lander"
    },
    "funnel-white-gold": {
        "title": "B2B Growth Agency & Retainer Acquisition",
        "subtitle": "Audit Booking, Case Studies & High-Ticket Pitch",
        "badge": "B2B Funnel",
        "btn": "B2B Growth Agency - High-Ticket Pitch"
    },
    "ecommerce-white-gold": {
        "title": "Designer Fashion & Minimalist Boutique",
        "subtitle": "Editorial Lookbook, Size Guide & Sticky Cart",
        "badge": "Fashion Store",
        "btn": "Designer Fashion - Minimalist Boutique"
    },
    "portfolio-white-gold": {
        "title": "Architecture & Modern Interior Studio",
        "subtitle": "High-Res Bento Gallery & VIP Client Booking",
        "badge": "Studio Bento",
        "btn": "Interior Design - Studio Architecture"
    },
    "single-product-dark-gold": {
        "title": "Smart Ring & Luxury Wearable DTC Lander",
        "subtitle": "Biometric Sensors, Titanium & Instant Buy",
        "badge": "Wearable Tech",
        "btn": "Smart Ring - Luxury Wearable Tech"
    },

    # Emerald Themes
    "funnel-dark-emerald": {
        "title": "Fintech & Wealth Advisory Sales Funnel",
        "subtitle": "High-Net-Worth Lead Form & Trust Proofs",
        "badge": "Fintech Funnel",
        "btn": "Fintech & Wealth Advisory Funnel"
    },
    "funnel-white-emerald": {
        "title": "Health & Wellness Clinic Patient Funnel",
        "subtitle": "Doctor Booking, Testimonials & WhatsApp CTA",
        "badge": "Medical Clinic",
        "btn": "Health Clinic - Patient Acquisition"
    },
    "course-dark-green": {
        "title": "Full-Stack Coding & DevOps Bootcamp",
        "subtitle": "Syllabus Roadmap, Terminal & Live Cohort",
        "badge": "Dev Bootcamp",
        "btn": "Full-Stack Dev & DevOps Bootcamp"
    },
    "course-white-green": {
        "title": "Organic Agri & Clean-Tech Academy",
        "subtitle": "Video Modules, Certifications & Enrollment",
        "badge": "Green Academy",
        "btn": "Organic Agriculture & Clean-Tech"
    },
    "ecommerce-dark-emerald": {
        "title": "Organic Skincare & Herbal Cosmetics",
        "subtitle": "Ingredient Spotlight & Bundle Discounts",
        "badge": "Skincare Store",
        "btn": "Herbal Cosmetics - Organic Skincare"
    },
    "ecommerce-white-emerald": {
        "title": "Eco-Friendly Bamboo Home Goods Store",
        "subtitle": "Sustainability Badges & Verified Reviews",
        "badge": "Eco Store",
        "btn": "Eco Home Goods - Bamboo Essentials"
    },
    "portfolio-dark-emerald": {
        "title": "Cybersecurity & Pentesting Consultant",
        "subtitle": "CVE Audits, Terminal Demos & Hire Form",
        "badge": "Cyber Security",
        "btn": "Cybersecurity & Penetration Testing"
    },
    "portfolio-white-emerald": {
        "title": "Landscape Architect & Sustainable Planner",
        "subtitle": "Green Blueprint Showcase & Consultation",
        "badge": "Landscape Bio",
        "btn": "Sustainable Landscape & Architect"
    },
    "single-product-dark-emerald": {
        "title": "Cold-Pressed Smart Juicer Appliance",
        "subtitle": "Macro Nutrition Specs & 1-Click Buy Box",
        "badge": "Smart Kitchen",
        "btn": "Cold-Pressed Smart Juicer Lander"
    },
    "single-product-white-emerald": {
        "title": "Hydroponic Indoor Smart Garden System",
        "subtitle": "IoT App Controls & Organic Harvest Proofs",
        "badge": "Smart Garden",
        "btn": "Hydroponic Indoor Smart Garden"
    },

    # Purple Themes
    "funnel-dark-purple": {
        "title": "Crypto & Web3 Token Pre-Sale Funnel",
        "subtitle": "Tokenomics, Roadmap & Investor KYC Flow",
        "badge": "Web3 & Crypto",
        "btn": "Web3 Token Pre-Sale & Launchpad"
    },
    "funnel-white-purple": {
        "title": "Creative Agency & Brand Studio Pitch",
        "subtitle": "Showreel Hero, Client Logos & Discovery Call",
        "badge": "Brand Agency",
        "btn": "Creative Agency - Studio Pitch Funnel"
    },
    "course-white-purple": {
        "title": "UI/UX Design & Figma Mastery Bootcamp",
        "subtitle": "Design Systems, Reviews & Mentorship",
        "badge": "UI/UX Course",
        "btn": "UI/UX & Figma Design System Mastery"
    },
    "ecommerce-dark-purple": {
        "title": "Gaming Peripherals & Pro RGB Hardware",
        "subtitle": "Specs Comparison & 1-Click Fast Cart",
        "badge": "Gaming Store",
        "btn": "Gaming Peripherals & Pro Hardware"
    },
    "ecommerce-white-purple": {
        "title": "Artisan Perfumes & Luxury Fragrance",
        "subtitle": "Scent Notes Matrix & Discovery Sample Kit",
        "badge": "Perfume House",
        "btn": "Artisan Perfumes - Luxury Fragrance"
    },
    "portfolio-dark-purple": {
        "title": "Motion Graphics Director & 3D VFX Artist",
        "subtitle": "Full-Screen 60fps Showreel & Project Quotes",
        "badge": "VFX Showreel",
        "btn": "3D VFX & Motion Graphics Director"
    },
    "portfolio-white-purple": {
        "title": "Fashion Stylist & Editorial Art Director",
        "subtitle": "Magazine Gallery, Runway & VIP Booking",
        "badge": "Fashion Stylist",
        "btn": "Fashion Stylist - Editorial Director"
    },
    "single-product-dark-purple": {
        "title": "Audiophile Studio Wireless Headphones",
        "subtitle": "Frequency Graph, Hi-Res Audio & Buy Box",
        "badge": "Pro Audio",
        "btn": "Audiophile Studio Headphones Lander"
    },
    "single-product-white-purple": {
        "title": "Smart Circadian Sunrise Sleep Lamp",
        "subtitle": "Sleep Science, App Rhythm & 30-Day Trial",
        "badge": "Sleep Wellness",
        "btn": "Circadian Sleep Lamp - DTC Wellness"
    },

    # Blue Themes
    "funnel-white-blue": {
        "title": "Dental & Implant Clinic Patient Funnel",
        "subtitle": "Doctor Profiles & Online Appointment Booking",
        "badge": "Dental Practice",
        "btn": "Dental Clinic - Patient Acquisition"
    },
    "course-white-blue": {
        "title": "Cloud Computing & AWS Architect Course",
        "subtitle": "Hands-On Labs, Practice Exams & Cert Pass",
        "badge": "Cloud Course",
        "btn": "AWS Solutions Architect Certification"
    },
    "ecommerce-white-blue": {
        "title": "Medical Equipment & Orthopedic Supplies",
        "subtitle": "FDA Compliance & Bulk Clinic Discounts",
        "badge": "Medical Supply",
        "btn": "Medical Supplies - Clinic Equipment"
    },
    "portfolio-white-blue": {
        "title": "Corporate Law Firm & Legal Strategist",
        "subtitle": "Practice Areas, Verdicts & Retainer Form",
        "badge": "Legal Partner",
        "btn": "Corporate Law - Legal Advisory Bio"
    },
    "single-product-white-blue": {
        "title": "Alkaline Multi-Stage Water Purifier",
        "subtitle": "Mineral Tech, Water Test & Install Order",
        "badge": "Home Purifier",
        "btn": "Alkaline Water Purifier - Home Tech"
    },

    # Classic Themes
    "funnel-dark": {
        "title": "Private Equity & M&A Deal Advisory",
        "subtitle": "Deal Room Access, Pitch Deck & NDA Gate",
        "badge": "Private Equity",
        "btn": "Private Equity - M&A Deal Advisory"
    },
    "funnel-white": {
        "title": "Executive Business Coaching Mastermind",
        "subtitle": "1-on-1 CEO Application & High-Ticket VSL",
        "badge": "CEO Coaching",
        "btn": "Executive Coaching - Mastermind Funnel"
    },
    "course-dark": {
        "title": "Quant Trading & Algo Finance Academy",
        "subtitle": "Backtesting Demos, Python Scripts & Alpha",
        "badge": "Quant Finance",
        "btn": "Quant Trading - Algorithmic Finance"
    },
    "ecommerce-dark": {
        "title": "Handcrafted Leather Goods & Luggage",
        "subtitle": "Heritage Craft, Monogram & Lifetime Proof",
        "badge": "Leather Goods",
        "btn": "Handcrafted Leather - Travel Luggage"
    },
    "ecommerce-white": {
        "title": "Italian Acetate Minimalist Eyewear",
        "subtitle": "Virtual 3D Try-On & Prescription Order",
        "badge": "Eyewear DTC",
        "btn": "Minimalist Eyewear - Acetate Glasses"
    },
    "portfolio-dark": {
        "title": "Cinematographer & Commercial Director",
        "subtitle": "4K Video Wall, Brand Ads & Booking Agency",
        "badge": "Cinematography",
        "btn": "Commercial Director - 4K Film Portfolio"
    },
    "portfolio-white": {
        "title": "Chartered Accountant & Corporate Tax Pro",
        "subtitle": "Audit Services, Tax Plans & Calendar Booking",
        "badge": "Chartered Tax",
        "btn": "Chartered Accountant - Tax Strategist"
    },
    "single-product-dark": {
        "title": "Automatic Mechanical Luxury Timepiece",
        "subtitle": "Sapphire Crystal, Skeleton Dial & Buy Now",
        "badge": "Luxury Watch",
        "btn": "Mechanical Timepiece - Luxury Horology"
    },
    "single-product-white": {
        "title": "Ceramic Pour-Over French Press Brewer",
        "subtitle": "Brew Ratio Calculator & Barista Bundle Box",
        "badge": "Artisan Coffee",
        "btn": "Ceramic French Press - Coffee Lander"
    }
}

GOLD_ORDER = [
    "portfolio-dark-gold",
    "funnel-dark-gold",
    "realstate-dark-gold",          # #3 strictly Real Estate
    "course-white-gold",             # #4 Tech Architect
    "ecommerce-dark-gold",
    "single-product-white-gold",
    "saas-dark-gold",
    "funnel-white-gold",
    "ecommerce-white-gold",
    "portfolio-white-gold",
    "single-product-dark-gold"
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
    
    # Hero row (top 4) loads eager with direct src; rest load lazy with data-src
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
    gold_pattern = r'(<div class="mb-6 template-group" id="group-gold">.*?<div class="grid[^>]*>).*?(</div>\s*</div>\s*<!-- =+ -->\s*<!-- SECTION 2: EMERALD)'
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
    print(f"Updated {filepath} successfully with perfect names and structure!")

def main():
    update_html("index.html")
    update_html("index.source.html")

if __name__ == "__main__":
    main()
