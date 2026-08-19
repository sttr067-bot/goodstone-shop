import os

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Build the complete SOOPTHAILAND-matching index.html
full_soop_index_html = """<!DOCTYPE html>
<html lang="th" data-theme="dark" class="h-full antialiased dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>GOODSTONE - หนังสติ๊กยุทธวิธีเกรดพรีเมียม & อุปกรณ์ครบวงจร</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        emerald: {
                            500: "#10B981",
                            600: "#059669",
                            400: "#34D399"
                        },
                        shopee: {
                            DEFAULT: "#EE4D2D",
                            hover: "#D73211"
                        }
                    }
                }
            }
        }
    </script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="thai_postal_db.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        body { 
            font-family: "Prompt", -apple-system, BlinkMacSystemFont, sans-serif; 
            letter-spacing: -0.01em; 
            transition: background-color 0.25s ease, color 0.25s ease; 
        }
        
        /* SOOPTHAILAND Color Scheme Tokens (Slate 950 Dark & Clean Light) */
        :root, [data-theme="dark"], .dark {
            --bg-body: #020617; /* slate-950 */
            --bg-header: rgba(15, 23, 42, 0.85); /* slate-900 with backdrop-blur */
            --bg-card: #0F172A; /* slate-900 */
            --bg-card-subtle: #1E293B; /* slate-800 */
            --bg-input: #0F172A;
            --border-main: #334155; /* slate-700 */
            --border-subtle: #1E293B;
            --text-main: #F8FAFC; /* slate-50 */
            --text-muted: #94A3B8; /* slate-400 */
            --badge-bg: rgba(16, 185, 129, 0.12);
            --badge-border: rgba(16, 185, 129, 0.3);
            --badge-text: #34D399;
            --accent-green: #10B981;
            --accent-orange: #EE4D2D;
        }

        [data-theme="light"], .light {
            --bg-body: #F8FAFC;
            --bg-header: rgba(255, 255, 255, 0.9);
            --bg-card: #FFFFFF;
            --bg-card-subtle: #F1F5F9;
            --bg-input: #FFFFFF;
            --border-main: #E2E8F0;
            --border-subtle: #F1F5F9;
            --text-main: #0F172A;
            --text-muted: #64748B;
            --badge-bg: #ECFDF5;
            --badge-border: #A7F3D0;
            --badge-text: #059669;
            --accent-green: #10B981;
            --accent-orange: #EE4D2D;
        }

        .theme-body { background-color: var(--bg-body) !important; color: var(--text-main) !important; }
        .theme-header { background-color: var(--bg-header) !important; border-color: var(--border-main) !important; }
        .theme-card { background-color: var(--bg-card) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .theme-card-subtle { background-color: var(--bg-card-subtle) !important; border-color: var(--border-subtle) !important; }
        .theme-input { background-color: var(--bg-input) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .theme-text-main { color: var(--text-main) !important; }
        .theme-text-muted { color: var(--text-muted) !important; }
        .theme-border { border-color: var(--border-main) !important; }

        /* SOOP Smooth Hover Effects */
        .soop-product-card {
            transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.25s ease;
        }
        .soop-product-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 30px -10px rgba(16, 185, 129, 0.15);
            border-color: #10B981 !important;
        }

        /* Marquee Animation */
        @keyframes marquee {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        .marquee-track { animation: marquee 25s linear infinite; }
        .marquee-track:hover { animation-play-state: paused; }
    </style>
</head>
<body class="theme-body min-h-screen flex flex-col font-sans" data-theme="dark">

    <!-- ================= 1. STICKY TOP HEADER (SOOPTHAILAND STYLE) ================= -->
    <header class="sticky top-0 z-40 theme-header border-b backdrop-blur-md supports-[backdrop-filter]:bg-opacity-80">
        <div class="max-w-7xl mx-auto flex h-16 md:h-20 items-center justify-between gap-3 px-4 md:px-8">
            
            <!-- Left Logo & Fast Shipping Badge -->
            <div class="flex items-center gap-3 cursor-pointer" onclick="showCatalogView()">
                <span class="inline-flex h-9 sm:h-10 items-center justify-center rounded-xl bg-[#10B981] px-3 text-sm sm:text-base font-black text-white shadow-md shadow-emerald-500/20">
                    GOODSTONE
                </span>
                <a href="/track.html" class="inline-flex items-center gap-1.5 rounded-full border border-emerald-500/30 bg-emerald-500/10 px-2.5 py-1 text-[11px] font-bold text-emerald-400 transition-colors hover:bg-emerald-500/20">
                    <i data-lucide="truck" class="w-3.5 h-3.5 text-emerald-400"></i>
                    <span class="sm:hidden">ส่งฟรี ฿200</span>
                    <span class="hidden sm:inline">ส่งด่วน SPX / EMS • สั่งครบ ฿200 ส่งฟรี</span>
                </a>
            </div>

            <!-- Middle Navigation Links -->
            <nav class="hidden md:flex items-center gap-6 text-sm font-semibold">
                <button onclick="showCatalogView()" class="theme-text-main hover:text-emerald-400 transition-colors">หน้าแรก</button>
                <button onclick="filterCategory('slingshot')" class="theme-text-muted hover:text-emerald-400 transition-colors">หนังสติ๊ก</button>
                <button onclick="filterCategory('rubber')" class="theme-text-muted hover:text-emerald-400 transition-colors">ยางแบน</button>
                <button onclick="filterCategory('ammo')" class="theme-text-muted hover:text-emerald-400 transition-colors">ลูกเหล็ก</button>
                <a href="track.html" class="theme-text-muted hover:text-emerald-400 transition-colors">เช็คพัสดุ</a>
            </nav>

            <!-- Search Bar (Desktop) -->
            <div class="hidden lg:flex items-center relative w-64">
                <i data-lucide="search" class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
                <input type="text" id="header-search-input" oninput="handleSearch(this.value)" placeholder="ค้นหาหนังสติ๊ก, ยางแบน..." class="w-full theme-input border rounded-xl pl-9 pr-3 py-1.5 text-xs font-medium focus:outline-none focus:ring-2 focus:ring-emerald-500">
            </div>

            <!-- Right Action Buttons (Theme Toggle, Direct LINE Order CTA) -->
            <div class="flex items-center gap-2">
                <button type="button" onclick="toggleTheme()" id="theme-toggle-btn" class="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-slate-700 bg-slate-800 text-slate-200 hover:border-emerald-500 text-xs font-bold transition-all shadow-sm active:scale-95 cursor-pointer">
                    <span id="theme-toggle-icon">🌙</span>
                    <span id="theme-toggle-text" class="hidden sm:inline">โหมดมืด</span>
                </button>

                <a href="https://lin.ee/qX9RSdN" target="_blank" class="inline-flex items-center gap-1.5 bg-[#06C755] hover:bg-[#05b049] text-white px-3 py-1.5 rounded-xl text-xs font-bold transition-all shadow-md active:scale-95">
                    <i data-lucide="message-circle" class="w-4 h-4"></i>
                    <span class="hidden sm:inline">สั่งซื้อทาง LINE</span>
                </a>
            </div>
        </div>
    </header>

    <!-- PROMOTION MARQUEE BANNER -->
    <div class="bg-gradient-to-r from-emerald-950 via-slate-900 to-emerald-950 text-emerald-300 py-2 border-b theme-border overflow-hidden text-xs font-bold">
        <div class="flex" style="width: max-content;">
            <div class="marquee-track flex items-center gap-8 px-4" style="width: max-content;">
                <span>🎯 หนังสติ๊กยุทธวิธีอัลลอยด์ CNC เกรดพรีเมียม</span>
                <span class="text-slate-600">•</span>
                <span>📮 ค่าจัดส่ง EMS ฿25 ทั่วไทย (สั่งครบ ฿200 ส่งฟรี)</span>
                <span class="text-slate-600">•</span>
                <span>⚡ โอนพร้อมเพย์ 0% หรือเก็บเงินปลายทาง (COD +3%)</span>
                <span class="text-slate-600">•</span>
                <span>✅ สินค้ามีรับประกัน เปลี่ยนชิ้นใหม่ทันที</span>
                <span class="text-slate-600">•</span>
                <span>🎯 หนังสติ๊กยุทธวิธีอัลลอยด์ CNC เกรดพรีเมียม</span>
                <span class="text-slate-600">•</span>
                <span>📮 ค่าจัดส่ง EMS ฿25 ทั่วไทย (สั่งครบ ฿200 ส่งฟรี)</span>
                <span class="text-slate-600">•</span>
                <span>⚡ โอนพร้อมเพย์ 0% หรือเก็บเงินปลายทาง (COD +3%)</span>
                <span class="text-slate-600">•</span>
                <span>✅ สินค้ามีรับประกัน เปลี่ยนชิ้นใหม่ทันที</span>
                <span class="text-slate-600">•</span>
            </div>
        </div>
    </div>

    <!-- MAIN CONTAINER -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-10 space-y-10">

        <!-- ================= VIEW 1: PRODUCT CATALOG / GRID (SOOPTHAILAND HERO & CATEGORY STYLE) ================= -->
        <section id="view-catalog" class="space-y-10">
            
            <!-- SOOP-STYLE HERO SECTION WITH DARK GRADIENT -->
            <section class="relative overflow-hidden rounded-3xl bg-gradient-to-br from-slate-950 via-slate-900 to-slate-800 border border-slate-800 text-white p-6 sm:p-10 md:p-12 shadow-2xl">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="space-y-4 max-w-xl">
                        <div class="inline-flex items-center gap-2 rounded-full bg-emerald-500/10 border border-emerald-500/30 px-3.5 py-1 text-xs font-bold text-emerald-400">
                            <i data-lucide="shield-check" class="w-4 h-4 text-emerald-400"></i>
                            <span>ของแท้เกรดพรีเมียม 100%</span>
                        </div>
                        <h1 class="text-3xl sm:text-5xl font-black tracking-tight leading-tight">
                            หนังสติ๊กยุทธวิธี<br>
                            <span class="text-emerald-400">GOODSTONE</span>
                        </h1>
                        <p class="text-sm sm:text-base text-slate-300 leading-relaxed">
                            ศูนย์รวมหนังสติ๊กอัลลอยด์ CNC เลเซอร์ช่วยเล็ง ยางแบนเกรด A และลูกเหล็กยุทธวิธี จัดส่งด่วนทั่วประเทศ 24 ชั่วโมง
                        </p>
                        
                        <div class="flex flex-wrap gap-3 pt-2">
                            <button onclick="document.getElementById('catalog-products-section').scrollIntoView({behavior:'smooth'})" class="bg-emerald-500 hover:bg-emerald-400 text-white font-black px-6 py-3 rounded-2xl text-sm shadow-lg shadow-emerald-500/25 transition-all active:scale-95 flex items-center gap-2">
                                <span>ดูสินค้าทั้งหมด</span>
                                <i data-lucide="arrow-right" class="w-4 h-4"></i>
                            </button>
                            <a href="https://lin.ee/qX9RSdN" target="_blank" class="border border-white/20 bg-white/10 hover:bg-white/20 text-white font-bold px-5 py-3 rounded-2xl text-sm transition-all flex items-center gap-2">
                                <i data-lucide="message-circle" class="w-4 h-4 text-[#06C755]"></i>
                                <span>สั่งผ่าน LINE</span>
                            </a>
                        </div>
                    </div>

                    <!-- Hero Visual Showcase -->
                    <div class="relative aspect-[4/3] rounded-2xl overflow-hidden bg-slate-800 border border-slate-700 shadow-2xl flex items-center justify-center p-4">
                        <img src="https://lh3.googleusercontent.com/d/1u5fhZmlGqWrCY7CJpGSe5xHQqbt6ArDa" alt="GOODSTONE Slingshot" class="max-h-full max-w-full object-contain filter drop-shadow-2xl">
                        <div class="absolute bottom-3 left-3 bg-black/70 backdrop-blur-md px-3 py-1.5 rounded-xl border border-white/10 text-xs font-bold text-emerald-400 flex items-center gap-2">
                            <span>⭐ รีวิว 4.9/5</span>
                            <span class="text-slate-400">|</span>
                            <span>📦 1,200+ ออเดอร์</span>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SOOP-STYLE 3 FEATURE GUARANTEE CARDS BAR -->
            <section class="border-y border-slate-800 py-6">
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-6">
                    <div class="flex items-start gap-4 p-4 rounded-2xl theme-card border theme-border">
                        <div class="w-10 h-10 rounded-full bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 shrink-0 font-bold">
                            <i data-lucide="truck" class="w-5 h-5"></i>
                        </div>
                        <div>
                            <h3 class="text-sm font-black theme-text-main">ส่งด่วน SPX / EMS ฿25</h3>
                            <p class="text-xs theme-text-muted mt-0.5">สั่งครบ 200 บาทขึ้นไป จัดส่งฟรีทันทีทั่วไทย</p>
                        </div>
                    </div>

                    <div class="flex items-start gap-4 p-4 rounded-2xl theme-card border theme-border">
                        <div class="w-10 h-10 rounded-full bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 shrink-0 font-bold">
                            <i data-lucide="shield-check" class="w-5 h-5"></i>
                        </div>
                        <div>
                            <h3 class="text-sm font-black theme-text-main">ของแท้เกรดพรีเมียม 100%</h3>
                            <p class="text-xs theme-text-muted mt-0.5">สแตนเลส CNC ไร้สนิม เลเซอร์ช่วยเล็งแม่นยำ</p>
                        </div>
                    </div>

                    <div class="flex items-start gap-4 p-4 rounded-2xl theme-card border theme-border">
                        <div class="w-10 h-10 rounded-full bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 shrink-0 font-bold">
                            <i data-lucide="clock" class="w-5 h-5"></i>
                        </div>
                        <div>
                            <h3 class="text-sm font-black theme-text-main">สั่งซื้อ 24 ชม. มีปลายทาง COD</h3>
                            <p class="text-xs theme-text-muted mt-0.5">โอนพร้อมเพย์ 0% หรือเก็บเงินปลายทาง (COD +3%)</p>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SOOP-STYLE CATEGORY SELECTOR CARDS -->
            <section id="catalog-products-section" class="space-y-6">
                <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
                    <div>
                        <p class="text-xs font-bold uppercase tracking-widest text-emerald-400">หมวดสินค้า</p>
                        <h2 class="text-2xl sm:text-3xl font-black tracking-tight theme-text-main mt-0.5">เลือกซื้อตามประเภท</h2>
                    </div>

                    <!-- Search Input for Mobile/Tablet -->
                    <div class="relative w-full sm:w-72">
                        <i data-lucide="search" class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
                        <input type="text" id="search-input" oninput="handleSearch(this.value)" placeholder="ค้นหาสินค้า เช่น เลเซอร์, ยาง..." class="w-full theme-input border rounded-xl pl-9 pr-3 py-2 text-xs font-medium focus:ring-2 focus:ring-emerald-500">
                    </div>
                </div>

                <!-- Category Pills -->
                <div class="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none" id="categories-filter-container">
                    <button onclick="filterCategory('all')" class="cat-pill active px-4 py-2 rounded-xl bg-emerald-500 text-white font-bold text-xs shadow-md shadow-emerald-500/20 flex-shrink-0 cursor-pointer">
                        ทั้งหมด
                    </button>
                    <button onclick="filterCategory('slingshot')" class="cat-pill px-4 py-2 rounded-xl theme-card-subtle theme-text-main hover:text-emerald-400 border theme-border font-bold text-xs transition-all flex-shrink-0 cursor-pointer">
                        🎯 หนังสติ๊กยุทธวิธี
                    </button>
                    <button onclick="filterCategory('rubber')" class="cat-pill px-4 py-2 rounded-xl theme-card-subtle theme-text-main hover:text-emerald-400 border theme-border font-bold text-xs transition-all flex-shrink-0 cursor-pointer">
                        ⚡ ยางแบนเกรด A
                    </button>
                    <button onclick="filterCategory('ammo')" class="cat-pill px-4 py-2 rounded-xl theme-card-subtle theme-text-main hover:text-emerald-400 border theme-border font-bold text-xs transition-all flex-shrink-0 cursor-pointer">
                        🔘 ลูกเหล็ก
                    </button>
                    <button onclick="filterCategory('accessories')" class="cat-pill px-4 py-2 rounded-xl theme-card-subtle theme-text-main hover:text-emerald-400 border theme-border font-bold text-xs transition-all flex-shrink-0 cursor-pointer">
                        🎒 อุปกรณ์เสริม
                    </button>
                </div>

                <!-- Products Grid Container (SOOP Style Clean Cards) -->
                <div id="product-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
                    <!-- Loaded dynamically by JS -->
                </div>
            </section>

        </section>

        <!-- ================= VIEW 2: SINGLE-PAGE DIRECT CHECKOUT ================= -->
        <section id="view-checkout" class="hidden space-y-6">
            
            <div class="flex items-center justify-between">
                <button onclick="showCatalogView()" class="theme-card border hover:border-emerald-500 theme-text-main hover:text-emerald-400 text-xs font-bold px-4 py-2 rounded-xl flex items-center gap-1.5 transition-all cursor-pointer">
                    ← กลับไปหน้าสินค้า
                </button>
                <span class="text-xs font-black text-emerald-400 bg-emerald-500/10 border border-emerald-500/30 px-3 py-1 rounded-full">
                    ⚡ สั่งซื้อด่วน (Direct Checkout)
                </span>
            </div>

            <!-- Product Showcase Box -->
            <div class="grid grid-cols-1 md:grid-cols-12 gap-6 theme-card border rounded-3xl p-5 sm:p-8 shadow-md">
                <!-- Gallery Slider -->
                <div class="md:col-span-5 space-y-3">
                    <div class="relative w-full h-64 sm:h-72 theme-card-subtle rounded-2xl border theme-border p-3 flex items-center justify-center overflow-hidden cursor-pointer group" onclick="openGalleryModal()">
                        <img id="checkout-main-img" src="" alt="สินค้า" class="max-h-full max-w-full object-contain transition-transform duration-300 group-hover:scale-105">
                        <div class="absolute bottom-2.5 right-2.5 bg-black/70 backdrop-blur-md text-white text-[10px] px-2.5 py-1 rounded-lg flex items-center gap-1">
                            <span>🔍 ดูรูปใหญ่</span>
                        </div>
                    </div>
                    <div id="checkout-gallery-thumbs" class="grid grid-cols-4 gap-2"></div>
                </div>

                <!-- Product Details & Variant Select -->
                <div class="md:col-span-7 space-y-4 flex flex-col justify-between">
                    <div class="space-y-2">
                        <span id="checkout-prod-category" class="emerald-badge border text-[10px] px-2.5 py-0.5 rounded-full font-black uppercase inline-block">CATEGORY</span>
                        <h2 id="checkout-prod-title" class="text-xl sm:text-2xl font-black theme-text-main leading-snug">ชื่อสินค้า</h2>
                        <p id="checkout-prod-desc" class="text-xs sm:text-sm theme-text-muted leading-relaxed">รายละเอียดสินค้า</p>
                    </div>

                    <!-- Shopee Review Button in Checkout -->
                    <div class="bg-orange-500/10 p-3 rounded-2xl border border-orange-500/30 flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="text-base">⭐</span>
                            <span class="text-xs font-bold text-orange-400">ดูรีวิวผู้ใช้งานจริงบน Shopee</span>
                        </div>
                        <a id="checkout-shopee-review-btn" href="https://th.shp.ee/sdFv2cS1" target="_blank" class="bg-[#EE4D2D] hover:bg-[#d73211] text-white text-xs px-3.5 py-1.5 rounded-xl font-bold transition-all flex items-center gap-1 shadow-sm">
                            <span>เปิดดู ↗</span>
                        </a>
                    </div>

                    <!-- Variants Selection -->
                    <div class="space-y-2 pt-2 border-t theme-border">
                        <label class="text-xs font-bold theme-text-main">เลือกสเปก / ตัวเลือกสินค้า:</label>
                        <div id="checkout-variants-container" class="flex flex-wrap gap-2"></div>
                    </div>

                    <!-- Quantity -->
                    <div class="flex items-center justify-between pt-2 border-t theme-border">
                        <label class="text-xs font-bold theme-text-main">จำนวนที่ต้องการสั่งซื้อ:</label>
                        <div class="flex items-center gap-2 theme-card-subtle border theme-border rounded-xl p-1">
                            <button type="button" onclick="changeQuantity(-1)" class="w-8 h-8 theme-card border theme-border rounded-lg font-black theme-text-main hover:bg-emerald-500 hover:text-white transition-all cursor-pointer">-</button>
                            <span id="checkout-quantity-display" class="w-8 text-center font-black text-sm theme-text-main">1</span>
                            <button type="button" onclick="changeQuantity(1)" class="w-8 h-8 theme-card border theme-border rounded-lg font-black theme-text-main hover:bg-emerald-500 hover:text-white transition-all cursor-pointer">+</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Address Form & Payment -->
            <form onsubmit="event.preventDefault(); submitDirectOrder();" class="theme-card border rounded-3xl p-5 sm:p-8 space-y-6 shadow-md">
                
                <!-- Section 1: Customer Address -->
                <div class="space-y-4">
                    <h3 class="text-sm font-black theme-text-main flex items-center gap-2 border-b theme-border pb-3">
                        <span class="w-6 h-6 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs font-bold">1</span>
                        <span>ข้อมูลผู้รับและที่อยู่จัดส่งพัสดุ</span>
                    </h3>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs font-bold theme-text-main mb-1.5">ชื่อ-นามสกุล ผู้รับ *</label>
                            <input type="text" id="cust-name" required placeholder="เช่น คุณสมชาย ใจดี" class="w-full theme-input border rounded-xl px-3.5 py-2.5 text-xs focus:ring-2 focus:ring-emerald-500">
                        </div>
                        <div>
                            <label class="block text-xs font-bold theme-text-main mb-1.5">เบอร์โทรศัพท์ติดต่อ *</label>
                            <input type="tel" id="cust-phone" inputmode="numeric" pattern="[0-9]*" maxlength="10" oninput="this.value = this.value.replace(/[^0-9]/g, ''); onPhoneChange(this.value);" required placeholder="เช่น 0819998877" class="w-full theme-input border rounded-xl px-3.5 py-2.5 text-xs focus:ring-2 focus:ring-emerald-500">
                        </div>
                    </div>

                    <div>
                        <label class="block text-xs font-bold theme-text-main mb-1.5">บ้านเลขที่, หมู่, ซอย, ถนน *</label>
                        <input type="text" id="cust-address-line" required placeholder="เช่น 45/2 หมู่ 3 ซอยสุขุมวิท 10" class="w-full theme-input border rounded-xl px-3.5 py-2.5 text-xs focus:ring-2 focus:ring-emerald-500">
                    </div>

                    <div class="relative">
                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
                            <div>
                                <label class="block text-xs font-black text-emerald-400 mb-1.5">รหัสไปรษณีย์ (5 หลัก) *</label>
                                <input type="text" id="cust-postcode" maxlength="5" inputmode="numeric" pattern="[0-9]*" oninput="this.value = this.value.replace(/[^0-9]/g, ''); handlePostalCodeInput(this.value);" autocomplete="off" required placeholder="เช่น 10150" class="w-full theme-input border-2 border-emerald-500 rounded-xl px-3.5 py-2.5 text-xs font-mono font-bold text-emerald-400 focus:ring-2 focus:ring-emerald-500">
                            </div>
                            <div>
                                <label class="block text-xs font-bold theme-text-muted mb-1.5">ตำบล / แขวง</label>
                                <input type="text" id="cust-subdistrict" placeholder="ตำบล/แขวง" class="w-full theme-input border rounded-xl px-3.5 py-2.5 text-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-bold theme-text-muted mb-1.5">อำเภอ / เขต</label>
                                <input type="text" id="cust-district" placeholder="อำเภอ/เขต" class="w-full theme-input border rounded-xl px-3.5 py-2.5 text-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-bold theme-text-muted mb-1.5">จังหวัด</label>
                                <input type="text" id="cust-province" placeholder="จังหวัด" class="w-full theme-input border rounded-xl px-3.5 py-2.5 text-xs">
                            </div>
                        </div>

                        <!-- Autocomplete Suggestion Dropdown List -->
                        <div id="postal-autocomplete-box" class="absolute left-0 right-0 top-full mt-1.5 z-50 theme-card border-2 border-emerald-500 rounded-2xl shadow-2xl overflow-hidden hidden transition-all">
                            <div class="bg-emerald-500/10 px-3 py-2 border-b border-emerald-500/30 flex items-center justify-between text-xs font-bold text-emerald-400">
                                <span>📍 เลือกว่าอยู่ใน ตำบล/แขวง ใด:</span>
                                <button type="button" onclick="closePostalDropdown()" class="text-xs font-bold hover:opacity-75 bg-red-500/20 px-2 py-0.5 rounded-lg text-red-400">✕ ปิด</button>
                            </div>
                            <div id="postal-autocomplete-items" class="max-h-60 overflow-y-auto divide-y theme-border"></div>
                        </div>
                    </div>

                    <!-- Logistics Routing Banner -->
                    <div id="routing-banner" class="theme-card-subtle p-3.5 rounded-2xl border theme-border flex items-center justify-between text-xs">
                        <div class="flex items-center gap-2">
                            <span class="text-base">🚚</span>
                            <div>
                                <span class="theme-text-muted text-[11px] block">ขนส่งที่จัดสรรอัตโนมัติ:</span>
                                <strong id="routing-carrier-name" class="theme-text-main text-xs">SPX Express (Shopee Express)</strong>
                            </div>
                        </div>
                        <span id="carrier-fee-badge" class="font-bold text-xs text-emerald-400 bg-emerald-500/10 border border-emerald-500/30 px-3 py-1 rounded-xl">
                            ส่งฟรี (฿0)
                        </span>
                    </div>
                </div>

                <!-- Section 2: Payment Method -->
                <div class="space-y-4 pt-2 border-t theme-border">
                    <h3 class="text-sm font-black theme-text-main flex items-center gap-2">
                        <span class="w-6 h-6 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs font-bold">2</span>
                        <span>เลือกช่องทางการชำระเงิน</span>
                    </h3>

                    <div class="grid grid-cols-3 gap-3">
                        <!-- 1. PromptPay -->
                        <button type="button" onclick="setPaymentMethod('PROMPTPAY')" id="btn-pay-promptpay" class="p-3 rounded-2xl border-2 border-emerald-500 bg-emerald-500/10 text-emerald-400 text-xs font-bold flex flex-col items-center gap-1 transition-all text-center cursor-pointer">
                            <span class="text-base">📱</span>
                            <span class="text-xs font-black">พร้อมเพย์</span>
                            <span class="text-[10px] text-emerald-400">ฟรีค่าธรรมเนียม</span>
                        </button>

                        <!-- 2. COD (+3%) -->
                        <button type="button" onclick="setPaymentMethod('COD')" id="btn-pay-cod" class="p-3 rounded-2xl border theme-border theme-card-subtle theme-text-main text-xs font-bold flex flex-col items-center gap-1 transition-all text-center cursor-pointer">
                            <span class="text-base">💵</span>
                            <span class="text-xs">เก็บปลายทาง</span>
                            <span class="text-[10px] text-orange-400 font-bold">+3%</span>
                        </button>

                        <!-- 3. Store Credit -->
                        <button type="button" onclick="setPaymentMethod('STORE_CREDIT')" id="btn-pay-wallet" class="p-3 rounded-2xl border theme-border theme-card-subtle theme-text-main text-xs font-bold flex flex-col items-center gap-1 transition-all text-center cursor-pointer">
                            <span class="text-base">👛</span>
                            <span class="text-xs">เครดิต</span>
                            <span id="wallet-btn-bal" class="text-[10px] text-emerald-400">฿0.00</span>
                        </button>
                    </div>

                    <!-- Panel: PromptPay -->
                    <div id="panel-promptpay" class="theme-card-subtle border theme-border rounded-2xl p-5 space-y-4 text-center">
                        <div class="space-y-1">
                            <span class="text-xs theme-text-muted">สแกน PromptPay QR เพื่อชำระเงิน:</span>
                            <p id="promptpay-amount-display" class="text-3xl font-black text-emerald-400">฿0.00</p>
                        </div>
                        
                        <!-- PromptPay QR Code Image -->
                        <div class="flex justify-center py-1">
                            <img id="promptpay-qr-img" src="" alt="PromptPay QR Code" class="w-52 h-52 rounded-2xl border-2 theme-border shadow-md bg-white p-2">
                        </div>

                        <!-- Action: Download QR Code Button -->
                        <div class="flex justify-center max-w-sm mx-auto">
                            <button type="button" onclick="downloadPromptPayQR()" id="btn-download-qr" class="w-full bg-emerald-600 hover:bg-emerald-500 text-white text-xs px-4 py-2.5 rounded-xl font-bold transition-all shadow-md flex items-center justify-center gap-1.5 active:scale-95 cursor-pointer">
                                <span>📥 ดาวน์โหลดภาพ QR Code</span>
                            </button>
                        </div>

                        <!-- Account Info Box -->
                        <div class="theme-card p-3 rounded-xl border flex items-center justify-between text-xs max-w-sm mx-auto shadow-sm">
                            <div class="text-left">
                                <span class="theme-text-muted text-[10px] block font-medium">ชื่อบัญชี: สุเมธา แท่นธรรมโรจน์ (KBANK)</span>
                                <span class="font-mono font-bold theme-text-main text-xs sm:text-sm">061-537-2239</span>
                            </div>
                            <button type="button" onclick="copyPromptPay()" class="bg-emerald-500 hover:bg-emerald-400 text-white text-[11px] px-3 py-1.5 rounded-lg font-bold shadow-sm active:scale-95">คัดลอก</button>
                        </div>

                        <!-- Slip Upload Button -->
                        <div>
                            <label class="inline-block bg-emerald-500 hover:bg-emerald-400 text-white text-xs px-5 py-2.5 rounded-xl font-bold cursor-pointer shadow-md active:scale-95">
                                📎 แตะแนบสลิปโอนเงิน *
                                <input type="file" accept="image/*" onchange="handleSlipFile(this)" class="hidden">
                            </label>
                            <p id="slip-status-msg" class="text-xs text-emerald-400 font-bold mt-2 hidden"></p>
                        </div>
                    </div>

                    <!-- Panel: COD (+3%) -->
                    <div id="panel-cod" class="bg-orange-500/10 border border-orange-500/30 rounded-2xl p-5 space-y-3 hidden">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-2xl bg-orange-500 text-white flex items-center justify-center text-xl flex-shrink-0 shadow-md">💵</div>
                            <div>
                                <h4 class="font-bold text-xs sm:text-sm theme-text-main">บริการเก็บเงินปลายทาง (COD)</h4>
                                <p class="text-[11px] theme-text-muted">มีค่าบริการเก็บเงินปลายทาง +3%</p>
                            </div>
                        </div>
                        <div class="theme-card p-3 rounded-xl border theme-border text-xs space-y-1.5 theme-text-main">
                            <p class="flex justify-between"><span>ราคาสินค้า + ค่าส่ง:</span> <span id="cod-base-amount" class="font-bold">฿0.00</span></p>
                            <p class="flex justify-between text-orange-400"><span>ค่าบริการ COD (+3%):</span> <span id="cod-fee-amount" class="font-bold">+฿0.00</span></p>
                            <div class="border-t theme-border pt-1 flex justify-between font-black text-sm">
                                <span>ยอดชำระเมื่อรับพัสดุ:</span>
                                <span id="cod-total-amount" class="text-orange-400">฿0.00</span>
                            </div>
                        </div>
                    </div>

                    <!-- Panel: Store Credit -->
                    <div id="panel-wallet" class="theme-card-subtle border theme-border rounded-2xl p-5 space-y-3 hidden">
                        <div class="flex items-center justify-between">
                            <span class="text-xs theme-text-muted">ยอดเงินในเครดิตคงเหลือ:</span>
                            <span id="wallet-balance-big" class="text-base font-black text-emerald-400">฿0.00</span>
                        </div>
                    </div>
                </div>

                <!-- Summary Box -->
                <div class="theme-card-subtle p-4 rounded-2xl border theme-border space-y-2 text-xs theme-text-main">
                    <div class="flex justify-between">
                        <span class="theme-text-muted">รายการสินค้า:</span>
                        <span class="font-bold"><span id="summary-variant-name">รุ่นมาตรฐาน</span> (x<span id="summary-qty">1</span>)</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="theme-text-muted">ราคาสินค้ารวม:</span>
                        <span id="summary-subtotal" class="font-bold">฿0.00</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="theme-text-muted">ค่าจัดส่ง:</span>
                        <span id="summary-shipping" class="font-bold text-emerald-400">ฟรี (฿0)</span>
                    </div>
                    <div id="summary-cod-row" class="flex justify-between text-orange-400 font-bold hidden">
                        <span>ค่าบริการเก็บเงินปลายทาง (+3%):</span>
                        <span id="summary-cod-fee">+฿0.00</span>
                    </div>
                    <div class="border-t theme-border pt-2 flex justify-between text-base font-black">
                        <span>ยอดสุทธิที่ต้องชำระ:</span>
                        <span id="summary-total" class="text-emerald-400">฿0.00</span>
                    </div>
                </div>

                <!-- Submit Button -->
                <button type="submit" id="submit-btn-text" class="w-full bg-emerald-500 hover:bg-emerald-400 text-white font-black py-4 rounded-2xl text-sm sm:text-base shadow-lg shadow-emerald-500/25 transition-all active:scale-95 cursor-pointer">
                    ⚡ สั่งซื้อและชำระเงิน
                </button>
            </form>
        </section>

    </main>

    <!-- ============= FOOTER (SOOPTHAILAND STYLE) ============= -->
    <footer class="theme-header border-t theme-border mt-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-8">
                <!-- Brand -->
                <div class="space-y-3">
                    <div class="flex items-center gap-2">
                        <span class="inline-flex h-8 items-center justify-center rounded-xl bg-emerald-500 px-3 text-xs font-black text-white">
                            GOODSTONE
                        </span>
                        <span class="text-xs font-bold theme-text-muted">ร้านหนังสติ๊กยุทธวิธี</span>
                    </div>
                    <p class="text-xs theme-text-muted leading-relaxed">
                        ศูนย์รวมหนังสติ๊กยุทธวิธีเกรดพรีเมียม สแตนเลส CNC เลเซอร์ช่วยเล็ง ยางแบน และอุปกรณ์ครบวงจร ของแท้ 100%
                    </p>
                </div>

                <!-- Quick Links -->
                <div class="space-y-3">
                    <h4 class="text-xs font-black uppercase tracking-widest text-emerald-400">หมวดสินค้า</h4>
                    <ul class="space-y-2 text-xs theme-text-muted">
                        <li><button onclick="filterCategory('slingshot'); showCatalogView();" class="hover:text-emerald-400 transition-colors">🎯 หนังสติ๊กยุทธวิธี</button></li>
                        <li><button onclick="filterCategory('rubber'); showCatalogView();" class="hover:text-emerald-400 transition-colors">⚡ ยางแบนเกรด A</button></li>
                        <li><button onclick="filterCategory('ammo'); showCatalogView();" class="hover:text-emerald-400 transition-colors">🔘 ลูกเหล็กคุณภาพสูง</button></li>
                        <li><a href="track.html" class="hover:text-emerald-400 transition-colors">🚚 ตรวจสอบพัสดุ</a></li>
                    </ul>
                </div>

                <!-- Contact -->
                <div class="space-y-3">
                    <h4 class="text-xs font-black uppercase tracking-widest text-emerald-400">ติดต่อและชำระเงิน</h4>
                    <ul class="space-y-2 text-xs theme-text-muted">
                        <li class="flex items-center gap-2"><span>📞</span><span class="font-bold text-white">061-537-2239</span></li>
                        <li class="flex items-center gap-2"><span>💬</span><a href="https://lin.ee/qX9RSdN" target="_blank" class="hover:underline text-emerald-400">LINE Official: @goodstone</a></li>
                        <li class="flex items-center gap-2"><span>💳</span><span>PromptPay: 061-537-2239 (0%)</span></li>
                        <li class="flex items-center gap-2"><span>💵</span><span>เก็บเงินปลายทาง (COD +3%)</span></li>
                    </ul>
                </div>
            </div>

            <!-- Footer Bottom Bar -->
            <div class="mt-8 pt-6 border-t theme-border flex flex-col sm:flex-row items-center justify-between gap-3 text-xs theme-text-muted">
                <span>© 2026 GOODSTONE. สงวนลิขสิทธิ์ทุกประการ.</span>
                <div class="flex items-center gap-4">
                    <span>🔒 ปลอดภัย 100%</span>
                    <span>📦 ส่งทั่วไทย 24 ชม.</span>
                </div>
            </div>
        </div>
    </footer>

    <!-- FULLSCREEN GALLERY LIGHTBOX MODAL -->
    <div id="gallery-modal" class="fixed inset-0 z-50 flex items-center justify-center p-3 bg-black/80 backdrop-blur-sm hidden" onclick="closeGalleryModal()">
        <div class="relative max-w-2xl max-h-[85vh] p-2 theme-card rounded-3xl border shadow-2xl" onclick="event.stopPropagation()">
            <button onclick="closeGalleryModal()" class="absolute -top-3 -right-3 w-8 h-8 rounded-full bg-emerald-500 text-white font-bold flex items-center justify-center shadow-lg cursor-pointer">✕</button>
            <img id="gallery-modal-img" src="" class="max-h-[75vh] max-w-full rounded-2xl object-contain mx-auto">
        </div>
    </div>

    <!-- JAVASCRIPT ENGINE -->
    <script>
        const DEFAULT_PRODUCTS = [{"id": "PROD-001", "name": "หนังสติ๊กอัลลอยด์ยุทธวิธี พร้อมเลเซอร์ช่วยเล็งและระดับน้ำ", "category": "slingshot", "price": 390.0, "stock": 35, "variants": [{"name": "ครบชุดพร้อมเลเซอร์ + ยาง 2 เส้น", "price": 390.0, "stock": 20}, {"name": "เฉพาะตัวด้ามหนังสติ๊ก", "price": 290.0, "stock": 10}, {"name": "ชุดโปร (ด้าม+เลเซอร์+ยาง 5 เส้น+ลูก 500 นัด)", "price": 550.0, "stock": 5}], "image_file": "https://lh3.googleusercontent.com/d/1u5fhZmlGqWrCY7CJpGSe5xHQqbt6ArDa", "fallback_image": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0MDAgMzAwIiB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCI+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJtZXRhbCIgeDE9IjAlIiB5MT0iMCUiIHgyPSIxMDAlIiB5Mj0iMTAwJSI+PHN0b3Agb2Zmc2V0PSIwJSIgc3RvcC1jb2xvcj0iIzQ3NTU2OSIvPjxzdG9wIG9mZnNldD0iNTAlIiBzdG9wLWNvbG9yPSIjMWUyOTNiIi8+PHN0b3Agb2Zmc2V0PSIxMDAlIiBzdG9wLWNvbG9yPSIjMGYxNzJhIi8+PC9saW5lYXJHcmFkaWVudD48L2RlZnM+PHJlY3Qgd2lkdGg9IjQwMCIgaGVpZ2h0PSIzMDAiIGZpbGw9IiMwZjE3MmEiLz48Y2lyY2xlIGN4PSIyMDAiIGN5PSIxNTAiIHI9IjExMCIgZmlsbD0iIzFlMjkzYiIgb3BhY2l0eT0iMC42Ii8+PHBhdGggZD0iTTEyMCA3MCBRMTQwIDE2MCAxODAgMTgwIEwxODAgMjcwIFEyMDAgMjg1IDIyMCAyNzAgTDIyMCAxODAgUTI2MCAxNjAgMjgwIDcwIEwyNTAgNjUgUTIzNSAxMzAgMjAwIDE0NSBRMTY1IDEzMCAxNTAgNjUgWiIgZmlsbD0idXJsKCNtZXRhbCkiIHN0cm9rZT0iI2Y1OWUwYiIgc3Ryb2tlLXdpZHRoPSIzIi8+PHJlY3QgeD0iMTg1IiB5PSIxODAiIHdpZHRoPSIzMCIgaGVpZ2h0PSI4NSIgcng9IjUiIGZpbGw9IiMzMzQxNTUiIHN0cm9rZT0iIzQ3NTU2OSIgc3Ryb2tlLXdpZHRoPSIyIi8+PGxpbmUgeDE9IjE4NSIgeTE9IjIwMCIgeDI9IjIxNSIgeTI9IjIwMCIgc3Ryb2tlPSIjMGYxNzJhIiBzdHJva2Utd2lkdGg9IjIiLz48bGluZSB4MT0iMTg1IiB5MT0iMjIwIiB4Mj0iMjE1IiB5Mj0iMjIwIiBzdHJva2U9IiMwZjE3MmEiIHN0cm9rZS13aWR0aD0iMiIvPjxsaW5lIHgxPSIxODUiIHkxPSIyNDAiIHgyPSIyMTVsIHkyPSIyNDAiIHN0cm9rZT0iIzBmMTcyYSIgc3Ryb2tlLXdpZHRoPSIyIi8+PHJlY3QgeD0iMTEwIiB5PSI1NSIgd2lkdGg9IjM1IiBoZWlnaHQ9IjIwIiByeD0iMyIgZmlsbD0iI2Y1OWUwYiIvPjxyZWN0IHg9IjI1NSIgeT0iNTUiIHdpZHRoPSIzNSIgaGVpZ2h0PSIyMCIgcng9IjMiIGZpbGw9IiNmNTllMGIiLz48Y2lyY2xlIGN4PSIxMjciIGN5PSI2NSIgcj0iNCIgZmlsbD0iIzEwYjk4MSIvPjxjaXJjbGUgY3g9IjI3MiIgY3k9IjY1IiByPSI0IiBmaWxsPSIjMTBiOTgxIi8+PHJlY3QgeD0iMTAwIiB5PSI3OCIgd2lkdGg9IjE4IiBoZWlnaHQ9IjMwIiByeD0iNCIgZmlsbD0iI2VmNDQ0NCIvPjxjaXJjbGUgY3g9IjEwOSIgY3k9IjkzIiByPSIzIiBmaWxsPSIjZmVjYWNhIi8+PGxpbmUgeDE9IjEwOSIgeTE9IjkzIiB4Mj0iMzAiIHkyPSI5MyIgc3Ryb2tlPSIjZWY0NDQ0IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1kYXNoYXJyYXk9IjQsNCIvPjxwYXRoIGQ9Ik0xMjUgNTUgUTE2MCAyMCAyMDAgMjUgUTI0MCAyMCAyNzUgNTUiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2ZiYmYyNCIgc3Ryb2tlLXdpZHRoPSI2IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz48cmVjdCB4PSIxODUiIHk9IjE4IiB3aWR0aD0iMzAiIGhlaWdodD0iMTQiIHJ4PSIzIiBmaWxsPSIjMWUyOTNiIiBzdHJva2U9IiNmNTllMGIiIHN0cm9rZS13aWR0aD0iMSIvPjx0ZXh0IHg9IjIwMCIgeT0iMjgiIGZvbnQtc2l6ZT0iOCIgZmlsbD0iI2ZmZiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPlRBQ1RJQ0FMPC90ZXh0Pjx0ZXh0IHg9IjIwMCIgeT0iMjg1IiBmb250LXNpemU9IjEzIiBmaWxsPSIjZmJiZjI0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmb250LXdlaWdodD0iYm9sZCIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiPuC4q+C4meC4seC4h+C4quC4leC4tOC5iuC4geC4reC4seC4peC4peC4reC4ouC4lOC5jOC4ouC4uOC4l+C4mOC4p+C4tOC4mOC4tSDguYDguKXguYDguIvguK3guKPguYzguIrguYjguKfguKLguYDguKXguYfguIc8L3RleHQ+PC9zdmc+", "description": "ด้ามจับอัลลอยด์ แข็งแรงทนทาน น้ำหนักกระชับมือ พร้อมศูนย์เล็งเลเซอร์และระดับน้ำ ช่วยจับเป้าแม่นยำ", "images": [{"file": "https://lh3.googleusercontent.com/d/1u5fhZmlGqWrCY7CJpGSe5xHQqbt6ArDa", "drive_id": "1u5fhZmlGqWrCY7CJpGSe5xHQqbt6ArDa", "name": "ภาพรวมหนังสติ๊กยุทธวิธี (มุมตรง)", "fallback": ""}, {"file": "https://lh3.googleusercontent.com/d/13Q49odl1sJZqAPlL85TG58Exa3C3SPPu", "drive_id": "13Q49odl1sJZqAPlL85TG58Exa3C3SPPu", "name": "ศูนย์เล็งเลเซอร์และระดับน้ำ", "fallback": ""}], "shopee_affiliate_url": "https://th.shp.ee/sdFv2cS1"}, {"id": "PROD-002", "name": "หนังสติ๊กสแตนเลส CNC ด้ามไม้ประกบเกรดพรีเมียม", "category": "slingshot", "price": 550.0, "stock": 20, "variants": [{"name": "ด้ามไม้มะค่าขัดเงา", "price": 550.0, "stock": 10}, {"name": "ด้ามไม้พะยูงดำ", "price": 550.0, "stock": 6}, {"name": "ชุดโปรพร้อมยางแบน 5 เส้น", "price": 650.0, "stock": 4}], "image_file": "https://lh3.googleusercontent.com/d/1cVe2KNdCNGARNMsbHqcMjRATBm1-c8xk", "fallback_image": "", "description": "สแตนเลส 304 กลึง CNC สวยงาม ไร้สนิม ประกบไม้แท้เนื้อแข็ง จับถนัดมือ ยิงนิ่ง แม่นยำสูง", "images": [{"file": "https://lh3.googleusercontent.com/d/1cVe2KNdCNGARNMsbHqcMjRATBm1-c8xk", "drive_id": "1cVe2KNdCNGARNMsbHqcMjRATBm1-c8xk", "name": "หนังสติ๊กเหล็กเลเซอร์ด้ามจับไม้โอ๊ค", "fallback": ""}], "shopee_affiliate_url": "https://th.shp.ee/sdFv2cS1"}];

        let products = DEFAULT_PRODUCTS;
        let selectedCategory = "all";
        let selectedProduct = null;
        let selectedVariantIdx = 0;
        let quantity = 1;
        let paymentMethod = "PROMPTPAY";
        let slipImageBase64 = "";
        let currentGalleryIdx = 0;
        let userWallet = { balance: 530, total_topup: 500, total_bonus: 30 };

        function init() {
            lucide.createIcons();
            loadSavedTheme();
            fetchProducts();
        }

        function toggleTheme() {
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
        }

        function loadSavedTheme() {
            const saved = localStorage.getItem("goodstone_theme") || "dark";
            document.body.setAttribute("data-theme", saved);
            if (saved === "dark") {
                document.documentElement.classList.add("dark");
            } else {
                document.documentElement.classList.remove("dark");
            }
        }

        function fetchProducts() {
            fetch("data.json")
                .then(res => res.json())
                .then(data => {
                    if (data && data.products && data.products.length > 0) {
                        products = data.products;
                    }
                    renderCatalogGrid();
                })
                .catch(() => renderCatalogGrid());
        }

        // ================= SOOP-STYLE CATALOG GRID RENDERING =================
        function renderCatalogGrid() {
            const container = document.getElementById("product-grid");
            if (!container) return;
            container.innerHTML = "";

            const searchVal = (document.getElementById("search-input")?.value || document.getElementById("header-search-input")?.value || "").toLowerCase().trim();

            const filtered = products.filter(p => {
                const matchCat = (selectedCategory === "all" || p.category === selectedCategory);
                const matchSearch = !searchVal || p.name.toLowerCase().includes(searchVal) || (p.description || "").toLowerCase().includes(searchVal);
                return matchCat && matchSearch;
            });

            if (filtered.length === 0) {
                container.innerHTML = `<div class="col-span-full py-16 text-center theme-text-muted text-sm">ไม่พบสินค้าที่ค้นหา ลองเปลี่ยนคำค้นหานะครับ</div>`;
                return;
            }

            filtered.forEach((p, idx) => {
                const mainImg = p.image_file || p.fallback_image;
                const minPrice = (p.variants && p.variants.length > 0)
                    ? Math.min(...p.variants.map(v => Number(v.price) || p.price))
                    : Number(p.price) || 390;

                const shopeeUrl = p.shopee_affiliate_url || "https://th.shp.ee/sdFv2cS1";

                const isBestseller = idx < 2;
                const badgeText = p.stock <= 0 ? "หมด" : (isBestseller ? "🔥 ขายดี" : "✅ พร้อมส่ง");
                const badgeClass = p.stock <= 0 ? "bg-slate-700 text-slate-300" : (isBestseller ? "bg-[#EE4D2D] text-white" : "emerald-badge font-bold");

                const card = document.createElement("div");
                card.className = "soop-product-card theme-card rounded-2xl border overflow-hidden shadow-sm flex flex-col justify-between group";
                card.innerHTML = `
                    <div>
                        <!-- Image Container (Square Aspect Ratio like SOOP) -->
                        <div onclick="openProductDirectCheckout('${p.id}')" class="relative w-full aspect-square theme-card-subtle p-4 flex items-center justify-center overflow-hidden cursor-pointer border-b theme-border">
                            <img src="${mainImg}" onerror="this.onerror=null; this.src='${p.fallback_image}';" loading="lazy" alt="${p.name}" class="max-h-full max-w-full object-contain transition-transform duration-300 group-hover:scale-105">
                            <span class="absolute top-3 left-3 text-[10px] px-2.5 py-0.5 rounded-full font-bold uppercase ${badgeClass}">
                                ${badgeText}
                            </span>
                            <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
                                <span class="bg-emerald-500 text-white text-xs font-bold px-3.5 py-1.5 rounded-xl shadow-lg">⚡ แตะซื้อด่วน</span>
                            </div>
                        </div>

                        <!-- Card Body -->
                        <div class="p-4 space-y-2">
                            <span class="text-[10px] font-bold uppercase tracking-wider text-emerald-400 block">${p.category}</span>
                            <h3 onclick="openProductDirectCheckout('${p.id}')" class="font-bold text-sm theme-text-main line-clamp-2 hover:text-emerald-400 cursor-pointer transition-colors leading-snug">
                                ${p.name}
                            </h3>
                            <p class="text-xs theme-text-muted line-clamp-1">${p.description || "หนังสติ๊กยุทธวิธีเกรดพรีเมียม"}</p>
                        </div>
                    </div>

                    <!-- Price & Action Button -->
                    <div class="p-4 pt-0 space-y-3">
                        <div class="flex items-baseline justify-between border-t theme-border pt-3">
                            <div>
                                <span class="text-[10px] theme-text-muted block font-medium">เริ่มต้น</span>
                                <span class="text-lg font-black text-emerald-400">฿${minPrice.toLocaleString()}</span>
                            </div>
                            <span class="text-[11px] theme-text-muted font-bold">สต็อก: ${p.stock}</span>
                        </div>

                        <button onclick="openProductDirectCheckout('${p.id}')" ${p.stock <= 0 ? 'disabled' : ''} class="w-full ${p.stock <= 0 ? 'bg-slate-700 cursor-not-allowed' : 'bg-emerald-500 hover:bg-emerald-400 cursor-pointer shadow-md shadow-emerald-500/20 active:scale-95'} text-white py-2.5 rounded-xl font-bold text-xs transition-all flex items-center justify-center gap-1.5">
                            <span>${p.stock <= 0 ? '⚠️ สินค้าหมด' : '⚡ สั่งซื้อด่วน'}</span>
                        </button>
                    </div>
                `;
                container.appendChild(card);
            });
        }

        function filterCategory(cat) {
            selectedCategory = cat;
            document.querySelectorAll(".cat-pill").forEach(el => {
                el.className = "cat-pill px-4 py-2 rounded-xl theme-card-subtle theme-text-main hover:text-emerald-400 border theme-border font-bold text-xs transition-all flex-shrink-0 cursor-pointer";
            });
            event.target.className = "cat-pill active px-4 py-2 rounded-xl bg-emerald-500 text-white font-bold text-xs shadow-md shadow-emerald-500/20 flex-shrink-0 cursor-pointer";
            renderCatalogGrid();
        }

        function handleSearch(val) {
            renderCatalogGrid();
        }

        function showCatalogView() {
            document.getElementById("view-catalog").classList.remove("hidden");
            document.getElementById("view-checkout").classList.add("hidden");
            window.scrollTo({ top: 0, behavior: "smooth" });
        }

        function openProductDirectCheckout(productId) {
            const found = products.find(p => p.id === productId);
            if (found) {
                selectedProduct = found;
                selectedVariantIdx = 0;
                quantity = 1;
                renderProductCheckoutDetail();
                updateCalculations();
                document.getElementById("view-catalog").classList.add("hidden");
                document.getElementById("view-checkout").classList.remove("hidden");
                window.scrollTo({ top: 0, behavior: "smooth" });
            }
        }

        function renderProductCheckoutDetail() {
            if (!selectedProduct) return;
            const p = selectedProduct;
            const mainImg = p.image_file || p.fallback_image;
            document.getElementById("checkout-main-img").src = mainImg;
            document.getElementById("checkout-prod-category").innerText = p.category;
            document.getElementById("checkout-prod-title").innerText = p.name;
            document.getElementById("checkout-prod-desc").innerText = p.description || "หนังสติ๊กยุทธวิธีเกรดพรีเมียม";

            // Render Variants
            const variantsContainer = document.getElementById("checkout-variants-container");
            variantsContainer.innerHTML = "";
            const vars = (p.variants && p.variants.length > 0) ? p.variants : [{ name: "รุ่นมาตรฐาน", price: p.price }];

            vars.forEach((v, idx) => {
                const pill = document.createElement("button");
                pill.type = "button";
                pill.className = `px-3.5 py-2 rounded-xl text-xs font-bold border-2 transition-all cursor-pointer ${idx === selectedVariantIdx ? 'border-emerald-500 bg-emerald-500/10 text-emerald-400' : 'theme-border theme-card-subtle theme-text-main'}`;
                pill.innerHTML = `${v.name} (฿${Number(v.price).toLocaleString()})`;
                pill.onclick = () => {
                    selectedVariantIdx = idx;
                    renderProductCheckoutDetail();
                    updateCalculations();
                };
                variantsContainer.appendChild(pill);
            });

            document.getElementById("checkout-quantity-display").innerText = quantity;
        }

        function changeQuantity(amt) {
            quantity = Math.max(1, quantity + amt);
            document.getElementById("checkout-quantity-display").innerText = quantity;
            updateCalculations();
        }

        function updateCalculations() {
            if (!selectedProduct) return;
            const p = selectedProduct;
            const vars = (p.variants && p.variants.length > 0) ? p.variants : [{ name: "รุ่นมาตรฐาน", price: p.price }];
            const activeV = vars[selectedVariantIdx] || vars[0];
            const unitPrice = Number(activeV.price) || 390;
            const subtotal = unitPrice * quantity;
            const isFreeShipping = (subtotal >= 200);
            const shippingCost = isFreeShipping ? 0 : 25;
            const baseTotal = subtotal + shippingCost;
            const codFee = (paymentMethod === "COD") ? Number((baseTotal * 0.03).toFixed(2)) : 0;
            const total = Number((baseTotal + codFee).toFixed(2));

            document.getElementById("summary-variant-name").innerText = activeV.name;
            document.getElementById("summary-qty").innerText = quantity;
            document.getElementById("summary-subtotal").innerText = `฿${subtotal.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("summary-shipping").innerText = isFreeShipping ? "ฟรี (฿0)" : `฿${shippingCost.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("summary-total").innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("promptpay-amount-display").innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            
            const submitBtn = document.getElementById("submit-btn-text");
            if (submitBtn) {
                submitBtn.innerText = paymentMethod === "COD" 
                    ? `📦 สั่งซื้อแบบเก็บเงินปลายทาง (฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})})`
                    : `⚡ สั่งซื้อและชำระเงิน (฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})})`;
            }

            // QR Code
            const qrImg = document.getElementById("promptpay-qr-img");
            if (qrImg) {
                const ppPayload = generatePromptPayQR(total);
                qrImg.src = `https://api.qrserver.com/v1/create-qr-code/?size=260x260&margin=12&data=${encodeURIComponent(ppPayload)}`;
            }
        }

        function generatePromptPayQR(amount) {
            const targetPhone = "0615372239";
            let formattedPhone = targetPhone.replace(/[^0-9]/g, "");
            if (formattedPhone.startsWith("0")) formattedPhone = "66" + formattedPhone.substring(1);
            const phoneTargetStr = "0112" + formattedPhone;
            const amountStr = amount.toFixed(2);
            const amountLength = ("0" + amountStr.length).slice(-2);
            const amountTagStr = "54" + amountLength + amountStr;
            const rawPayloadWithoutCRC = "00020101021229370016A000000677010111" + phoneTargetStr + "5802TH" + amountTagStr + "53037646304";

            function crc16Hex(str) {
                let crc = 0xFFFF;
                for (let i = 0; i < str.length; i++) {
                    crc ^= str.charCodeAt(i) << 8;
                    for (let j = 0; j < 8; j++) {
                        if ((crc & 0x8000) !== 0) crc = ((crc << 1) ^ 0x1021) & 0xFFFF;
                        else crc = (crc << 1) & 0xFFFF;
                    }
                }
                return ("000" + crc.toString(16).toUpperCase()).slice(-4);
            }
            return rawPayloadWithoutCRC + crc16Hex(rawPayloadWithoutCRC);
        }

        function setPaymentMethod(method) {
            paymentMethod = method;
            const btnPP = document.getElementById("btn-pay-promptpay");
            const btnCOD = document.getElementById("btn-pay-cod");
            const btnW = document.getElementById("btn-pay-wallet");
            const panelPP = document.getElementById("panel-promptpay");
            const panelCOD = document.getElementById("panel-cod");
            const panelW = document.getElementById("panel-wallet");

            const inactiveCls = "p-3 rounded-2xl border theme-border theme-card-subtle theme-text-main text-xs font-bold flex flex-col items-center gap-1 transition-all text-center cursor-pointer";
            const activeCls = "p-3 rounded-2xl border-2 border-emerald-500 bg-emerald-500/10 text-emerald-400 text-xs font-bold flex flex-col items-center gap-1 transition-all text-center cursor-pointer";

            if (btnPP) btnPP.className = inactiveCls;
            if (btnCOD) btnCOD.className = inactiveCls;
            if (btnW) btnW.className = inactiveCls;

            if (panelPP) panelPP.classList.add("hidden");
            if (panelCOD) panelCOD.classList.add("hidden");
            if (panelW) panelW.classList.add("hidden");

            if (method === "PROMPTPAY") {
                if (btnPP) btnPP.className = activeCls;
                if (panelPP) panelPP.classList.remove("hidden");
            } else if (method === "COD") {
                if (btnCOD) btnCOD.className = activeCls;
                if (panelCOD) panelCOD.classList.remove("hidden");
            } else if (method === "STORE_CREDIT") {
                if (btnW) btnW.className = activeCls;
                if (panelW) panelW.classList.remove("hidden");
            }
            updateCalculations();
        }

        function downloadPromptPayQR() {
            const qrImg = document.getElementById("promptpay-qr-img");
            if (!qrImg || !qrImg.src) return;
            const activeV = (selectedProduct.variants && selectedProduct.variants[selectedVariantIdx]) ? selectedProduct.variants[selectedVariantIdx] : { price: selectedProduct.price };
            const subtotal = activeV.price * quantity;
            const total = subtotal + (subtotal >= 200 ? 0 : 25);
            const fileName = `PromptPay_GOODSTONE_฿${total.toFixed(2)}.png`;

            fetch(qrImg.src)
                .then(res => res.blob())
                .then(blob => {
                    const blobUrl = window.URL.createObjectURL(blob);
                    const link = document.createElement("a");
                    link.href = blobUrl;
                    link.download = fileName;
                    document.body.appendChild(link);
                    link.click();
                    window.URL.revokeObjectURL(blobUrl);
                    document.body.removeChild(link);
                });
        }

        function onPhoneChange(val) {
            const clean = (val || "").replace(/[^0-9]/g, "");
            if (clean.length >= 9) {
                document.getElementById("user-wallet-display").innerText = `฿${userWallet.balance.toLocaleString()}`;
                updateCalculations();
            }
        }

        function handleSlipFile(input) {
            const file = input.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = function(e) {
                slipImageBase64 = e.target.result;
                const msgBox = document.getElementById("slip-status-msg");
                if (msgBox) {
                    msgBox.classList.remove("hidden");
                    msgBox.innerText = "✅ แนบสลิปโอนเงินเรียบร้อยแล้ว";
                }
            };
            reader.readAsDataURL(file);
        }

        function copyPromptPay() {
            navigator.clipboard.writeText("0615372239").then(() => {
                alert("คัดลอกเลขพร้อมเพย์ 061-537-2239 แล้วครับ!");
            });
        }

        // THAI POSTAL AUTOCOMPLETE
        function handlePostalCodeInput(val) {
            const clean = (val || "").replace(/[^0-9]/g, "");
            const box = document.getElementById("postal-autocomplete-box");
            const itemsBox = document.getElementById("postal-autocomplete-items");
            if (!box || !itemsBox) return;

            if (clean.length === 5) {
                const found = (window.FULL_THAI_POSTAL_DB && window.FULL_THAI_POSTAL_DB[clean]) || THAI_POSTAL_DB[clean];
                if (found && found.length > 0) {
                    itemsBox.innerHTML = "";
                    found.forEach(item => {
                        const row = document.createElement("div");
                        row.className = "p-3 hover:bg-emerald-500/10 cursor-pointer text-xs font-bold theme-text-main flex justify-between transition-colors";
                        row.innerHTML = `<span>📍 ต.${item.subdistrict} > อ.${item.district} > จ.${item.province}</span><span class="text-emerald-400">เลือก ✓</span>`;
                        row.onclick = () => {
                            document.getElementById("cust-subdistrict").value = item.subdistrict;
                            document.getElementById("cust-district").value = item.district;
                            document.getElementById("cust-province").value = item.province;
                            closePostalDropdown();
                        };
                        itemsBox.appendChild(row);
                    });
                    box.classList.remove("hidden");
                }
            } else {
                box.classList.add("hidden");
            }
        }

        function closePostalDropdown() {
            const box = document.getElementById("postal-autocomplete-box");
            if (box) box.classList.add("hidden");
        }

        function submitDirectOrder() {
            const name = document.getElementById("cust-name").value.trim();
            const phone = document.getElementById("cust-phone").value.trim();
            const addr = document.getElementById("cust-address-line").value.trim();
            const postcode = document.getElementById("cust-postcode").value.trim();
            const subdistrict = document.getElementById("cust-subdistrict").value.trim();
            const district = document.getElementById("cust-district").value.trim();
            const province = document.getElementById("cust-province").value.trim();

            if (!name || !phone || !addr || !postcode) {
                alert("กรุณากรอกข้อมูลชื่อ, เบอร์โทร, และที่อยู่ให้ครบถ้วนครับ");
                return;
            }

            const activeV = (selectedProduct.variants && selectedProduct.variants[selectedVariantIdx]) ? selectedProduct.variants[selectedVariantIdx] : { name: "รุ่นมาตรฐาน", price: selectedProduct.price };
            const subtotal = activeV.price * quantity;
            const isFree = subtotal >= 200;
            const shipCost = isFree ? 0 : 25;
            const baseTotal = subtotal + shipCost;
            const codFee = paymentMethod === "COD" ? Number((baseTotal * 0.03).toFixed(2)) : 0;
            const grandTotal = Number((baseTotal + codFee).toFixed(2));

            const newOrder = {
                id: "ORD-" + Math.floor(100000 + Math.random() * 900000),
                created_at: new Date().toISOString(),
                customer: { name, phone, addressLine: addr, postal_code: postcode, subdistrict, district, province },
                items: [{ product_id: selectedProduct.id, name: selectedProduct.name, variant: activeV.name, price: activeV.price, qty: quantity }],
                total_amount: grandTotal,
                payment_method: paymentMethod,
                shipping_provider: "SPX Express",
                tracking_number: "TH" + Math.floor(100000000 + Math.random() * 900000000)
            };

            const existing = JSON.parse(localStorage.getItem("goodstone_orders") || "[]");
            existing.unshift(newOrder);
            localStorage.setItem("goodstone_orders", JSON.stringify(existing));

            alert(`🎉 สั่งซื้อสำเร็จ! รหัสคำสั่งซื้อ: ${newOrder.id}\nเลขพัสดุ SPX Express: ${newOrder.tracking_number}`);
            window.location.href = "track.html";
        }

        function openGalleryModal() {
            if (!selectedProduct) return;
            const imgs = (selectedProduct.images && selectedProduct.images.length > 0) ? selectedProduct.images : [{ file: selectedProduct.image_file || selectedProduct.fallback_image }];
            document.getElementById("gallery-modal-img").src = imgs[0].file;
            document.getElementById("gallery-modal").classList.remove("hidden");
        }

        function closeGalleryModal() {
            document.getElementById("gallery-modal").classList.add("hidden");
        }

        window.onload = init;
    </script>
</body>
</html>
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(full_soop_index_html)

print("Rebuilt index.html to match SOOPTHAILAND UI/UX layout 100%!")
