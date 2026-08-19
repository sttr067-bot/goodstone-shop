import os, re

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update <style> block to include SOOP-style smooth transitions, glassmorphism, and badge styles
soop_css_additions = """
        /* ---- SOOPTHAILAND DESIGN SYSTEM ENHANCements ---- */
        .glass-header {
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
        }
        .soop-card {
            transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.2s ease;
        }
        .soop-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 12px 30px -10px rgba(0, 0, 0, 0.25);
        }
        .emerald-badge {
            background-color: rgba(16, 185, 129, 0.1);
            color: #10B981;
            border: 1px solid rgba(16, 185, 129, 0.3);
        }
"""

if "SOOPTHAILAND DESIGN SYSTEM ENHANCements" not in content:
    content = content.replace("</style>", soop_css_additions + "\n    </style>")

# 2. Replace Header with SOOP Style Header
old_header_pattern = re.compile(r'<header class="sticky top-0 z-40 theme-header border-b-2 shadow-sm">.*?</header>', re.DOTALL)
new_header_html = """<header class="sticky top-0 z-40 theme-header border-b glass-header shadow-sm">
        <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16 sm:h-20">
                <!-- Logo & Brand Badge -->
                <div class="flex items-center gap-2.5 sm:gap-3 cursor-pointer" onclick="showCatalogView()">
                    <div class="w-10 h-10 rounded-2xl bg-[#EE4D2D] flex items-center justify-center text-white font-black text-xl shadow-md shadow-orange-500/20 flex-shrink-0">
                        🎯
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="font-black text-base sm:text-xl tracking-tight theme-text-main">GOODSTONE</span>
                            <span class="inline-flex items-center gap-1 rounded-full emerald-badge px-2.5 py-0.5 text-[10px] font-bold">
                                <span>🚚</span>
                                <span class="hidden sm:inline">ส่งด่วน SPX / EMS</span>
                                <span class="sm:hidden">ส่งด่วน</span>
                            </span>
                        </div>
                        <span class="text-[10px] sm:text-xs block theme-text-muted font-medium">ร้านหนังสติ๊กยุทธวิธีและอุปกรณ์ครบวงจร</span>
                    </div>
                </div>

                <!-- Nav Menu & Actions -->
                <div class="flex items-center gap-2 sm:gap-3">
                    <button onclick="showCatalogView()" class="theme-text-main hover:text-[#EE4D2D] text-xs sm:text-sm font-bold transition-colors flex items-center gap-1 px-2.5 py-1.5 rounded-xl hover:bg-black/5 dark:hover:bg-white/5">
                        <i data-lucide="store" class="w-4 h-4 text-[#EE4D2D]"></i>
                        <span class="hidden xs:inline">หน้าร้านค้า</span>
                    </button>
                    <a href="track.html" class="theme-text-muted hover:text-[#EE4D2D] text-xs sm:text-sm font-bold transition-colors flex items-center gap-1 px-2.5 py-1.5 rounded-xl hover:bg-black/5 dark:hover:bg-white/5">
                        <i data-lucide="truck" class="w-4 h-4"></i>
                        <span class="hidden xs:inline">เช็คพัสดุ</span>
                    </a>

                    <!-- Light / Dark Mode Toggle Button -->
                    <button type="button" onclick="toggleTheme()" id="theme-toggle-btn" class="flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-xl border border-[#333342] bg-[#272732] text-[#F4F0EA] hover:border-[#FF6E4E] text-xs font-bold transition-all shadow-sm active:scale-95 cursor-pointer" title="สลับโหมดมืด / สว่าง">
                        <span id="theme-toggle-icon">🌙</span>
                        <span id="theme-toggle-text" class="hidden sm:inline">โหมดมืด</span>
                    </button>

                    <!-- Customer Wallet Badge -->
                    <div id="header-wallet-badge" class="hidden md:flex items-center gap-1.5 theme-badge px-3 py-1.5 rounded-xl text-xs font-bold border">
                        <span class="theme-text-muted">👛 เครดิต:</span>
                        <span id="user-wallet-display" class="font-black text-[#EE4D2D]">฿0.00</span>
                    </div>
                </div>
            </div>
        </div>
    </header>"""

if old_header_pattern.search(content):
    content = old_header_pattern.sub(new_header_html, content)

# 3. Add 3 SOOP-Style Feature Guarantee Cards after Hero Section
soop_features_html = """
            <!-- SOOP-STYLE 3 FEATURE GUARANTEE CARDS BAR -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 sm:gap-4 border-y theme-border py-4 my-2">
                <div class="flex items-center gap-3.5 p-3 rounded-2xl theme-card-subtle border theme-border">
                    <div class="w-10 h-10 rounded-2xl bg-[#EE4D2D]/10 text-[#EE4D2D] flex items-center justify-center text-xl flex-shrink-0 font-bold">
                        🚚
                    </div>
                    <div>
                        <p class="text-xs sm:text-sm font-black theme-text-main">ส่งด่วน SPX / EMS ฿25</p>
                        <p class="text-[11px] theme-text-muted">ส่งฟรีเมื่อสั่งซื้อครบ 200 บาทขึ้นไป</p>
                    </div>
                </div>
                <div class="flex items-center gap-3.5 p-3 rounded-2xl theme-card-subtle border theme-border">
                    <div class="w-10 h-10 rounded-2xl bg-emerald-500/10 text-emerald-500 flex items-center justify-center text-xl flex-shrink-0 font-bold">
                        🛡️
                    </div>
                    <div>
                        <p class="text-xs sm:text-sm font-black theme-text-main">ของแท้เกรดพรีเมียม 100%</p>
                        <p class="text-[11px] theme-text-muted">สแตนเลส CNC / เลเซอร์ช่วยเล็งแม่นยำ</p>
                    </div>
                </div>
                <div class="flex items-center gap-3.5 p-3 rounded-2xl theme-card-subtle border theme-border">
                    <div class="w-10 h-10 rounded-2xl bg-blue-500/10 text-blue-500 flex items-center justify-center text-xl flex-shrink-0 font-bold">
                        🕒
                    </div>
                    <div>
                        <p class="text-xs sm:text-sm font-black theme-text-main">สั่งซื้อ 24 ชม. ปลายทางได้</p>
                        <p class="text-[11px] theme-text-muted">โอนพร้อมเพย์ 0% หรือเก็บปลายทาง COD</p>
                    </div>
                </div>
            </div>
"""

if "SOOP-STYLE 3 FEATURE GUARANTEE CARDS BAR" not in content:
    search_target = '<!-- Search & Categories Filter -->'
    content = content.replace(search_target, soop_features_html + "\n            " + search_target)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied SOOP-style design upgrades successfully!")
