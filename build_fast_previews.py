import os
import base64
from bs4 import BeautifulSoup
from re_encrypt import encrypt_payload, build_protected_html

CLEAN_DIR = ".clean_templates_source"

# 4 Courses static HTML for course-white-gold preview (fills 2 full rows without empty bottom space)
COURSE_STATIC_HTML = '''
          <!-- Course 1: Full-Stack Next.js 15 -->
          <div class="course-card white-gold-card rounded-2xl p-2 sm:p-3.5 text-left space-y-2 shadow-xs flex flex-col justify-between transition-all duration-300 group">
            <div class="space-y-2">
              <div class="relative w-full aspect-square rounded-xl overflow-hidden bg-slate-100 border border-amber-200/80">
                <img src="image/1.png" alt="Full-Stack Next.js 15" class="w-full h-full object-cover" />
                <div class="absolute top-1.5 left-1.5 flex items-center gap-1 z-10">
                  <span class="text-[7.5px] sm:text-[9px] uppercase font-black bg-amber-500 text-slate-950 px-1.5 py-0.5 rounded shadow-xs">BEST SELLER</span>
                </div>
                <div class="absolute bottom-1.5 right-1.5 z-10">
                  <span class="text-[8px] sm:text-[9px] font-mono font-bold text-slate-950 bg-amber-400/90 px-1.5 py-0.5 rounded border border-amber-500/50">18.5 Hours</span>
                </div>
              </div>
              <div>
                <span class="text-[8px] sm:text-[9px] uppercase font-bold text-amber-700">Full-Stack Dev</span>
                <h4 class="text-xs sm:text-sm font-extrabold text-slate-900 tracking-tight line-clamp-2">Full-Stack Next.js 15 &amp; Supabase Masterclass</h4>
              </div>
              <div class="flex items-center space-x-1 text-amber-500 text-[8px] sm:text-[10px]">
                <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                <span class="text-slate-500 font-mono font-bold">4.9</span>
                <span class="text-slate-400 font-mono">(480)</span>
              </div>
            </div>
            <div class="space-y-2 pt-1 border-t border-slate-100">
              <div class="flex items-baseline justify-between">
                <div>
                  <span class="text-xs sm:text-base font-black text-amber-600 font-sans">₹1,499</span>
                  <span class="text-[9px] sm:text-xs text-slate-400 line-through ml-1 font-sans">₹4,999</span>
                </div>
              </div>
              <button class="w-full py-1.5 px-2 rounded-xl bg-gradient-to-r from-amber-500 via-amber-400 to-yellow-500 text-slate-950 font-black text-[10px] uppercase tracking-tight flex items-center justify-center space-x-1 shadow-xs">
                <i class="fa-solid fa-bolt text-[9px]"></i>
                <span>ENROLL</span>
              </button>
            </div>
          </div>

          <!-- Course 2: AI Web Automation -->
          <div class="course-card white-gold-card rounded-2xl p-2 sm:p-3.5 text-left space-y-2 shadow-xs flex flex-col justify-between transition-all duration-300 group">
            <div class="space-y-2">
              <div class="relative w-full aspect-square rounded-xl overflow-hidden bg-slate-100 border border-amber-200/80">
                <img src="image/2.png" alt="AI Automation Masterclass" class="w-full h-full object-cover" />
                <div class="absolute top-1.5 left-1.5 flex items-center gap-1 z-10">
                  <span class="text-[7.5px] sm:text-[9px] uppercase font-black bg-emerald-600 text-white px-1.5 py-0.5 rounded shadow-xs">TRENDING</span>
                </div>
                <div class="absolute bottom-1.5 right-1.5 z-10">
                  <span class="text-[8px] sm:text-[9px] font-mono font-bold text-slate-950 bg-amber-400/90 px-1.5 py-0.5 rounded border border-amber-500/50">14 Hours</span>
                </div>
              </div>
              <div>
                <span class="text-[8px] sm:text-[9px] uppercase font-bold text-amber-700">AI &amp; Automation</span>
                <h4 class="text-xs sm:text-sm font-extrabold text-slate-900 tracking-tight line-clamp-2">AI Web Automation &amp; Custom Scrapers Mastery</h4>
              </div>
              <div class="flex items-center space-x-1 text-amber-500 text-[8px] sm:text-[10px]">
                <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star-half-stroke"></i>
                <span class="text-slate-500 font-mono font-bold">4.8</span>
                <span class="text-slate-400 font-mono">(520)</span>
              </div>
            </div>
            <div class="space-y-2 pt-1 border-t border-slate-100">
              <div class="flex items-baseline justify-between">
                <div>
                  <span class="text-xs sm:text-base font-black text-amber-600 font-sans">₹1,299</span>
                  <span class="text-[9px] sm:text-xs text-slate-400 line-through ml-1 font-sans">₹3,999</span>
                </div>
              </div>
              <button class="w-full py-1.5 px-2 rounded-xl bg-gradient-to-r from-amber-500 via-amber-400 to-yellow-500 text-slate-950 font-black text-[10px] uppercase tracking-tight flex items-center justify-center space-x-1 shadow-xs">
                <i class="fa-solid fa-bolt text-[9px]"></i>
                <span>ENROLL</span>
              </button>
            </div>
          </div>

          <!-- Course 3: Freelancing & International Agency Blueprint -->
          <div class="course-card white-gold-card rounded-2xl p-2 sm:p-3.5 text-left space-y-2 shadow-xs flex flex-col justify-between transition-all duration-300 group">
            <div class="space-y-2">
              <div class="relative w-full aspect-square rounded-xl overflow-hidden bg-slate-100 border border-amber-200/80">
                <img src="image/6.png" alt="Freelancing &amp; Agency Blueprint" class="w-full h-full object-cover" />
                <div class="absolute top-1.5 left-1.5 flex items-center gap-1 z-10">
                  <span class="text-[7.5px] sm:text-[9px] uppercase font-black bg-sky-600 text-white px-1.5 py-0.5 rounded shadow-xs">CAREER GROWTH</span>
                </div>
                <div class="absolute bottom-1.5 right-1.5 z-10">
                  <span class="text-[8px] sm:text-[9px] font-mono font-bold text-slate-950 bg-amber-400/90 px-1.5 py-0.5 rounded border border-amber-500/50">10 Hours</span>
                </div>
              </div>
              <div>
                <span class="text-[8px] sm:text-[9px] uppercase font-bold text-amber-700">Agency Scaling</span>
                <h4 class="text-xs sm:text-sm font-extrabold text-slate-900 tracking-tight line-clamp-2">Freelancing &amp; International Agency Blueprint</h4>
              </div>
              <div class="flex items-center space-x-1 text-amber-500 text-[8px] sm:text-[10px]">
                <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                <span class="text-slate-500 font-mono font-bold">4.9</span>
                <span class="text-slate-400 font-mono">(390)</span>
              </div>
            </div>
            <div class="space-y-2 pt-1 border-t border-slate-100">
              <div class="flex items-baseline justify-between">
                <div>
                  <span class="text-xs sm:text-base font-black text-amber-600 font-sans">₹899</span>
                  <span class="text-[9px] sm:text-xs text-slate-400 line-through ml-1 font-sans">₹2,999</span>
                </div>
              </div>
              <button class="w-full py-1.5 px-2 rounded-xl bg-gradient-to-r from-amber-500 via-amber-400 to-yellow-500 text-slate-950 font-black text-[10px] uppercase tracking-tight flex items-center justify-center space-x-1 shadow-xs">
                <i class="fa-solid fa-bolt text-[9px]"></i>
                <span>ENROLL</span>
              </button>
            </div>
          </div>

          <!-- Course 4: High-Converting Sales Funnels & Ads Engineering -->
          <div class="course-card white-gold-card rounded-2xl p-2 sm:p-3.5 text-left space-y-2 shadow-xs flex flex-col justify-between transition-all duration-300 group">
            <div class="space-y-2">
              <div class="relative w-full aspect-square rounded-xl overflow-hidden bg-slate-100 border border-amber-200/80">
                <img src="image/4.png" alt="Sales Funnels &amp; Ads Engineering" class="w-full h-full object-cover" />
                <div class="absolute top-1.5 left-1.5 flex items-center gap-1 z-10">
                  <span class="text-[7.5px] sm:text-[9px] uppercase font-black bg-rose-600 text-white px-1.5 py-0.5 rounded shadow-xs">HOT SELLER</span>
                </div>
                <div class="absolute bottom-1.5 right-1.5 z-10">
                  <span class="text-[8px] sm:text-[9px] font-mono font-bold text-slate-950 bg-amber-400/90 px-1.5 py-0.5 rounded border border-amber-500/50">16 Hours</span>
                </div>
              </div>
              <div>
                <span class="text-[8px] sm:text-[9px] uppercase font-bold text-amber-700">Funnel &amp; CRO</span>
                <h4 class="text-xs sm:text-sm font-extrabold text-slate-900 tracking-tight line-clamp-2">High-Converting Sales Funnels &amp; Ads Engineering</h4>
              </div>
              <div class="flex items-center space-x-1 text-amber-500 text-[8px] sm:text-[10px]">
                <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                <span class="text-slate-500 font-mono font-bold">4.9</span>
                <span class="text-slate-400 font-mono">(610)</span>
              </div>
            </div>
            <div class="space-y-2 pt-1 border-t border-slate-100">
              <div class="flex items-baseline justify-between">
                <div>
                  <span class="text-xs sm:text-base font-black text-amber-600 font-sans">₹1,999</span>
                  <span class="text-[9px] sm:text-xs text-slate-400 line-through ml-1 font-sans">₹5,999</span>
                </div>
              </div>
              <button class="w-full py-1.5 px-2 rounded-xl bg-gradient-to-r from-amber-500 via-amber-400 to-yellow-500 text-slate-950 font-black text-[10px] uppercase tracking-tight flex items-center justify-center space-x-1 shadow-xs">
                <i class="fa-solid fa-bolt text-[9px]"></i>
                <span>ENROLL</span>
              </button>
            </div>
          </div>
'''

CUTOFF_CONFIG = {
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
    },
    "course-white-gold": {
        "cut_line": 426,
        "closer": COURSE_STATIC_HTML + "</div></section></main></body></html>"
    }
}

def generate_preview(theme_key):
    src_file = os.path.join(CLEAN_DIR, theme_key, "index.html")
    if not os.path.exists(src_file):
        print(f"Error: {src_file} does not exist!")
        return

    with open(src_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cfg = CUTOFF_CONFIG[theme_key]
    cut_content = "".join(lines[:cfg["cut_line"]]) + cfg["closer"]

    # Balance any tags using BeautifulSoup
    soup = BeautifulSoup(cut_content, "html.parser")
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
    print(f"[{theme_key}] Generated encrypted preview: clean {orig_size}B -> cut {prev_size}B -> enc {enc_size}B ({(1 - enc_size/orig_size)*100:.1f}% reduction)")

def main():
    for key in CUTOFF_CONFIG.keys():
        generate_preview(key)

if __name__ == "__main__":
    main()
