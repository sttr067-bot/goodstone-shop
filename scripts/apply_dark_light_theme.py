import re

with open("/working_dir/slingshot-shop/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update <style> block to define theme variables and classes
theme_styles = """    <style>
        body { font-family: "Prompt", sans-serif; transition: background-color 0.25s ease, color 0.25s ease; }
        
        /* Dark Theme (Default) */
        :root, [data-theme="dark"] {
            --bg-body: #121215;
            --bg-header: #1A1A20;
            --bg-card: #1F1F26;
            --bg-card-subtle: #272732;
            --bg-input: #181820;
            --border-main: #333342;
            --border-subtle: #2A2A38;
            --text-main: #F4F0EA;
            --text-muted: #A1A1B0;
            --text-sub: #787888;
            --badge-bg: #2E1B17;
            --badge-border: #5C2B1F;
            --badge-text: #FF6E4E;
            --hero-from: #261B18;
            --hero-via: #211C20;
            --hero-to: #1A1A22;
            --tab-inactive-bg: #272732;
            --tab-inactive-text: #B4B4C2;
            --shopee-btn-bg: #EE4D2D;
            --shopee-btn-hover: #D73211;
        }

        /* Light Theme (Warm Cream) */
        [data-theme="light"] {
            --bg-body: #F9F6F0;
            --bg-header: #FFFFFF;
            --bg-card: #FFFFFF;
            --bg-card-subtle: #FAF7F2;
            --bg-input: #FAF7F2;
            --border-main: #EBE3D5;
            --border-subtle: #F0EAE1;
            --text-main: #2C241E;
            --text-muted: #64748B;
            --text-sub: #94A3B8;
            --badge-bg: #FFF2EE;
            --badge-border: #FFD5CC;
            --badge-text: #EE4D2D;
            --hero-from: #FFF6F2;
            --hero-via: #FDF3EA;
            --hero-to: #FBF0E4;
            --tab-inactive-bg: #FAF7F2;
            --tab-inactive-text: #64748B;
            --shopee-btn-bg: #EE4D2D;
            --shopee-btn-hover: #D73211;
        }

        /* Dynamic Theme Classes */
        .theme-body { background-color: var(--bg-body) !important; color: var(--text-main) !important; }
        .theme-header { background-color: var(--bg-header) !important; border-color: var(--border-main) !important; }
        .theme-card { background-color: var(--bg-card) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .theme-card-subtle { background-color: var(--bg-card-subtle) !important; border-color: var(--border-subtle) !important; }
        .theme-input { background-color: var(--bg-input) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .theme-text-main { color: var(--text-main) !important; }
        .theme-text-muted { color: var(--text-muted) !important; }
        .theme-badge { background-color: var(--badge-bg) !important; border-color: var(--badge-border) !important; color: var(--badge-text) !important; }
        .theme-hero { background: linear-gradient(135deg, var(--hero-from), var(--hero-via), var(--hero-to)) !important; border-color: var(--border-main) !important; }
        .theme-border { border-color: var(--border-main) !important; }
    </style>"""

# Replace <style> block
style_pattern = r"<style>[\s\S]*?<\/style>"
html = re.sub(style_pattern, theme_styles, html)

# 2. Update <body> tag to include theme-body class and data-theme="dark" by default
html = html.replace(
    '<body class="bg-[#F9F6F0] text-[#2C241E] min-h-screen flex flex-col font-sans">',
    '<body class="theme-body min-h-screen flex flex-col font-sans" data-theme="dark">'
)

# 3. Update Header to include Theme Toggle button
old_header_start = '<header class="sticky top-0 z-40 bg-white border-b-2 border-[#EBE3D5] shadow-sm">'
new_header_start = '<header class="sticky top-0 z-40 theme-header border-b-2 shadow-sm">'

if old_header_start in html:
    html = html.replace(old_header_start, new_header_start)

old_header_right = """                <!-- Customer Wallet Badge -->
                <div id="header-wallet-badge" class="hidden sm:flex items-center gap-2 bg-[#FFF5F2] border border-[#FFD5CC] px-3 py-1.5 rounded-xl text-xs font-bold">
                    <span class="text-slate-600">👛 กระเป๋าเครดิต:</span>
                    <span id="user-wallet-display" class="font-black text-[#EE4D2D]">฿0.00</span>
                </div>
            </div>
        </div>
    </header>"""

new_header_right = """                <!-- Header Right: Theme Toggle & Wallet Badge -->
                <div class="flex items-center gap-2">
                    <!-- Light / Dark Mode Toggle Button (Default: Dark Mode) -->
                    <button type="button" onclick="toggleTheme()" id="theme-toggle-btn" class="flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-xl border border-[#333342] bg-[#272732] text-[#F4F0EA] hover:border-[#FF6E4E] text-xs font-bold transition-all shadow-sm active:scale-95" title="สลับโหมดมืด / สว่าง">
                        <span id="theme-toggle-icon">🌙</span>
                        <span id="theme-toggle-text" class="hidden sm:inline">โหมดมืด</span>
                    </button>

                    <!-- Customer Wallet Badge -->
                    <div id="header-wallet-badge" class="hidden sm:flex items-center gap-2 theme-badge px-3 py-1.5 rounded-xl text-xs font-bold border">
                        <span class="theme-text-muted">👛 กระเป๋า:</span>
                        <span id="user-wallet-display" class="font-black text-[#EE4D2D]">฿0.00</span>
                    </div>
                </div>
            </div>
        </div>
    </header>"""

if old_header_right in html:
    html = html.replace(old_header_right, new_header_right)
    print("Added theme toggle to Header!")

# 4. Update Hero Banner to theme-hero
html = html.replace(
    'class="rounded-3xl bg-gradient-to-r from-[#FFF6F2] via-[#FDF3EA] to-[#FBF0E4] p-6 sm:p-10 border-2 border-[#EBE3D5] shadow-sm space-y-3"',
    'class="rounded-3xl theme-hero p-6 sm:p-10 border-2 shadow-sm space-y-3"'
)

# 5. Update Search & Filter Bar
html = html.replace(
    'class="bg-white p-3.5 sm:p-4 rounded-3xl border-2 border-[#EBE3D5] shadow-sm space-y-3"',
    'class="theme-card p-3.5 sm:p-4 rounded-3xl border-2 shadow-sm space-y-3"'
)
html = html.replace(
    'class="w-full bg-[#FAF7F2] border border-[#EBE3D5] rounded-2xl pl-10 pr-4 py-2.5 text-xs sm:text-sm text-[#2C241E] focus:outline-none focus:ring-2 focus:ring-[#EE4D2D] focus:bg-white transition-all font-medium"',
    'class="w-full theme-input border rounded-2xl pl-10 pr-4 py-2.5 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-[#EE4D2D] transition-all font-medium"'
)

# 6. Update Direct Checkout View containers
html = html.replace(
    'class="grid grid-cols-1 md:grid-cols-12 gap-6 bg-white border-2 border-[#EBE3D5] rounded-3xl p-4 sm:p-8 shadow-sm"',
    'class="grid grid-cols-1 md:grid-cols-12 gap-6 theme-card border-2 rounded-3xl p-4 sm:p-8 shadow-sm"'
)
html = html.replace(
    'class="bg-white border-2 border-[#EBE3D5] rounded-3xl p-4 sm:p-8 space-y-6 shadow-sm"',
    'class="theme-card border-2 rounded-3xl p-4 sm:p-8 space-y-6 shadow-sm"'
)

# 7. Add Theme Controller JS
theme_js = """
        // ================= LIGHT / DARK MODE CONTROLLER (LOCKED DEFAULT TO DARK) =================
        let currentTheme = localStorage.getItem("goodstone_theme") || "dark";

        function applyTheme(theme) {
            currentTheme = theme;
            document.documentElement.setAttribute("data-theme", theme);
            document.body.setAttribute("data-theme", theme);
            localStorage.setItem("goodstone_theme", theme);

            const btn = document.getElementById("theme-toggle-btn");
            const icon = document.getElementById("theme-toggle-icon");
            const text = document.getElementById("theme-toggle-text");

            if (theme === "dark") {
                if (icon) icon.innerText = "🌙";
                if (text) text.innerText = "โหมดมืด";
                if (btn) {
                    btn.className = "flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-xl border border-[#333342] bg-[#272732] text-[#F4F0EA] hover:border-[#FF6E4E] text-xs font-bold transition-all shadow-sm active:scale-95";
                }
            } else {
                if (icon) icon.innerText = "☀️";
                if (text) text.innerText = "โหมดสว่าง";
                if (btn) {
                    btn.className = "flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-xl border border-[#EBE3D5] bg-[#FAF7F2] text-[#2C241E] hover:border-[#EE4D2D] text-xs font-bold transition-all shadow-sm active:scale-95";
                }
            }

            // Re-render views if initialized
            if (typeof renderCatalogGrid === "function") {
                renderCatalogGrid();
            }
        }

        function toggleTheme() {
            const next = currentTheme === "dark" ? "light" : "dark";
            applyTheme(next);
        }
"""

# Insert Theme Controller into JS
if "window.onload = init;" in html:
    html = html.replace("window.onload = init;", theme_js + "\n        window.onload = init;")

# Update init() in JS to call applyTheme(currentTheme)
if "function init() {" in html:
    html = html.replace("function init() {", "function init() {\n            applyTheme(currentTheme);")

# Update renderCatalogGrid product cards styling for dark/light
old_card_render = """                card.className = "bg-white rounded-3xl border-2 border-[#EBE3D5] overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group";"""
new_card_render = """                card.className = "theme-card rounded-3xl border-2 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group";"""

if old_card_render in html:
    html = html.replace(old_card_render, new_card_render)

old_img_box = """                    <div class="relative w-full h-56 bg-[#FAF7F2] p-4 flex items-center justify-center overflow-hidden cursor-pointer" onclick="openDirectCheckout('${p.id}')">"""
new_img_box = """                    <div class="relative w-full h-56 theme-card-subtle p-4 flex items-center justify-center overflow-hidden cursor-pointer" onclick="openDirectCheckout('${p.id}')">"""

if old_img_box in html:
    html = html.replace(old_img_box, new_img_box)

with open("/working_dir/slingshot-shop/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated with Light/Dark Theme Controller (Default: Dark)!")
