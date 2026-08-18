import re

with open("/working_dir/slingshot-shop/admin.html", "r", encoding="utf-8") as f:
    adm_html = f.read()

# Add theme styles to admin.html
theme_styles_admin = """    <style>
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
            --tab-inactive-bg: #272732;
            --tab-inactive-text: #B4B4C2;
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
            --tab-inactive-bg: #F2EDE4;
            --tab-inactive-text: #2C241E;
        }

        .theme-body { background-color: var(--bg-body) !important; color: var(--text-main) !important; }
        .theme-header { background-color: var(--bg-header) !important; border-color: var(--border-main) !important; }
        .theme-card { background-color: var(--bg-card) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .theme-card-subtle { background-color: var(--bg-card-subtle) !important; border-color: var(--border-subtle) !important; }
        .theme-input { background-color: var(--bg-input) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .theme-text-main { color: var(--text-main) !important; }
        .theme-text-muted { color: var(--text-muted) !important; }
    </style>"""

adm_html = re.sub(r"<style>[\s\S]*?<\/style>", theme_styles_admin, adm_html)

# Update body tag
adm_html = adm_html.replace(
    '<body class="bg-[#F9F6F0] text-[#2C241E] min-h-screen flex flex-col font-sans">',
    '<body class="theme-body min-h-screen flex flex-col font-sans" data-theme="dark">'
)

# Add Toggle button to Header right
old_nav_action = """                <!-- Navigation Action -->
                <div class="flex items-center gap-2">
                    <a href="index.html" target="_blank" class="bg-[#FFF2EE] hover:bg-[#FFE3DC] text-[#EE4D2D] border border-[#FFD5CC] text-xs px-3 py-1.5 rounded-xl font-bold flex items-center gap-1 shadow-sm transition-all">
                        <span>หน้าร้าน ↗</span>
                    </a>
                </div>"""

new_nav_action = """                <!-- Navigation Action: Theme Toggle & Storefront Link -->
                <div class="flex items-center gap-2">
                    <button type="button" onclick="toggleTheme()" id="theme-toggle-btn" class="flex items-center gap-1 px-2.5 py-1.5 rounded-xl border border-[#333342] bg-[#272732] text-[#F4F0EA] hover:border-[#FF6E4E] text-xs font-bold transition-all shadow-sm active:scale-95" title="สลับโหมดมืด / สว่าง">
                        <span id="theme-toggle-icon">🌙</span>
                        <span id="theme-toggle-text" class="hidden sm:inline">โหมดมืด</span>
                    </button>
                    <a href="index.html" target="_blank" class="bg-[#FFF2EE] hover:bg-[#FFE3DC] text-[#EE4D2D] border border-[#FFD5CC] text-xs px-3 py-1.5 rounded-xl font-bold flex items-center gap-1 shadow-sm transition-all">
                        <span>หน้าร้าน ↗</span>
                    </a>
                </div>"""

if old_nav_action in adm_html:
    adm_html = adm_html.replace(old_nav_action, new_nav_action)

# Add JS theme controller
theme_js_adm = """
        // ================= THEME CONTROLLER (DEFAULT: DARK) =================
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
                if (btn) btn.className = "flex items-center gap-1 px-2.5 py-1.5 rounded-xl border border-[#333342] bg-[#272732] text-[#F4F0EA] hover:border-[#FF6E4E] text-xs font-bold transition-all shadow-sm active:scale-95";
            } else {
                if (icon) icon.innerText = "☀️";
                if (text) text.innerText = "โหมดสว่าง";
                if (btn) btn.className = "flex items-center gap-1 px-2.5 py-1.5 rounded-xl border border-[#EBE3D5] bg-[#FAF7F2] text-[#2C241E] hover:border-[#EE4D2D] text-xs font-bold transition-all shadow-sm active:scale-95";
            }
        }

        function toggleTheme() {
            const next = currentTheme === "dark" ? "light" : "dark";
            applyTheme(next);
        }
"""

if "window.onload = init;" in adm_html:
    adm_html = adm_html.replace("window.onload = init;", theme_js_adm + "\n        window.onload = init;")

if "function init() {" in adm_html:
    adm_html = adm_html.replace("function init() {", "function init() {\n            applyTheme(currentTheme);")

with open("/working_dir/slingshot-shop/admin.html", "w", encoding="utf-8") as f:
    f.write(adm_html)

print("admin.html updated with Theme toggle (Default: Dark)!")
