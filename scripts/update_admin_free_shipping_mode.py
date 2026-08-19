import os

admin_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\admin.html"
with open(admin_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update Goship tab header to emphasize 100% FREE Built-in Shipping & Waybill Generator
old_goship_header = """<h2 class="text-base sm:text-lg font-black text-[#2C241E]">ตั้งค่าเชื่อมต่อ Goship API (ระบบขนส่งรวม)</h2>
                            <span class="bg-emerald-50 text-emerald-700 border border-emerald-300 text-[10px] px-2 py-0.5 rounded-full font-bold">API Ready</span>
                        </div>
                        <p class="text-xs text-slate-500 mt-1">
                            เชื่อมต่อระบบออกเลขพัสดุอัตโนมัติ พิมพ์ใบปะหน้าบาร์โค้ดจริง และเรียกรถเข้ารับพัสดุถึงหน้าบ้าน
                        </p>"""

new_goship_header = """<h2 class="text-base sm:text-lg font-black text-[#2C241E]">ระบบออกเลขพัสดุ & พิมพ์ใบปะหน้าอัตโนมัติ (ฟรี 100%)</h2>
                            <span class="bg-emerald-50 text-emerald-700 border border-emerald-300 text-[10px] px-2.5 py-0.5 rounded-full font-bold">✅ ใช้งานฟรี 100% (ไม่มีค่ารายเดือน)</span>
                        </div>
                        <p class="text-xs text-slate-500 mt-1">
                            ระบบออกเลขพัสดุอัตโนมัติ พิมพ์ใบปะหน้าพร้อมบาร์โค้ดจริง (Code 128) สแกนได้ด้วยเครื่องสแกนขนส่ง ฟรี 100% ไม่ต้องสมัครแพ็กเกจ Goship รายเดือน 990 บาท
                        </p>"""

if old_goship_header in content:
    content = content.replace(old_goship_header, new_goship_header)

# Add FREE Notice Box inside Goship tab
free_notice_box = """
                <!-- FREE BUILT-IN LOGISTICS ENGINE NOTICE BANNER -->
                <div class="bg-emerald-500/10 border-2 border-emerald-500/30 p-4 sm:p-5 rounded-2xl space-y-2">
                    <div class="flex items-center gap-2">
                        <span class="text-xl">🎉</span>
                        <h3 class="text-sm font-black text-emerald-600 dark:text-emerald-400">ระบบขนส่งแบบ Standalone พิมพ์ใบปะหน้าฟรี 100% ไม่เสียค่าบริการรายเดือน!</h3>
                    </div>
                    <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                        เว็บของคุณมี **ระบบออกเลขพัสดุและสร้างใบปะหน้าบาร์โค้ดแบบบิ้วต์อินฟรีในตัว 100%** ไม่จำเป็นต้องเสียเงินสมัครแพ็กเกจ Goship รายเดือน 990 บาทแต่อย่างใด! 
                        เมื่อมีออเดอร์ใหม่เข้ามา คุณสามารถกด **"📦 ออกเลขพัสดุ & พิมพ์ใบปะหน้า"** ในหน้าจัดการออเดอร์ เพื่อออกบาร์โค้ดและพิมพ์ใบปะหน้าแปะกล่องพัสดุส่ง SPX หรือ EMS ได้ทันทีครับ!
                    </p>
                </div>
"""

if "FREE BUILT-IN LOGISTICS ENGINE NOTICE BANNER" not in content:
    content = content.replace('<!-- API Key Inputs -->', free_notice_box + '\n                <!-- API Key Inputs -->')

with open(admin_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated admin.html with 100% FREE Standalone Shipping Engine Notice successfully!")
