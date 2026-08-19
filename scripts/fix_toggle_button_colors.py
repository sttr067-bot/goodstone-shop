import os

index_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\index.html"
admin_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\admin.html"

# 1. Update index.html
with open(index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

toggle_btn_css = """
        /* Theme Toggle Button Adaptive Style */
        .theme-toggle-btn {
            background-color: #F1F5F9 !important;
            border-color: #CBD5E1 !important;
            color: #1E293B !important;
        }
        .dark .theme-toggle-btn, [data-theme="dark"] .theme-toggle-btn {
            background-color: #1E293B !important;
            border-color: #334155 !important;
            color: #F8FAFC !important;
        }
"""

if "Theme Toggle Button Adaptive Style" not in idx_content:
    idx_content = idx_content.replace("</style>", toggle_btn_css + "\n    </style>")

idx_content = idx_content.replace(
    'class="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-200 hover:border-[#EE4D2D] text-xs font-bold transition-all shadow-sm active:scale-95 cursor-pointer"',
    'class="theme-toggle-btn flex items-center gap-1.5 px-3 py-1.5 rounded-xl border hover:border-[#EE4D2D] text-xs font-bold transition-all shadow-sm active:scale-95 cursor-pointer"'
)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_content)

# 2. Update admin.html
with open(admin_path, "r", encoding="utf-8") as f:
    admin_content = f.read()

admin_toggle_css = """
        .app-toggle-btn {
            background-color: #F1F5F9 !important;
            border-color: #CBD5E1 !important;
            color: #1E293B !important;
        }
        .dark .app-toggle-btn, [data-theme="dark"] .app-toggle-btn {
            background-color: #272732 !important;
            border-color: #333342 !important;
            color: #F4F0EA !important;
        }
"""

if ".app-toggle-btn" not in admin_content:
    admin_content = admin_content.replace("</style>", admin_toggle_css + "\n    </style>")

admin_content = admin_content.replace(
    'class="flex items-center gap-1 px-2.5 py-1.5 rounded-xl border border-[#333342] bg-[#272732] text-[#F4F0EA] hover:border-[#FF6E4E] text-xs font-bold transition-all shadow-sm active:scale-95"',
    'class="app-toggle-btn flex items-center gap-1 px-2.5 py-1.5 rounded-xl border hover:border-[#EE4D2D] text-xs font-bold transition-all shadow-sm active:scale-95"'
)

with open(admin_path, "w", encoding="utf-8") as f:
    f.write(admin_content)

print("Updated theme toggle buttons to adapt colors dynamically in both light and dark mode!")
