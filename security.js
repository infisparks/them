(function() {
  'use strict';

  // If running inside the showcase preview iframe, do not attach security listeners
  if (window.top !== window.self) {
    return;
  }

  // 1. Disable Right-Click Context Menu
  document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    return false;
  }, true);

  // 2. Disable Keyboard Shortcuts (Inspect, View Source, Save, Print)
  document.addEventListener('keydown', function(e) {
    // F12 key
    if (e.key === 'F12' || e.keyCode === 123) {
      e.preventDefault();
      return false;
    }
    var isCmdOrCtrl = e.ctrlKey || e.metaKey;
    if (isCmdOrCtrl) {
      // Ctrl+Shift+I / J / C (DevTools & Console)
      if (e.shiftKey && (e.key === 'I' || e.key === 'i' || e.key === 'J' || e.key === 'j' || e.key === 'C' || e.key === 'c')) {
        e.preventDefault();
        return false;
      }
      // Ctrl+U (View Source)
      if (e.key === 'U' || e.key === 'u') {
        e.preventDefault();
        return false;
      }
      // Ctrl+S (Save Webpage)
      if (e.key === 'S' || e.key === 's') {
        e.preventDefault();
        return false;
      }
      // Ctrl+P (Print)
      if (e.key === 'P' || e.key === 'p') {
        e.preventDefault();
        return false;
      }
    }
  }, true);

  // 3. Disable Dragging of Images / Elements
  document.addEventListener('dragstart', function(e) {
    e.preventDefault();
    return false;
  }, true);

  // 4. Console Protection Warning
  if (window.console) {
    setInterval(function() {
      console.clear();
      console.log("%c🔒 SECURITY PROTECTED", "color:#eab308;font-size:24px;font-weight:900;background:#090d16;padding:8px 16px;border-radius:8px;");
      console.log("%cUnauthorized downloading, code scraping, or reverse engineering is strictly prohibited.", "color:#94a3b8;font-size:13px;font-weight:bold;");
    }, 2500);
  }
})();
