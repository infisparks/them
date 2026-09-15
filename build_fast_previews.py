import os
import base64
from bs4 import BeautifulSoup
from re_encrypt import encrypt_payload, build_protected_html

CLEAN_DIR = ".clean_templates_source"

def build_course_cards(theme_key):
    courses = [
        {
            "title": "Full-Stack Next.js 15 & Supabase Masterclass",
            "cat": "Full-Stack Dev",
            "img": "image/1.png",
            "badge": "BEST SELLER",
            "duration": "18.5 Hours",
            "rating": "4.9",
            "reviews": "480",
            "price": "₹1,499",
            "origPrice": "₹4,999"
        },
        {
            "title": "AI Web Automation & Custom Scrapers",
            "cat": "AI & Automation",
            "img": "image/2.png",
            "badge": "TRENDING",
            "duration": "14 Hours",
            "rating": "4.8",
            "reviews": "520",
            "price": "₹1,299",
            "origPrice": "₹3,999"
        },
        {
            "title": "Cloud DevOps & Architecture Blueprint",
            "cat": "Cloud & Infra",
            "img": "image/6.png",
            "badge": "CAREER GROWTH",
            "duration": "10 Hours",
            "rating": "4.9",
            "reviews": "390",
            "price": "₹899",
            "origPrice": "₹2,999"
        },
        {
            "title": "High-Converting Sales Funnels Engineering",
            "cat": "Funnel & CRO",
            "img": "image/4.png",
            "badge": "HOT SELLER",
            "duration": "16 Hours",
            "rating": "4.9",
            "reviews": "610",
            "price": "₹1,999",
            "origPrice": "₹5,999"
        }
    ]

    is_dark = "dark" in theme_key
    
    if "blue" in theme_key:
        card_cls = "course-card white-card rounded-2xl p-2 sm:p-3.5 text-left space-y-2 shadow-xs flex flex-col justify-between border border-slate-200"
        title_cls = "text-xs sm:text-sm font-extrabold text-slate-900 tracking-tight line-clamp-2"
        cat_cls = "text-[8px] sm:text-[9px] uppercase font-bold text-indigo-600 font-mono"
        price_cls = "text-xs sm:text-base font-black text-indigo-600 font-sans"
        orig_cls = "text-[9px] sm:text-xs text-slate-400 line-through ml-1 font-sans"
        btn_cls = "w-full py-1.5 px-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-black text-[10px] uppercase tracking-tight flex items-center justify-center space-x-1 shadow-xs"
        badge_bg = "bg-indigo-600 text-white"
        img_border = "border border-slate-200"
    elif "purple" in theme_key:
        card_cls = "course-card white-purple-card rounded-2xl p-2 sm:p-3.5 text-left space-y-2 shadow-xs flex flex-col justify-between border border-purple-200"
        title_cls = "text-xs sm:text-sm font-extrabold text-slate-900 tracking-tight line-clamp-2"
        cat_cls = "text-[8px] sm:text-[9px] uppercase font-bold text-purple-600 font-mono"
        price_cls = "text-xs sm:text-base font-black text-purple-600 font-sans"
        orig_cls = "text-[9px] sm:text-xs text-slate-400 line-through ml-1 font-sans"
        btn_cls = "w-full py-1.5 px-2 rounded-xl bg-purple-600 hover:bg-purple-700 text-white font-black text-[10px] uppercase tracking-tight flex items-center justify-center space-x-1 shadow-xs"
        badge_bg = "bg-purple-600 text-white"
        img_border = "border border-purple-200"
    elif "green" in theme_key and not is_dark:
        card_cls = "course-card white-green-card rounded-2xl p-2 sm:p-3.5 text-left space-y-2 shadow-xs flex flex-col justify-between border border-emerald-200"
        title_cls = "text-xs sm:text-sm font-extrabold text-slate-900 tracking-tight line-clamp-2"
        cat_cls = "text-[8px] sm:text-[9px] uppercase font-bold text-emerald-600 font-mono"
        price_cls = "text-xs sm:text-base font-black text-emerald-600 font-sans"
        orig_cls = "text-[9px] sm:text-xs text-slate-400 line-through ml-1 font-sans"
        btn_cls = "w-full py-1.5 px-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-black text-[10px] uppercase tracking-tight flex items-center justify-center space-x-1 shadow-xs"
        badge_bg = "bg-emerald-600 text-white"
        img_border = "border border-emerald-200"
    elif "green" in theme_key and is_dark:
        card_cls = "course-card bg-zinc-950/90 border border-emerald-950/80 rounded-2xl p-2 sm:p-3.5 text-left space-y-2 shadow-lg flex flex-col justify-between"
        title_cls = "text-xs sm:text-sm font-extrabold text-slate-100 tracking-tight line-clamp-2"
        cat_cls = "text-[8px] sm:text-[9px] uppercase font-bold text-emerald-400 font-mono"
        price_cls = "text-xs sm:text-base font-black text-emerald-400 font-sans"
        orig_cls = "text-[9px] sm:text-xs text-slate-500 line-through ml-1 font-sans"
        btn_cls = "w-full py-1.5 px-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-black text-[10px] uppercase tracking-tight flex items-center justify-center space-x-1 shadow-xs"
        badge_bg = "bg-emerald-600 text-white"
        img_border = "border border-emerald-950/80"
    elif is_dark:
        card_cls = "course-card bg-zinc-950/90 border border-zinc-800/90 rounded-2xl p-2 sm:p-3.5 text-left space-y-2 shadow-lg flex flex-col justify-between"
        title_cls = "text-xs sm:text-sm font-extrabold text-slate-100 tracking-tight line-clamp-2"
        cat_cls = "text-[8px] sm:text-[9px] uppercase font-bold text-amber-400 font-mono"
        price_cls = "text-xs sm:text-base font-black text-amber-400 font-sans"
        orig_cls = "text-[9px] sm:text-xs text-slate-500 line-through ml-1 font-sans"
        btn_cls = "w-full py-1.5 px-2 rounded-xl bg-gradient-to-r from-amber-500 via-amber-400 to-yellow-500 text-slate-950 font-black text-[10px] uppercase tracking-tight flex items-center justify-center space-x-1 shadow-xs"
        badge_bg = "bg-amber-500 text-slate-950"
        img_border = "border border-zinc-800/80"
    else: # white gold
        card_cls = "course-card white-gold-card rounded-2xl p-2 sm:p-3.5 text-left space-y-2 shadow-xs flex flex-col justify-between border border-amber-200/80"
        title_cls = "text-xs sm:text-sm font-extrabold text-slate-900 tracking-tight line-clamp-2"
        cat_cls = "text-[8px] sm:text-[9px] uppercase font-bold text-amber-700 font-mono"
        price_cls = "text-xs sm:text-base font-black text-amber-600 font-sans"
        orig_cls = "text-[9px] sm:text-xs text-slate-400 line-through ml-1 font-sans"
        btn_cls = "w-full py-1.5 px-2 rounded-xl bg-gradient-to-r from-amber-500 via-amber-400 to-yellow-500 text-slate-950 font-black text-[10px] uppercase tracking-tight flex items-center justify-center space-x-1 shadow-xs"
        badge_bg = "bg-amber-500 text-slate-950"
        img_border = "border border-amber-200/80"

    cards_html = []
    for c in courses:
        card = f"""
          <div class="{card_cls}">
            <div class="space-y-2">
              <div class="relative w-full aspect-square rounded-xl overflow-hidden bg-slate-900 {img_border}">
                <img src="{c["img"]}" alt="{c["title"]}" class="w-full h-full object-cover" />
                <div class="absolute top-1.5 left-1.5 flex items-center gap-1 z-10">
                  <span class="text-[7.5px] sm:text-[9px] uppercase font-black {badge_bg} px-1.5 py-0.5 rounded shadow-xs">{c["badge"]}</span>
                </div>
                <div class="absolute bottom-1.5 right-1.5 z-10">
                  <span class="text-[8px] sm:text-[9px] font-mono font-bold text-white bg-slate-950/80 px-1.5 py-0.5 rounded border border-white/20">{c["duration"]}</span>
                </div>
              </div>
              <div>
                <span class="{cat_cls}">{c["cat"]}</span>
                <h4 class="{title_cls}">{c["title"]}</h4>
              </div>
              <div class="flex items-center space-x-1 text-amber-500 text-[8px] sm:text-[10px]">
                <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                <span class="font-mono font-bold">{c["rating"]}</span>
                <span class="text-slate-400 font-mono">({c["reviews"]})</span>
              </div>
            </div>
            <div class="space-y-2 pt-1 border-t border-slate-100/10">
              <div class="flex items-baseline justify-between">
                <div>
                  <span class="{price_cls}">{c["price"]}</span>
                  <span class="{orig_cls}">{c["origPrice"]}</span>
                </div>
              </div>
              <button class="{btn_cls}">
                <i class="fa-solid fa-bolt text-[9px]"></i>
                <span>ENROLL</span>
              </button>
            </div>
          </div>
        """
        cards_html.append(card)
    return "\n".join(cards_html)

