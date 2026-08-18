import json

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))
products_json = json.dumps(data["products"], ensure_ascii=False)

index_html = """<!DOCTYPE html>
<html lang="th" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>GOODSTONE - ร้านหนังสติ๊กยุทธวิธีและอุปกรณ์</title>
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
        body { font-family: "Prompt", sans-serif; transition: background-color 0.2s ease, color 0.2s ease; margin: 0; padding: 0; }
        
        /* Dark Theme (Default) */
        :root, [data-theme="dark"] {
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
            --hero-from: #261B18;
            --hero-via: #211C20;
            --hero-to: #1A1A22;
        }

        /* Light Theme (Warm Cream) */
        [data-theme="light"] {
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
            --hero-from: #FFF6F2;
            --hero-via: #FDF3EA;
            --hero-to: #FBF0E4;
        }

        .app-body { background-color: var(--bg-page) !important; color: var(--text-main) !important; }
        .app-header { background-color: var(--bg-header) !important; border-color: var(--border-main) !important; }
        .app-card { background-color: var(--bg-card) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .app-card-subtle { background-color: var(--bg-card-subtle) !important; border-color: var(--border-subtle) !important; }
        .app-input { background-color: var(--bg-input) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .app-text-main { color: var(--text-main) !important; }
        .app-text-muted { color: var(--text-muted) !important; }
        .app-badge { background-color: var(--badge-bg) !important; border-color: var(--badge-border) !important; color: var(--badge-text) !important; }
        .app-hero { background: linear-gradient(135deg, var(--hero-from), var(--hero-via), var(--hero-to)) !important; border-color: var(--border-main) !important; }
        .app-border { border-color: var(--border-main) !important; }
    </style>
</head>
<body class="app-body min-h-screen flex flex-col font-sans" data-theme="dark">

    <!-- HEADER (STICKY) -->
    <header class="sticky top-0 z-40 app-header border-b-2 shadow-sm">
        <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <!-- Logo -->
                <div class="flex items-center gap-2.5 cursor-pointer" onclick="showCatalogView()">
                    <div class="w-10 h-10 rounded-2xl bg-[#EE4D2D] flex items-center justify-center text-white font-black text-xl shadow-md shadow-orange-500/20 flex-shrink-0">
                        🎯
                    </div>
                    <div>
                        <div class="flex items-center gap-1.5">
                            <span class="font-black text-base sm:text-lg tracking-wide app-text-main">GOODSTONE</span>
                            <span class="bg-[#EE4D2D] text-white text-[9px] px-1.5 py-0.2 rounded font-black uppercase">SHOP</span>
                        </div>
                        <span class="text-[10px] sm:text-xs block app-text-muted font-medium">ร้านหนังสติ๊กยุทธวิธีและอุปกรณ์</span>
                    </div>
                </div>

                <!-- Nav Menu & Actions -->
                <div class="flex items-center gap-2 sm:gap-4 text-xs font-bold">
                    <button onclick="showCatalogView()" class="app-text-main hover:text-[#EE4D2D] transition-colors flex items-center gap-1">
                        <span>หน้าร้านค้า</span>
                    </button>
                    <a href="track.html" class="app-text-muted hover:text-[#EE4D2D] transition-colors flex items-center gap-1">
                        <span>เช็คพัสดุ</span>
                    </a>

                    <!-- Light / Dark Mode Toggle (Default: Dark Mode) -->
                    <button type="button" onclick="toggleTheme()" id="theme-toggle-btn" class="flex items-center gap-1 px-2.5 py-1.5 rounded-xl border app-border app-card-subtle app-text-main hover:border-[#EE4D2D] text-xs font-bold transition-all shadow-sm active:scale-95" title="สลับโหมดมืด / สว่าง">
                        <span id="theme-toggle-icon">🌙</span>
                        <span id="theme-toggle-text" class="hidden sm:inline">โหมดมืด</span>
                    </button>

                    <!-- Customer Wallet Badge -->
                    <div id="header-wallet-badge" class="hidden sm:flex items-center gap-1.5 app-badge px-2.5 py-1.5 rounded-xl text-xs font-bold border">
                        <span class="app-text-muted">👛</span>
                        <span id="user-wallet-display" class="font-black text-[#EE4D2D]">฿0.00</span>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- FREE SHIPPING PROMOTION BANNER -->
    <div class="bg-[#EE4D2D] text-white py-1.5 px-3 text-center text-xs sm:text-sm font-bold shadow-sm">
        📮 ค่าจัดส่ง EMS/SPX 25 บาททั่วไทย (พิเศษ! สั่งซื้อครบ 200 บาทขึ้นไป จัดส่งฟรีทันที)
    </div>

    <!-- MAIN CONTAINER -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-3 sm:px-6 lg:px-8 py-4 sm:py-6 space-y-6">

        <!-- ================= VIEW 1: PRODUCT CATALOG / GRID (หน้าแรกหลัก) ================= -->
        <section id="view-catalog" class="space-y-5">
            
            <!-- Hero Banner -->
            <div class="rounded-3xl app-hero p-5 sm:p-8 border-2 shadow-sm space-y-2.5">
                <div class="inline-flex items-center gap-1.5 px-3 py-0.5 rounded-full app-badge text-xs font-extrabold">
                    <span>🔥 หนังสติ๊กยุทธวิธีเกรดพรีเมียม & อุปกรณ์ครบวงจร</span>
                </div>
                <h1 class="text-xl sm:text-3xl font-black app-text-main leading-tight">
                    หนังสติ๊กยุทธวิธี ยางแบนแรงสูง <span class="text-[#EE4D2D]">จัดส่งด่วน EMS / SPX ทั่วประเทศ</span>
                </h1>
                <p class="text-xs sm:text-sm app-text-muted leading-relaxed max-w-2xl">
                    ด้ามจับอัลลอยด์ CNC เลเซอร์ช่วยเล็ง ยางแบนสโลปทนทาน ลูกเหล็กขัดเงามาตรฐาน แตะที่รูปภาพเพื่อสั่งซื้อด่วน หรือกดดูรีวิวจาก Shopee ได้ทันที
                </p>
            </div>

            <!-- Categories Filter & Search Bar -->
            <div class="app-card p-3 sm:p-4 rounded-3xl border-2 shadow-sm space-y-3">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <!-- Category Pills -->
                    <div class="flex flex-wrap items-center gap-1.5">
                        <button onclick="filterCategory('all')" data-category="all" class="cat-filter-btn px-3.5 py-1.5 rounded-2xl text-xs font-bold bg-[#EE4D2D] text-white shadow-md transition-all">
                            ทั้งหมด
                        </button>
                        <button onclick="filterCategory('slingshot')" data-category="slingshot" class="cat-filter-btn px-3.5 py-1.5 rounded-2xl text-xs font-bold app-card-subtle app-text-main border app-border hover:border-[#EE4D2D] transition-all">
                            🎯 หนังสติ๊ก
                        </button>
                        <button onclick="filterCategory('rubber')" data-category="rubber" class="cat-filter-btn px-3.5 py-1.5 rounded-2xl text-xs font-bold app-card-subtle app-text-main border app-border hover:border-[#EE4D2D] transition-all">
                            ⚡ ยางหนังสติ๊ก
                        </button>
                        <button onclick="filterCategory('ammo')" data-category="ammo" class="cat-filter-btn px-3.5 py-1.5 rounded-2xl text-xs font-bold app-card-subtle app-text-main border app-border hover:border-[#EE4D2D] transition-all">
                            🔘 ลูกเหล็ก/กระสุน
                        </button>
                        <button onclick="filterCategory('accessories')" data-category="accessories" class="cat-filter-btn px-3.5 py-1.5 rounded-2xl text-xs font-bold app-card-subtle app-text-main border app-border hover:border-[#EE4D2D] transition-all">
                            🎒 อุปกรณ์เสริม/เลเซอร์
                        </button>
                    </div>

                    <!-- Search Input -->
                    <div class="relative w-full sm:w-64">
                        <input type="text" id="search-input" oninput="searchProducts()" placeholder="🔍 ค้นหาสินค้า..." class="w-full app-input border rounded-2xl pl-3 pr-3 py-2 text-xs focus:outline-none focus:ring-2 focus:ring-[#EE4D2D] font-medium">
                    </div>
                </div>
            </div>

            <!-- Product Grid Container (id="products-catalog-grid") -->
            <div id="products-catalog-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
                <!-- Loaded dynamically by JavaScript -->
            </div>
        </section>

        <!-- ================= VIEW 2: SINGLE-PAGE DIRECT-TO-CHECKOUT ================= -->
        <section id="view-checkout" class="hidden space-y-5 max-w-4xl mx-auto">
            
            <button onclick="showCatalogView()" class="app-card-subtle app-text-main hover:text-[#EE4D2D] text-xs font-bold px-3.5 py-2 rounded-2xl border app-border flex items-center gap-1 shadow-sm transition-all active:scale-95">
                ← กลับไปดูสินค้าทั้งหมด
            </button>

            <!-- Product Detail Card -->
            <div class="grid grid-cols-1 md:grid-cols-12 gap-5 app-card border-2 rounded-3xl p-4 sm:p-6 shadow-sm">
                <!-- Gallery -->
                <div class="md:col-span-5 space-y-3">
                    <div class="w-full h-64 sm:h-72 app-card-subtle rounded-2xl border app-border p-2 flex items-center justify-center overflow-hidden cursor-pointer relative group" onclick="openGalleryModal()">
                        <img id="detail-main-img" src="" class="max-h-full max-w-full object-contain transition-transform duration-300 group-hover:scale-105">
                        <div class="absolute bottom-2 right-2 bg-black/60 text-white text-[10px] px-2 py-0.5 rounded-full font-bold">
                            🔍 <span id="detail-gallery-label">แตะดูรูปใหญ่</span>
                        </div>
                    </div>

                    <!-- Thumbnails Strip -->
                    <div id="detail-thumbs-strip" class="flex gap-2 overflow-x-auto pb-1"></div>
                </div>

                <!-- Info & Variants -->
                <div class="md:col-span-7 space-y-3.5 flex flex-col justify-between">
                    <div class="space-y-2.5">
                        <span id="detail-cat-tag" class="app-badge text-[10px] px-2.5 py-0.5 rounded-full font-black uppercase inline-block border">SLINGSHOT</span>
                        <h2 id="detail-title" class="text-base sm:text-xl font-black app-text-main leading-snug"></h2>
                        <p id="detail-desc" class="text-xs app-text-muted leading-relaxed"></p>

                        <!-- Stock Badge -->
                        <span id="detail-stock-badge" class="inline-block bg-emerald-50 text-emerald-700 border border-emerald-300 text-[10px] font-bold px-2 py-0.5 rounded-full">
                            มีสินค้าพร้อมส่ง
                        </span>

                        <!-- Variants -->
                        <div class="space-y-1.5 pt-2 border-t app-border">
                            <label class="text-xs font-bold app-text-main block">เลือกตัวเลือก / สเปกสินค้า:</label>
                            <div id="detail-variant-pills" class="flex flex-wrap gap-1.5"></div>
                        </div>

                        <!-- Quantity Selector -->
                        <div class="flex items-center justify-between pt-2 border-t app-border">
                            <label class="text-xs font-bold app-text-main">จำนวนที่ต้องการสั่งซื้อ:</label>
                            <div class="flex items-center gap-2 app-card-subtle border app-border rounded-xl p-1">
                                <button type="button" onclick="changeQuantity(-1)" class="w-7 h-7 bg-white dark:bg-[#1A1A20] rounded-lg font-black text-slate-700 dark:text-slate-200">-</button>
                                <span id="detail-qty-display" class="w-8 text-center font-black text-sm app-text-main">1</span>
                                <button type="button" onclick="changeQuantity(1)" class="w-7 h-7 bg-white dark:bg-[#1A1A20] rounded-lg font-black text-slate-700 dark:text-slate-200">+</button>
                            </div>
                        </div>
                    </div>

                    <!-- Shopee Affiliate Review Box -->
                    <div id="shopee-affiliate-box" class="pt-2 border-t app-border hidden">
                        <a id="shopee-affiliate-btn" href="" target="_blank" class="w-full bg-[#FFF2EE] hover:bg-[#FFE3DC] border-2 border-[#FFD5CC] text-[#EE4D2D] py-2 rounded-2xl text-xs font-bold flex items-center justify-center gap-1.5 shadow-sm transition-all">
                            <span>⭐ ดูรีวิวสินค้าจริงบน Shopee (Shopee Mall) ↗</span>
                        </a>
                    </div>
                </div>
            </div>

            <!-- Guest Address Form & Payment Box -->
            <div class="app-card border-2 rounded-3xl p-4 sm:p-6 space-y-5 shadow-sm">
                
                <!-- 1. Address -->
                <div class="space-y-3">
                    <h3 class="text-sm font-black app-text-main flex items-center gap-2 border-b app-border pb-2">
                        <span>📍</span> ข้อมูลผู้รับและที่อยู่จัดส่ง (Guest Checkout)
                    </h3>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div>
                            <label class="block text-xs font-bold app-text-main mb-1">ชื่อ-นามสกุล ผู้รับ *</label>
                            <input type="text" id="cust-name" placeholder="เช่น คุณสมชาย ใจดี" class="w-full app-input border rounded-xl px-3 py-2 text-xs">
                        </div>
                        <div>
                            <label class="block text-xs font-bold app-text-main mb-1">เบอร์โทรศัพท์ (ติดต่อส่งของ) *</label>
                            <input type="tel" id="cust-phone" oninput="onPhoneChange(this.value)" placeholder="เช่น 081-999-8877" class="w-full app-input border rounded-xl px-3 py-2 text-xs">
                        </div>
                    </div>
                    <div>
                        <label class="block text-xs font-bold app-text-main mb-1">บ้านเลขที่, หมู่, ซอย, ถนน *</label>
                        <input type="text" id="cust-address-line" placeholder="เช่น 45/2 หมู่ 3 ซอยสุขุมวิท 10" class="w-full app-input border rounded-xl px-3 py-2 text-xs">
                    </div>
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
                        <div>
                            <label class="block text-xs font-bold app-text-main mb-1">รหัสไปรษณีย์ *</label>
                            <input type="text" id="cust-postcode" maxlength="5" oninput="handlePostalCodeInput(this.value)" placeholder="เช่น 10150" class="w-full app-input border rounded-xl px-3 py-2 text-xs font-mono font-bold text-[#EE4D2D]">
                        </div>
                        <div>
                            <label class="block text-xs font-bold app-text-main mb-1">ตำบล/แขวง</label>
                            <input type="text" id="cust-subdistrict" placeholder="ตำบล/แขวง" class="w-full app-input border rounded-xl px-3 py-2 text-xs">
                        </div>
                        <div>
                            <label class="block text-xs font-bold app-text-main mb-1">อำเภอ/เขต</label>
                            <input type="text" id="cust-district" placeholder="อำเภอ/เขต" class="w-full app-input border rounded-xl px-3 py-2 text-xs">
                        </div>
                        <div>
                            <label class="block text-xs font-bold app-text-main mb-1">จังหวัด</label>
                            <input type="text" id="cust-province" placeholder="จังหวัด" class="w-full app-input border rounded-xl px-3 py-2 text-xs">
                        </div>
                    </div>

                    <!-- Carrier Auto-Allocation Badge -->
                    <div class="app-card-subtle p-3 rounded-2xl border app-border space-y-1">
                        <div class="flex justify-between items-center text-xs">
                            <span class="app-text-main font-bold flex items-center gap-1">
                                <span>🚚</span> ขนส่งที่ระบบจัดสรร: <span id="carrier-allocated-badge" class="text-[#EE4D2D] font-black">SPX Express (Shopee Express)</span>
                            </span>
                            <span id="carrier-fee-badge" class="bg-emerald-50 text-emerald-700 border border-emerald-200 text-[10px] px-2 py-0.5 rounded font-bold">ส่งฟรี (฿0)</span>
                        </div>
                        <p id="carrier-allocated-desc" class="text-[10px] app-text-muted leading-relaxed">
                            • จัดส่งมาตรฐานในเขตพื้นที่ทั่วไป (SPX Express ด่วนทั่วไทย)
                        </p>
                    </div>
                </div>

                <!-- 2. Payment Method -->
                <div class="space-y-3 pt-2 border-t app-border">
                    <h3 class="text-sm font-black app-text-main flex items-center gap-2">
                        <span>💳</span> เลือกช่องทางการชำระเงิน
                    </h3>

                    <!-- 3 Payment Tabs -->
                    <div class="grid grid-cols-3 gap-2">
                        <button type="button" onclick="setPaymentMethod('PROMPTPAY')" id="btn-pay-promptpay" class="p-2.5 rounded-2xl border-2 border-[#EE4D2D] bg-[#FFF2EE] text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-0.5 shadow-sm transition-all text-center">
                            <span class="text-base">📱</span>
                            <span class="text-[11px] sm:text-xs">พร้อมเพย์</span>
                            <span class="text-[9px] text-emerald-700 font-normal">ฟรีค่าส่งเมื่อครบ 200</span>
                        </button>

                        <button type="button" onclick="setPaymentMethod('COD')" id="btn-pay-cod" class="p-2.5 rounded-2xl border-2 app-border app-card-subtle app-text-main text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center">
                            <span class="text-base">💵</span>
                            <span class="text-[11px] sm:text-xs">เก็บปลายทาง</span>
                            <span class="text-[9px] text-[#EE4D2D] font-bold">บวก 3%</span>
                        </button>

                        <button type="button" onclick="setPaymentMethod('STORE_CREDIT')" id="btn-pay-wallet" class="p-2.5 rounded-2xl border-2 app-border app-card-subtle app-text-main text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center">
                            <span class="text-base">👛</span>
                            <span class="text-[11px] sm:text-xs">กระเป๋าเครดิต</span>
                            <span id="wallet-btn-bal" class="text-[9px] text-emerald-700 font-normal">฿530.00</span>
                        </button>
                    </div>

                    <!-- PROMPTPAY PANEL -->
                    <div id="panel-promptpay" class="app-card-subtle border app-border rounded-2xl p-4 space-y-3 text-center">
                        <span class="text-xs app-text-muted block">ยอดชำระสุทธิ (สแกนผ่านแอปธนาคาร):</span>
                        <p id="promptpay-amount-display" class="text-2xl sm:text-3xl font-black text-[#EE4D2D]">฿390.00</p>
                        <div class="flex justify-center">
                            <img id="promptpay-qr-img" src="" class="w-44 h-44 rounded-xl border-2 app-border bg-white p-2">
                        </div>
                        <div class="text-xs app-text-muted space-y-1">
                            <p><strong>ชื่อบัญชี:</strong> สุเมธา แท่นธรรมโรจน์ (กสิกรไทย)</p>
                            <div class="flex items-center justify-center gap-2">
                                <span>เลขพร้อมเพย์: <strong class="font-mono text-sm app-text-main">061-537-2239</strong></span>
                                <button type="button" onclick="copyPromptPay()" class="bg-[#EE4D2D] text-white text-[10px] px-2 py-0.5 rounded font-bold">คัดลอก</button>
                            </div>
                        </div>
                        <label class="inline-block bg-[#EE4D2D] hover:bg-[#d73211] text-white text-xs px-4 py-2 rounded-xl font-bold cursor-pointer shadow-md active:scale-95">
                            📎 แนบสลิปโอนเงิน (Anti-Replay)
                            <input type="file" accept="image/*" onchange="handleSlipFile(this)" class="hidden">
                        </label>
                        <p id="slip-status-msg" class="text-xs text-emerald-600 font-bold hidden"></p>
                    </div>

                    <!-- COD PANEL -->
                    <div id="panel-cod" class="bg-[#FFF8F5] border-2 border-[#FFD5CC] rounded-2xl p-4 space-y-2.5 hidden text-[#2C241E]">
                        <div class="flex items-center gap-2.5">
                            <span class="text-2xl">💵</span>
                            <div>
                                <h4 class="font-bold text-xs sm:text-sm text-[#2C241E]">บริการเก็บเงินปลายทาง (Cash on Delivery)</h4>
                                <p class="text-[10px] text-slate-600">มีค่าบริการเก็บเงินปลายทาง +3% ของยอดรวม</p>
                            </div>
                        </div>
                        <div class="bg-white p-2.5 rounded-xl border border-[#FFD5CC] text-xs space-y-1 text-slate-700">
                            <div class="flex justify-between"><span>ราคาสินค้า + ค่าส่ง:</span> <span id="cod-base-amount" class="font-bold">฿0.00</span></div>
                            <div class="flex justify-between text-[#EE4D2D]"><span>ค่าบริการ COD (+3%):</span> <span id="cod-fee-amount" class="font-bold">+฿0.00</span></div>
                            <div class="border-t border-slate-100 pt-1 flex justify-between font-black text-sm text-[#2C241E]">
                                <span>ยอดชำระเมื่อรับพัสดุ:</span>
                                <span id="cod-total-amount" class="text-[#EE4D2D]">฿0.00</span>
                            </div>
                        </div>
                        <p class="text-[10px] text-slate-500 bg-orange-50/70 p-2 rounded-lg border border-orange-100">
                            💡 ไม่ต้องโอนเงินล่วงหน้า กรุณาเตรียมเงินสดพอดีให้กับพนักงานขนส่งเมื่อพัสดุไปถึงครับ
                        </p>
                    </div>

                    <!-- WALLET PANEL -->
                    <div id="panel-wallet" class="app-card-subtle border app-border rounded-2xl p-4 space-y-3 hidden">
                        <div class="flex justify-between items-center">
                            <span class="text-xs app-text-muted">ยอดเงินในกระเป๋าเครดิต:</span>
                            <span id="wallet-balance-big" class="text-sm font-black text-emerald-600">฿530.00</span>
                        </div>
                        <div class="bg-white dark:bg-[#1A1A20] p-3 rounded-xl border app-border text-xs space-y-1">
                            <div class="flex justify-between app-text-muted"><span>ยอดชำระออเดอร์นี้:</span> <span id="wallet-order-amt" class="font-bold text-[#EE4D2D]">฿390.00</span></div>
                            <div class="flex justify-between app-text-muted"><span>ยอดคงเหลือหลังชำระ:</span> <span id="wallet-after-bal" class="font-bold text-emerald-600">฿140.00</span></div>
                        </div>
                    </div>
                </div>

                <!-- Order Pricing Breakdown Summary Table -->
                <div class="app-card-subtle p-4 rounded-2xl border app-border space-y-2 text-xs app-text-main">
                    <div class="flex justify-between">
                        <span>ราคาสินค้า (<span id="summary-variant-name">รุ่นมาตรฐาน</span> x<span id="summary-qty">1</span>):</span>
                        <span id="summary-subtotal" class="font-bold">฿390.00</span>
                    </div>
                    <div class="flex justify-between">
                        <span>ค่าจัดส่ง:</span>
                        <span id="summary-shipping" class="font-bold text-emerald-600">ฟรี (฿0.00)</span>
                    </div>
                    <div id="summary-cod-row" class="flex justify-between text-[#EE4D2D] hidden font-bold">
                        <span>ค่าบริการเก็บปลายทาง (COD +3%):</span>
                        <span id="summary-cod-fee">+฿0.00</span>
                    </div>
                    <div class="border-t app-border pt-2 flex justify-between text-base font-black app-text-main">
                        <span>ยอดสุทธิที่ต้องชำระ:</span>
                        <span id="summary-total" class="text-[#EE4D2D] text-lg font-black">฿390.00</span>
                    </div>
                </div>

                <!-- Submit Button -->
                <button type="button" onclick="submitDirectOrder()" class="w-full bg-[#EE4D2D] hover:bg-[#d73211] text-white font-extrabold py-3.5 rounded-2xl shadow-xl shadow-orange-500/25 transition-all text-sm sm:text-base flex items-center justify-center gap-2 active:scale-95 cursor-pointer">
                    <span id="submit-btn-text">⚡ สั่งซื้อทันที (฿390.00)</span>
                </button>
            </div>
        </section>
    </main>

    <!-- FOOTER -->
    <footer class="app-header border-t-2 py-6 text-center text-xs app-text-muted space-y-1">
        <p class="font-bold app-text-main">GOODSTONE TACTICAL SLINGSHOT © 2026</p>
        <p>Single-Page Direct-to-Checkout • จัดส่งด่วน SPX Express / ไปรษณีย์ไทย EMS • พร้อมเพย์ & COD +3%</p>
    </footer>

    <!-- JAVASCRIPT LOGIC -->
    <script>
        const DEFAULT_PRODUCTS = """ + products_json + """;

        let products = DEFAULT_PRODUCTS;
        let selectedProduct = DEFAULT_PRODUCTS[0];
        let selectedVariantIdx = 0;
        let selectedCategory = "all";
        let quantity = 1;
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
            } else {
                if (icon) icon.innerText = "☀️";
                if (text) text.innerText = "โหมดสว่าง";
            }
        }

        function toggleTheme() {
            const next = currentTheme === "dark" ? "light" : "dark";
            applyTheme(next);
        }

        function init() {
            applyTheme(currentTheme);
            lucide.createIcons();

            const savedProds = localStorage.getItem("goodstone_products");
            if (savedProds) {
                try {
                    const parsed = JSON.parse(savedProds);
                    if (Array.isArray(parsed) && parsed.length > 0) {
                        products = parsed;
                    }
                } catch(e) {}
            } else {
                localStorage.setItem("goodstone_products", JSON.stringify(DEFAULT_PRODUCTS));
            }

            selectedProduct = products[0] || DEFAULT_PRODUCTS[0];
            selectedVariantIdx = 0;
            quantity = 1;

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
            renderProductCheckoutDetail();
            updateCalculations();
        }

        function showCatalogView() {
            document.getElementById("view-catalog").classList.remove("hidden");
            document.getElementById("view-checkout").classList.add("hidden");
            window.scrollTo({ top: 0, behavior: "smooth" });
        }

        function openProductDirectCheckout(productId) {
            const p = products.find(x => x.id === productId);
            if (p) {
                selectedProduct = p;
                selectedVariantIdx = 0;
                quantity = 1;
                renderProductCheckoutDetail();
                updateCalculations();
                document.getElementById("view-catalog").classList.add("hidden");
                document.getElementById("view-checkout").classList.remove("hidden");
                window.scrollTo({ top: 0, behavior: "smooth" });
            }
        }

        function filterCategory(cat) {
            selectedCategory = cat;
            renderCatalogGrid();
        }

        function searchProducts() {
            renderCatalogGrid();
        }

        // ================= RENDER CATALOG GRID (FIXED CONTAINER ID) =================
        function renderCatalogGrid() {
            const container = document.getElementById("products-catalog-grid");
            if (!container) return;

            const query = (document.getElementById("search-input")?.value || "").toLowerCase().trim();
            container.innerHTML = "";

            // Update category pills
            const catButtons = document.querySelectorAll(".cat-filter-btn");
            catButtons.forEach(btn => {
                const cat = btn.getAttribute("data-category");
                if (cat === selectedCategory) {
                    btn.className = "cat-filter-btn px-3.5 py-1.5 rounded-2xl text-xs font-bold bg-[#EE4D2D] text-white shadow-md transition-all";
                } else {
                    btn.className = "cat-filter-btn px-3.5 py-1.5 rounded-2xl text-xs font-bold app-card-subtle app-text-main border app-border hover:border-[#EE4D2D] transition-all";
                }
            });

            const filtered = products.filter(p => {
                const matchCat = (selectedCategory === "all" || p.category === selectedCategory);
                const matchQuery = !query || p.name.toLowerCase().includes(query) || (p.description && p.description.toLowerCase().includes(query));
                return matchCat && matchQuery;
            });

            if (filtered.length === 0) {
                container.innerHTML = `<div class="col-span-full py-12 text-center app-text-muted text-sm">ไม่พบสินค้าที่ตรงกับการค้นหา</div>`;
                return;
            }

            filtered.forEach(p => {
                const minPrice = (p.variants && p.variants.length > 0)
                    ? Math.min(...p.variants.map(v => Number(v.price) || p.price))
                    : p.price;
                const imgSrc = p.image_file || p.fallback_image;
                const shopeeUrl = p.shopee_affiliate_url || "https://th.shp.ee/sdFv2cS1";

                const card = document.createElement("div");
                card.className = "app-card rounded-3xl border-2 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group";
                card.innerHTML = `
                    <div>
                        <!-- Clickable Product Image triggers Direct Checkout -->
                        <div onclick="openProductDirectCheckout('${p.id}')" class="h-48 sm:h-52 overflow-hidden app-card-subtle relative flex items-center justify-center cursor-pointer group/img border-b app-border">
                            <img src="${imgSrc}" onerror="this.onerror=null; this.src='${p.fallback_image}';" class="w-full h-full object-contain p-3 transition-transform duration-300 group-hover/img:scale-105" alt="${p.name}">
                            <span class="absolute top-2.5 left-2.5 app-badge border text-[9px] px-2 py-0.5 rounded-full font-black uppercase tracking-wider">
                                ${p.category}
                            </span>
                            <span class="absolute bottom-2.5 right-2.5 bg-black/60 text-white text-[9px] px-2 py-0.5 rounded-full font-bold">
                                ⚡ แตะสั่งซื้อด่วน
                            </span>
                        </div>

                        <!-- Info Area -->
                        <div class="p-4 space-y-2">
                            <h3 onclick="openProductDirectCheckout('${p.id}')" class="font-bold app-text-main text-xs sm:text-sm line-clamp-2 cursor-pointer hover:text-[#EE4D2D] transition-colors leading-snug">
                                ${p.name}
                            </h3>
                            <p class="text-[11px] app-text-muted line-clamp-1">${p.description || ''}</p>
                        </div>
                    </div>

                    <!-- Actions Area: Price + Direct Checkout Button + Shopee Review Button -->
                    <div class="p-4 pt-0 space-y-2.5">
                        <div class="flex items-center justify-between">
                            <div>
                                <span class="text-[9px] app-text-muted block">เริ่มต้น</span>
                                <span class="text-base font-black text-[#EE4D2D]">฿${Number(minPrice).toLocaleString(undefined, {minimumFractionDigits: 0})}</span>
                            </div>
                            <button onclick="openProductDirectCheckout('${p.id}')" class="bg-[#EE4D2D] hover:bg-[#d73211] text-white px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-1 shadow-md active:scale-95 cursor-pointer">
                                <span>⚡ ซื้อด่วน</span>
                            </button>
                        </div>

                        <!-- PROMINENT PER-PRODUCT SHOPEE REVIEW BUTTON -->
                        <a href="${shopeeUrl}" target="_blank" onclick="event.stopPropagation()" class="w-full bg-[#FFF2EE] hover:bg-[#FFE3DC] border border-[#FFD5CC] text-[#EE4D2D] py-1.5 rounded-xl text-[11px] font-bold flex items-center justify-center gap-1 shadow-sm transition-all">
                            <span>⭐ ดูรีวิวใน Shopee ></span>
                        </a>
                    </div>
                `;
                container.appendChild(card);
            });
        }

        // ================= RENDER DIRECT CHECKOUT VIEW =================
        function renderProductCheckoutDetail() {
            if (!selectedProduct) {
                selectedProduct = (products && products.length > 0) ? products[0] : DEFAULT_PRODUCTS[0];
            }
            const p = selectedProduct;

            document.getElementById("detail-title").innerText = p.name || "";
            document.getElementById("detail-desc").innerText = p.description || "";
            document.getElementById("detail-cat-tag").innerText = (p.category || "slingshot").toUpperCase();
            document.getElementById("detail-stock-badge").innerText = `สต็อก: ${p.stock || 20} ชิ้น`;

            const images = (p.images && p.images.length > 0) ? p.images : [{ file: p.image_file || p.fallback_image, name: `${p.id}_main.jpg` }];
            document.getElementById("detail-main-img").src = images[0].file;
            document.getElementById("detail-gallery-label").innerText = `แตะดูรูปใหญ่ (${images.length} ภาพ)`;

            // Thumbnails Strip
            const thumbsStrip = document.getElementById("detail-thumbs-strip");
            thumbsStrip.innerHTML = "";
            images.forEach((img, idx) => {
                const thumb = document.createElement("div");
                thumb.className = `w-14 h-14 rounded-xl p-1 app-card-subtle border-2 cursor-pointer transition-all flex-shrink-0 flex items-center justify-center ${idx === 0 ? "border-[#EE4D2D] scale-105 shadow-md" : "app-border opacity-70"}`;
                thumb.innerHTML = `<img src="${img.file}" class="w-full h-full object-contain">`;
                thumb.onclick = () => {
                    document.getElementById("detail-main-img").src = img.file;
                    Array.from(thumbsStrip.children).forEach((c, i) => {
                        c.className = `w-14 h-14 rounded-xl p-1 app-card-subtle border-2 cursor-pointer transition-all flex-shrink-0 flex items-center justify-center ${i === idx ? "border-[#EE4D2D] scale-105 shadow-md" : "app-border opacity-70"}`;
                    });
                };
                thumbsStrip.appendChild(thumb);
            });

            // Shopee Affiliate Button
            const shopeeBox = document.getElementById("shopee-affiliate-box");
            const shopeeBtn = document.getElementById("shopee-affiliate-btn");
            if (p.shopee_affiliate_url) {
                shopeeBtn.href = p.shopee_affiliate_url;
                shopeeBox.classList.remove("hidden");
            } else {
                shopeeBox.classList.add("hidden");
            }

            // Ensure variants exists
            if (!p.variants || !Array.isArray(p.variants) || p.variants.length === 0) {
                p.variants = [{ name: "รุ่นมาตรฐาน", price: Number(p.price) || 390, stock: Number(p.stock) || 20 }];
            }
            if (selectedVariantIdx < 0 || selectedVariantIdx >= p.variants.length) {
                selectedVariantIdx = 0;
            }

            // Variant Pills
            const pillsContainer = document.getElementById("detail-variant-pills");
            pillsContainer.innerHTML = "";
            p.variants.forEach((v, idx) => {
                const isSel = (idx === selectedVariantIdx);
                const vPrice = Number(v.price) || Number(p.price) || 390;
                const btn = document.createElement("button");
                btn.type = "button";
                btn.className = `px-3.5 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 ${isSel ? "bg-[#EE4D2D] text-white border-2 border-[#d73211] shadow-md scale-105" : "app-card-subtle hover:border-[#EE4D2D] app-text-main border app-border"}`;
                btn.innerHTML = `${isSel ? "<span>✓</span>" : ""}<span>${v.name}</span><span class="${isSel ? "bg-black/30 text-amber-300" : "app-badge"} text-[11px] px-1.5 py-0.5 rounded font-black">฿${vPrice.toLocaleString()}</span>`;
                btn.onclick = () => {
                    selectedVariantIdx = idx;
                    renderProductCheckoutDetail();
                    updateCalculations();
                };
                pillsContainer.appendChild(btn);
            });

            document.getElementById("detail-qty-display").innerText = quantity;
        }

        function changeQuantity(delta) {
            quantity = Math.max(1, quantity + delta);
            document.getElementById("detail-qty-display").innerText = quantity;
            updateCalculations();
        }

        function getActiveVariant() {
            if (!selectedProduct) {
                selectedProduct = (products && products.length > 0) ? products[0] : DEFAULT_PRODUCTS[0];
            }
            const basePrice = Number(selectedProduct.price) || 390;
            if (!selectedProduct.variants || !Array.isArray(selectedProduct.variants) || selectedProduct.variants.length === 0) {
                return { name: "รุ่นมาตรฐาน", price: basePrice, stock: Number(selectedProduct.stock) || 20 };
            }
            if (selectedVariantIdx < 0 || selectedVariantIdx >= selectedProduct.variants.length) {
                selectedVariantIdx = 0;
            }
            const v = selectedProduct.variants[selectedVariantIdx];
            if (!v) {
                return { name: "รุ่นมาตรฐาน", price: basePrice, stock: Number(selectedProduct.stock) || 20 };
            }
            const vPrice = Number(v.price);
            return {
                name: v.name || "รุ่นมาตรฐาน",
                price: (!isNaN(vPrice) && vPrice > 0) ? vPrice : basePrice,
                stock: Number(v.stock) || 20
            };
        }

        // ================= BULLETPROOF PRICING & COD CALCULATION =================
        function updateCalculations() {
            const activeV = getActiveVariant();
            const unitPrice = Number(activeV.price) || 390;
            const qty = Math.max(1, Number(quantity) || 1);
            const subtotal = unitPrice * qty;
            const isFreeShipping = (subtotal >= 200);
            const shippingCost = isFreeShipping ? 0 : 25;
            const baseTotal = subtotal + shippingCost;
            const codFee = (paymentMethod === "COD") ? Number((baseTotal * 0.03).toFixed(2)) : 0;
            const total = Number((baseTotal + codFee).toFixed(2));

            const varNameEl = document.getElementById("summary-variant-name");
            if (varNameEl) varNameEl.innerText = activeV.name;

            const qtyEl = document.getElementById("summary-qty");
            if (qtyEl) qtyEl.innerText = qty;

            const subtotalEl = document.getElementById("summary-subtotal");
            if (subtotalEl) subtotalEl.innerText = `฿${subtotal.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;

            const shipEl = document.getElementById("summary-shipping");
            if (shipEl) shipEl.innerText = isFreeShipping ? "ฟรี (฿0.00)" : "฿25.00";

            const codRow = document.getElementById("summary-cod-row");
            if (codRow) {
                if (paymentMethod === "COD") {
                    codRow.classList.remove("hidden");
                    document.getElementById("summary-cod-fee").innerText = `+฿${codFee.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;
                } else {
                    codRow.classList.add("hidden");
                }
            }

            const totalEl = document.getElementById("summary-total");
            if (totalEl) totalEl.innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;

            const ppEl = document.getElementById("promptpay-amount-display");
            if (ppEl) ppEl.innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;

            const submitBtn = document.getElementById("submit-btn-text");
            if (submitBtn) {
                if (paymentMethod === "COD") {
                    submitBtn.innerText = `📦 สั่งซื้อแบบเก็บเงินปลายทาง (฿${total.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})})`;
                } else {
                    submitBtn.innerText = `⚡ สั่งซื้อทันที (฿${total.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})})`;
                }
            }

            const carrierFeeBadge = document.getElementById("carrier-fee-badge");
            if (carrierFeeBadge) carrierFeeBadge.innerText = isFreeShipping ? "ส่งฟรี (฿0)" : "฿25";

            const walletAmt = document.getElementById("wallet-order-amt");
            if (walletAmt) walletAmt.innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;

            const walletAfter = document.getElementById("wallet-after-bal");
            if (walletAfter) walletAfter.innerText = `฿${Math.max(0, userWallet.balance - total).toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;

            const codBaseEl = document.getElementById("cod-base-amount");
            if (codBaseEl) codBaseEl.innerText = `฿${baseTotal.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;

            const codFeeEl = document.getElementById("cod-fee-amount");
            if (codFeeEl) codFeeEl.innerText = `+฿${codFee.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;

            const codTotalEl = document.getElementById("cod-total-amount");
            if (codTotalEl) codTotalEl.innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;

            // Dynamic PromptPay QR
            const ppPayload = generatePromptPayQR(total);
            const qrImg = document.getElementById("promptpay-qr-img");
            if (qrImg) qrImg.src = `https://api.qrserver.com/v1/create-qr-code/?size=260x260&margin=12&data=${encodeURIComponent(ppPayload)}`;
        }

        function setPaymentMethod(method) {
            paymentMethod = method;
            const btnPP = document.getElementById("btn-pay-promptpay");
            const btnCOD = document.getElementById("btn-pay-cod");
            const btnW = document.getElementById("btn-pay-wallet");
            const panelPP = document.getElementById("panel-promptpay");
            const panelCOD = document.getElementById("panel-cod");
            const panelW = document.getElementById("panel-wallet");

            btnPP.className = "p-2.5 rounded-2xl border-2 app-border app-card-subtle app-text-main text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";
            btnCOD.className = "p-2.5 rounded-2xl border-2 app-border app-card-subtle app-text-main text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";
            btnW.className = "p-2.5 rounded-2xl border-2 app-border app-card-subtle app-text-main text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";

            panelPP.classList.add("hidden");
            panelCOD.classList.add("hidden");
            panelW.classList.add("hidden");

            if (method === "PROMPTPAY") {
                btnPP.className = "p-2.5 rounded-2xl border-2 border-[#EE4D2D] bg-[#FFF2EE] text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-0.5 shadow-sm transition-all text-center";
                panelPP.classList.remove("hidden");
            } else if (method === "COD") {
                btnCOD.className = "p-2.5 rounded-2xl border-2 border-[#EE4D2D] bg-[#FFF2EE] text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-0.5 shadow-sm transition-all text-center";
                panelCOD.classList.remove("hidden");
            } else if (method === "STORE_CREDIT") {
                btnW.className = "p-2.5 rounded-2xl border-2 border-[#EE4D2D] bg-[#FFF2EE] text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-0.5 shadow-sm transition-all text-center";
                panelW.classList.remove("hidden");
            }
            updateCalculations();
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

        function handlePostalCodeInput(val) {
            const clean = val.replace(/[^0-9]/g, "").substring(0, 5);
            document.getElementById("cust-postcode").value = clean;
            if (clean.length === 5) {
                const isRemote = clean.startsWith("94") || clean.startsWith("95") || clean.startsWith("96") || clean.startsWith("58") || ["84320", "84360", "23170", "23120", "81150", "82160", "63170", "50310"].includes(clean);
                const badge = document.getElementById("carrier-allocated-badge");
                const desc = document.getElementById("carrier-allocated-desc");

                if (isRemote) {
                    badge.innerText = "ไปรษณีย์ไทย ด่วนพิเศษ (EMS)";
                    desc.innerText = "จัดส่งด่วนพื้นที่ห่างไกล / เกาะ / 3 จังหวัดชายแดนใต้ (EMS ด่วนพิเศษ ไม่คิดค่าพื้นที่ห่างไกล 50 บาท)";
                } else {
                    badge.innerText = "SPX Express (Shopee Express)";
                    desc.innerText = "จัดส่งมาตรฐานในเขตพื้นที่ทั่วไป (SPX Express ด่วนทั่วไทย)";
                }

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

        function handleSlipFile(input) {
            const file = input.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = function(e) {
                slipImageBase64 = e.target.result;
                const msgBox = document.getElementById("slip-status-msg");
                msgBox.classList.remove("hidden");
                msgBox.innerText = "✅ แนบสลิปโอนเงินเรียบร้อยแล้ว";
            };
            reader.readAsDataURL(file);
        }

        function copyPromptPay() {
            navigator.clipboard.writeText("0615372239").then(() => {
                alert("คัดลอกเลขพร้อมเพย์ 061-537-2239 แล้วครับ!");
            });
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

            const activeV = getActiveVariant();
            const subtotal = activeV.price * quantity;
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
                alert(`📦 สั่งซื้อแบบเก็บเงินปลายทาง (COD) สำเร็จ!\nรหัสคำสั่งซื้อ: ${newOrder.id}\nยอดชำระเมื่อของถึง: ฿${newOrder.total_amount.toLocaleString(undefined, {minimumFractionDigits: 2})}\nขนส่ง: ${newOrder.shipping_provider}\nเลขพัสดุ: ${newOrder.tracking_number}`);
            } else {
                alert(`🎉 สั่งซื้อและชำระเงินสำเร็จ!\nรหัสคำสั่งซื้อ: ${newOrder.id}\nขนส่งที่จัดสรร: ${newOrder.shipping_provider}\nเลขพัสดุ: ${newOrder.tracking_number}`);
            }
            window.location.href = "track.html";
        }

        // ================= PROMPTPAY QR GENERATOR =================
        function generatePromptPayQR(amount) {
            const clean = "0615372239".replace(/[^0-9]/g, "");
            let target = clean;
            if (clean.length === 10 && clean.startsWith("0")) {
                target = "0066" + clean.substring(1);
            }
            const tag00 = "000201";
            const tag01 = "010211";
            const tag29_00 = "0016A000000677010111";
            const tag29_01 = "01" + String(target.length).padStart(2, "0") + target;
            const tag29_val = tag29_00 + tag29_01;
            const tag29 = "29" + String(tag29_val.length).padStart(2, "0") + tag29_val;
            const tag53 = "5303764";
            const amtStr = Number(amount).toFixed(2);
            const tag54 = "54" + String(amtStr.length).padStart(2, "0") + amtStr;
            const tag58 = "5802TH";
            const raw = tag00 + tag01 + tag29 + tag53 + tag54 + tag58 + "6304";
            const crc = crc16(raw);
            return raw + crc.toUpperCase();
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

        window.onload = init;
    </script>
</body>
</html>"""

with open("/working_dir/slingshot-shop/index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print("slingshot-shop/index.html successfully rebuilt!")
