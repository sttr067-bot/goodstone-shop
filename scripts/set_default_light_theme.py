import os

index_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\index.html"
admin_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\admin.html"

# Update index.html
with open(index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

idx_content = idx_content.replace('<html lang="th" data-theme="dark" class="h-full antialiased dark">', '<html lang="th" data-theme="light" class="h-full antialiased light">')
idx_content = idx_content.replace('<body class="theme-body min-h-screen flex flex-col font-sans" data-theme="dark">', '<body class="theme-body min-h-screen flex flex-col font-sans" data-theme="light">')
idx_content = idx_content.replace('const saved = localStorage.getItem("goodstone_theme") || "dark";', 'const saved = localStorage.getItem("goodstone_theme") || "light";')
idx_content = idx_content.replace('<span id="theme-toggle-icon">🌙</span>', '<span id="theme-toggle-icon">☀️</span>')
idx_content = idx_content.replace('<span id="theme-toggle-text" class="hidden sm:inline">โหมดมืด</span>', '<span id="theme-toggle-text" class="hidden sm:inline">โหมดสว่าง</span>')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_content)

# Update admin.html
with open(admin_path, "r", encoding="utf-8") as f:
    admin_content = f.read()

admin_content = admin_content.replace('<body class="app-body min-h-screen flex flex-col font-sans" data-theme="dark">', '<body class="app-body min-h-screen flex flex-col font-sans" data-theme="light">')
admin_content = admin_content.replace('const saved = localStorage.getItem("goodstone_admin_theme") || "dark";', 'const saved = localStorage.getItem("goodstone_admin_theme") || "light";')
admin_content = admin_content.replace('let currentTheme = localStorage.getItem("goodstone_admin_theme") || "dark";', 'let currentTheme = localStorage.getItem("goodstone_admin_theme") || "light";')

with open(admin_path, "w", encoding="utf-8") as f:
    f.write(admin_content)

print("Set default theme to Light mode across index.html and admin.html successfully!")
