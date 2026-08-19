import os

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Hero Section with Option 1: Shopee Mall Clean Light Style
old_hero_marker_start = '<section class="relative overflow-hidden rounded-3xl bg-gradient-to-br from-slate-950 via-slate-900 to-slate-800 border border-slate-800 text-white p-6 sm:p-10 md:p-12 shadow-2xl">'
old_hero_marker_end = '</section>'

shopee_mall_hero_html = """<!-- SHOPEE MALL CLEAN LIGHT HERO SECTION -->
            <section class="relative overflow-hidden rounded-3xl bg-gradient-to-br from-[#FFF5F2] via-[#FFF0EC] to-[#FFE8E2] border-2 border-[#FFD5CC] text-slate-800 p-6 sm:p-10 md:p-12 shadow-md">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="space-y-4 max-w-xl">
                        <div class="inline-flex items-center gap-2 rounded-full bg-[#FFF2EE] border border-[#FFD5CC] px-3.5 py-1 text-xs font-bold text-[#EE4D2D]">
                            <i data-lucide="shield-check" class="w-4 h-4 text-[#EE4D2D]"></i>
                            <span>ของแท้เกรดพรีเมียม 100% • Shopee Mall Quality</span>
                        </div>
                        <h1 class="text-3xl sm:text-5xl font-black tracking-tight leading-tight text-slate-900">
                            หนังสติ๊กยุทธวิธี<br>
                            <span class="text-[#EE4D2D]">GOODSTONE</span>
                        </h1>
                        <p class="text-sm sm:text-base text-slate-600 leading-relaxed font-medium">
                            ศูนย์รวมหนังสติ๊กอัลลอยด์ CNC เลเซอร์ช่วยเล็ง ยางแบนเกรด A และลูกเหล็กยุทธวิธี จัดส่งด่วนทั่วประเทศ 24 ชั่วโมง
                        </p>
                        
                        <div class="flex flex-wrap gap-3 pt-2">
                            <button onclick="document.getElementById('catalog-products-section').scrollIntoView({behavior:'smooth'})" class="bg-[#EE4D2D] hover:bg-[#d73211] text-white font-black px-6 py-3 rounded-2xl text-sm shadow-lg shadow-orange-500/25 transition-all active:scale-95 flex items-center gap-2 cursor-pointer">
                                <span>ดูสินค้าทั้งหมด</span>
                                <i data-lucide="arrow-right" class="w-4 h-4"></i>
                            </button>
                            <a href="https://lin.ee/qX9RSdN" target="_blank" class="border border-[#FFD5CC] bg-white hover:bg-[#FFF2EE] text-slate-800 font-bold px-5 py-3 rounded-2xl text-sm transition-all flex items-center gap-2 shadow-sm">
                                <i data-lucide="message-circle" class="w-4 h-4 text-[#06C755]"></i>
                                <span>สั่งผ่าน LINE</span>
                            </a>
                        </div>
                    </div>

                    <!-- Hero Visual Showcase (Clean White Border Box) -->
                    <div class="relative aspect-[4/3] rounded-2xl overflow-hidden bg-white border-2 border-[#FFD5CC] shadow-md flex items-center justify-center p-4">
                        <img src="https://lh3.googleusercontent.com/d/1u5fhZmlGqWrCY7CJpGSe5xHQqbt6ArDa" alt="GOODSTONE Slingshot" class="max-h-full max-w-full object-contain filter drop-shadow-md">
                        <div class="absolute bottom-3 left-3 bg-white/90 backdrop-blur-md px-3 py-1.5 rounded-xl border border-[#FFD5CC] text-xs font-bold text-[#EE4D2D] flex items-center gap-2 shadow-sm">
                            <span>⭐ รีวิว 4.9/5</span>
                            <span class="text-slate-300">|</span>
                            <span class="text-slate-600">📦 1,200+ ออเดอร์</span>
                        </div>
                    </div>
                </div>
            </section>"""

if old_hero_marker_start in content:
    pos_start = content.find(old_hero_marker_start)
    pos_end = content.find(old_hero_marker_end, pos_start) + len(old_hero_marker_end)
    content = content[:pos_start] + shopee_mall_hero_html + content[pos_end:]

# Replace Marquee Banner Background to match Shopee Light Style
content = content.replace(
    'bg-gradient-to-r from-[#261B18] via-[#211C20] to-[#1A1A22] text-[#FF6E4E]',
    'bg-[#FFF2EE] text-[#EE4D2D] border-b border-[#FFD5CC]'
)
content = content.replace('text-slate-600">•</span>', 'text-[#FFD5CC]">•</span>')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied Option 1: Shopee Mall Clean Light Style Hero Section successfully!")