CURATED_CUTOFFS = {
    "portfolio-dark-gold": {
        "cut_line": 582,
        "closer": "</div></body></html>"
    },
    "funnel-dark-gold": {
        "cut_line": 480,
        "closer": "</div></section></main></body></html>"
    },
    "realstate-dark-gold": {
        "cut_line": 386,
        "closer": "</body></html>"
    },
    "single-product-white-gold": {
        "cut_line": 464,
        "closer": "</main></body></html>"
    },
    "funnel-white-gold": {
        "cut_line": 455,
        "closer": "</div></section></main></body></html>"
    },
    "ecommerce-dark-gold": {
        "cut_line": 490,
        "closer": "</div></section></main></body></html>"
    }
}

def generate_preview(theme_key):
    src_file = os.path.join(CLEAN_DIR, theme_key, "index.html")
    if not os.path.exists(src_file):
        src_file = os.path.join(theme_key, "index.html")
    if not os.path.exists(src_file):
        print(f"Error: {src_file} does not exist!")
        return

    with open(src_file, "r", encoding="utf-8") as f:
        content = f.read()

    if theme_key in CURATED_CUTOFFS:
        lines = content.splitlines(True)
        cfg = CURATED_CUTOFFS[theme_key]
        cut_content = "".join(lines[:cfg["cut_line"]]) + cfg["closer"]
        soup = BeautifulSoup(cut_content, "html.parser")
        clean_preview_html = str(soup)
    else:
        soup = BeautifulSoup(content, "html.parser")
        
        # If this is a course template, populate #courseGrid with rich static cards
        if "course-" in theme_key:
            course_grid = soup.find(id="courseGrid")
            if course_grid:
                course_cards_html = build_course_cards(theme_key)
                cards_soup = BeautifulSoup(course_cards_html, "html.parser")
                course_grid.append(cards_soup)

        sections = soup.find_all("section")
        if len(sections) > 2:
            for s in sections[2:]:
                s.decompose()
        for f in soup.find_all(["footer"]):
            f.decompose()
        for mod in soup.find_all("div", id=lambda x: x and ("modal" in x.lower() or "auth" in x.lower() or "checkout" in x.lower())):
            mod.decompose()
        clean_preview_html = str(soup)

    # Special check for course-white-gold (curated cut)
    if theme_key == "course-white-gold":
        soup = BeautifulSoup(content, "html.parser")
        course_grid = soup.find(id="courseGrid")
        if course_grid:
            course_cards_html = build_course_cards(theme_key)
            cards_soup = BeautifulSoup(course_cards_html, "html.parser")
            course_grid.append(cards_soup)
        sections = soup.find_all("section")
        if len(sections) > 2:
            for s in sections[2:]:
                s.decompose()
        for f in soup.find_all(["footer"]):
            f.decompose()
        clean_preview_html = str(soup)

    # Encrypt preview HTML using exact commercial encryption
    chunks = encrypt_payload(clean_preview_html)
    encrypted_preview_html = build_protected_html(chunks)

    dest_file = os.path.join(theme_key, "preview.html")
    with open(dest_file, "w", encoding="utf-8") as f:
        f.write(encrypted_preview_html)

    orig_size = os.path.getsize(src_file)
    prev_size = len(clean_preview_html)
    enc_size = len(encrypted_preview_html)
    print(f"[{theme_key}] Generated encrypted preview: clean {orig_size}B -> cut {prev_size}B -> enc {enc_size}B")

def main():
    themes = [d for d in os.listdir(CLEAN_DIR) if os.path.isdir(os.path.join(CLEAN_DIR, d))]
    print(f"Building fast hero preview for ALL {len(themes)} themes...")
    for key in sorted(themes):
        generate_preview(key)

if __name__ == "__main__":
    main()
