import os

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\admin.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace CSS definition block
old_style_start = content.find("<style>")
old_style_end = content.find("</style>") + 8

new_style = """<style>
        body { font-family: "Prompt", sans-serif; transition: background-color 0.25s ease, color 0.25s ease; margin: 0; padding: 0; }
        
        /* Dark Theme (Default) */
        :root, [data-theme="dark"], .dark {
            --bg-page: #121215;
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
        [data-theme="light"], .light {
            --bg-page: #F9F6F0;
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

        .app-body { background-color: var(--bg-page) !important; color: var(--text-main) !important; }
        .app-header { background-color: var(--bg-header) !important; border-color: var(--border-main) !important; }
        .app-card { background-color: var(--bg-card) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .app-card-subtle { background-color: var(--bg-card-subtle) !important; border-color: var(--border-subtle) !important; }
        .app-input { background-color: var(--bg-input) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .app-text-main { color: var(--text-main) !important; }
        .app-text-muted { color: var(--text-muted) !important; }
        .app-border { border-color: var(--border-main) !important; }
        .app-border-subtle { border-color: var(--border-subtle) !important; }
        .app-badge { background-color: var(--badge-bg) !important; border-color: var(--badge-border) !important; color: var(--badge-text) !important; }
        .app-tab-inactive { background-color: var(--tab-inactive-bg) !important; color: var(--tab-inactive-text) !important; }
    </style>"""

if old_style_start != -1 and old_style_end != -1:
    content = content[:old_style_start] + new_style + content[old_style_end:]

# Body class
content = content.replace('class="theme-body min-h-screen flex flex-col font-sans"', 'class="app-body min-h-screen flex flex-col font-sans"')

# Header class
content = content.replace('class="sticky top-0 z-40 bg-white border-b-2 border-[#EBE3D5] shadow-sm"', 'class="sticky top-0 z-40 app-header border-b-2 app-border shadow-sm"')
content = content.replace('text-[#2C241E] tracking-tight', 'app-text-main tracking-tight')
content = content.replace('text-slate-500 block font-medium truncate max-w-[180px]', 'app-text-muted block font-medium truncate max-w-[180px]')
content = content.replace('bg-[#FFF2EE] hover:bg-[#FFE3DC] text-[#EE4D2D] border border-[#FFD5CC] text-xs px-3 py-1.5 rounded-xl font-bold flex items-center gap-1 shadow-sm transition-all', 'app-badge text-xs px-3 py-1.5 rounded-xl font-bold flex items-center gap-1 shadow-sm transition-all border')

# Mobile tabs inactive classes in HTML
content = content.replace('bg-[#F2EDE4] text-slate-700 hover:text-[#EE4D2D]', 'app-tab-inactive hover:text-[#EE4D2D]')

# Orders tab controls box
content = content.replace('bg-white p-4 sm:p-5 rounded-3xl border-2 border-[#EBE3D5] flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-sm', 'app-card p-4 sm:p-5 rounded-3xl border-2 app-border flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-sm')
content = content.replace('text-[#2C241E] flex items-center gap-2', 'app-text-main flex items-center gap-2')

# Filter dropdown
content = content.replace('bg-white border border-[#EBE3D5] text-xs font-bold rounded-xl px-3 py-1.5 text-slate-700', 'app-input border app-border text-xs font-bold rounded-xl px-3 py-1.5 app-text-main')

# Goship tab box
content = content.replace('bg-white p-5 sm:p-7 rounded-3xl border-2 border-[#EBE3D5] space-y-5 shadow-sm', 'app-card p-5 sm:p-7 rounded-3xl border-2 app-border space-y-5 shadow-sm')
content = content.replace('border-b border-[#EBE3D5] pb-4', 'border-b app-border pb-4')
content = content.replace('bg-[#FAF7F2] p-4 rounded-2xl border border-[#EBE3D5] space-y-2', 'app-card-subtle p-4 rounded-2xl border app-border-subtle space-y-2')
content = content.replace('bg-white border border-[#EBE3D5] rounded-xl px-3 py-2 text-xs font-mono text-[#2C241E]', 'app-input border app-border rounded-xl px-3 py-2 text-xs font-mono app-text-main')
content = content.replace('bg-white p-3 rounded-xl border border-orange-200', 'app-card p-3 rounded-xl border app-border')
content = content.replace('text-slate-800 block', 'app-text-main block')

# VAT tab box
content = content.replace('bg-[#F2EDE4] rounded-full overflow-hidden border border-[#EBE3D5]', 'app-card-subtle rounded-full overflow-hidden border app-border')

# Modal
content = content.replace('bg-white border-2 border-[#EBE3D5] rounded-3xl max-w-xl w-full p-4 sm:p-6 space-y-4 shadow-2xl my-4 text-[#2C241E]', 'app-card border-2 app-border rounded-3xl max-w-xl w-full p-4 sm:p-6 space-y-4 shadow-2xl my-4 app-text-main')
content = content.replace('bg-[#FAF7F2] border border-[#EBE3D5] rounded-xl px-3 py-2 text-xs sm:text-sm text-[#2C241E]', 'app-input border app-border rounded-xl px-3 py-2 text-xs sm:text-sm app-text-main')

# JS renderOrdersView card class
content = content.replace('card.className = "bg-white p-4 sm:p-5 rounded-3xl border-2 border-[#EBE3D5] shadow-sm space-y-3.5";', 'card.className = "app-card p-4 sm:p-5 rounded-3xl border-2 app-border shadow-sm space-y-3.5";')
content = content.replace('bg-[#FAF7F2] p-2.5 rounded-2xl border border-[#EBE3D5] flex items-center justify-between text-xs', 'app-card-subtle p-2.5 rounded-2xl border app-border-subtle flex items-center justify-between text-xs')
content = content.replace('text-slate-700 space-y-1', 'app-text-main space-y-1')
content = content.replace('text-slate-500 text-[11px]', 'app-text-muted text-[11px]')
content = content.replace('border-t border-slate-100', 'border-t app-border-subtle')

# JS renderInventoryView card class
content = content.replace('card.className = "bg-white p-4 sm:p-5 rounded-3xl border-2 border-[#EBE3D5] shadow-sm space-y-3.5 flex flex-col justify-between";', 'card.className = "app-card p-4 sm:p-5 rounded-3xl border-2 app-border shadow-sm space-y-3.5 flex flex-col justify-between";')
content = content.replace('bg-[#FAF7F2] rounded-2xl border border-[#EBE3D5]', 'app-card-subtle rounded-2xl border app-border-subtle')
content = content.replace('text-[#2C241E] text-xs', 'app-text-main text-xs')
content = content.replace('bg-[#FAF7F2] border border-[#EBE3D5] px-2 py-0.5 rounded text-[10px] text-slate-700', 'app-card-subtle border app-border-subtle px-2 py-0.5 rounded text-[10px] app-text-main')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated admin.html theme styles successfully!")
