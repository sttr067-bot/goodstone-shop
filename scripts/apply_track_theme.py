import re

with open("/working_dir/slingshot-shop/track.html", "r", encoding="utf-8") as f:
    track_html = f.read()

theme_styles_track = """    <style>
        body { font-family: "Prompt", sans-serif; transition: background-color 0.2s ease, color 0.2s ease; margin: 0; padding: 0; }
        
        /* 🌙 Dark Theme (DEFAULT) */
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
            --badge-bg: #2E1B17;
            --badge-border: #5C2B1F;
            --badge-text: #FF6E4E;
        }

        /* ☀️ Light Theme (Warm Cream) */
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
            --badge-bg: #FFF2EE;
            --badge-border: #FFD5CC;
            --badge-text: #EE4D2D;
        }

        .theme-body { background-color: var(--bg-body) !important; color: var(--text-main) !important; }
        .theme-header { background-color: var(--bg-header) !important; border-color: var(--border-main) !important; }
        .theme-card { background-color: var(--bg-card) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .theme-card-subtle { background-color: var(--bg-card-subtle) !important; border-color: var(--border-subtle) !important; }
        .theme-input { background-color: var(--bg-input) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .theme-text-main { color: var(--text-main) !important; }
        .theme-text-muted { color: var(--text-muted) !important; }
    </style>"""

track_html = re.sub(r"<style>[\s\S]*?<\/style>", theme_styles_track, track_html)

track_html = track_html.replace(
    '<body class="bg-[#F9F6F0] text-[#2C241E] min-h-screen flex flex-col font-sans">',
    '<body class="theme-body min-h-screen flex flex-col font-sans" data-theme="dark">'
)

# Header update in track.html
track_html = track_html.replace(
    '<header class="sticky top-0 z-40 bg-white border-b-2 border-[#EBE3D5] shadow-sm">',
    '<header class="sticky top-0 z-40 theme-header border-b-2 shadow-sm">'
)

track_js = """
        let currentTheme = localStorage.getItem("goodstone_theme") || "dark";
        function applyTheme(theme) {
            currentTheme = theme;
            document.documentElement.setAttribute("data-theme", theme);
            document.body.setAttribute("data-theme", theme);
            localStorage.setItem("goodstone_theme", theme);
        }
        applyTheme(currentTheme);
"""

if "window.onload = function()" in track_html:
    track_html = track_html.replace("window.onload = function()", track_js + "\n        window.onload = function()")

with open("/working_dir/slingshot-shop/track.html", "w", encoding="utf-8") as f:
    f.write(track_html)

print("track.html updated with Theme persistence!")
