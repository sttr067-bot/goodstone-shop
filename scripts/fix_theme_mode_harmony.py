import os

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add CSS rules for theme-hero and theme-marquee that automatically adapt to light/dark mode
soop_theme_css = """
        /* Adaptive Hero Section for Light & Dark Mode */
        .theme-hero-container {
            background: linear-gradient(135deg, #FFF5F2, #FFF0EC, #FFE8E2);
            border-color: #FFD5CC;
            color: #1E293B;
        }
        .dark .theme-hero-container, [data-theme="dark"] .theme-hero-container {
            background: linear-gradient(135deg, #261B18, #211C20, #1A1A22) !important;
            border-color: #333342 !important;
            color: #F8FAFC !important;
        }

        .theme-hero-title { color: #0F172A; }
        .dark .theme-hero-title, [data-theme="dark"] .theme-hero-title { color: #F8FAFC !important; }

        .theme-hero-desc { color: #475569; }
        .dark .theme-hero-desc, [data-theme="dark"] .theme-hero-desc { color: #94A3B8 !important; }

        .theme-hero-img-box {
            background-color: #FFFFFF;
            border-color: #FFD5CC;
        }
        .dark .theme-hero-img-box, [data-theme="dark"] .theme-hero-img-box {
            background-color: #1E293B !important;
            border-color: #333342 !important;
        }

        .theme-marquee-banner {
            background-color: #FFF2EE;
            border-color: #FFD5CC;
            color: #EE4D2D;
        }
        .dark .theme-marquee-banner, [data-theme="dark"] .theme-marquee-banner {
            background-color: #1A1A22 !important;
            border-color: #333342 !important;
            color: #FF6E4E !important;
        }

        .theme-marquee-bullet { color: #FFD5CC; }
        .dark .theme-marquee-bullet, [data-theme="dark"] .theme-marquee-bullet { color: #333342 !important; }
"""

if "Adaptive Hero Section for Light & Dark Mode" not in content:
    content = content.replace("</style>", soop_theme_css + "\n    </style>")

# Update Marquee Banner HTML class
content = content.replace(
    'class="bg-[#FFF2EE] text-[#EE4D2D] border-b border-[#FFD5CC] py-2 border-b theme-border overflow-hidden text-xs font-bold"',
    'class="theme-marquee-banner py-2 border-b overflow-hidden text-xs font-bold"'
)
content = content.replace(
    'class="bg-gradient-to-r from-[#261B18] via-[#211C20] to-[#1A1A22] text-[#FF6E4E] py-2 border-b theme-border overflow-hidden text-xs font-bold"',
    'class="theme-marquee-banner py-2 border-b overflow-hidden text-xs font-bold"'
)
content = content.replace('text-[#FFD5CC]">•</span>', 'theme-marquee-bullet">•</span>')

# Update Hero Section HTML classes
old_hero_sec = '<section class="relative overflow-hidden rounded-3xl bg-gradient-to-br from-[#FFF5F2] via-[#FFF0EC] to-[#FFE8E2] border-2 border-[#FFD5CC] text-slate-800 p-6 sm:p-10 md:p-12 shadow-md">'
new_hero_sec = '<section class="relative overflow-hidden rounded-3xl theme-hero-container border-2 p-6 sm:p-10 md:p-12 shadow-md">'
content = content.replace(old_hero_sec, new_hero_sec)

content = content.replace('text-slate-900">\n                            หนังสติ๊กยุทธวิธี', 'theme-hero-title">\n                            หนังสติ๊กยุทธวิธี')
content = content.replace('text-slate-600 leading-relaxed font-medium">\n                            ศูนย์รวมหนังสติ๊กอัลลอยด์', 'theme-hero-desc leading-relaxed font-medium">\n                            ศูนย์รวมหนังสติ๊กอัลลอยด์')

old_hero_img_box = '<div class="relative aspect-[4/3] rounded-2xl overflow-hidden bg-white border-2 border-[#FFD5CC] shadow-md flex items-center justify-center p-4">'
new_hero_img_box = '<div class="relative aspect-[4/3] rounded-2xl overflow-hidden theme-hero-img-box border-2 shadow-md flex items-center justify-center p-4">'
content = content.replace(old_hero_img_box, new_hero_img_box)

# Fix Theme Toggle Button Text & Icon Logic in toggleTheme()
old_toggle_js = """        function toggleTheme() {
            const current = document.body.getAttribute("data-theme") || "dark";
            const target = current === "dark" ? "light" : "dark";
            document.body.setAttribute("data-theme", target);
            if (target === "dark") {
                document.documentElement.classList.add("dark");
                document.getElementById("theme-toggle-icon").innerText = "🌙";
                document.getElementById("theme-toggle-text").innerText = "โหมดมืด";
            } else {
                document.documentElement.classList.remove("dark");
                document.getElementById("theme-toggle-icon").innerText = "☀️";
                document.getElementById("theme-toggle-text").innerText = "โหมดสว่าง";
            }
            localStorage.setItem("goodstone_theme", target);
        }"""

new_toggle_js = """        function toggleTheme() {
            const current = document.body.getAttribute("data-theme") || "light";
            const target = current === "dark" ? "light" : "dark";
            document.body.setAttribute("data-theme", target);
            applyThemeUI(target);
            localStorage.setItem("goodstone_theme", target);
        }

        function applyThemeUI(theme) {
            const iconEl = document.getElementById("theme-toggle-icon");
            const textEl = document.getElementById("theme-toggle-text");
            if (theme === "dark") {
                document.documentElement.classList.add("dark");
                document.body.classList.add("dark");
                if (iconEl) iconEl.innerText = "☀️";
                if (textEl) textEl.innerText = "โหมดสว่าง";
            } else {
                document.documentElement.classList.remove("dark");
                document.body.classList.remove("dark");
                if (iconEl) iconEl.innerText = "🌙";
                if (textEl) textEl.innerText = "โหมดมืด";
            }
        }"""

if "function applyThemeUI(theme)" not in content:
    content = content.replace(old_toggle_js, new_toggle_js)
    content = content.replace(
        'function loadSavedTheme() {\n            const saved = localStorage.getItem("goodstone_theme") || "light";\n            document.body.setAttribute("data-theme", saved);\n            if (saved === "dark") {\n                document.documentElement.classList.add("dark");\n            } else {\n                document.documentElement.classList.remove("dark");\n            }\n        }',
        'function loadSavedTheme() {\n            const saved = localStorage.getItem("goodstone_theme") || "light";\n            document.body.setAttribute("data-theme", saved);\n            applyThemeUI(saved);\n        }'
    )

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed theme mode harmony across Hero, Marquee, and Toggle Button successfully!")
