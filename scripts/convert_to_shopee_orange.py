import os

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace CSS Variables & Emerald Class References with Shopee Orange Theme (#EE4D2D)
content = content.replace('--badge-bg: rgba(16, 185, 129, 0.12);', '--badge-bg: rgba(238, 77, 45, 0.12);')
content = content.replace('--badge-border: rgba(16, 185, 129, 0.3);', '--badge-border: rgba(238, 77, 45, 0.3);')
content = content.replace('--badge-text: #34D399;', '--badge-text: #FF6E4E;')
content = content.replace('--accent-green: #10B981;', '--accent-green: #EE4D2D;')

content = content.replace('bg-emerald-500 hover:bg-emerald-400', 'bg-[#EE4D2D] hover:bg-[#d73211]')
content = content.replace('bg-emerald-600 hover:bg-emerald-500', 'bg-[#EE4D2D] hover:bg-[#d73211]')
content = content.replace('bg-emerald-500/10', 'bg-[#EE4D2D]/10')
content = content.replace('border-emerald-500/30', 'border-[#EE4D2D]/30')
content = content.replace('border-emerald-500', 'border-[#EE4D2D]')
content = content.replace('text-emerald-400', 'text-[#FF6E4E]')
content = content.replace('text-emerald-500', 'text-[#EE4D2D]')
content = content.replace('focus:ring-emerald-500', 'focus:ring-[#EE4D2D]')
content = content.replace('shadow-emerald-500/20', 'shadow-orange-500/20')
content = content.replace('shadow-emerald-500/25', 'shadow-orange-500/25')
content = content.replace('from-emerald-950 via-slate-900 to-emerald-950', 'from-[#261B18] via-[#211C20] to-[#1A1A22]')
content = content.replace('text-emerald-300', 'text-[#FF6E4E]')
content = content.replace('emerald-badge', 'shopee-badge')

# Restore LINE green specifically for LINE button
content = content.replace('bg-[#EE4D2D] hover:bg-[#d73211] text-white px-3 py-1.5 rounded-xl text-xs font-bold transition-all shadow-md active:scale-95 inline-flex items-center gap-1.5', 'bg-[#06C755] hover:bg-[#05b049] text-white px-3 py-1.5 rounded-xl text-xs font-bold transition-all shadow-md active:scale-95 inline-flex items-center gap-1.5')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Converted accent colors to Shopee Orange (#EE4D2D) successfully!")
