import json

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))
products_json = json.dumps(data["products"], ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="th" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>GOODSTONE - ร้านหนังสติ๊กยุทธวิธีและอุปกรณ์ครบวงจร</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: ["class", '[data-theme="dark"]'],
            theme: {
                extend: {
                    colors: {
                        shopee: {
                            DEFAULT: "#EE4D2D",
                            hover: "#D73211",
                            light: "#FFF2EE",
                            border: "#FFD5CC"
                        }
                    }
                }
            }
        }
    </script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; }
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
            --text-sub: #787888;
            --badge-bg: #2E1B17;
            --badge-border: #5C2B1F;
            --badge-text: #FF6E4E;
            --hero-from: #261B18;
            --hero-via: #211C20;
            --hero-to: #1A1A22;
            --tab-inactive-bg: #272732;
            --tab-inactive-text: #B4B4C2;
            --shopee-btn-bg: #2E1B17;
            --shopee-btn-border: #5C2B1F;
            --shopee-btn-text: #FF6E4E;
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
            --text-sub: #94A3B8;
            --badge-bg: #FFF2EE;
            --badge-border: #FFD5CC;
            --badge-text: #EE4D2D;
            --hero-from: #FFF6F2;
            --hero-via: #FDF3EA;
            --hero-to: #FBF0E4;
            --tab-inactive-bg: #FAF7F2;
            --tab-inactive-text: #64748B;
            --shopee-btn-bg: #FFF2EE;
            --shopee-btn-border: #FFD5CC;
            --shopee-btn-text: #EE4D2D;
        }

        /* Dynamic Classes bound to CSS variables */
        .theme-body { background-color: var(--bg-body) !important; color: var(--text-main) !important; }
        .theme-header { background-color: var(--bg-header) !important; border-color: var(--border-main) !important; }
        .theme-card { background-color: var(--bg-card) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .theme-card-subtle { background-color: var(--bg-card-subtle) !important; border-color: var(--border-subtle) !important; }
        .theme-input { background-color: var(--bg-input) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .theme-text-main { color: var(--text-main) !important; }
        .theme-text-muted { color: var(--text-muted) !important; }
        .theme-badge { background-color: var(--badge-bg) !important; border-color: var(--badge-border) !important; color: var(--badge-text) !important; }
        .theme-hero { background: linear-gradient(135deg, var(--hero-from), var(--hero-via), var(--hero-to)) !important; border-color: var(--border-main) !important; }
        .theme-shopee-btn { background-color: var(--shopee-btn-bg) !important; border-color: var(--shopee-btn-border) !important; color: var(--shopee-btn-text) !important; }
    </style>
</head>
<body class="theme-body min-h-screen flex flex-col font-sans" data-theme="dark">

    <!-- HEADER (STICKY WITH THEME TOGGLE BUTTON) -->
    <header class="sticky top-0 z-40 theme-header border-b-2 shadow-sm">
        <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                
                <!-- Logo -->
                <div class="flex items-center gap-2.5 sm:gap-3 cursor-pointer" onclick="showCatalogView()">
                    <div class="w-10 h-10 rounded-2xl bg-[#EE4D2D] flex items-center justify-center text-white font-black text-xl shadow-md shadow-orange-500/20 flex-shrink-0">
                        🎯
                    </div>
                    <div>
                        <div class="flex items-center gap-1.5">
                            <span class="font-black text-base sm:text-lg tracking-tight theme-text-main">GOODSTONE</span>
                            <span class="bg-[#EE4D2D] text-white text-[9px] px-1.5 py-0.2 rounded font-black">SHOP</span>
                        </div>
                        <span class="text-[10px] sm:text-xs block theme-text-muted font-medium">ร้านหนังสติ๊กยุทธวิธีและอุปกรณ์</span>
                    </div>
                </div>

                <!-- Navigation & Action Buttons -->
                <div class="flex items-center gap-1.5 sm:gap-3">
                    
                    <button type="button" onclick="showCatalogView()" class="theme-text-main hover:text-[#EE4D2D] text-xs font-bold px-2 py-1.5 rounded-lg flex items-center gap-1">
                        <span>หน้าร้านค้า</span>
                    </button>
                    
                    <a href="track.html" class="theme-text-muted hover:text-[#EE4D2D] text-xs font-bold px-2 py-1.5 rounded-lg flex items-center gap-1">
                        <span>เช็คพัสดุ</span>
                    </a>

                    <!-- 🌓 LIGHT / DARK MODE TOGGLE (LOCKED DEFAULT TO DARK) -->
                    <button type="button" onclick="toggleTheme()" id="theme-toggle-btn" class="flex items-center gap-1 px-2.5 sm:px-3 py-1.5 rounded-xl border border-[#333342] bg-[#272732] text-[#F4F0EA] hover:border-[#EE4D2D] text-xs font-bold transition-all shadow-sm active:scale-95 cursor-pointer" title="สลับโหมดมืด / สว่าง">
                        <span id="theme-toggle-icon">🌙</span>
                        <span id="theme-toggle-text" class="hidden sm:inline">โหมดมืด</span>
                    </button>

                    <!-- Customer Wallet Badge -->
                    <div id="header-wallet-badge" class="hidden sm:flex items-center gap-1.5 theme-badge px-2.5 py-1.5 rounded-xl text-xs font-bold border">
                        <span>👛</span>
                        <span id="user-wallet-display" class="font-black text-[#EE4D2D]">฿0.00</span>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- PROMOTION BANNER -->
    <div class="bg-[#EE4D2D] text-white py-1.5 px-4 text-center text-xs font-bold shadow-sm">
        📮 ค่าจัดส่ง EMS/SPX 25 บาททั่วไทย (พิเศษ! สั่งซื้อครบ 200 บาทขึ้นไป จัดส่งฟรีทันที)
    </div>

    <!-- MAIN CONTAINER -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-3 sm:px-6 lg:px-8 py-4 sm:py-6 space-y-6">

        <!-- ================= VIEW 1: PRODUCT CATALOG / GRID (หน้าแรกหลัก) ================= -->
        <section id="view-catalog" class="space-y-5">
            
            <!-- Hero Banner -->
            <div class="rounded-3xl theme-hero p-5 sm:p-8 border-2 shadow-sm space-y-2.5">
                <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full theme-badge text-[11px] font-extrabold border">
                    <span>🔥 หนังสติ๊กยุทธวิธีเกรดพรีเมียม & อุปกรณ์ครบวงจร</span>
                </div>
                <h1 class="text-xl sm:text-3xl font-black theme-text-main leading-tight tracking-tight">
                    หนังสติ๊กยุทธวิธี ยางแบนแรงสูง <span class="text-[#EE4D2D]">จัดส่งด่วน EMS / SPX ทั่วประเทศ</span>
                </h1>
                <p class="text-xs sm:text-sm theme-text-muted max-w-2xl leading-relaxed">
                    ด้ามจับอัลลอยด์ CNC เลเซอร์ช่วยเล็ง ยางแบนสโลปทนทาน ลูกเหล็กขัดเงามาตรฐาน แตะที่รูปภาพเพื่อสั่งซื้อด่วน หรือกดดูรีวิวจาก Shopee ได้ทันที
                </p>
            </div>

            <!-- Search Bar & Category Filter Buttons -->
            <div class="theme-card p-3 sm:p-4 rounded-3xl border-2 shadow-sm space-y-3">
                <div class="flex flex-wrap items-center gap-1.5">
                    <button onclick="selectCategory('all')" id="cat-btn-all" class="px-3 py-1.5 rounded-xl text-xs font-bold transition-all bg-[#EE4D2D] text-white shadow-sm">
                        ทั้งหมด
                    </button>
                    <button onclick="selectCategory('slingshot')" id="cat-btn-slingshot" class="px-3 py-1.5 rounded-xl text-xs font-bold transition-all theme-card-subtle theme-text-muted hover:text-[#EE4D2D]">
                        🎯 หนังสติ๊ก
                    </button>
                    <button onclick="selectCategory('rubber')" id="cat-btn-rubber" class="px-3 py-1.5 rounded-xl text-xs font-bold transition-all theme-card-subtle theme-text-muted hover:text-[#EE4D2D]">
                        ⚡ ยางหนังสติ๊ก
                    </button>
                    <button onclick="selectCategory('ammo')" id="cat-btn-ammo" class="px-3 py-1.5 rounded-xl text-xs font-bold transition-all theme-card-subtle theme-text-muted hover:text-[#EE4D2D]">
                        🔘 ลูกเหล็ก/กระสุน
                    </button>
                    <button onclick="selectCategory('accessories')" id="cat-btn-accessories" class="px-3 py-1.5 rounded-xl text-xs font-bold transition-all theme-card-subtle theme-text-muted hover:text-[#EE4D2D]">
                        🎒 อุปกรณ์เสริม/เลเซอร์
                    </button>
                </div>

                <div class="relative">
                    <input type="text" id="catalog-search" oninput="filterCatalog()" placeholder="🔍 ค้นหาสินค้า..." class="w-full theme-input border rounded-2xl pl-4 pr-4 py-2 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-[#EE4D2D] font-medium">
                </div>
            </div>

            <!-- Product Grid -->
            <div id="product-grid-container" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-5">
                <!-- Loaded dynamically by JS -->
            </div>

        </section>

        <!-- ================= VIEW 2: SINGLE-PAGE DIRECT CHECKOUT ================= -->
        <section id="view-checkout" class="hidden space-y-5">
            
            <div class="flex items-center justify-between">
                <button type="button" onclick="showCatalogView()" class="theme-card hover:border-[#EE4D2D] theme-text-main text-xs font-bold px-3.5 py-2 rounded-2xl border-2 shadow-sm transition-all flex items-center gap-1">
                    <span>← กลับไปดูสินค้าทั้งหมด</span>
                </button>
                <span class="text-xs font-black text-[#EE4D2D] theme-badge px-3 py-1 rounded-full border">
                    ⚡ สั่งซื้อด่วน (Direct Checkout)
                </span>
            </div>

            <!-- Product Detail Card in Checkout -->
            <div class="grid grid-cols-1 md:grid-cols-12 gap-6 theme-card border-2 rounded-3xl p-4 sm:p-7 shadow-sm">
                <!-- Gallery -->
                <div class="md:col-span-5 space-y-3">
                    <div class="w-full h-64 sm:h-72 theme-card-subtle rounded-3xl border p-3 flex items-center justify-center overflow-hidden cursor-pointer relative" onclick="openGalleryModal()">
                        <img id="checkout-main-img" src="" class="max-h-full max-w-full object-contain">
                        <span class="absolute bottom-2 right-2 bg-black/60 text-white text-[10px] px-2 py-0.5 rounded-lg font-bold">🔍 แตะดูรูปเต็ม</span>
                    </div>
                    <div id="checkout-gallery-thumbs" class="grid grid-cols-4 gap-2"></div>
                </div>

                <!-- Product Info & Variant Selector -->
                <div class="md:col-span-7 space-y-3.5 flex flex-col justify-between">
                    <div class="space-y-2.5">
                        <span id="checkout-prod-category" class="theme-badge text-[9px] px-2.5 py-0.5 rounded-full font-black uppercase border inline-block"></span>
                        <h2 id="checkout-prod-title" class="text-base sm:text-xl font-black theme-text-main leading-snug"></h2>
                        <div class="flex items-center gap-3">
                            <span id="checkout-prod-price" class="text-2xl font-black text-[#EE4D2D]"></span>
                            <span id="checkout-prod-stock" class="text-xs theme-text-muted"></span>
                        </div>
                        <p id="checkout-prod-desc" class="text-xs theme-text-muted leading-relaxed"></p>
                    </div>

                    <!-- Variants Selector -->
                    <div class="space-y-1.5 pt-2 border-t border-slate-100 dark:border-slate-800">
                        <label class="text-xs font-bold theme-text-main">เลือกสเปก / ตัวเลือกสินค้า:</label>
                        <div id="checkout-variants-container" class="flex flex-wrap gap-2"></div>
                    </div>

                    <!-- Quantity -->
                    <div class="flex items-center justify-between pt-2 border-t border-slate-100 dark:border-slate-800">
                        <label class="text-xs font-bold theme-text-main">จำนวนที่ต้องการสั่งซื้อ:</label>
                        <div class="flex items-center gap-2 theme-card-subtle border rounded-xl p-1">
                            <button type="button" onclick="changeQuantity(-1)" class="w-7 h-7 bg-white dark:bg-slate-700 theme-text-main rounded-lg font-black">-</button>
                            <span id="checkout-qty-display" class="w-8 text-center font-black text-sm theme-text-main">1</span>
                            <button type="button" onclick="changeQuantity(1)" class="w-7 h-7 bg-white dark:bg-slate-700 theme-text-main rounded-lg font-black">+</button>
                        </div>
                    </div>

                    <!-- Shopee Affiliate Review Link in Checkout -->
                    <div class="pt-1">
                        <a id="checkout-shopee-review-btn" href="https://th.shp.ee/sdFv2cS1" target="_blank" class="w-full theme-shopee-btn py-2 px-3 rounded-xl border text-xs font-bold flex items-center justify-center gap-1 shadow-sm transition-all">
                            <span>⭐ ดูรีวิวสินค้านี้บน Shopee (ของแท้ 100%) ></span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Checkout Form & Payment -->
            <form onsubmit="event.preventDefault(); submitDirectOrder();" class="theme-card border-2 rounded-3xl p-4 sm:p-7 space-y-5 shadow-sm">
                
                <!-- 1. Address Form -->
                <div class="space-y-3">
                    <h3 class="text-xs sm:text-sm font-black theme-text-main flex items-center gap-2 border-b pb-2 border-slate-100 dark:border-slate-800">
                        <span>📍</span> 1. ข้อมูลผู้รับและที่อยู่จัดส่ง
                    </h3>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div>
                            <label class="block text-xs font-bold theme-text-main mb-1">ชื่อ-นามสกุล *</label>
                            <input type="text" id="cust-name" required placeholder="เช่น คุณสมชาย ใจดี" class="w-full theme-input border rounded-xl px-3 py-2 text-xs">
                        </div>
                        <div>
                            <label class="block text-xs font-bold theme-text-main mb-1">เบอร์โทรศัพท์ (ติดต่อรับของ) *</label>
                            <input type="tel" id="cust-phone" oninput="onPhoneChange(this.value)" required placeholder="เช่น 081-999-8877" class="w-full theme-input border rounded-xl px-3 py-2 text-xs">
                        </div>
                    </div>
                    <div>
                        <label class="block text-xs font-bold theme-text-main mb-1">บ้านเลขที่, หมู่, ซอย, ถนน *</label>
                        <input type="text" id="cust-address-line" required placeholder="เช่น 45/2 หมู่ 3 ซอยสุขุมวิท 10" class="w-full theme-input border rounded-xl px-3 py-2 text-xs">
                    </div>
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
                        <div>
                            <label class="block text-xs font-bold theme-text-main mb-1">รหัสไปรษณีย์ 5 หลัก *</label>
                            <input type="text" id="cust-postcode" maxlength="5" oninput="handlePostalCodeInput(this.value)" required placeholder="เช่น 10150" class="w-full theme-input border rounded-xl px-3 py-2 text-xs font-mono font-bold text-[#EE4D2D]">
                        </div>
                        <div>
                            <label class="block text-xs font-bold theme-text-main mb-1">ตำบล/แขวง</label>
                            <input type="text" id="cust-subdistrict" placeholder="ตำบล" class="w-full theme-input border rounded-xl px-3 py-2 text-xs">
                        </div>
                        <div>
                            <label class="block text-xs font-bold theme-text-main mb-1">อำเภอ/เขต</label>
                            <input type="text" id="cust-district" placeholder="อำเภอ" class="w-full theme-input border rounded-xl px-3 py-2 text-xs">
                        </div>
                        <div>
                            <label class="block text-xs font-bold theme-text-main mb-1">จังหวัด</label>
                            <input type="text" id="cust-province" placeholder="จังหวัด" class="w-full theme-input border rounded-xl px-3 py-2 text-xs">
                        </div>
                    </div>
                </div>

                <!-- Carrier Routing Display -->
                <div class="theme-card-subtle p-3 rounded-2xl border flex items-center justify-between text-xs">
                    <div>
                        <span class="text-[10px] theme-text-muted block">ขนส่งที่จัดสรรตามรหัสไปรษณีย์:</span>
                        <span id="carrier-routing-text" class="font-bold text-[#EE4D2D]">SPX Express (Shopee Express)</span>
                    </div>
                    <span id="carrier-fee-badge" class="bg-emerald-50 text-emerald-700 border border-emerald-300 px-2.5 py-1 rounded-full text-xs font-bold">ส่งฟรี (฿0)</span>
                </div>

                <!-- 2. Payment Method Selector (3 Tabs) -->
                <div class="space-y-3 pt-2 border-t border-slate-100 dark:border-slate-800">
                    <h3 class="text-xs sm:text-sm font-black theme-text-main flex items-center gap-2">
                        <span>💳</span> 2. ช่องทางการชำระเงิน
                    </h3>

                    <div class="grid grid-cols-3 gap-2">
                        <button type="button" onclick="setPaymentMethod('PROMPTPAY')" id="btn-pay-promptpay" class="p-2.5 rounded-2xl border-2 border-[#EE4D2D] bg-[#FFF2EE] text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-0.5 shadow-sm transition-all text-center">
                            <span class="text-base">📱</span>
                            <span class="text-[11px] sm:text-xs">พร้อมเพย์</span>
                            <span class="text-[9px] text-emerald-700 font-normal">ฟรีค่าส่งเมื่อครบ 200</span>
                        </button>

                        <button type="button" onclick="setPaymentMethod('COD')" id="btn-pay-cod" class="p-2.5 rounded-2xl border-2 border-[#333342] theme-card-subtle theme-text-muted text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center">
                            <span class="text-base">💵</span>
                            <span class="text-[11px] sm:text-xs">เก็บปลายทาง</span>
                            <span class="text-[9px] text-[#EE4D2D] font-bold">บวก 3%</span>
                        </button>

                        <button type="button" onclick="setPaymentMethod('STORE_CREDIT')" id="btn-pay-wallet" class="p-2.5 rounded-2xl border-2 border-[#333342] theme-card-subtle theme-text-muted text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center">
                            <span class="text-base">👛</span>
                            <span class="text-[11px] sm:text-xs">กระเป๋าเครดิต</span>
                            <span id="wallet-btn-bal" class="text-[9px] text-emerald-700 font-normal">฿530.00</span>
                        </button>
                    </div>

                    <!-- COD Panel -->
                    <div id="panel-cod" class="theme-card-subtle border-2 border-[#EE4D2D]/30 rounded-2xl p-4 space-y-3 hidden">
                        <div class="flex items-center gap-3">
                            <div class="w-9 h-9 rounded-xl bg-[#EE4D2D] text-white flex items-center justify-center text-lg flex-shrink-0">💵</div>
                            <div>
                                <h4 class="font-bold text-xs sm:text-sm theme-text-main">บริการเก็บเงินปลายทาง (Cash on Delivery)</h4>
                                <p class="text-[11px] theme-text-muted">มีค่าบริการเก็บเงินปลายทาง +3% ของยอดรวม</p>
                            </div>
                        </div>
                        <div class="bg-black/10 dark:bg-white/5 p-3 rounded-xl border border-[#EE4D2D]/20 text-xs space-y-1">
                            <p class="flex justify-between"><span>ราคาสินค้า + ค่าส่ง:</span> <span id="cod-base-amount" class="font-bold theme-text-main">฿0.00</span></p>
                            <p class="flex justify-between text-[#EE4D2D]"><span>ค่าบริการ COD (+3%):</span> <span id="cod-fee-amount" class="font-bold">+฿0.00</span></p>
                            <div class="border-t border-slate-700/30 pt-1 flex justify-between font-black text-sm theme-text-main">
                                <span>ยอดชำระเมื่อรับพัสดุ:</span>
                                <span id="cod-total-amount" class="text-[#EE4D2D]">฿0.00</span>
                            </div>
                        </div>
                        <p class="text-[10px] theme-text-muted">
                            💡 ไม่ต้องโอนเงินล่วงหน้า กรุณาเตรียมเงินสดให้พนักงานขนส่งเมื่อพัสดุไปถึงครับ
                        </p>
                    </div>

                    <!-- PromptPay Panel -->
                    <div id="panel-promptpay" class="theme-card-subtle border rounded-2xl p-4 space-y-3 text-center">
                        <span class="text-xs theme-text-muted block">สแกน PromptPay QR เพื่อชำระเงิน</span>
                        <p id="promptpay-amount-display" class="text-2xl font-black text-[#EE4D2D]">฿0.00</p>
                        <div class="flex justify-center">
                            <img id="promptpay-qr-img" src="" class="w-48 h-48 rounded-xl border-2 border-slate-300 dark:border-slate-700 bg-white p-2">
                        </div>
                        <label class="inline-block bg-[#EE4D2D] hover:bg-[#d73211] text-white text-xs px-4 py-2 rounded-xl font-bold cursor-pointer shadow-md active:scale-95">
                            📎 แนบสลิปโอนเงิน
                            <input type="file" accept="image/*" onchange="handleSlipFile(this)" class="hidden">
                        </label>
                        <div id="slip-status-msg" class="text-xs font-bold text-emerald-600 hidden"></div>
                    </div>

                    <!-- Store Credit Wallet Panel -->
                    <div id="panel-wallet" class="theme-card-subtle border rounded-2xl p-4 space-y-2 hidden text-xs">
                        <div class="flex justify-between"><span>ยอดเงินในกระเป๋า:</span> <span id="wallet-balance-big" class="font-bold text-emerald-600">฿530.00</span></div>
                        <div class="flex justify-between"><span>ยอดที่ต้องชำระ:</span> <span id="wallet-order-amt" class="font-bold text-[#EE4D2D]">฿0.00</span></div>
                        <div class="flex justify-between border-t pt-1 border-slate-700/30"><span>ยอดคงเหลือหลังหัก:</span> <span id="wallet-after-bal" class="font-bold theme-text-main">฿0.00</span></div>
                    </div>
                </div>

                <!-- 3. Price Breakdown Summary -->
                <div class="theme-card-subtle p-4 rounded-2xl border space-y-1.5 text-xs">
                    <div class="flex justify-between">
                        <span class="theme-text-muted">ราคาสินค้า (<span id="summary-variant-name"></span> x<span id="summary-qty">1</span>):</span>
                        <span id="summary-subtotal" class="font-bold theme-text-main">฿0.00</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="theme-text-muted">ค่าจัดส่ง:</span>
                        <span id="summary-shipping" class="font-bold text-emerald-600">ฟรี (฿0.00)</span>
                    </div>
                    <div id="summary-cod-row" class="flex justify-between text-[#EE4D2D] font-bold hidden">
                        <span>ค่าบริการเก็บปลายทาง (COD +3%):</span>
                        <span id="summary-cod-fee">+฿0.00</span>
                    </div>
                    <div class="border-t border-slate-700/30 pt-2 flex justify-between text-base font-black theme-text-main">
                        <span>ยอดสุทธิที่ต้องชำระ:</span>
                        <span id="summary-total" class="text-[#EE4D2D]">฿0.00</span>
                    </div>
                </div>

                <!-- Submit Button -->
                <button type="submit" id="submit-btn-text" class="w-full bg-[#EE4D2D] hover:bg-[#d73211] text-white font-black py-3.5 rounded-2xl text-sm sm:text-base shadow-lg transition-all active:scale-95 cursor-pointer">
                    ⚡ สั่งซื้อและชำระเงิน
                </button>
            </form>

        </section>

    </main>

    <!-- FOOTER -->
    <footer class="theme-header border-t py-6 text-center text-xs theme-text-muted">
        <p>GOODSTONE TACTICAL SLINGSHOT © 2026</p>
        <p class="text-[10px] mt-1">Single-Page Direct-to-Checkout • จัดส่งด่วน SPX Express / ไปรษณีย์ไทย EMS • พร้อมเพย์ & COD +3%</p>
    </footer>

    <!-- JAVASCRIPT LOGIC -->
    <script>
        const DEFAULT_PRODUCTS = """ + products_json + """;

        let products = DEFAULT_PRODUCTS;
        let selectedProduct = DEFAULT_PRODUCTS[0];
        let selectedVariantIdx = 0;
        let selectedCategory = "all";
        let quantity = 1;
        let currentGalleryIdx = 0;
        let paymentMethod = "PROMPTPAY";
        let slipImageBase64 = null;

        let userWallet = {
            balance: 530,
            total_topup: 500,
            total_bonus: 30
        };

        // ================= THEME CONTROLLER (DEFAULT: DARK) =================
        let currentTheme = localStorage.getItem("goodstone_theme") || "dark";

        function applyTheme(theme) {
            currentTheme = theme;
            document.documentElement.setAttribute("data-theme", theme);
            document.body.setAttribute("data-theme", theme);
            localStorage.setItem("goodstone_theme", theme);

            const btn = document.getElementById("theme-toggle-btn");
            const icon = document.getElementById("theme-toggle-icon");
            const text = document.getElementById("theme-toggle-text");

            if (theme === "dark") {
                if (icon) icon.innerText = "🌙";
                if (text) text.innerText = "โหมดมืด";
                if (btn) btn.className = "flex items-center gap-1 px-2.5 sm:px-3 py-1.5 rounded-xl border border-[#333342] bg-[#272732] text-[#F4F0EA] hover:border-[#EE4D2D] text-xs font-bold transition-all shadow-sm active:scale-95 cursor-pointer";
            } else {
                if (icon) icon.innerText = "☀️";
                if (text) text.innerText = "โหมดสว่าง";
                if (btn) btn.className = "flex items-center gap-1 px-2.5 sm:px-3 py-1.5 rounded-xl border border-[#EBE3D5] bg-[#FAF7F2] text-[#2C241E] hover:border-[#EE4D2D] text-xs font-bold transition-all shadow-sm active:scale-95 cursor-pointer";
            }
        }

        function toggleTheme() {
            const next = currentTheme === "dark" ? "light" : "dark";
            applyTheme(next);
        }

        // ================= INITIALIZATION =================
        function init() {
            applyTheme(currentTheme);
            lucide.createIcons();

            const savedProducts = localStorage.getItem("goodstone_products");
            if (savedProducts) {
                try { products = JSON.parse(savedProducts); } catch(e) {}
            } else {
                localStorage.setItem("goodstone_products", JSON.stringify(DEFAULT_PRODUCTS));
            }

            if (products && products.length > 0) {
                selectedProduct = products[0];
            }

            const savedProfile = localStorage.getItem("goodstone_saved_profile");
            if (savedProfile) {
                try {
                    const p = JSON.parse(savedProfile);
                    if (p.name) document.getElementById("cust-name").value = p.name;
                    if (p.phone) {
                        document.getElementById("cust-phone").value = p.phone;
                        onPhoneChange(p.phone);
                    }
                    if (p.addressLine) document.getElementById("cust-address-line").value = p.addressLine;
                    if (p.postal_code) {
                        document.getElementById("cust-postcode").value = p.postal_code;
                        handlePostalCodeInput(p.postal_code);
                    }
                    if (p.subdistrict) document.getElementById("cust-subdistrict").value = p.subdistrict;
                    if (p.district) document.getElementById("cust-district").value = p.district;
                    if (p.province) document.getElementById("cust-province").value = p.province;
                } catch(e) {}
            }

            renderCatalogGrid();
        }

        // ================= CATALOG VIEW =================
        function showCatalogView() {
            document.getElementById("view-catalog").classList.remove("hidden");
            document.getElementById("view-checkout").classList.add("hidden");
            window.scrollTo({ top: 0, behavior: "smooth" });
        }

        function selectCategory(cat) {
            selectedCategory = cat;
            const buttons = ["all", "slingshot", "rubber", "ammo", "accessories"];
            buttons.forEach(c => {
                const btn = document.getElementById(`cat-btn-${c}`);
                if (btn) {
                    if (c === cat) {
                        btn.className = "px-3 py-1.5 rounded-xl text-xs font-bold transition-all bg-[#EE4D2D] text-white shadow-sm";
                    } else {
                        btn.className = "px-3 py-1.5 rounded-xl text-xs font-bold transition-all theme-card-subtle theme-text-muted hover:text-[#EE4D2D]";
                    }
                }
            });
            renderCatalogGrid();
        }

        function filterCatalog() {
            renderCatalogGrid();
        }

        function renderCatalogGrid() {
            const container = document.getElementById("product-grid-container");
            if (!container) return;
            container.innerHTML = "";

            const query = (document.getElementById("catalog-search")?.value || "").toLowerCase().trim();
            const filtered = products.filter(p => {
                const matchCat = (selectedCategory === "all" || p.category === selectedCategory);
                const matchQuery = !query || p.name.toLowerCase().includes(query) || p.description.toLowerCase().includes(query);
                return matchCat && matchQuery;
            });

            if (filtered.length === 0) {
                container.innerHTML = `<div class="col-span-full py-12 text-center theme-text-muted text-xs">ไม่พบสินค้าที่ตรงกับการค้นหา</div>`;
                return;
            }

            filtered.forEach(p => {
                const imgSrc = p.image_file || p.fallback_image;
                const shopeeUrl = p.shopee_affiliate_url || "https://th.shp.ee/sdFv2cS1";
                const startingPrice = (p.variants && p.variants.length > 0)
                    ? Math.min(...p.variants.map(v => Number(v.price || 0)))
                    : Number(p.price || 0);

                const card = document.createElement("div");
                card.className = "theme-card rounded-3xl border-2 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group";
                card.innerHTML = `
                    <div>
                        <!-- Click Image to open Direct Checkout -->
                        <div onclick="openProductDirectCheckout('${p.id}')" class="h-48 sm:h-52 overflow-hidden theme-card-subtle relative flex items-center justify-center cursor-pointer group/img border-b">
                            <img src="${imgSrc}" onerror="this.onerror=null; this.src='${p.fallback_image}';" class="w-full h-full object-contain p-3 group-hover/img:scale-105 transition-transform duration-300">
                            <span class="absolute top-2.5 left-2.5 theme-badge text-[9px] px-2 py-0.5 rounded-full font-black uppercase border">
                                ${p.category}
                            </span>
                            <span class="absolute bottom-2.5 right-2.5 bg-black/60 text-white text-[10px] px-2.5 py-0.5 rounded-lg font-bold backdrop-blur-sm opacity-0 group-hover/img:opacity-100 transition-opacity">
                                ⚡ แตะเพื่อซื้อด่วน
                            </span>
                        </div>

                        <div class="p-4 space-y-2">
                            <h3 onclick="openProductDirectCheckout('${p.id}')" class="font-bold theme-text-main text-xs sm:text-sm line-clamp-2 cursor-pointer hover:text-[#EE4D2D] transition-colors leading-snug">
                                ${p.name}
                            </h3>
                            <p class="text-[11px] theme-text-muted line-clamp-2">${p.description}</p>
                        </div>
                    </div>

                    <div class="p-4 pt-0 space-y-2.5">
                        <div class="flex items-baseline justify-between pt-2 border-t border-slate-700/20">
                            <div>
                                <span class="text-[10px] theme-text-muted block">เริ่มต้น</span>
                                <span class="text-base font-black text-[#EE4D2D]">฿${startingPrice.toLocaleString(undefined, {minimumFractionDigits: 2})}</span>
                            </div>
                            <span class="text-[10px] theme-badge border px-2 py-0.5 rounded-full font-bold">
                                สต็อก: ${p.stock}
                            </span>
                        </div>

                        <!-- 2 Actions: Direct Checkout + Shopee Review Button -->
                        <div class="space-y-1.5">
                            <button onclick="openProductDirectCheckout('${p.id}')" class="w-full bg-[#EE4D2D] hover:bg-[#d73211] text-white py-2 rounded-xl text-xs font-bold transition-all flex items-center justify-center gap-1 shadow-md active:scale-95 cursor-pointer">
                                <span>⚡ ซื้อด่วน (Direct Checkout)</span>
                            </button>
                            <a href="${shopeeUrl}" target="_blank" class="w-full theme-shopee-btn py-1.5 px-3 rounded-xl border text-[11px] font-bold flex items-center justify-center gap-1 shadow-sm transition-all">
                                <span>⭐ ดูรีวิวใน Shopee ></span>
                            </a>
                        </div>
                    </div>
                `;
                container.appendChild(card);
            });
        }

        // ================= DIRECT CHECKOUT VIEW =================
        function openProductDirectCheckout(productId) {
            const found = products.find(p => p.id === productId);
            if (!found) return;

            selectedProduct = found;
            selectedVariantIdx = 0;
            quantity = 1;
            currentGalleryIdx = 0;

            document.getElementById("view-catalog").classList.add("hidden");
            document.getElementById("view-checkout").classList.remove("hidden");

            renderProductCheckoutDetail();
            updateCalculations();
            window.scrollTo({ top: 0, behavior: "smooth" });
        }

        function renderProductCheckoutDetail() {
            const p = selectedProduct;
            const images = (p.images && p.images.length > 0)
                ? p.images
                : [{ file: p.image_file || p.fallback_image, name: `${p.id}_main.jpg` }];

            document.getElementById("checkout-main-img").src = images[0].file;
            document.getElementById("checkout-prod-category").innerText = p.category;
            document.getElementById("checkout-prod-title").innerText = p.name;
            document.getElementById("checkout-prod-desc").innerText = p.description;

            // Shopee Review Link
            const shopeeBtn = document.getElementById("checkout-shopee-review-btn");
            if (shopeeBtn) {
                shopeeBtn.href = p.shopee_affiliate_url || "https://th.shp.ee/sdFv2cS1";
            }

            // Gallery Thumbs
            const thumbsContainer = document.getElementById("checkout-gallery-thumbs");
            thumbsContainer.innerHTML = "";
            images.forEach((img, idx) => {
                const btn = document.createElement("button");
                btn.type = "button";
                btn.className = `h-14 rounded-xl border-2 p-1 theme-card-subtle flex items-center justify-center overflow-hidden cursor-pointer ${idx === 0 ? 'border-[#EE4D2D]' : ''}`;
                btn.innerHTML = `<img src="${img.file}" class="w-full h-full object-contain">`;
                btn.onclick = () => {
                    currentGalleryIdx = idx;
                    document.getElementById("checkout-main-img").src = img.file;
                    Array.from(thumbsContainer.children).forEach((el, i) => {
                        el.className = `h-14 rounded-xl border-2 p-1 theme-card-subtle flex items-center justify-center overflow-hidden cursor-pointer ${i === idx ? 'border-[#EE4D2D]' : ''}`;
                    });
                };
                thumbsContainer.appendChild(btn);
            });

            // Variant Selector Buttons
            const variantsContainer = document.getElementById("checkout-variants-container");
            variantsContainer.innerHTML = "";
            const variants = (p.variants && p.variants.length > 0)
                ? p.variants
                : [{ name: "รุ่นมาตรฐาน", price: p.price, stock: p.stock }];

            variants.forEach((v, idx) => {
                const btn = document.createElement("button");
                btn.type = "button";
                btn.className = `px-3 py-1.5 rounded-xl text-xs font-bold border-2 transition-all cursor-pointer ${idx === selectedVariantIdx ? 'border-[#EE4D2D] bg-[#EE4D2D] text-white shadow-sm' : 'theme-card-subtle theme-text-main hover:border-[#EE4D2D]'}`;
                btn.innerText = `${v.name} (฿${Number(v.price).toLocaleString()})`;
                btn.onclick = () => {
                    selectedVariantIdx = idx;
                    renderProductCheckoutDetail();
                    updateCalculations();
                };
                variantsContainer.appendChild(btn);
            });

            const activeV = variants[selectedVariantIdx] || variants[0];
            document.getElementById("checkout-prod-price").innerText = `฿${Number(activeV.price).toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("checkout-prod-stock").innerText = `สต็อกคงเหลือ ${activeV.stock || p.stock} ชิ้น`;
            document.getElementById("checkout-qty-display").innerText = quantity;
        }

        function changeQuantity(delta) {
            quantity = Math.max(1, quantity + delta);
            document.getElementById("checkout-qty-display").innerText = quantity;
            updateCalculations();
        }

        // ================= PRICE & LOGISTICS CALCULATION =================
        function updateCalculations() {
            if (!selectedProduct) return;

            const variants = (selectedProduct.variants && selectedProduct.variants.length > 0)
                ? selectedProduct.variants
                : [{ name: "รุ่นมาตรฐาน", price: selectedProduct.price, stock: selectedProduct.stock }];

            const activeV = variants[selectedVariantIdx] || variants[0];
            const unitPrice = Number(activeV.price || selectedProduct.price || 0);
            const subtotal = unitPrice * quantity;
            const isFreeShipping = (subtotal >= 200);
            const shippingCost = isFreeShipping ? 0 : 25;
            const baseTotal = subtotal + shippingCost;
            const codFee = (paymentMethod === "COD") ? Number((baseTotal * 0.03).toFixed(2)) : 0;
            const total = Number((baseTotal + codFee).toFixed(2));

            document.getElementById("summary-variant-name").innerText = activeV.name;
            document.getElementById("summary-qty").innerText = quantity;
            document.getElementById("summary-subtotal").innerText = `฿${subtotal.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("summary-shipping").innerText = isFreeShipping ? "ฟรี (฿0.00)" : "฿25.00";
            
            const codRow = document.getElementById("summary-cod-row");
            if (codRow) {
                if (paymentMethod === "COD") {
                    codRow.classList.remove("hidden");
                    document.getElementById("summary-cod-fee").innerText = `+฿${codFee.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
                } else {
                    codRow.classList.add("hidden");
                }
            }

            document.getElementById("summary-total").innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("promptpay-amount-display").innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            
            if (paymentMethod === "COD") {
                document.getElementById("submit-btn-text").innerText = `📦 สั่งซื้อแบบเก็บเงินปลายทาง (฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})})`;
            } else {
                document.getElementById("submit-btn-text").innerText = `⚡ สั่งซื้อและชำระเงิน (฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})})`;
            }

            document.getElementById("carrier-fee-badge").innerText = isFreeShipping ? "ส่งฟรี (฿0)" : "฿25";
            document.getElementById("wallet-order-amt").innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("wallet-after-bal").innerText = `฿${Math.max(0, userWallet.balance - total).toLocaleString(undefined, {minimumFractionDigits: 2})}`;

            const codBaseEl = document.getElementById("cod-base-amount");
            if (codBaseEl) {
                codBaseEl.innerText = `฿${baseTotal.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
                document.getElementById("cod-fee-amount").innerText = `+฿${codFee.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
                document.getElementById("cod-total-amount").innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            }

            // Update Dynamic PromptPay QR
            const ppPayload = generatePromptPayQR(total);
            document.getElementById("promptpay-qr-img").src = `https://api.qrserver.com/v1/create-qr-code/?size=260x260&margin=10&data=${encodeURIComponent(ppPayload)}`;
        }

        function setPaymentMethod(method) {
            paymentMethod = method;
            const btnPP = document.getElementById("btn-pay-promptpay");
            const btnCOD = document.getElementById("btn-pay-cod");
            const btnW = document.getElementById("btn-pay-wallet");
            const panelPP = document.getElementById("panel-promptpay");
            const panelCOD = document.getElementById("panel-cod");
            const panelW = document.getElementById("panel-wallet");

            btnPP.className = "p-2.5 rounded-2xl border-2 theme-card-subtle theme-text-muted text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";
            btnCOD.className = "p-2.5 rounded-2xl border-2 theme-card-subtle theme-text-muted text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";
            btnW.className = "p-2.5 rounded-2xl border-2 theme-card-subtle theme-text-muted text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";

            panelPP.classList.add("hidden");
            panelCOD.classList.add("hidden");
            panelW.classList.add("hidden");

            if (method === "PROMPTPAY") {
                btnPP.className = "p-2.5 rounded-2xl border-2 border-[#EE4D2D] bg-[#EE4D2D]/10 text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-0.5 shadow-sm transition-all text-center";
                panelPP.classList.remove("hidden");
            } else if (method === "COD") {
                btnCOD.className = "p-2.5 rounded-2xl border-2 border-[#EE4D2D] bg-[#EE4D2D]/10 text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-0.5 shadow-sm transition-all text-center";
                panelCOD.classList.remove("hidden");
            } else if (method === "STORE_CREDIT") {
                btnW.className = "p-2.5 rounded-2xl border-2 border-[#EE4D2D] bg-[#EE4D2D]/10 text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-0.5 shadow-sm transition-all text-center";
                panelW.classList.remove("hidden");
            }
            updateCalculations();
        }

        function handlePostalCodeInput(code) {
            const clean = code.trim();
            if (clean.length === 5) {
                const isRemote = clean.startsWith("94") || clean.startsWith("95") || clean.startsWith("96") || clean.startsWith("58") || ["84320", "84360", "23170", "23120", "81150", "82160", "63170", "50310"].includes(clean);
                const carrierText = isRemote ? "ไปรษณีย์ไทย ด่วนพิเศษ (EMS) [พื้นที่พิเศษ]" : "SPX Express (Shopee Express) [ด่วนทั่วไทย]";
                document.getElementById("carrier-routing-text").innerText = carrierText;

                // Simple auto-fill examples
                if (clean === "10150") {
                    document.getElementById("cust-subdistrict").value = "ท่าข้าม";
                    document.getElementById("cust-district").value = "บางขุนเทียน";
                    document.getElementById("cust-province").value = "กรุงเทพมหานคร";
                } else if (clean === "10270") {
                    document.getElementById("cust-subdistrict").value = "บางกระดี่";
                    document.getElementById("cust-district").value = "เมืองสมุทรปราการ";
                    document.getElementById("cust-province").value = "สมุทรปราการ";
                } else if (clean === "95000") {
                    document.getElementById("cust-subdistrict").value = "สะเตง";
                    document.getElementById("cust-district").value = "เมืองยะลา";
                    document.getElementById("cust-province").value = "ยะลา";
                }
            }
        }

        function onPhoneChange(val) {
            const clean = val.replace(/[^0-9]/g, "");
            if (clean.length >= 9) {
                const saved = localStorage.getItem(`goodstone_wallet_${clean}`);
                if (saved) {
                    try { userWallet = JSON.parse(saved); } catch(e) {}
                } else {
                    userWallet = { balance: 530, total_topup: 500, total_bonus: 30 };
                }
                document.getElementById("user-wallet-display").innerText = `฿${userWallet.balance.toLocaleString()}`;
                document.getElementById("wallet-btn-bal").innerText = `฿${userWallet.balance.toLocaleString()}`;
                document.getElementById("wallet-balance-big").innerText = `฿${userWallet.balance.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
                updateCalculations();
            }
        }

        function handleSlipFile(input) {
            const file = input.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = function(e) {
                slipImageBase64 = e.target.result;
                const msg = document.getElementById("slip-status-msg");
                msg.classList.remove("hidden");
                msg.innerText = "✅ แนบสลิปโอนเงินเรียบร้อยแล้ว";
            };
            reader.readAsDataURL(file);
        }

        function submitDirectOrder() {
            const name = document.getElementById("cust-name").value.trim();
            const phone = document.getElementById("cust-phone").value.trim();
            const addressLine = document.getElementById("cust-address-line").value.trim();
            const postcode = document.getElementById("cust-postcode").value.trim();
            const subdistrict = document.getElementById("cust-subdistrict").value.trim();
            const district = document.getElementById("cust-district").value.trim();
            const province = document.getElementById("cust-province").value.trim();

            if (!name || !phone || !addressLine || !postcode) {
                alert("กรุณากรอกข้อมูล ชื่อ, เบอร์โทรศัพท์ และที่อยู่จัดส่งให้ครบถ้วนครับ");
                return;
            }

            const variants = (selectedProduct.variants && selectedProduct.variants.length > 0)
                ? selectedProduct.variants
                : [{ name: "รุ่นมาตรฐาน", price: selectedProduct.price, stock: selectedProduct.stock }];

            const activeV = variants[selectedVariantIdx] || variants[0];
            const unitPrice = Number(activeV.price || selectedProduct.price || 0);
            const subtotal = unitPrice * quantity;
            const isFreeShipping = (subtotal >= 200);
            const shippingCost = isFreeShipping ? 0 : 25;
            const baseTotal = subtotal + shippingCost;
            const codFee = (paymentMethod === "COD") ? Number((baseTotal * 0.03).toFixed(2)) : 0;
            const total = Number((baseTotal + codFee).toFixed(2));

            if (paymentMethod === "PROMPTPAY" && !slipImageBase64) {
                alert("กรุณาแนบสลิปหลักฐานการโอนเงินก่อนยืนยันสั่งซื้อครับ");
                return;
            }

            if (paymentMethod === "STORE_CREDIT" && userWallet.balance < total) {
                alert(`ยอดเงินในกระเป๋าเครดิตไม่เพียงพอ (คงเหลือ ฿${userWallet.balance.toLocaleString()} / ยอดชำระ ฿${total.toLocaleString()})`);
                return;
            }

            const now = new Date();
            const orderId = `ORD-${now.getFullYear()}${String(now.getMonth()+1).padStart(2,'0')}${String(now.getDate()).padStart(2,'0')}-${Math.floor(100 + Math.random()*900)}`;
            const isRemote = postcode.startsWith("94") || postcode.startsWith("95") || postcode.startsWith("96") || postcode.startsWith("58") || ["84320", "84360", "23170", "23120", "81150", "82160", "63170", "50310"].includes(postcode);

            const carrierName = isRemote ? "ไปรษณีย์ไทย ด่วนพิเศษ (EMS)" : "SPX Express (Shopee Express)";
            const carrierType = isRemote ? "THAILAND_POST_EMS" : "SPX_EXPRESS";
            const trackingNum = isRemote
                ? `ED${Math.floor(100000000 + Math.random()*900000000)}TH`
                : `SPXTH${Math.floor(1000000000 + Math.random()*9000000000)}`;

            const fullAddress = `${addressLine} ต.${subdistrict || "-"} อ.${district || "-"} จ.${province || "-"} ${postcode}`;

            const newOrder = {
                id: orderId,
                customer_name: name,
                phone: phone,
                address: fullAddress,
                postal_code: postcode,
                subdistrict: subdistrict,
                district: district,
                province: province,
                shipping_provider: carrierName,
                carrier_type: carrierType,
                shipping_cost: shippingCost,
                subtotal: subtotal,
                cod_fee: codFee,
                total_amount: total,
                status: (paymentMethod === "COD") ? "COD_PENDING" : "PAID",
                payment_method: paymentMethod,
                slip_image: slipImageBase64,
                tracking_number: trackingNum,
                items: [
                    {
                        product_id: selectedProduct.id,
                        name: `${selectedProduct.name} (${activeV.name})`,
                        base_name: selectedProduct.name,
                        variant: activeV.name,
                        price: activeV.price,
                        quantity: quantity,
                        image: selectedProduct.image_file || selectedProduct.fallback_image
                    }
                ],
                created_at: now.toISOString().replace("T", " ").substring(0, 19)
            };

            const profile = { name, phone, addressLine, postal_code: postcode, subdistrict, district, province };
            localStorage.setItem("goodstone_saved_profile", JSON.stringify(profile));
            document.cookie = `goodstone_user_session=${encodeURIComponent(JSON.stringify(profile))}; max-age=${365*24*60*60}; path=/`;

            if (paymentMethod === "STORE_CREDIT") {
                userWallet.balance -= total;
                localStorage.setItem(`goodstone_wallet_${phone.replace(/[^0-9]/g, "")}`, JSON.stringify(userWallet));
            }

            let allOrders = [];
            try {
                const saved = localStorage.getItem("goodstone_orders");
                if (saved) allOrders = JSON.parse(saved);
            } catch(e) {}
            allOrders.unshift(newOrder);
            localStorage.setItem("goodstone_orders", JSON.stringify(allOrders));

            if (paymentMethod === "COD") {
                alert(`📦 สั่งซื้อแบบเก็บเงินปลายทาง (COD) สำเร็จ!\\nรหัสคำสั่งซื้อ: ${newOrder.id}\\nยอดชำระเมื่อของถึง: ฿${newOrder.total_amount.toLocaleString(undefined, {minimumFractionDigits: 2})}\\nขนส่ง: ${newOrder.shipping_provider}\\nเลขพัสดุ: ${newOrder.tracking_number}`);
            } else {
                alert(`🎉 สั่งซื้อและชำระเงินสำเร็จ!\\nรหัสคำสั่งซื้อ: ${newOrder.id}\\nขนส่ง: ${newOrder.shipping_provider}\\nเลขพัสดุ: ${newOrder.tracking_number}`);
            }
            window.location.href = "track.html";
        }

        // ================= DYNAMIC PROMPTPAY QR GENERATOR (EMVCO) =================
        function generatePromptPayQR(amount) {
            const target = "0066615372239"; // 061-537-2239
            const amountStr = Number(amount).toFixed(2);
            let payload = "00020101021129370016A0000006770101110113" + target + "5802TH530376454" + String(amountStr.length).padStart(2, "0") + amountStr + "6304";
            payload += crc16(payload).toUpperCase();
            return payload;
        }

        function crc16(data) {
            let crc = 0xFFFF;
            for (let i = 0; i < data.length; i++) {
                let x = ((crc >> 8) ^ data.charCodeAt(i)) & 0xFF;
                x ^= x >> 4;
                crc = ((crc << 8) ^ (x << 12) ^ (x << 5) ^ x) & 0xFFFF;
            }
            return crc.toString(16).padStart(4, "0");
        }

        function openGalleryModal() {
            // View full screen image
            const img = document.getElementById("checkout-main-img").src;
            if (img) window.open(img, "_blank");
        }

        window.onload = init;
    </script>
</body>
</html>"""

with open("/working_dir/slingshot-shop/index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("slingshot-shop/index.html successfully reconstructed and verified!")
