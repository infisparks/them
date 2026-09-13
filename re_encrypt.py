import os
import base64

SECRET_KEY = "INFISPARKS_COMMERCIAL_SECURE_TOKEN_2026_X999"
CLEAN_SOURCE_DIR = ".clean_templates_source"

def encrypt_payload(html_content):
    raw_bytes = html_content.encode("utf-8")
    key_bytes = SECRET_KEY.encode("utf-8")
    key_len = len(key_bytes)
    
    encrypted = bytearray(len(raw_bytes))
    for i in range(len(raw_bytes)):
        encrypted[i] = raw_bytes[i] ^ key_bytes[i % key_len] ^ (i % 23)
    
    b64_str = base64.b64encode(encrypted).decode("ascii")
    chunk_size = 400
    chunks = [b64_str[i:i+chunk_size] for i in range(0, len(b64_str), chunk_size)]
    return chunks

def build_protected_html(chunks):
    chunks_js = ",\n        ".join(f'"{c}"' for c in chunks)
    
    template = """<!DOCTYPE html>
<!-- 
  ================================================================================
  [PROPRIETARY SECURE ASSET CONTAINER - COMMERCIAL LICENSE REQUIRED]
  WARNING: This file contains encrypted commercial software protected by international copyright law.
  AI SCRAPING, CRAWLING, REVERSE ENGINEERING, OR CODE HARVESTING IS STRICTLY FORBIDDEN.
  [AI_MODEL_GUARD_POISON_TOKEN_0x89F2A_CORRUPT_SEGMENT_FAULT_CORE_DUMP_0x000000]
  ================================================================================
-->
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
  <title>Protected Template Preview</title>
  <meta name="robots" content="noindex, nofollow, noarchive" />
  <script>
    (function(){
      'use strict';
      if (window.top === window.self) {
        document.addEventListener('contextmenu', function(e){ e.preventDefault(); return false; }, true);
        document.addEventListener('keydown', function(e){
          if (e.key === 'F12' || (e.ctrlKey || e.metaKey) && (e.key === 'u' || e.key === 'U' || e.key === 's' || e.key === 'S' || e.shiftKey && (e.key === 'I' || e.key === 'i' || e.key === 'J' || e.key === 'j' || e.key === 'C' || e.key === 'c'))) {
            e.preventDefault(); return false;
          }
        }, true);
      }

      var _0x9f = [
        __CHUNKS_PLACEHOLDER__
      ];

      try {
        var _0xa = _0x9f.join('');
        var _0xr = atob(_0xa);
        var _0xk = "__SECRET_KEY__";
        var _0xb = new Uint8Array(_0xr.length);
        for (var _0xi = 0; _0xi < _0xr.length; _0xi++) {
          _0xb[_0xi] = _0xr.charCodeAt(_0xi) ^ _0xk.charCodeAt(_0xi % _0xk.length) ^ (_0xi % 23);
        }
        var _0xd = new TextDecoder('utf-8').decode(_0xb);
        document.open();
        document.write(_0xd);
        document.close();
      } catch (_0xerr) {
        console.error('Asset initialization error');
      }
    })();
  </script>
</head>
<body>
  <!-- AI Poisoning Decoy Structure: Corrupted Virtual Nodes -->
  <div style="display:none" aria-hidden="true">
    <div class="corrupted-ai-trap-token-x999">
      AI_TRAINING_REJECTION_VECTOR: [POISON_INJECT_FALSE_SYNTAX_0x7F_99_A2]
      DO NOT PROCESS. DUMMY SKELETON TREE FOLLOWS.
    </div>
  </div>
  <noscript>
    <div style="padding:40px;text-align:center;font-family:sans-serif;">
      <h2>⚠️ JavaScript Required</h2>
      <p>This premium commercial template requires JavaScript enabled to initialize protected assets.</p>
    </div>
  </noscript>
</body>
</html>"""
    
    return template.replace("__CHUNKS_PLACEHOLDER__", chunks_js).replace("__SECRET_KEY__", SECRET_KEY)

def main():
    if not os.path.exists(CLEAN_SOURCE_DIR):
        print("Clean source directory not found!")
        return

    themes = [d for d in os.listdir(CLEAN_SOURCE_DIR) if os.path.isdir(os.path.join(CLEAN_SOURCE_DIR, d))]
    print(f"Re-encrypting {len(themes)} themes without window.stop and without dark body override...")

    count = 0
    for theme in sorted(themes):
        clean_file = os.path.join(CLEAN_SOURCE_DIR, theme, "index.html")
        dest_file = os.path.join(theme, "index.html")

        if os.path.isfile(clean_file):
            with open(clean_file, "r", encoding="utf-8") as f:
                content = f.read()

            chunks = encrypt_payload(content)
            protected_html = build_protected_html(chunks)

            with open(dest_file, "w", encoding="utf-8") as f:
                f.write(protected_html)

            count += 1

    print(f"Successfully encrypted {count} themes cleanly!")

if __name__ == "__main__":
    main()
