import json

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))
products_json = json.dumps(data["products"], ensure_ascii=False)
orders_json = json.dumps(data["orders"], ensure_ascii=False)

index_html_code = """<!DOCTYPE html>
<html lang="th" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>GOODSTONE - ร้านหนังสติ๊กยุทธวิธีเกรดพรีเมียม & อุปกรณ์ครบวงจร</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
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
            --bg-body: #111114;
            --bg-header: #191920;
            --bg-card: #1D1D24;
            --bg-card-subtle: #252530;
            --bg-input: #15151B;
            --border-main: #363645;
            --border-subtle: #2C2C38;
            --text-main: #FFFFFF;
            --text-muted: #B8B8C8;
            --text-sub: #8E8E9F;
            --badge-bg: #2D1B17;
            --badge-border: #5A2B20;
            --badge-text: #FF7555;
            --hero-from: #261B18;
            --hero-via: #201C22;
            --hero-to: #1A1A22;
        }

        /* Light Theme (Warm Cream) */
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
        }

        .theme-body { background-color: var(--bg-body) !important; color: var(--text-main) !important; }
        .theme-header { background-color: var(--bg-header) !important; border-color: var(--border-main) !important; }
        .theme-card { background-color: var(--bg-card) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .theme-card-subtle { background-color: var(--bg-card-subtle) !important; border-color: var(--border-subtle) !important; }
        .theme-input { background-color: var(--bg-input) !important; border-color: var(--border-main) !important; color: var(--text-main) !important; }
        .theme-text-main { color: var(--text-main) !important; }
        .theme-text-muted { color: var(--text-muted) !important; }
        .theme-badge { background-color: var(--badge-bg) !important; border-color: var(--badge-border) !important; color: var(--badge-text) !important; }
        .theme-hero { background: linear-gradient(135deg, var(--hero-from), var(--hero-via), var(--hero-to)) !important; border-color: var(--border-main) !important; }
    </style>
</head>
<body class="theme-body min-h-screen flex flex-col font-sans" data-theme="dark">

    <!-- HEADER (RESPONSIVE WITH THEME TOGGLE) -->
    <header class="sticky top-0 z-40 theme-header border-b-2 shadow-sm">
        <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <!-- Logo -->
                <div class="flex items-center gap-2.5 sm:gap-3 cursor-pointer" onclick="showCatalogView()">
                    <div class="w-10 h-10 rounded-2xl bg-[#EE4D2D] flex items-center justify-center text-white font-black text-xl shadow-md shadow-orange-500/20 flex-shrink-0">
                        🎯
                    </div>
                    <div>
                        <span class="font-black text-base sm:text-lg tracking-wide theme-text-main">GOODSTONE</span>
                        <span class="text-[10px] sm:text-[11px] block theme-text-muted font-medium">ร้านหนังสติ๊กยุทธวิธีและอุปกรณ์</span>
                    </div>
                </div>

                <!-- Header Actions: Nav, Theme Toggle, Wallet -->
                <div class="flex items-center gap-2 sm:gap-4 text-xs font-bold">
                    <button onclick="showCatalogView()" class="theme-text-main hover:text-[#EE4D2D] transition-colors flex items-center gap-1">
                        <span>หน้าร้านค้า</span>
                    </button>
                    <a href="track.html" class="theme-text-muted hover:text-[#EE4D2D] transition-colors flex items-center gap-1">
                        <span>เช็คพัสดุ</span>
                    </a>

                    <!-- Theme Switcher (Default: Dark Mode) -->
                    <button type="button" onclick="toggleTheme()" id="theme-toggle-btn" class="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-[#363645] bg-[#252530] text-[#FFFFFF] hover:border-[#EE4D2D] text-xs font-bold transition-all shadow-sm active:scale-95 cursor-pointer">
                        <span id="theme-toggle-icon">🌙</span>
                        <span id="theme-toggle-text" class="hidden sm:inline">โหมดมืด</span>
                    </button>

                    <!-- Customer Wallet Badge -->
                    <div id="header-wallet-badge" class="hidden sm:flex items-center gap-1.5 theme-badge px-3 py-1.5 rounded-xl text-xs font-bold border">
                        <span>👛</span>
                        <span class="theme-text-muted">กระเป๋า:</span>
                        <span id="user-wallet-display" class="font-black text-[#EE4D2D]">฿0.00</span>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <!-- FREE SHIPPING PROMOTION BANNER -->
    <div class="bg-[#EE4D2D] text-white py-2 px-3 text-center text-xs font-bold shadow-sm">
        📮 ค่าจัดส่ง EMS/SPX 25 บาททั่วไทย (พิเศษ! สั่งซื้อครบ 200 บาทขึ้นไป จัดส่งฟรีทันที)
    </div>

    <!-- MAIN CONTAINER -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-3 sm:px-6 lg:px-8 py-4 sm:py-6 space-y-6">

        <!-- ================= VIEW 1: PRODUCT CATALOG / GRID ================= -->
        <section id="view-catalog" class="space-y-6">
            
            <!-- Hero Banner -->
            <div class="rounded-3xl theme-hero p-5 sm:p-8 border-2 shadow-sm space-y-2">
                <div class="inline-flex items-center gap-1.5 px-3 py-0.5 rounded-full theme-badge text-[11px] font-extrabold border">
                    <span>🔥 หนังสติ๊กยุทธวิธีเกรดพรีเมียม & อุปกรณ์ครบวงจร</span>
                </div>
                <h1 class="text-lg sm:text-2xl font-black theme-text-main leading-tight">
                    ศูนย์รวมหนังสติ๊กยุทธวิธี เลเซอร์ช่วยเล็ง ยางแบน และลูกเหล็กคุณภาพสูง
                </h1>
                <p class="text-xs sm:text-sm theme-text-muted">
                    จัดส่งด่วน SPX Express / ไปรษณีย์ไทย EMS • โอนพร้อมเพย์ 0% • เก็บเงินปลายทาง (COD +3%)
                </p>
            </div>

            <!-- Search & Categories Bar -->
            <div class="theme-card p-3.5 sm:p-4 rounded-3xl border-2 shadow-sm space-y-3">
                <div class="relative">
                    <span class="absolute left-3.5 top-2.5 text-slate-400">🔍</span>
                    <input type="text" id="search-input" oninput="handleSearch(this.value)" placeholder="ค้นหาสินค้า เช่น หนังสติ๊กเลเซอร์, ยางแบน 0.75mm, ลูกเหล็ก..." class="w-full theme-input border rounded-2xl pl-10 pr-4 py-2 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-[#EE4D2D] font-medium">
                </div>

                <!-- Category Filters -->
                <div class="flex items-center gap-1.5 overflow-x-auto pb-1 text-xs font-bold scrollbar-none">
                    <button onclick="filterCategory('all')" class="cat-pill px-3.5 py-1.5 rounded-xl border transition-all whitespace-nowrap bg-[#EE4D2D] text-white border-[#EE4D2D] shadow-sm">ทั้งหมด</button>
                    <button onclick="filterCategory('slingshot')" class="cat-pill px-3.5 py-1.5 rounded-xl border transition-all whitespace-nowrap theme-card-subtle theme-text-muted hover:text-[#EE4D2D]">🎯 หนังสติ๊ก</button>
                    <button onclick="filterCategory('rubber')" class="cat-pill px-3.5 py-1.5 rounded-xl border transition-all whitespace-nowrap theme-card-subtle theme-text-muted hover:text-[#EE4D2D]">⚡ ยางแบน</button>
                    <button onclick="filterCategory('ammo')" class="cat-pill px-3.5 py-1.5 rounded-xl border transition-all whitespace-nowrap theme-card-subtle theme-text-muted hover:text-[#EE4D2D]">🔘 ลูกเหล็ก</button>
                    <button onclick="filterCategory('accessories')" class="cat-pill px-3.5 py-1.5 rounded-xl border transition-all whitespace-nowrap theme-card-subtle theme-text-muted hover:text-[#EE4D2D]">🎒 อุปกรณ์</button>
                </div>
            </div>

            <!-- Product Grid -->
            <div id="product-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                <!-- Loaded dynamically -->
            </div>
        </section>

        <!-- ================= VIEW 2: SINGLE-PAGE DIRECT CHECKOUT ================= -->
        <section id="view-checkout" class="hidden space-y-6">
            
            <div class="flex items-center justify-between">
                <button onclick="showCatalogView()" class="theme-card hover:border-[#EE4D2D] theme-text-main text-xs font-bold px-3.5 py-2 rounded-2xl border-2 shadow-sm flex items-center gap-1 transition-all active:scale-95">
                    <span>← กลับไปดูสินค้าทั้งหมด</span>
                </button>
                <span class="theme-badge border text-[11px] font-black px-3 py-1 rounded-full">
                    ⚡ ซื้อด่วน (Direct Checkout)
                </span>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                
                <!-- Product Detail & Images (Left) -->
                <div class="lg:col-span-5 theme-card border-2 rounded-3xl p-4 sm:p-6 space-y-4 shadow-sm">
                    <div class="w-full h-64 sm:h-72 theme-card-subtle rounded-3xl border p-2 flex items-center justify-center overflow-hidden cursor-pointer" onclick="openGalleryModal()">
                        <img id="checkout-main-img" src="" class="max-h-full max-w-full object-contain">
                    </div>
                    
                    <!-- Thumbnails -->
                    <div id="checkout-gallery-thumbs" class="grid grid-cols-4 gap-2"></div>

                    <div class="space-y-1 pt-2 border-t border-slate-700/20">
                        <span id="checkout-prod-category" class="theme-badge border text-[9px] px-2 py-0.2 rounded-full font-black uppercase inline-block"></span>
                        <h2 id="checkout-prod-title" class="text-sm sm:text-base font-black theme-text-main leading-snug"></h2>
                        <p id="checkout-prod-desc" class="text-xs theme-text-muted line-clamp-3"></p>
                    </div>

                    <!-- Shopee Review Button in Checkout -->
                    <a id="checkout-shopee-review-btn" href="https://th.shp.ee/sdFv2cS1" target="_blank" class="w-full theme-badge hover:bg-orange-500/10 text-xs py-2 rounded-xl font-bold border flex items-center justify-center gap-1 transition-all">
                        <span>⭐ ดูรีวิวสินค้านี้บน Shopee ></span>
                    </a>
                </div>

                <!-- Order Form & Payment (Right) -->
                <div class="lg:col-span-7 theme-card border-2 rounded-3xl p-4 sm:p-6 space-y-5 shadow-sm">
                    
                    <!-- 1. Variants & Quantity -->
                    <div class="space-y-3">
                        <h3 class="text-xs sm:text-sm font-black theme-text-main flex items-center gap-1.5 border-b pb-2 border-slate-700/20">
                            <span class="w-5 h-5 rounded-full bg-[#EE4D2D] text-white flex items-center justify-center text-[10px] font-bold">1</span>
                            เลือกสเปกสินค้าและจำนวน
                        </h3>

                        <div class="space-y-1.5">
                            <label class="text-xs font-bold theme-text-muted">ตัวเลือกสินค้า:</label>
                            <div id="checkout-variants-container" class="flex flex-wrap gap-2"></div>
                        </div>

                        <div class="flex items-center justify-between pt-2 border-t border-slate-700/20">
                            <label class="text-xs font-bold theme-text-muted">จำนวน:</label>
                            <div class="flex items-center gap-2 theme-card-subtle border rounded-xl p-1">
                                <button type="button" onclick="changeQuantity(-1)" class="w-7 h-7 theme-card rounded-lg font-black theme-text-main shadow-sm">-</button>
                                <span id="checkout-quantity-display" class="w-8 text-center font-black text-sm theme-text-main">1</span>
                                <button type="button" onclick="changeQuantity(1)" class="w-7 h-7 theme-card rounded-lg font-black theme-text-main shadow-sm">+</button>
                            </div>
                        </div>
                    </div>

                    <!-- 2. Customer Address -->
                    <div class="space-y-3 pt-2">
                        <h3 class="text-xs sm:text-sm font-black theme-text-main flex items-center gap-1.5 border-b pb-2 border-slate-700/20">
                            <span class="w-5 h-5 rounded-full bg-[#EE4D2D] text-white flex items-center justify-center text-[10px] font-bold">2</span>
                            ข้อมูลผู้รับพัสดุ (ที่อยู่จัดส่ง)
                        </h3>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                            <div>
                                <label class="block text-xs font-bold theme-text-muted mb-1">ชื่อ-นามสกุล ผู้รับ *</label>
                                <input type="text" id="cust-name" placeholder="เช่น คุณสมชาย ใจดี" class="w-full theme-input border rounded-xl px-3 py-2 text-xs focus:ring-2 focus:ring-[#EE4D2D]">
                            </div>
                            <div>
                                <label class="block text-xs font-bold theme-text-muted mb-1">เบอร์โทรศัพท์ (ติดต่อส่งของ) *</label>
                                <input type="tel" id="cust-phone" oninput="onPhoneChange(this.value)" placeholder="เช่น 081-999-8877" class="w-full theme-input border rounded-xl px-3 py-2 text-xs focus:ring-2 focus:ring-[#EE4D2D]">
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-bold theme-text-muted mb-1">บ้านเลขที่, หมู่, ซอย, ถนน *</label>
                            <input type="text" id="cust-address-line" placeholder="เช่น 45/2 หมู่ 3 ถนนพระราม 2" class="w-full theme-input border rounded-xl px-3 py-2 text-xs focus:ring-2 focus:ring-[#EE4D2D]">
                        </div>

                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
                            <div>
                                <label class="block text-xs font-bold theme-text-muted mb-1">รหัสไปรษณีย์ 5 หลัก *</label>
                                <input type="text" id="cust-postcode" maxlength="5" oninput="handlePostalCodeInput(this.value)" placeholder="เช่น 10150" class="w-full theme-input border rounded-xl px-3 py-2 text-xs font-mono font-bold text-[#EE4D2D] focus:ring-2 focus:ring-[#EE4D2D]">
                            </div>
                            <div>
                                <label class="block text-xs font-bold theme-text-muted mb-1">ตำบล/แขวง</label>
                                <input type="text" id="cust-subdistrict" placeholder="ตำบล" class="w-full theme-input border rounded-xl px-3 py-2 text-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-bold theme-text-muted mb-1">อำเภอ/เขต</label>
                                <input type="text" id="cust-district" placeholder="อำเภอ" class="w-full theme-input border rounded-xl px-3 py-2 text-xs">
                            </div>
                            <div>
                                <label class="block text-xs font-bold theme-text-muted mb-1">จังหวัด</label>
                                <input type="text" id="cust-province" placeholder="จังหวัด" class="w-full theme-input border rounded-xl px-3 py-2 text-xs">
                            </div>
                        </div>

                        <!-- Routing Banner -->
                        <div id="routing-banner" class="theme-card-subtle p-2.5 rounded-2xl border flex items-center justify-between text-xs">
                            <div>
                                <span class="theme-text-muted text-[10px] block">ขนส่งที่ระบบจัดสรร:</span>
                                <span id="routing-carrier-name" class="font-black text-[#EE4D2D] text-xs">SPX Express (Shopee Express)</span>
                            </div>
                            <span id="carrier-fee-badge" class="font-bold text-emerald-500 bg-emerald-950/40 border border-emerald-700/50 px-2.5 py-0.5 rounded-full text-[10px]">
                                ค่าส่ง ฿25
                            </span>
                        </div>
                    </div>

                    <!-- 3. Payment Selection -->
                    <div class="space-y-3 pt-2">
                        <h3 class="text-xs sm:text-sm font-black theme-text-main flex items-center gap-1.5 border-b pb-2 border-slate-700/20">
                            <span class="w-5 h-5 rounded-full bg-[#EE4D2D] text-white flex items-center justify-center text-[10px] font-bold">3</span>
                            ช่องทางการชำระเงิน
                        </h3>

                        <div class="grid grid-cols-3 gap-2">
                            <button type="button" onclick="setPaymentMethod('PROMPTPAY')" id="btn-pay-promptpay" class="p-2.5 rounded-2xl border-2 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center border-[#EE4D2D] bg-[#FFF2EE] text-[#EE4D2D] shadow-sm">
                                <span class="text-base">📱</span>
                                <span class="text-[11px] sm:text-xs">พร้อมเพย์</span>
                                <span class="text-[9px] text-emerald-500 font-normal">ฟรีค่าธรรมเนียม</span>
                            </button>

                            <button type="button" onclick="setPaymentMethod('COD')" id="btn-pay-cod" class="p-2.5 rounded-2xl border-2 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center theme-card-subtle theme-text-muted border-slate-700/30">
                                <span class="text-base">💵</span>
                                <span class="text-[11px] sm:text-xs">เก็บปลายทาง</span>
                                <span class="text-[9px] text-[#EE4D2D] font-bold">บวก 3%</span>
                            </button>

                            <button type="button" onclick="setPaymentMethod('STORE_CREDIT')" id="btn-pay-wallet" class="p-2.5 rounded-2xl border-2 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center theme-card-subtle theme-text-muted border-slate-700/30">
                                <span class="text-base">👛</span>
                                <span class="text-[11px] sm:text-xs">กระเป๋าเครดิต</span>
                                <span id="wallet-btn-bal" class="text-[9px] text-emerald-500 font-normal">฿530.00</span>
                            </button>
                        </div>

                        <!-- PROMPTPAY PANEL WITH DOWNLOAD QR BUTTON -->
                        <div id="panel-promptpay" class="theme-card-subtle border rounded-2xl p-4 sm:p-5 space-y-3.5 text-center">
                            <div>
                                <span class="text-xs theme-text-muted block">ยอดชำระสุทธิ (แอปธนาคารจะกรอกตัวเลขให้อัตโนมัติ):</span>
                                <p id="promptpay-amount-display" class="text-3xl font-black text-[#EE4D2D] mt-1">฿390.00</p>
                            </div>

                            <!-- QR Image -->
                            <div class="flex justify-center">
                                <div class="bg-white p-2.5 rounded-2xl border-2 border-[#EE4D2D] shadow-md inline-block">
                                    <img id="promptpay-qr-img" src="" class="w-48 h-48 sm:w-52 sm:h-52 object-contain block" alt="PromptPay QR Code">
                                </div>
                            </div>

                            <!-- ACTION BUTTONS: DOWNLOAD QR & COPY PROMPTPAY -->
                            <div class="flex flex-col sm:flex-row items-center justify-center gap-2 max-w-sm mx-auto">
                                <button type="button" onclick="downloadPromptPayQR()" class="w-full sm:flex-1 bg-emerald-600 hover:bg-emerald-500 text-white text-xs px-3 py-2 rounded-xl font-bold shadow-md transition-all active:scale-95 flex items-center justify-center gap-1.5 cursor-pointer">
                                    <span>📥 บันทึกรูปภาพ QR Code</span>
                                </button>
                                <button type="button" onclick="copyPromptPay()" class="w-full sm:flex-1 bg-[#272732] hover:bg-[#363645] border border-slate-600 text-white text-xs px-3 py-2 rounded-xl font-bold shadow-sm transition-all active:scale-95 flex items-center justify-center gap-1 cursor-pointer">
                                    <span>📋 คัดลอกเลขพร้อมเพย์</span>
                                </button>
                            </div>

                            <!-- Account Details -->
                            <div class="bg-[#15151B]/80 dark:bg-black/40 p-2.5 rounded-xl border border-slate-700/30 text-xs theme-text-muted space-y-0.5 max-w-sm mx-auto">
                                <p><strong>ชื่อบัญชี:</strong> สุเมธา แท่นธรรมโรจน์ (กสิกรไทย)</p>
                                <p><strong>เลขพร้อมเพย์:</strong> <span class="text-[#EE4D2D] font-mono font-bold text-sm">061-537-2239</span></p>
                            </div>

                            <!-- Slip Upload -->
                            <div class="space-y-1 pt-1 border-t border-slate-700/20 max-w-sm mx-auto">
                                <label class="w-full bg-[#EE4D2D] hover:bg-[#d73211] text-white text-xs py-2.5 px-4 rounded-xl font-bold cursor-pointer shadow-md flex items-center justify-center gap-1.5 active:scale-95">
                                    <span>📎 แนบสลิปหลักฐานการโอนเงิน *</span>
                                    <input type="file" accept="image/*" onchange="handleSlipFile(this)" class="hidden">
                                </label>
                                <div id="slip-status-msg" class="text-xs font-bold text-emerald-500 hidden pt-1"></div>
                            </div>
                        </div>

                        <!-- COD PANEL -->
                        <div id="panel-cod" class="theme-card-subtle border-2 border-[#FF7555]/40 rounded-2xl p-4 space-y-3 hidden">
                            <div class="flex items-center gap-2.5">
                                <div class="w-9 h-9 rounded-xl bg-[#EE4D2D] text-white flex items-center justify-center text-lg flex-shrink-0">💵</div>
                                <div>
                                    <h4 class="font-bold text-xs sm:text-sm theme-text-main">บริการเก็บเงินปลายทาง (Cash on Delivery)</h4>
                                    <p class="text-[11px] theme-text-muted">มีค่าบริการเก็บปลายทาง +3% ของยอดรวม</p>
                                </div>
                            </div>
                            <div class="theme-card p-3 rounded-xl border text-xs space-y-1">
                                <p class="flex justify-between"><span class="theme-text-muted">ราคาสินค้า + ค่าส่ง:</span> <span id="cod-base-amount" class="font-bold theme-text-main">฿0.00</span></p>
                                <p class="flex justify-between text-[#EE4D2D]"><span>ค่าบริการ COD (+3%):</span> <span id="cod-fee-amount" class="font-bold">+฿0.00</span></p>
                                <div class="border-t border-slate-700/20 pt-1 flex justify-between font-black text-sm theme-text-main">
                                    <span>ยอดชำระเมื่อรับพัสดุ:</span>
                                    <span id="cod-total-amount" class="text-[#EE4D2D]">฿0.00</span>
                                </div>
                            </div>
                            <p class="text-[10px] theme-text-muted bg-orange-950/20 p-2 rounded-lg border border-orange-800/30">
                                💡 ไม่ต้องโอนเงินล่วงหน้า กรุณาเตรียมเงินสดพอดีให้กับพนักงานขนส่งเมื่อพัสดุไปถึงครับ
                            </p>
                        </div>

                        <!-- WALLET PANEL -->
                        <div id="panel-wallet" class="theme-card-subtle border rounded-2xl p-4 space-y-2 hidden text-xs">
                            <div class="flex justify-between"><span class="theme-text-muted">ยอดเงินในกระเป๋า:</span> <span id="wallet-balance-big" class="font-bold text-emerald-500">฿530.00</span></div>
                            <div class="flex justify-between"><span class="theme-text-muted">ยอดที่ต้องชำระ:</span> <span id="wallet-order-amt" class="font-bold text-[#EE4D2D]">฿0.00</span></div>
                            <div class="flex justify-between border-t pt-1 border-slate-700/30"><span class="theme-text-muted">คงเหลือหลังหัก:</span> <span id="wallet-after-bal" class="font-bold theme-text-main">฿0.00</span></div>
                        </div>
                    </div>

                    <!-- 4. Price Breakdown Summary -->
                    <div class="theme-card-subtle p-4 rounded-2xl border space-y-1.5 text-xs">
                        <div class="flex justify-between">
                            <span class="theme-text-muted">ราคาสินค้า (<span id="summary-variant-name"></span> x<span id="summary-qty">1</span>):</span>
                            <span id="summary-subtotal" class="font-bold theme-text-main">฿0.00</span>
                        </div>
                        <div class="flex justify-between">
                            <span class="theme-text-muted">ค่าจัดส่ง:</span>
                            <span id="summary-shipping" class="font-bold text-emerald-500">ฟรี (฿0.00)</span>
                        </div>
                        <div id="summary-cod-row" class="flex justify-between text-[#EE4D2D] hidden">
                            <span>ค่าบริการเก็บปลายทาง (COD +3%):</span>
                            <span id="summary-cod-fee" class="font-bold">+฿0.00</span>
                        </div>
                        <div class="border-t border-slate-700/20 pt-2 flex justify-between text-base font-black theme-text-main">
                            <span>ยอดสุทธิที่ต้องชำระ:</span>
                            <span id="summary-total" class="text-[#EE4D2D]">฿0.00</span>
                        </div>
                    </div>

                    <!-- Submit Button -->
                    <button type="button" onclick="submitDirectOrder()" class="w-full bg-[#EE4D2D] hover:bg-[#d73211] text-white font-black py-3.5 rounded-2xl text-sm sm:text-base shadow-lg transition-all active:scale-95 cursor-pointer">
                        <span id="submit-btn-text">⚡ สั่งซื้อและชำระเงิน</span>
                    </button>
                </div>
            </div>
        </section>

    </main>

    <!-- ================= LIGHTBOX GALLERY MODAL ================= -->
    <div id="gallery-modal" class="fixed inset-0 z-50 flex items-center justify-center p-3 bg-black/90 backdrop-blur-md hidden" onclick="closeGalleryModal()">
        <div class="relative max-w-2xl w-full p-2" onclick="event.stopPropagation()">
            <button onclick="closeGalleryModal()" class="absolute -top-10 right-0 text-white font-bold text-2xl hover:text-slate-300">✕</button>
            <div class="bg-[#1D1D24] rounded-3xl p-4 flex items-center justify-center border border-slate-700">
                <img id="gallery-modal-img" src="" class="max-h-[75vh] max-w-full object-contain rounded-2xl">
            </div>
        </div>
    </div>

    <!-- JAVASCRIPT ENGINE -->
    <script>
        const DEFAULT_PRODUCTS = """ + products_json + """;
        const DEFAULT_ORDERS = """ + orders_json + """;

        let products = DEFAULT_PRODUCTS;
        let selectedProduct = DEFAULT_PRODUCTS[0];
        let selectedVariantIdx = 0;
        let selectedCategory = "all";
        let quantity = 1;
        let currentGalleryIdx = 0;
        let paymentMethod = "PROMPTPAY";
        let slipImageBase64 = null;
        let currentTheme = localStorage.getItem("goodstone_theme") || "dark";

        let userWallet = {
            balance: 530,
            total_topup: 500,
            total_bonus: 30
        };

        // ================= OFFICIAL PROMPTPAY CRC16 GENERATOR =================
        function crc16(data) {
            let crc = 0xFFFF;
            for (let i = 0; i < data.length; i++) {
                crc ^= data.charCodeAt(i) << 8;
                for (let j = 0; j < 8; j++) {
                    if ((crc & 0x8000) !== 0) {
                        crc = ((crc << 1) ^ 0x1021) & 0xFFFF;
                    } else {
                        crc = (crc << 1) & 0xFFFF;
                    }
                }
            }
            let hex = (crc & 0xFFFF).toString(16).toUpperCase();
            return hex.padStart(4, "0");
        }

        function generatePromptPayQR(amount) {
            const phone = "0066615372239"; // 061-537-2239
            const tag29_val = "0016A000000677010111" + "01" + String(phone.length).padStart(2, "0") + phone;
            const tag29 = "29" + String(tag29_val.length).padStart(2, "0") + tag29_val;
            
            const amtStr = Number(amount || 0).toFixed(2);
            const tag54 = "54" + String(amtStr.length).padStart(2, "0") + amtStr;
            
            const raw = "000201010212" + tag29 + "5303764" + tag54 + "5802TH6304";
            const checksum = crc16(raw);
            return raw + checksum;
        }

        // ================= THEME CONTROLLER =================
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
                if (btn) btn.className = "flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-[#363645] bg-[#252530] text-[#FFFFFF] hover:border-[#EE4D2D] text-xs font-bold transition-all shadow-sm active:scale-95 cursor-pointer";
            } else {
                if (icon) icon.innerText = "☀️";
                if (text) text.innerText = "โหมดสว่าง";
                if (btn) btn.className = "flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl border border-[#EBE3D5] bg-[#FAF7F2] text-[#2C241E] hover:border-[#EE4D2D] text-xs font-bold transition-all shadow-sm active:scale-95 cursor-pointer";
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

            const savedProds = localStorage.getItem("goodstone_products");
            if (savedProds) {
                try { products = JSON.parse(savedProds); } catch(e) {}
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
                    if (p.address) document.getElementById("cust-address-line").value = p.address;
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

        function getSafeProduct(prodOrId) {
            if (typeof prodOrId === "string") {
                const found = products.find(x => x.id === prodOrId);
                if (found) return found;
            }
            if (prodOrId && typeof prodOrId === "object") return prodOrId;
            return products[0] || DEFAULT_PRODUCTS[0];
        }

        function getSafeVariant(p, idx) {
            if (p && p.variants && Array.isArray(p.variants) && p.variants.length > 0) {
                return p.variants[idx] || p.variants[0];
            }
            return { name: "รุ่นมาตรฐาน", price: Number(p?.price || 390), stock: Number(p?.stock || 50) };
        }

        // ================= CATALOG VIEW =================
        function showCatalogView() {
            document.getElementById("view-checkout").classList.add("hidden");
            document.getElementById("view-catalog").classList.remove("hidden");
            window.scrollTo({ top: 0, behavior: "smooth" });
        }

        function filterCategory(cat) {
            selectedCategory = cat;
            document.querySelectorAll(".cat-pill").forEach(btn => {
                btn.className = "cat-pill px-3.5 py-1.5 rounded-xl border transition-all whitespace-nowrap theme-card-subtle theme-text-muted hover:text-[#EE4D2D]";
            });
            event.target.className = "cat-pill px-3.5 py-1.5 rounded-xl border transition-all whitespace-nowrap bg-[#EE4D2D] text-white border-[#EE4D2D] shadow-sm";
            renderCatalogGrid();
        }

        function handleSearch(query) {
            const q = query.trim().toLowerCase();
            const filtered = products.filter(p => p.name.toLowerCase().includes(q) || (p.description && p.description.toLowerCase().includes(q)));
            renderGridItems(filtered);
        }

        function renderCatalogGrid() {
            const list = selectedCategory === "all" ? products : products.filter(p => p.category === selectedCategory);
            renderGridItems(list);
        }

        function renderGridItems(list) {
            const container = document.getElementById("product-grid");
            container.innerHTML = "";

            if (list.length === 0) {
                container.innerHTML = `<div class="col-span-full py-12 text-center theme-text-muted text-xs">ไม่พบสินค้าที่ตรงกับการค้นหา</div>`;
                return;
            }

            list.forEach(p => {
                const img = (p.images && p.images.length > 0) ? p.images[0].file : (p.image_file || p.fallback_image);
                const shopeeUrl = p.shopee_affiliate_url || "https://th.shp.ee/sdFv2cS1";
                const displayPrice = Number(p.price || 390).toLocaleString();

                const card = document.createElement("div");
                card.className = "theme-card rounded-3xl border-2 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group";
                card.innerHTML = `
                    <div>
                        <div onclick="openProductDirectCheckout('${p.id}')" class="h-48 sm:h-52 overflow-hidden theme-card-subtle relative flex items-center justify-center cursor-pointer border-b border-slate-700/20 p-3">
                            <img src="${img}" onerror="this.onerror=null; this.src='${p.fallback_image}';" class="max-h-full max-w-full object-contain group-hover:scale-105 transition-transform duration-300">
                            <span class="absolute top-2.5 left-2.5 theme-badge border text-[9px] px-2 py-0.5 rounded-full font-black uppercase">${p.category}</span>
                            <span class="absolute top-2.5 right-2.5 bg-black/60 text-white text-[9px] px-2 py-0.5 rounded-full font-bold">สต็อก ${p.stock}</span>
                        </div>

                        <div class="p-3.5 sm:p-4 space-y-2">
                            <h3 onclick="openProductDirectCheckout('${p.id}')" class="font-bold theme-text-main text-xs sm:text-sm line-clamp-2 cursor-pointer hover:text-[#EE4D2D] transition-colors leading-snug">${p.name}</h3>
                            <div class="flex items-baseline gap-1">
                                <span class="text-[10px] theme-text-muted">เริ่มต้น</span>
                                <span class="text-sm sm:text-base font-black text-[#EE4D2D]">฿${displayPrice}</span>
                            </div>
                        </div>
                    </div>

                    <div class="p-3.5 sm:p-4 pt-0 space-y-1.5">
                        <button onclick="openProductDirectCheckout('${p.id}')" class="w-full bg-[#EE4D2D] hover:bg-[#d73211] text-white py-2 rounded-xl text-xs font-bold transition-all shadow-md active:scale-95 cursor-pointer flex items-center justify-center gap-1">
                            <span>⚡ ซื้อด่วน</span>
                        </button>
                        <a href="${shopeeUrl}" target="_blank" class="w-full theme-badge hover:bg-orange-500/10 text-[11px] py-1.5 rounded-xl font-bold border flex items-center justify-center gap-1 transition-all">
                            <span>⭐ ดูรีวิวใน Shopee ></span>
                        </a>
                    </div>
                `;
                container.appendChild(card);
            });
        }

        // ================= DIRECT CHECKOUT LOGIC =================
        function openProductDirectCheckout(productId) {
            selectedProduct = getSafeProduct(productId);
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
            const p = getSafeProduct(selectedProduct);
            selectedProduct = p;

            const images = (p.images && p.images.length > 0) ? p.images : [{ file: p.image_file || p.fallback_image, name: "main.jpg" }];
            document.getElementById("checkout-main-img").src = images[currentGalleryIdx]?.file || p.fallback_image;

            document.getElementById("checkout-prod-category").innerText = p.category;
            document.getElementById("checkout-prod-title").innerText = p.name;
            document.getElementById("checkout-prod-desc").innerText = p.description || "";
            document.getElementById("checkout-shopee-review-btn").href = p.shopee_affiliate_url || "https://th.shp.ee/sdFv2cS1";

            // Thumbs
            const thumbs = document.getElementById("checkout-gallery-thumbs");
            thumbs.innerHTML = "";
            images.forEach((img, idx) => {
                const btn = document.createElement("button");
                btn.type = "button";
                btn.onclick = () => { currentGalleryIdx = idx; document.getElementById("checkout-main-img").src = img.file; renderProductCheckoutDetail(); };
                btn.className = `h-14 rounded-xl border-2 p-1 theme-card-subtle overflow-hidden flex items-center justify-center ${currentGalleryIdx === idx ? 'border-[#EE4D2D]' : 'border-slate-700/30'}`;
                btn.innerHTML = `<img src="${img.file}" class="max-h-full max-w-full object-contain">`;
                thumbs.appendChild(btn);
            });

            // Variants
            const vContainer = document.getElementById("checkout-variants-container");
            vContainer.innerHTML = "";
            const variants = (p.variants && p.variants.length > 0) ? p.variants : [{ name: "รุ่นมาตรฐาน", price: p.price, stock: p.stock }];

            variants.forEach((v, idx) => {
                const vBtn = document.createElement("button");
                vBtn.type = "button";
                vBtn.onclick = () => { selectedVariantIdx = idx; updateCalculations(); renderProductCheckoutDetail(); };
                vBtn.className = `px-3 py-1.5 rounded-xl text-xs font-bold border-2 transition-all cursor-pointer ${selectedVariantIdx === idx ? 'border-[#EE4D2D] bg-[#EE4D2D] text-white shadow-sm' : 'theme-card-subtle theme-text-muted border-slate-700/30 hover:border-slate-500'}`;
                vBtn.innerText = `${v.name} (฿${Number(v.price).toLocaleString()})`;
                vContainer.appendChild(vBtn);
            });
        }

        function changeQuantity(delta) {
            quantity = Math.max(1, quantity + delta);
            document.getElementById("checkout-quantity-display").innerText = quantity;
            updateCalculations();
        }

        function updateCalculations() {
            const p = getSafeProduct(selectedProduct);
            const activeV = getSafeVariant(p, selectedVariantIdx);

            const unitPrice = Number(activeV.price || p.price || 390);
            const subtotal = unitPrice * Math.max(1, quantity);
            const isFreeShipping = (subtotal >= 200);
            const shippingCost = isFreeShipping ? 0 : 25;
            const baseTotal = subtotal + shippingCost;
            const codFee = (paymentMethod === "COD") ? Number((baseTotal * 0.03).toFixed(2)) : 0;
            const total = Number((baseTotal + codFee).toFixed(2));

            // DOM updates
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

            document.getElementById("carrier-fee-badge").innerText = isFreeShipping ? "ส่งฟรี (฿0)" : "ค่าส่ง ฿25";
            document.getElementById("wallet-order-amt").innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("wallet-after-bal").innerText = `฿${Math.max(0, userWallet.balance - total).toLocaleString(undefined, {minimumFractionDigits: 2})}`;

            const codBaseEl = document.getElementById("cod-base-amount");
            if (codBaseEl) {
                codBaseEl.innerText = `฿${baseTotal.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
                document.getElementById("cod-fee-amount").innerText = `+฿${codFee.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
                document.getElementById("cod-total-amount").innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            }

            // Generate Dynamic PromptPay QR
            try {
                const ppPayload = generatePromptPayQR(total);
                document.getElementById("promptpay-qr-img").src = `https://api.qrserver.com/v1/create-qr-code/?size=300x300&margin=10&data=${encodeURIComponent(ppPayload)}`;
            } catch(e) {
                console.error("QR Generation error:", e);
            }
        }

        // ================= DOWNLOAD PROMPTPAY QR CODE =================
        function downloadPromptPayQR() {
            const qrImg = document.getElementById("promptpay-qr-img");
            if (!qrImg || !qrImg.src) {
                alert("ไม่พบรูปภาพ QR Code ครับ");
                return;
            }

            fetch(qrImg.src)
                .then(res => res.blob())
                .then(blob => {
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement("a");
                    a.style.display = "none";
                    a.href = url;
                    a.download = `PromptPay_GOODSTONE_${selectedProduct ? selectedProduct.id : 'ORD'}.png`;
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(url);
                    alert("📥 บันทึกรูปภาพ QR Code ลงในเครื่องเรียบร้อยแล้วครับ!\nสามารถเปิดแอปธนาคารแล้วเลือก 'สแกนจากรูปภาพ' เพื่อชำระเงินได้ทันที");
                })
                .catch(err => {
                    window.open(qrImg.src, "_blank");
                });
        }

        function copyPromptPay() {
            navigator.clipboard.writeText("0615372239").then(() => {
                alert("📋 คัดลอกเลขพร้อมเพย์ 061-537-2239 เรียบร้อยแล้วครับ!");
            }).catch(() => {
                alert("เลขพร้อมเพย์: 061-537-2239");
            });
        }

        function setPaymentMethod(method) {
            paymentMethod = method;
            const btnPP = document.getElementById("btn-pay-promptpay");
            const btnCOD = document.getElementById("btn-pay-cod");
            const btnW = document.getElementById("btn-pay-wallet");
            const panelPP = document.getElementById("panel-promptpay");
            const panelCOD = document.getElementById("panel-cod");
            const panelW = document.getElementById("panel-wallet");

            btnPP.className = "p-2.5 rounded-2xl border-2 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center theme-card-subtle theme-text-muted border-slate-700/30";
            btnCOD.className = "p-2.5 rounded-2xl border-2 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center theme-card-subtle theme-text-muted border-slate-700/30";
            btnW.className = "p-2.5 rounded-2xl border-2 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center theme-card-subtle theme-text-muted border-slate-700/30";

            panelPP.classList.add("hidden");
            panelCOD.classList.add("hidden");
            panelW.classList.add("hidden");

            if (method === "PROMPTPAY") {
                btnPP.className = "p-2.5 rounded-2xl border-2 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center border-[#EE4D2D] bg-[#EE4D2D] text-white shadow-sm";
                panelPP.classList.remove("hidden");
            } else if (method === "COD") {
                btnCOD.className = "p-2.5 rounded-2xl border-2 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center border-[#EE4D2D] bg-[#EE4D2D] text-white shadow-sm";
                panelCOD.classList.remove("hidden");
            } else if (method === "STORE_CREDIT") {
                btnW.className = "p-2.5 rounded-2xl border-2 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center border-[#EE4D2D] bg-[#EE4D2D] text-white shadow-sm";
                panelW.classList.remove("hidden");
            }
            updateCalculations();
        }

        function handlePostalCodeInput(code) {
            const clean = code.replace(/[^0-9]/g, "");
            if (clean.length === 5) {
                if (clean === "10150") {
                    document.getElementById("cust-subdistrict").value = "ท่าข้าม";
                    document.getElementById("cust-district").value = "บางขุนเทียน";
                    document.getElementById("cust-province").value = "กรุงเทพมหานคร";
                } else if (clean === "10270") {
                    document.getElementById("cust-subdistrict").value = "บางกระดี่";
                    document.getElementById("cust-district").value = "เมืองสมุทรปราการ";
                    document.getElementById("cust-province").value = "สมุทรปราการ";
                }

                const isRemote = clean.startsWith("94") || clean.startsWith("95") || clean.startsWith("96") || clean.startsWith("58") || ["84320", "84360", "23170", "23120", "81150", "82160", "63170", "50310"].includes(clean);
                const carrierEl = document.getElementById("routing-carrier-name");
                if (isRemote) {
                    carrierEl.innerText = "ไปรษณีย์ไทย ด่วนพิเศษ (EMS)";
                } else {
                    carrierEl.innerText = "SPX Express (Shopee Express)";
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
                const msgBox = document.getElementById("slip-status-msg");
                msgBox.classList.remove("hidden");
                msgBox.innerText = "✅ แนบสลิปโอนเงินเรียบร้อยแล้ว";
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

            const p = getSafeProduct(selectedProduct);
            const activeV = getSafeVariant(p, selectedVariantIdx);

            const unitPrice = Number(activeV.price || p.price || 390);
            const subtotal = unitPrice * Math.max(1, quantity);
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
                        product_id: p.id,
                        name: `${p.name} (${activeV.name})`,
                        base_name: p.name,
                        variant: activeV.name,
                        price: activeV.price,
                        quantity: quantity,
                        image: p.image_file || p.fallback_image
                    }
                ],
                created_at: now.toISOString().replace("T", " ").substring(0, 19)
            };

            const profile = { name, phone, address: addressLine, postal_code: postcode, subdistrict, district, province };
            localStorage.setItem("goodstone_saved_profile", JSON.stringify(profile));

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

        // ================= GALLERY MODAL =================
        function openGalleryModal() {
            const p = getSafeProduct(selectedProduct);
            const images = (p.images && p.images.length > 0) ? p.images : [{ file: p.image_file || p.fallback_image, name: "main.jpg" }];
            document.getElementById("gallery-modal-img").src = images[currentGalleryIdx]?.file || p.fallback_image;
            document.getElementById("gallery-modal").classList.remove("hidden");
        }

        function closeGalleryModal() {
            document.getElementById("gallery-modal").classList.add("hidden");
        }

        window.onload = init;
    </script>
</body>
</html>"""

with open("/working_dir/slingshot-shop/index.html", "w", encoding="utf-8") as f:
    f.write(index_html_code)

print("slingshot-shop/index.html rebuilt with full PromptPay QR generator + Download QR Button + Rock-solid Dark/Light Theme!")
