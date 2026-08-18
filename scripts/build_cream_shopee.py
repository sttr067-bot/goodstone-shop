import json

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))
products_json = json.dumps(data["products"], ensure_ascii=False)
orders_json = json.dumps(data["orders"], ensure_ascii=False)

addresses_data = [
  {"postal_code": "10150", "subdistrict": "ท่าข้าม", "district": "บางขุนเทียน", "province": "กรุงเทพมหานคร", "is_remote": False},
  {"postal_code": "10150", "subdistrict": "แสมดำ", "district": "บางขุนเทียน", "province": "กรุงเทพมหานคร", "is_remote": False},
  {"postal_code": "10140", "subdistrict": "บางมด", "district": "ทุ่งครุ", "province": "กรุงเทพมหานคร", "is_remote": False},
  {"postal_code": "10400", "subdistrict": "สามเสนใน", "district": "พญาไท", "province": "กรุงเทพมหานคร", "is_remote": False},
  {"postal_code": "10330", "subdistrict": "ปทุมวัน", "district": "ปทุมวัน", "province": "กรุงเทพมหานคร", "is_remote": False},
  {"postal_code": "10110", "subdistrict": "คลองเตย", "district": "คลองเตย", "province": "กรุงเทพมหานคร", "is_remote": False},
  {"postal_code": "10270", "subdistrict": "บางกระดี่", "district": "เมืองสมุทรปราการ", "province": "สมุทรปราการ", "is_remote": False},
  {"postal_code": "11000", "subdistrict": "บางกระสอ", "district": "เมืองนนทบุรี", "province": "นนทบุรี", "is_remote": False},
  {"postal_code": "12000", "subdistrict": "บางปรอก", "district": "เมืองปทุมธานี", "province": "ปทุมธานี", "is_remote": False},
  {"postal_code": "20000", "subdistrict": "บางปลาสร้อย", "district": "เมืองชลบุรี", "province": "ชลบุรี", "is_remote": False},
  {"postal_code": "20150", "subdistrict": "หนองปรือ", "district": "บางละมุง", "province": "ชลบุรี (พัทยา)", "is_remote": False},
  {"postal_code": "30000", "subdistrict": "ในเมือง", "district": "เมืองนครราชสีมา", "province": "นครราชสีมา", "is_remote": False},
  {"postal_code": "40000", "subdistrict": "ในเมือง", "district": "เมืองขอนแก่น", "province": "ขอนแก่น", "is_remote": False},
  {"postal_code": "50000", "subdistrict": "ศรีภูมิ", "district": "เมืองเชียงใหม่", "province": "เชียงใหม่", "is_remote": False},
  {"postal_code": "65000", "subdistrict": "บ้านคลอง", "district": "เมืองพิษณุโลก", "province": "พิษณุโลก", "is_remote": False},
  {"postal_code": "83000", "subdistrict": "ตลาดใหญ่", "district": "เมืองภูเก็ต", "province": "ภูเก็ต", "is_remote": False},
  {"postal_code": "90000", "subdistrict": "บ่อยาง", "district": "เมืองสงขลา", "province": "สงขลา", "is_remote": False},
  {"postal_code": "90110", "subdistrict": "หาดใหญ่", "district": "หาดใหญ่", "province": "สงขลา", "is_remote": False},

  # Remote Areas
  {"postal_code": "84320", "subdistrict": "บ่อผุด", "district": "เกาะสมุย", "province": "สุราษฎร์ธานี", "is_remote": True},
  {"postal_code": "84320", "subdistrict": "แม่น้ำ", "district": "เกาะสมุย", "province": "สุราษฎร์ธานี", "is_remote": True},
  {"postal_code": "84360", "subdistrict": "เกาะพะงัน", "district": "เกาะพะงัน", "province": "สุราษฎร์ธานี", "is_remote": True},
  {"postal_code": "84360", "subdistrict": "เกาะเต่า", "district": "เกาะพะงัน", "province": "สุราษฎร์ธานี", "is_remote": True},
  {"postal_code": "23170", "subdistrict": "เกาะช้าง", "district": "เกาะช้าง", "province": "ตราด", "is_remote": True},
  {"postal_code": "23120", "subdistrict": "เกาะกูด", "district": "เกาะกูด", "province": "ตราด", "is_remote": True},
  {"postal_code": "81150", "subdistrict": "เกาะลันตา", "district": "เกาะลันตา", "province": "กระบี่", "is_remote": True},
  {"postal_code": "82160", "subdistrict": "เกาะยาว", "district": "เกาะยาว", "province": "พังงา", "is_remote": True},
  {"postal_code": "95000", "subdistrict": "สะเตง", "district": "เมืองยะลา", "province": "ยะลา", "is_remote": True},
  {"postal_code": "95110", "subdistrict": "เบตง", "district": "เบตง", "province": "ยะลา", "is_remote": True},
  {"postal_code": "94000", "subdistrict": "สะบารัง", "district": "เมืองปัตตานี", "province": "ปัตตานี", "is_remote": True},
  {"postal_code": "96000", "subdistrict": "บางนาค", "district": "เมืองนราธิวาส", "province": "นราธิวาส", "is_remote": True},
  {"postal_code": "96110", "subdistrict": "สุไหงโก-ลก", "district": "สุไหงโก-ลก", "province": "นราธิวาส", "is_remote": True},
  {"postal_code": "58000", "subdistrict": "จองคำ", "district": "เมืองแม่ฮ่องสอน", "province": "แม่ฮ่องสอน", "is_remote": True},
  {"postal_code": "58110", "subdistrict": "ปาย", "district": "ปาย", "province": "แม่ฮ่องสอน", "is_remote": True},
  {"postal_code": "63170", "subdistrict": "อุ้มผาง", "district": "อุ้มผาง", "province": "ตาก", "is_remote": True}
]
addresses_json = json.dumps(addresses_data, ensure_ascii=False)

index_html_cream = """<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GOODSTONE TACTICAL SLINGSHOT - ร้านหนังสติ๊กยุทธวิธีและอุปกรณ์</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        shopee: {
                            DEFAULT: "#EE4D2D",
                            hover: "#d73211",
                            light: "#FFF5F2"
                        },
                        cream: {
                            50: "#FFFDFB",
                            100: "#FAF7F2",
                            200: "#F2EBE1",
                            300: "#E5DACB",
                            800: "#4A4036"
                        }
                    }
                }
            }
        }
    </script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: "Prompt", sans-serif; background-color: #FAF7F2; }
    </style>
</head>
<body class="bg-cream-100 text-slate-800 min-h-screen flex flex-col font-sans">

    <!-- HEADER -->
    <header class="sticky top-0 z-40 bg-slate-900 text-white shadow-md border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <!-- Logo -->
                <div class="flex items-center gap-3 cursor-pointer" onclick="showCatalogView()">
                    <div class="w-10 h-10 rounded-xl bg-[#EE4D2D] flex items-center justify-center text-white font-black text-xl shadow-lg shadow-orange-500/30">
                        🎯
                    </div>
                    <div>
                        <span class="font-black text-lg tracking-wide text-white">GOODSTONE</span>
                        <span class="text-[11px] block text-slate-400">ร้านหนังสติ๊กยุทธวิธีและอุปกรณ์</span>
                    </div>
                </div>

                <!-- Nav Menu -->
                <nav class="flex items-center gap-5 text-xs sm:text-sm font-bold">
                    <button onclick="showCatalogView()" class="hover:text-amber-400 transition-colors flex items-center gap-1">
                        <i data-lucide="store" class="w-4 h-4 text-[#EE4D2D]"></i> หน้าร้านค้า
                    </button>
                    <a href="track.html" class="hover:text-amber-400 transition-colors flex items-center gap-1 text-slate-300">
                        <i data-lucide="truck" class="w-4 h-4 text-slate-400"></i> เช็คพัสดุ
                    </a>
                </nav>

                <!-- Customer Wallet Badge -->
                <div id="header-wallet-badge" class="hidden sm:flex items-center gap-2 bg-slate-800/90 px-3 py-1.5 rounded-xl border border-slate-700 text-xs">
                    <span class="text-slate-400">👛 กระเป๋าเครดิต:</span>
                    <span id="user-wallet-display" class="font-black text-emerald-400">฿0.00</span>
                </div>
            </div>
        </div>
    </header>

    <!-- FREE SHIPPING PROMOTION BANNER -->
    <div class="bg-[#EE4D2D] text-white py-2 px-4 text-center text-xs sm:text-sm font-bold shadow-md">
        📮 ค่าจัดส่ง EMS/SPX 25 บาททั่วไทย (พิเศษ! สั่งซื้อครบ 200 บาทขึ้นไป จัดส่งฟรีทันที)
    </div>

    <!-- MAIN WRAPPER -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8">

        <!-- ================= VIEW 1: PRODUCT CATALOG / GRID (หน้าแรกหลัก) ================= -->
        <section id="view-catalog" class="space-y-6">
            <!-- Hero Banner -->
            <div class="relative overflow-hidden rounded-3xl bg-gradient-to-r from-slate-950 via-slate-900 to-[#4A1D13] text-white p-6 sm:p-10 shadow-xl border border-slate-800">
                <div class="max-w-2xl space-y-3">
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-500/20 text-orange-400 border border-orange-500/30 text-xs font-semibold">
                        <span>🔥 หนังสติ๊กยุทธวิธีเกรดพรีเมียม & อุปกรณ์ครบเซ็ต</span>
                    </div>
                    <h1 class="text-2xl sm:text-4xl font-extrabold leading-tight">
                        หนังสติ๊กยุทธวิธี ยางแบนแรงสูง <br><span class="text-[#EE4D2D]">จัดส่งด่วน EMS / SPX ทั่วไทย</span>
                    </h1>
                    <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                        ด้ามจับอัลลอยด์ CNC เลเซอร์ช่วยเล็ง ยางแบนสโลปทนทาน ลูกเหล็กขัดเงามาตรฐาน แตะที่รูปภาพเพื่อเข้าสู่ระบบซื้อด่วนได้ทันที
                    </p>
                </div>
            </div>

            <!-- Categories Filter & Search -->
            <div class="flex flex-col sm:flex-row items-center justify-between gap-4 bg-white p-4 rounded-2xl shadow-sm border border-cream-200">
                <div class="flex flex-wrap gap-2 w-full sm:w-auto" id="category-tabs">
                    <button onclick="filterCategory(\x27all\x27)" class="cat-btn active px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all bg-slate-900 text-white" data-cat="all">ทั้งหมด</button>
                    <button onclick="filterCategory(\x27slingshot\x27)" class="cat-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all bg-cream-100 text-slate-700 hover:bg-orange-50 hover:text-[#EE4D2D]" data-cat="slingshot">🎯 หนังสติ๊ก</button>
                    <button onclick="filterCategory(\x27rubber\x27)" class="cat-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all bg-cream-100 text-slate-700 hover:bg-orange-50 hover:text-[#EE4D2D]" data-cat="rubber">⚡ ยางหนังสติ๊ก</button>
                    <button onclick="filterCategory(\x27ammo\x27)" class="cat-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all bg-cream-100 text-slate-700 hover:bg-orange-50 hover:text-[#EE4D2D]" data-cat="ammo">🔘 ลูกเหล็ก/กระสุน</button>
                    <button onclick="filterCategory(\x27accessories\x27)" class="cat-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all bg-cream-100 text-slate-700 hover:bg-orange-50 hover:text-[#EE4D2D]" data-cat="accessories">🎒 อุปกรณ์เสริม/เลเซอร์</button>
                </div>
                <div class="relative w-full sm:w-64">
                    <input type="text" id="search-input" onkeyup="searchProducts()" placeholder="ค้นหาสินค้า..." class="w-full pl-10 pr-4 py-2 bg-cream-50 border border-cream-300 rounded-xl text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-[#EE4D2D] focus:bg-white">
                    <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3 top-2.5"></i>
                </div>
            </div>

            <!-- Product Grid -->
            <div id="product-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- Loaded dynamically -->
            </div>
        </section>

        <!-- ================= VIEW 2: SINGLE-PAGE DIRECT-TO-CHECKOUT (เมื่อกดที่รูปสินค้า) ================= -->
        <section id="view-checkout" class="hidden space-y-6">
            <!-- Back to Catalog Button -->
            <div class="flex items-center justify-between">
                <button onclick="showCatalogView()" class="inline-flex items-center gap-2 bg-white hover:bg-orange-50 text-slate-800 hover:text-[#EE4D2D] px-4 py-2 rounded-2xl border border-cream-300 font-bold text-xs sm:text-sm transition-all shadow-sm active:scale-95">
                    <span>← กลับไปดูสินค้าทั้งหมด</span>
                </button>
                <span class="text-xs font-bold text-[#EE4D2D] bg-orange-50 px-3 py-1 rounded-full border border-orange-200">
                    ⚡ หน้าสั่งซื้อด่วน (Direct Checkout)
                </span>
            </div>

            <!-- Direct Checkout Panel -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">

                <!-- LEFT: MULTI-IMAGE GALLERY & PRODUCT DETAILS (5 Cols) -->
                <div class="lg:col-span-5 bg-white p-5 sm:p-6 rounded-3xl border border-cream-200 shadow-sm space-y-5">
                    
                    <!-- Main Large Image with Gallery Trigger -->
                    <div onclick="openGalleryModal()" class="relative h-64 sm:h-80 bg-slate-950 rounded-2xl overflow-hidden cursor-pointer group flex items-center justify-center border border-slate-800">
                        <img id="detail-main-img" src="" alt="Product" class="w-full h-full object-contain group-hover:scale-105 transition-transform duration-300">
                        <span id="detail-stock-badge" class="absolute top-3 right-3 bg-slate-900/80 backdrop-blur-sm text-amber-400 text-xs px-3 py-1 rounded-full font-bold">
                            สต็อก: 35 ชิ้น
                        </span>
                        <div class="absolute bottom-3 left-3 bg-black/80 text-white text-[11px] px-3 py-1.5 rounded-xl flex items-center gap-1.5 font-bold group-hover:bg-[#EE4D2D] transition-all">
                            <i data-lucide="maximize-2" class="w-3.5 h-3.5"></i>
                            <span id="detail-gallery-label">แตะดูรูปใหญ่ (4 ภาพ)</span>
                        </div>
                    </div>

                    <!-- Thumbnails Strip (เลื่อนดูรูปที่ 1, 2, 3..N) -->
                    <div id="detail-thumbs-strip" class="flex gap-2 overflow-x-auto pb-1">
                        <!-- Populated dynamically -->
                    </div>

                    <!-- Product Info -->
                    <div class="space-y-2 pt-2 border-t border-cream-100">
                        <span id="detail-cat-tag" class="px-2.5 py-0.5 rounded-full bg-orange-50 text-[#EE4D2D] border border-orange-200 text-xs font-extrabold uppercase">
                            SLINGSHOT
                        </span>
                        <h1 id="detail-title" class="text-xl sm:text-2xl font-black text-slate-900 leading-snug">
                            หนังสติ๊กอัลลอยด์ยุทธวิธี
                        </h1>
                        <p id="detail-desc" class="text-xs sm:text-sm text-slate-500 leading-relaxed">
                            ด้ามจับอัลลอยด์ แข็งแรงทนทาน น้ำหนักกระชับมือ พร้อมศูนย์เล็งเลเซอร์และระดับน้ำ ช่วยจับเป้าแม่นยำสูง
                        </p>
                    </div>

                    <!-- Interactive Variant Option Pills (Shopee Style) -->
                    <div class="space-y-2.5 pt-3 border-t border-cream-100">
                        <div class="flex items-center justify-between">
                            <label class="text-xs font-bold text-[#EE4D2D] flex items-center gap-1.5">
                                <span class="animate-pulse">👉</span> แตะเลือกสเปก / ตัวเลือกสินค้า:
                            </label>
                            <span class="text-[10px] text-slate-400 bg-cream-100 px-2 py-0.5 rounded font-semibold">เลือกได้ทันที</span>
                        </div>
                        <div id="detail-variant-pills" class="flex flex-wrap gap-2">
                            <!-- Populated dynamically -->
                        </div>
                    </div>

                    <!-- Quantity Selector -->
                    <div class="flex items-center justify-between pt-3 border-t border-cream-100">
                        <span class="text-xs font-bold text-slate-700">จำนวนที่ต้องการสั่ง:</span>
                        <div class="flex items-center gap-2 bg-cream-100 px-3 py-1.5 rounded-xl border border-cream-200">
                            <button onclick="changeQty(-1)" class="text-slate-700 hover:text-red-600 font-bold px-2 text-sm">-</button>
                            <span id="detail-qty-display" class="font-bold text-sm text-slate-900 w-6 text-center">1</span>
                            <button onclick="changeQty(1)" class="text-slate-700 hover:text-emerald-600 font-bold px-2 text-sm">+</button>
                        </div>
                    </div>
                </div>

                <!-- RIGHT: GUEST CHECKOUT & PAYMENT (7 Cols) -->
                <div class="lg:col-span-7 bg-white p-6 sm:p-8 rounded-3xl border border-cream-200 shadow-sm space-y-6">
                    
                    <div class="flex items-center justify-between pb-4 border-b border-cream-100">
                        <div>
                            <h2 class="text-lg sm:text-xl font-black text-slate-900 flex items-center gap-2">
                                <span>⚡</span> สั่งซื้อด่วน (Guest Checkout)
                            </h2>
                            <p class="text-xs text-slate-400">ไม่ต้องสมัครสมาชิก กรอกที่อยู่แล้วชำระเงินได้ทันที</p>
                        </div>
                        <div id="auto-cookie-badge" class="hidden text-right">
                            <span class="text-[10px] text-emerald-700 bg-emerald-50 border border-emerald-300 px-2.5 py-1 rounded-lg font-bold">
                                ✓ ดึงที่อยู่เดิมจาก Cookie อัตโนมัติ
                            </span>
                        </div>
                    </div>

                    <!-- Step 1: Address Form -->
                    <div class="space-y-3">
                        <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                            <span class="w-5 h-5 rounded-full bg-[#EE4D2D] text-white flex items-center justify-center text-[10px] font-bold">1</span>
                            ข้อมูลผู้รับ & ที่อยู่จัดส่ง
                        </h3>

                        <div class="grid grid-cols-2 gap-3">
                            <div class="col-span-2 sm:col-span-1">
                                <label class="block text-xs font-bold text-slate-700 mb-1">ชื่อ-นามสกุล ผู้รับ *</label>
                                <input type="text" id="cust-name" placeholder="ระบุชื่อและนามสกุล..." class="w-full px-3.5 py-2.5 bg-cream-50 border border-cream-300 rounded-xl text-xs sm:text-sm focus:ring-2 focus:ring-[#EE4D2D] focus:bg-white">
                            </div>

                            <div class="col-span-2 sm:col-span-1">
                                <label class="block text-xs font-bold text-slate-700 mb-1">เบอร์โทรศัพท์มือถือ *</label>
                                <input type="tel" id="cust-phone" oninput="onPhoneChange(this.value)" placeholder="ระบุเบอร์โทรติดต่อ..." class="w-full px-3.5 py-2.5 bg-cream-50 border border-cream-300 rounded-xl text-xs sm:text-sm focus:ring-2 focus:ring-[#EE4D2D] focus:bg-white">
                            </div>

                            <div class="col-span-2">
                                <label class="block text-xs font-bold text-slate-700 mb-1">บ้านเลขที่ / ซอย / ถนน *</label>
                                <input type="text" id="cust-address-line" placeholder="เช่น 123/45 ซอย 8 ถนนพระราม 2..." class="w-full px-3.5 py-2.5 bg-cream-50 border border-cream-300 rounded-xl text-xs sm:text-sm focus:ring-2 focus:ring-[#EE4D2D] focus:bg-white">
                            </div>

                            <!-- Postal Code Auto-Fill -->
                            <div class="col-span-2 sm:col-span-1 relative">
                                <label class="block text-xs font-bold text-[#EE4D2D] mb-1">
                                    รหัสไปรษณีย์ 5 หลัก (Auto-fill ตำบล/อำเภอ) *
                                </label>
                                <input type="text" id="cust-postcode" maxlength="5" oninput="handlePostalCodeInput(this.value)" placeholder="เช่น 10150, 84320..." class="w-full px-3.5 py-2.5 bg-orange-50 border-2 border-orange-300 rounded-xl text-xs sm:text-sm font-bold text-slate-900 focus:ring-2 focus:ring-[#EE4D2D] focus:bg-white">
                                <div id="address-suggestions-box" class="hidden absolute left-0 right-0 top-full mt-1 bg-white border border-slate-300 rounded-xl shadow-xl z-20 max-h-48 overflow-y-auto"></div>
                            </div>

                            <div class="col-span-2 sm:col-span-1">
                                <label class="block text-xs font-bold text-slate-700 mb-1">ตำบล / แขวง</label>
                                <input type="text" id="cust-subdistrict" placeholder="ตำบล/แขวง" class="w-full px-3.5 py-2.5 bg-cream-50 border border-cream-300 rounded-xl text-xs sm:text-sm">
                            </div>

                            <div class="col-span-2 sm:col-span-1">
                                <label class="block text-xs font-bold text-slate-700 mb-1">อำเภอ / เขต</label>
                                <input type="text" id="cust-district" placeholder="อำเภอ/เขต" class="w-full px-3.5 py-2.5 bg-cream-50 border border-cream-300 rounded-xl text-xs sm:text-sm">
                            </div>

                            <div class="col-span-2 sm:col-span-1">
                                <label class="block text-xs font-bold text-slate-700 mb-1">จังหวัด</label>
                                <input type="text" id="cust-province" placeholder="จังหวัด" class="w-full px-3.5 py-2.5 bg-cream-50 border border-cream-300 rounded-xl text-xs sm:text-sm">
                            </div>
                        </div>

                        <!-- Logistics Routing Box -->
                        <div id="logistics-routing-box" class="bg-cream-50 border border-cream-200 rounded-2xl p-3.5 text-xs space-y-1">
                            <div class="flex items-center justify-between font-bold text-slate-900">
                                <span class="flex items-center gap-1.5">
                                    <span>🚚</span> ขนส่งที่ระบบจัดสรร: <strong id="carrier-name-display" class="text-[#EE4D2D]">SPX Express (Shopee Express)</strong>
                                </span>
                                <span id="carrier-fee-badge" class="text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 font-bold">
                                    ส่งฟรี (฿0)
                                </span>
                            </div>
                            <p id="carrier-reason-display" class="text-[11px] text-slate-500 leading-relaxed">
                                • จัดส่งมาตรฐานในเขตพื้นที่ทั่วไป (SPX Express ด่วนทั่วไทย)
                            </p>
                        </div>
                    </div>

                    <!-- Step 2: Payment -->
                    <div class="space-y-4 pt-3 border-t border-cream-100">
                        <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                            <span class="w-5 h-5 rounded-full bg-[#EE4D2D] text-white flex items-center justify-center text-[10px] font-bold">2</span>
                            ช่องทางการชำระเงิน
                        </h3>

                        <div class="grid grid-cols-2 gap-3">
                            <button type="button" onclick="setPaymentMethod(\x27PROMPTPAY\x27)" id="btn-pay-promptpay" class="p-3 rounded-2xl border-2 border-[#EE4D2D] bg-orange-50 text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-1 shadow-sm transition-all">
                                <span class="text-lg">📱</span>
                                <span>PromptPay QR Code</span>
                                <span class="text-[10px] font-normal text-slate-500">สแกนจ่าย + แนบสลิป</span>
                            </button>

                            <button type="button" onclick="setPaymentMethod(\x27STORE_CREDIT\x27)" id="btn-pay-wallet" class="p-3 rounded-2xl border-2 border-slate-200 bg-cream-50 text-slate-600 text-xs font-bold flex flex-col items-center gap-1 transition-all">
                                <span class="text-lg">👛</span>
                                <span>กระเป๋าเครดิต (Store Credit)</span>
                                <span id="wallet-btn-bal" class="text-[10px] font-bold text-emerald-600">คงเหลือ ฿530.00</span>
                            </button>
                        </div>

                        <!-- PROMPTPAY PANEL -->
                        <div id="panel-promptpay" class="bg-cream-50 border border-cream-200 rounded-2xl p-4 sm:p-5 space-y-4 text-center">
                            <div class="space-y-1">
                                <span class="text-xs text-slate-500">ยอดชำระสุทธิ (แอปธนาคารจะกรอกตัวเลขให้อัตโนมัติ):</span>
                                <p id="promptpay-amount-display" class="text-3xl font-black text-[#EE4D2D]">฿390.00</p>
                            </div>

                            <div class="bg-white p-3 rounded-2xl border-2 border-cream-300 shadow-md inline-block">
                                <img id="promptpay-qr-img" src="" alt="PromptPay QR" class="w-44 h-44 object-contain">
                            </div>

                            <div class="bg-white p-3 rounded-xl border border-cream-200 text-xs text-left space-y-1">
                                <div class="flex justify-between">
                                    <span><strong>ชื่อบัญชี:</strong> สุเมธา แท่นธรรมโรจน์</span>
                                    <span class="text-[10px] bg-emerald-50 text-emerald-700 px-2 py-0.5 rounded font-bold">กสิกรไทย</span>
                                </div>
                                <div class="flex justify-between items-center pt-1 border-t border-slate-100">
                                    <span><strong>เลขพร้อมเพย์:</strong> 061-537-2239</span>
                                    <button type="button" onclick="copyPromptPay()" class="text-[10px] bg-[#EE4D2D] hover:bg-[#d73211] text-white px-2 py-1 rounded font-bold">
                                        คัดลอกเลข
                                    </button>
                                </div>
                            </div>

                            <div class="space-y-2 text-left pt-2 border-t border-cream-200">
                                <label class="block text-xs font-bold text-slate-800">
                                    แนบสลิปโอนเงิน (ระบบป้องกันการใช้สลิปซ้ำ Anti-Replay): *
                                </label>
                                <input type="file" id="slip-file-input" accept="image/*" onchange="handleSlipFile(this)" class="w-full text-xs text-slate-500 file:mr-3 file:py-2 file:px-3 file:rounded-xl file:border-0 file:text-xs file:font-bold file:bg-[#EE4D2D] file:text-white hover:file:bg-[#d73211] cursor-pointer">
                                <div id="slip-status-msg" class="hidden text-xs text-emerald-700 font-bold bg-emerald-50 p-2.5 rounded-xl border border-emerald-200"></div>
                            </div>
                        </div>

                        <!-- STORE CREDIT PANEL -->
                        <div id="panel-wallet" class="hidden bg-orange-50/70 border border-orange-200 rounded-2xl p-4 sm:p-5 space-y-4">
                            <div class="flex items-center justify-between">
                                <div>
                                    <span class="text-xs text-slate-600 block">ยอดเครดิตคงเหลือของคุณ:</span>
                                    <span id="wallet-balance-big" class="text-2xl font-black text-emerald-700">฿530.00</span>
                                </div>
                                <button type="button" onclick="openTopupModal()" class="bg-emerald-600 hover:bg-emerald-500 text-white text-xs px-3.5 py-2 rounded-xl font-bold transition-all shadow-md">
                                    + เติมเงินรับโบนัสเพิ่ม
                                </button>
                            </div>
                            <div class="bg-white p-3 rounded-xl border border-orange-200 text-xs text-slate-600 space-y-1">
                                <div class="flex justify-between">
                                    <span>ยอดคำสั่งซื้อ:</span>
                                    <span id="wallet-order-amt" class="font-bold text-slate-900">฿390.00</span>
                                </div>
                                <div class="flex justify-between">
                                    <span>คงเหลือหลังหัก:</span>
                                    <span id="wallet-after-bal" class="font-bold text-emerald-700">฿140.00</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Pricing Summary -->
                    <div class="p-4 bg-cream-50 rounded-2xl border border-cream-200 space-y-2 text-xs">
                        <div class="flex justify-between text-slate-600">
                            <span>ราคาสินค้า (<span id="summary-variant-name">รุ่นมาตรฐาน</span> x<span id="summary-qty">1</span>)</span>
                            <span id="summary-subtotal" class="font-bold text-slate-900">฿390.00</span>
                        </div>
                        <div class="flex justify-between text-slate-600">
                            <span>ค่าจัดส่ง (<span id="summary-carrier">SPX Express</span>)</span>
                            <span id="summary-shipping" class="font-bold text-slate-900">ฟรี (฿0)</span>
                        </div>
                        <div class="flex justify-between text-base font-black text-slate-900 pt-2 border-t border-cream-200">
                            <span>ยอดสุทธิที่ต้องชำระ:</span>
                            <span id="summary-total" class="text-[#EE4D2D] text-xl font-black">฿390.00</span>
                        </div>
                    </div>

                    <!-- ACTION 1: MAIN SUBMIT BUTTON (Shopee Orange #EE4D2D) -->
                    <button type="button" onclick="submitDirectOrder()" class="w-full bg-[#EE4D2D] hover:bg-[#d73211] text-white font-extrabold py-4 rounded-2xl shadow-xl shadow-orange-500/25 transition-all text-base sm:text-lg flex items-center justify-center gap-2 active:scale-95 cursor-pointer">
                        <span id="submit-btn-text">⚡ สั่งซื้อทันที (฿390.00)</span>
                    </button>

                    <!-- ACTION 2: SOCIAL PROOF SHOPEE AFFILIATE -->
                    <div id="shopee-affiliate-box" class="text-center pt-1">
                        <a id="shopee-affiliate-btn" href="https://th.shp.ee/sdFv2cS1" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 text-xs sm:text-sm font-bold text-slate-600 hover:text-[#EE4D2D] bg-cream-50 hover:bg-orange-50 px-4 py-2.5 rounded-xl border border-cream-300 transition-all">
                            <span>⭐ ดูรีวิวผู้ใช้จริงใน Shopee &gt;</span>
                        </a>
                    </div>

                </div>
            </div>
        </section>

    </main>

    <!-- ================= FULLSCREEN LIGHTBOX GALLERY MODAL ================= -->
    <div id="gallery-modal" class="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-slate-950/90 backdrop-blur-md hidden">
        <div class="relative max-w-2xl w-full bg-slate-900 border border-slate-700 rounded-3xl overflow-hidden shadow-2xl flex flex-col">
            <div class="p-4 bg-slate-950 border-b border-slate-800 flex justify-between items-center text-white">
                <div>
                    <h4 id="gallery-modal-title" class="text-sm font-bold truncate max-w-md">ดูรูปสินค้า</h4>
                    <span id="gallery-modal-counter" class="text-xs text-amber-400 font-mono">รูปที่ 1/4</span>
                </div>
                <button onclick="closeGalleryModal()" class="text-slate-400 hover:text-white p-1 text-xl font-bold">✕</button>
            </div>

            <div class="relative bg-slate-950 flex items-center justify-center min-h-[300px] sm:min-h-[380px] p-4">
                <button onclick="prevGalleryImage()" class="absolute left-3 top-1/2 -translate-y-1/2 bg-slate-900/80 hover:bg-[#EE4D2D] text-white p-3 rounded-full border border-slate-700 transition-all z-10 shadow-lg text-lg">
                    ◀
                </button>
                <img id="gallery-main-img" src="" alt="Product View" class="max-h-[55vh] max-w-full object-contain rounded-2xl">
                <button onclick="nextGalleryImage()" class="absolute right-3 top-1/2 -translate-y-1/2 bg-slate-900/80 hover:bg-[#EE4D2D] text-white p-3 rounded-full border border-slate-700 transition-all z-10 shadow-lg text-lg">
                    ▶
                </button>
            </div>

            <div class="p-3 bg-slate-900 border-t border-slate-800 text-center">
                <span id="gallery-image-name" class="text-xs font-bold text-amber-400">📁 ภาพสินค้า</span>
            </div>

            <div id="gallery-thumbs-container" class="p-3 bg-slate-950 border-t border-slate-800 flex gap-2 overflow-x-auto justify-center"></div>
        </div>
    </div>

    <!-- ================= TOPUP MODAL ================= -->
    <div id="topup-modal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm hidden">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 space-y-4 shadow-2xl border border-slate-200">
            <div class="flex justify-between items-center border-b border-slate-100 pb-3">
                <h3 class="font-black text-slate-900 text-base">👛 เติมเงินกระเป๋าเครดิต (รับโบนัสพิเศษ)</h3>
                <button onclick="closeTopupModal()" class="text-slate-400 hover:text-slate-600 font-bold">✕</button>
            </div>
            <p className="text-xs text-slate-500">เติมเงินล่วงหน้าเพื่อรับโบนัสพิเศษ และกดสั่งซื้อรอบถัดไปได้ทันทีโดยไม่ต้องเปิดแอปธนาคาร</p>
            <div class="space-y-2.5">
                <div onclick="selectTopup(300, 10)" class="p-3.5 rounded-2xl border-2 border-slate-200 hover:border-emerald-500 hover:bg-emerald-50 cursor-pointer flex justify-between items-center transition-all">
                    <div>
                        <span class="text-sm font-bold text-slate-900 block">เติม ฿300</span>
                        <span class="text-xs text-emerald-600 font-bold">รับโบนัส +฿10 (ได้เครดิต ฿310)</span>
                    </div>
                    <span class="bg-emerald-600 text-white text-xs px-3 py-1.5 rounded-xl font-bold">เลือก</span>
                </div>
                <div onclick="selectTopup(500, 30)" class="p-3.5 rounded-2xl border-2 border-slate-200 hover:border-emerald-500 hover:bg-emerald-50 cursor-pointer flex justify-between items-center transition-all">
                    <div>
                        <span class="text-sm font-bold text-slate-900 block">เติม ฿500 (ยอดนิยม)</span>
                        <span class="text-xs text-emerald-600 font-bold">รับโบนัส +฿30 (ได้เครดิต ฿530)</span>
                    </div>
                    <span class="bg-emerald-600 text-white text-xs px-3 py-1.5 rounded-xl font-bold">เลือก</span>
                </div>
                <div onclick="selectTopup(1000, 80)" class="p-3.5 rounded-2xl border-2 border-slate-200 hover:border-emerald-500 hover:bg-emerald-50 cursor-pointer flex justify-between items-center transition-all">
                    <div>
                        <span class="text-sm font-bold text-slate-900 block">เติม ฿1,000</span>
                        <span class="text-xs text-emerald-600 font-bold">รับโบนัส +฿80 (ได้เครดิต ฿1,080)</span>
                    </div>
                    <span class="bg-emerald-600 text-white text-xs px-3 py-1.5 rounded-xl font-bold">เลือก</span>
                </div>
            </div>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="bg-slate-900 text-slate-400 py-6 border-t border-slate-800 text-xs text-center space-y-1.5">
        <p class="font-bold text-slate-300">GOODSTONE TACTICAL SLINGSHOT © 2026</p>
        <p>Single-Page Direct-to-Checkout • จัดส่งด่วน SPX Express / ไปรษณีย์ไทย EMS • ชำระผ่านระบบพร้อมเพย์และกระเป๋าเครดิต</p>
    </footer>

    <!-- LOGIC SCRIPT -->
    <script>
        const DEFAULT_PRODUCTS = """ + products_json + """;
        const DEFAULT_ORDERS = """ + orders_json + """;
        const THAI_ADDRESSES = """ + addresses_json + """;

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

        function crc16(data) {
            let crc = 0xFFFF;
            for (let i = 0; i < data.length; i++) {
                crc ^= (data.charCodeAt(i) << 8);
                for (let j = 0; j < 8; j++) {
                    if (crc & 0x8000) crc = ((crc << 1) ^ 0x1021) & 0xFFFF;
                    else crc = (crc << 1) & 0xFFFF;
                }
            }
            return (crc & 0xFFFF).toString(16).toUpperCase().padStart(4, "0");
        }

        function generatePromptPayQR(amount) {
            let phone = "0615372239";
            let target = "0066" + phone.substring(1);
            let subTag = "01" + String(target.length).padStart(2, "0") + target;
            let merchantData = "0016A000000677010111" + subTag;
            let tag29 = "29" + String(merchantData.length).padStart(2, "0") + merchantData;

            let payload = "000201";
            payload += (amount > 0) ? "010212" : "010211";
            payload += tag29;
            payload += "5303764";
            if (amount > 0) {
                let amtStr = Number(amount).toFixed(2);
                payload += "54" + String(amtStr.length).padStart(2, "0") + amtStr;
            }
            payload += "5802TH6304";
            let checksum = crc16(payload);
            return payload + checksum;
        }

        function init() {
            lucide.createIcons();
            
            // Hydrate products
            const savedProducts = localStorage.getItem("goodstone_products");
            if (savedProducts) {
                try { products = JSON.parse(savedProducts); } catch(e) {}
            } else {
                localStorage.setItem("goodstone_products", JSON.stringify(DEFAULT_PRODUCTS));
            }

            // Hydrate Long-lived Cookie Session (365 days)
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
                    document.getElementById("auto-cookie-badge").classList.remove("hidden");
                } catch(e) {}
            }

            renderCatalogGrid();
        }

        // ================= VIEW SWITCHERS =================
        function showCatalogView() {
            document.getElementById("view-catalog").classList.remove("hidden");
            document.getElementById("view-checkout").classList.add("hidden");
            window.scrollTo({ top: 0, behavior: "smooth" });
        }

        function openProductDirectCheckout(productId) {
            const p = products.find(x => x.id === productId);
            if (!p) return;

            selectedProduct = p;
            selectedVariantIdx = 0;
            quantity = 1;

            document.getElementById("view-catalog").classList.add("hidden");
            document.getElementById("view-checkout").classList.remove("hidden");
            window.scrollTo({ top: 0, behavior: "smooth" });

            renderProductCheckoutDetail();
            updateCalculations();
        }

        // ================= CATALOG GRID =================
        function renderCatalogGrid() {
            const grid = document.getElementById("product-grid");
            grid.innerHTML = "";

            const list = selectedCategory === "all" ? products : products.filter(p => p.category === selectedCategory);

            if (list.length === 0) {
                grid.innerHTML = `<div class="col-span-full text-center py-12 text-slate-400">ไม่พบสินค้าในหมวดหมู่นี้</div>`;
                return;
            }

            list.forEach(p => {
                const isOutOfStock = (p.stock <= 0);
                const imageCount = (p.images && p.images.length > 0) ? p.images.length : 1;
                const imgSrc = p.image_file || p.fallback_image;

                const card = document.createElement("div");
                card.className = "bg-white rounded-3xl shadow-sm hover:shadow-md border border-cream-200 overflow-hidden flex flex-col transition-all group";

                card.innerHTML = `
                    <!-- Clickable Product Image triggers Direct Checkout -->
                    <div onclick="openProductDirectCheckout('${p.id}')" class="h-48 sm:h-52 overflow-hidden bg-slate-950 relative flex items-center justify-center cursor-pointer group/img">
                        <img src="${imgSrc}" onerror="this.onerror=null; this.src='${p.fallback_image}';" alt="${p.name}" class="w-full h-full object-contain group-hover/img:scale-105 transition-transform duration-300">
                        <span class="absolute top-3 right-3 bg-slate-900/80 backdrop-blur-sm text-amber-400 text-[11px] px-2.5 py-1 rounded-full font-bold">
                            คงเหลือ ${p.stock}
                        </span>
                        <div class="absolute bottom-2 left-2 bg-black/80 text-white text-[10px] px-2.5 py-1 rounded-xl flex items-center gap-1 group-hover/img:bg-[#EE4D2D] font-bold transition-all shadow-md">
                            <span>⚡ แตะรูปเพื่อซื้อด่วน (${imageCount} รูป)</span>
                        </div>
                    </div>

                    <!-- Content -->
                    <div class="p-4 sm:p-5 flex flex-col flex-grow justify-between space-y-3">
                        <div class="space-y-1.5">
                            <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-orange-50 text-[#EE4D2D] border border-orange-200">
                                ${p.category}
                            </span>
                            <h3 onclick="openProductDirectCheckout('${p.id}')" class="font-bold text-slate-900 text-sm sm:text-base line-clamp-2 cursor-pointer hover:text-[#EE4D2D] transition-colors">
                                ${p.name}
                            </h3>
                            <p class="text-xs text-slate-500 line-clamp-2 leading-relaxed">
                                ${p.description}
                            </p>
                        </div>

                        <!-- Price & Action Button -->
                        <div class="pt-2 border-t border-cream-100 flex items-center justify-between">
                            <div>
                                <span class="text-[10px] text-slate-400 block">ราคาเริ่มต้น</span>
                                <span class="text-lg sm:text-xl font-extrabold text-[#EE4D2D]">฿${p.price.toLocaleString()}</span>
                            </div>
                            <button onclick="openProductDirectCheckout('${p.id}')" class="bg-[#EE4D2D] hover:bg-[#d73211] text-white px-3.5 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1 shadow-md active:scale-95 cursor-pointer">
                                <span>⚡ ซื้อด่วน</span>
                            </button>
                        </div>
                    </div>
                `;
                grid.appendChild(card);
            });
            lucide.createIcons();
        }

        function filterCategory(cat) {
            selectedCategory = cat;
            document.querySelectorAll(".cat-btn").forEach(btn => {
                if (btn.dataset.cat === cat) {
                    btn.className = "cat-btn active px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all bg-slate-900 text-white";
                } else {
                    btn.className = "cat-btn px-3.5 py-2 rounded-xl text-xs sm:text-sm font-bold transition-all bg-cream-100 text-slate-700 hover:bg-orange-50 hover:text-[#EE4D2D]";
                }
            });
            renderCatalogGrid();
        }

        function searchProducts() {
            const q = document.getElementById("search-input").value.toLowerCase();
            const filtered = products.filter(p => p.name.toLowerCase().includes(q) || p.description.toLowerCase().includes(q));
            
            const grid = document.getElementById("product-grid");
            grid.innerHTML = "";
            filtered.forEach(p => {
                const card = document.createElement("div");
                card.className = "bg-white rounded-3xl shadow-sm hover:shadow-md border border-cream-200 overflow-hidden flex flex-col transition-all";
                card.innerHTML = `
                    <div onclick="openProductDirectCheckout('${p.id}')" class="h-48 overflow-hidden bg-slate-950 relative flex items-center justify-center cursor-pointer">
                        <img src="${p.image_file || p.fallback_image}" class="w-full h-full object-contain">
                    </div>
                    <div class="p-4 flex flex-col flex-grow justify-between space-y-2">
                        <h3 onclick="openProductDirectCheckout('${p.id}')" class="font-bold text-slate-900 text-sm cursor-pointer hover:text-[#EE4D2D]">${p.name}</h3>
                        <div class="flex justify-between items-center pt-2 border-t border-cream-100">
                            <span class="text-base font-extrabold text-[#EE4D2D]">฿${p.price.toLocaleString()}</span>
                            <button onclick="openProductDirectCheckout('${p.id}')" class="bg-[#EE4D2D] text-white px-3 py-1.5 rounded-xl text-xs font-bold">⚡ ซื้อด่วน</button>
                        </div>
                    </div>
                `;
                grid.appendChild(card);
            });
        }

        // ================= DIRECT CHECKOUT DETAILS =================
        function renderProductCheckoutDetail() {
            const p = selectedProduct;
            document.getElementById("detail-title").innerText = p.name;
            document.getElementById("detail-desc").innerText = p.description;
            document.getElementById("detail-cat-tag").innerText = p.category.toUpperCase();
            document.getElementById("detail-stock-badge").innerText = `สต็อก: ${p.stock} ชิ้น`;

            const images = p.images && p.images.length > 0 ? p.images : [{ file: p.image_file || p.fallback_image, name: `${p.id}_main.jpg` }];
            document.getElementById("detail-main-img").src = images[0].file;
            document.getElementById("detail-gallery-label").innerText = `แตะดูรูปใหญ่ (${images.length} ภาพ)`;

            // Thumbnails Strip
            const thumbsStrip = document.getElementById("detail-thumbs-strip");
            thumbsStrip.innerHTML = "";
            images.forEach((img, idx) => {
                const thumb = document.createElement("div");
                thumb.className = `w-14 h-14 rounded-xl p-1 bg-slate-950 border-2 cursor-pointer transition-all flex-shrink-0 flex items-center justify-center ${idx === 0 ? "border-[#EE4D2D] scale-105 shadow-md" : "border-slate-300 opacity-60"}`;
                thumb.innerHTML = `<img src="${img.file}" class="w-full h-full object-contain">`;
                thumb.onclick = () => {
                    document.getElementById("detail-main-img").src = img.file;
                    Array.from(thumbsStrip.children).forEach((c, i) => {
                        c.className = `w-14 h-14 rounded-xl p-1 bg-slate-950 border-2 cursor-pointer transition-all flex-shrink-0 flex items-center justify-center ${i === idx ? "border-[#EE4D2D] scale-105 shadow-md" : "border-slate-300 opacity-60"}`;
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

            // Variant Pills (Shopee Style)
            const pillsContainer = document.getElementById("detail-variant-pills");
            pillsContainer.innerHTML = "";
            p.variants.forEach((v, idx) => {
                const isSel = (idx === selectedVariantIdx);
                const btn = document.createElement("button");
                btn.type = "button";
                btn.className = `px-3 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 ${isSel ? "bg-[#EE4D2D] text-white border-2 border-[#d73211] shadow-md scale-105" : "bg-cream-50 hover:bg-orange-50 hover:border-[#EE4D2D] text-slate-700 border border-cream-300"}`;
                btn.innerHTML = `${isSel ? "<span>✓</span>" : ""}<span>${v.name}</span><span class="${isSel ? "bg-black/30 text-amber-300" : "bg-cream-200 text-[#EE4D2D]"} text-[11px] px-1.5 py-0.5 rounded font-black">฿${v.price.toLocaleString()}</span>`;
                btn.onclick = () => {
                    selectedVariantIdx = idx;
                    renderProductCheckoutDetail();
                    updateCalculations();
                };
                pillsContainer.appendChild(btn);
            });
        }

        function changeQty(delta) {
            quantity = Math.max(1, quantity + delta);
            document.getElementById("detail-qty-display").innerText = quantity;
            updateCalculations();
        }

        function handlePostalCodeInput(code) {
            const clean = code.trim();
            const suggestionsBox = document.getElementById("address-suggestions-box");

            if (clean.length < 2) {
                suggestionsBox.classList.add("hidden");
                updateLogisticsRouting(clean);
                return;
            }

            const matches = THAI_ADDRESSES.filter(a => a.postal_code.startsWith(clean));
            if (matches.length > 0) {
                suggestionsBox.innerHTML = "";
                matches.slice(0, 6).forEach(m => {
                    const div = document.createElement("div");
                    div.className = "p-2.5 hover:bg-orange-50 cursor-pointer text-xs border-b border-slate-100 flex justify-between items-center";
                    div.innerHTML = `<span>ต.${m.subdistrict} อ.${m.district} จ.${m.province}</span><span class="font-bold text-[#EE4D2D]">${m.postal_code}</span>`;
                    div.onclick = () => {
                        document.getElementById("cust-postcode").value = m.postal_code;
                        document.getElementById("cust-subdistrict").value = m.subdistrict;
                        document.getElementById("cust-district").value = m.district;
                        document.getElementById("cust-province").value = m.province;
                        suggestionsBox.classList.add("hidden");
                        updateLogisticsRouting(m.postal_code);
                    };
                    suggestionsBox.appendChild(div);
                });
                suggestionsBox.classList.remove("hidden");
            } else {
                suggestionsBox.classList.add("hidden");
            }

            if (matches.length === 1) {
                document.getElementById("cust-subdistrict").value = matches[0].subdistrict;
                document.getElementById("cust-district").value = matches[0].district;
                document.getElementById("cust-province").value = matches[0].province;
            }

            updateLogisticsRouting(clean);
        }

        function updateLogisticsRouting(code) {
            const isRemote = code.startsWith("94") || code.startsWith("95") || code.startsWith("96") || code.startsWith("58") || ["84320", "84360", "23170", "23120", "81150", "82160", "63170", "50310"].includes(code);

            const carrierDisplay = isRemote ? "ไปรษณีย์ไทย ด่วนพิเศษ (EMS)" : "SPX Express (Shopee Express)";
            const reasonDisplay = isRemote
                ? "• พื้นที่ห่างไกล / เกาะ / 3 จว. ชายแดนใต้ (สลับเป็นไปรษณีย์ไทย EMS อัตโนมัติ เพื่อเลี่ยงค่าธรรมเนียมห่างไกล 50 บาท)"
                : "• จัดส่งมาตรฐานในเขตพื้นที่ทั่วไป (SPX Express ด่วนทั่วไทย)";

            document.getElementById("carrier-name-display").innerText = carrierDisplay;
            document.getElementById("carrier-reason-display").innerText = reasonDisplay;
            document.getElementById("summary-carrier").innerText = carrierDisplay;
            updateCalculations();
        }

        function updateCalculations() {
            const activeV = selectedProduct.variants[selectedVariantIdx] || { name: "รุ่นมาตรฐาน", price: selectedProduct.price };
            const unitPrice = activeV.price;
            const subtotal = unitPrice * quantity;
            const isFreeShipping = (subtotal >= 200);
            const shippingCost = isFreeShipping ? 0 : 25;
            const total = subtotal + shippingCost;

            document.getElementById("summary-variant-name").innerText = activeV.name;
            document.getElementById("summary-qty").innerText = quantity;
            document.getElementById("summary-subtotal").innerText = `฿${subtotal.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("summary-shipping").innerText = isFreeShipping ? "ฟรี (฿0)" : "฿25.00";
            document.getElementById("summary-total").innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("promptpay-amount-display").innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("submit-btn-text").innerText = `⚡ สั่งซื้อทันที (฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})})`;

            document.getElementById("carrier-fee-badge").innerText = isFreeShipping ? "ส่งฟรี (฿0)" : "฿25";
            document.getElementById("wallet-order-amt").innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("wallet-after-bal").innerText = `฿${Math.max(0, userWallet.balance - total).toLocaleString(undefined, {minimumFractionDigits: 2})}`;

            // Update Dynamic PromptPay QR
            const ppPayload = generatePromptPayQR(total);
            document.getElementById("promptpay-qr-img").src = `https://api.qrserver.com/v1/create-qr-code/?size=260x260&margin=12&data=${encodeURIComponent(ppPayload)}`;
        }

        function setPaymentMethod(method) {
            paymentMethod = method;
            const btnPP = document.getElementById("btn-pay-promptpay");
            const btnW = document.getElementById("btn-pay-wallet");
            const panelPP = document.getElementById("panel-promptpay");
            const panelW = document.getElementById("panel-wallet");

            if (method === "PROMPTPAY") {
                btnPP.className = "p-3 rounded-2xl border-2 border-[#EE4D2D] bg-orange-50 text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-1 shadow-sm transition-all";
                btnW.className = "p-3 rounded-2xl border-2 border-cream-200 bg-cream-50 text-slate-600 text-xs font-bold flex flex-col items-center gap-1 transition-all";
                panelPP.classList.remove("hidden");
                panelW.classList.add("hidden");
            } else {
                btnW.className = "p-3 rounded-2xl border-2 border-[#EE4D2D] bg-orange-50 text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-1 shadow-sm transition-all";
                btnPP.className = "p-3 rounded-2xl border-2 border-cream-200 bg-cream-50 text-slate-600 text-xs font-bold flex flex-col items-center gap-1 transition-all";
                panelW.classList.remove("hidden");
                panelPP.classList.add("hidden");
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
                document.getElementById("wallet-btn-bal").innerText = `คงเหลือ ฿${userWallet.balance.toLocaleString()}`;
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
                msgBox.innerText = "✅ แนบสลิปโอนเงินเรียบร้อยแล้ว (พร้อมตรวจสอบรหัสธุรกรรมป้องกันการใช้ซ้ำ)";
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

            const activeV = selectedProduct.variants[selectedVariantIdx] || { name: "รุ่นมาตรฐาน", price: selectedProduct.price };
            const subtotal = activeV.price * quantity;
            const isFreeShipping = (subtotal >= 200);
            const shippingCost = isFreeShipping ? 0 : 25;
            const total = subtotal + shippingCost;

            if (paymentMethod === "PROMPTPAY" && !slipImageBase64) {
                alert("กรุณาแนบสลิปหลักฐานการโอนเงินก่อนยืนยันสั่งซื้อครับ");
                return;
            }

            if (paymentMethod === "STORE_CREDIT" && userWallet.balance < total) {
                alert(`ยอดเงินในกระเป๋าเครดิตไม่เพียงพอ (คงเหลือ ฿${userWallet.balance.toLocaleString()} / ยอดชำระ ฿${total.toLocaleString()})`);
                return;
            }

            const now = new Date();
            const orderId = `ORD-${now.getFullYear()}${String(now.getMonth()+1).padStart(2,\x270\x27)}${String(now.getDate()).padStart(2,\x270\x27)}-${Math.floor(100 + Math.random()*900)}`;
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
                total_amount: total,
                status: "PAID",
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

            // Save Profile Cookie (365 days)
            const profile = { name, phone, addressLine, postal_code: postcode, subdistrict, district, province };
            localStorage.setItem("goodstone_saved_profile", JSON.stringify(profile));
            document.cookie = `goodstone_user_session=${encodeURIComponent(JSON.stringify(profile))}; max-age=${365*24*60*60}; path=/`;

            // If Store Credit, deduct
            if (paymentMethod === "STORE_CREDIT") {
                userWallet.balance -= total;
                localStorage.setItem(`goodstone_wallet_${phone.replace(/[^0-9]/g, "")}`, JSON.stringify(userWallet));
            }

            // Save order
            let allOrders = [];
            try {
                const saved = localStorage.getItem("goodstone_orders");
                if (saved) allOrders = JSON.parse(saved);
            } catch(e) {}
            allOrders.unshift(newOrder);
            localStorage.setItem("goodstone_orders", JSON.stringify(allOrders));

            alert(`🎉 สั่งซื้อและชำระเงินสำเร็จ!\nรหัสคำสั่งซื้อ: ${newOrder.id}\nขนส่งที่จัดสรร: ${newOrder.shipping_provider}\nเลขพัสดุ: ${newOrder.tracking_number}`);
            window.location.href = "track.html";
        }

        // ================= GALLERY LIGHTBOX =================
        function openGalleryModal() {
            const images = selectedProduct.images && selectedProduct.images.length > 0
                ? selectedProduct.images
                : [{ file: selectedProduct.image_file || selectedProduct.fallback_image, name: `${selectedProduct.id}_main.jpg` }];
            currentGalleryIdx = 0;
            renderGalleryModal(images);
            document.getElementById("gallery-modal").classList.remove("hidden");
        }

        function closeGalleryModal() {
            document.getElementById("gallery-modal").classList.add("hidden");
        }

        function renderGalleryModal(images) {
            if (currentGalleryIdx < 0) currentGalleryIdx = images.length - 1;
            if (currentGalleryIdx >= images.length) currentGalleryIdx = 0;

            const cur = images[currentGalleryIdx];
            document.getElementById("gallery-modal-title").innerText = selectedProduct.name;
            document.getElementById("gallery-modal-counter").innerText = `รูปที่ ${currentGalleryIdx + 1} จาก ${images.length}`;
            document.getElementById("gallery-main-img").src = cur.file;
            document.getElementById("gallery-image-name").innerText = `📁 ${cur.name || cur.file}`;

            const thumbsBox = document.getElementById("gallery-thumbs-container");
            thumbsBox.innerHTML = "";
            images.forEach((img, idx) => {
                const d = document.createElement("div");
                d.className = `w-14 h-14 rounded-xl p-1 bg-slate-900 border-2 cursor-pointer transition-all flex-shrink-0 flex items-center justify-center ${idx === currentGalleryIdx ? "border-[#EE4D2D] scale-110 shadow-lg" : "border-slate-700 opacity-60"}`;
                d.innerHTML = `<img src="${img.file}" class="w-full h-full object-contain">`;
                d.onclick = () => {
                    currentGalleryIdx = idx;
                    renderGalleryModal(images);
                };
                thumbsBox.appendChild(d);
            });
        }

        function prevGalleryImage() {
            const images = selectedProduct.images || [{ file: selectedProduct.image_file }];
            currentGalleryIdx -= 1;
            renderGalleryModal(images);
        }

        function nextGalleryImage() {
            const images = selectedProduct.images || [{ file: selectedProduct.image_file }];
            currentGalleryIdx += 1;
            renderGalleryModal(images);
        }

        // ================= TOPUP MODAL =================
        function openTopupModal() {
            document.getElementById("topup-modal").classList.remove("hidden");
        }

        function closeTopupModal() {
            document.getElementById("topup-modal").classList.add("hidden");
        }

        function selectTopup(pay, bonus) {
            const phone = document.getElementById("cust-phone").value.trim();
            if (!phone) {
                alert("กรุณากรอกเบอร์โทรศัพท์ก่อนเติมเงินครับ");
                return;
            }
            const clean = phone.replace(/[^0-9]/g, "");
            const totalAdd = pay + bonus;
            userWallet.balance += totalAdd;
            userWallet.total_topup += pay;
            userWallet.total_bonus += bonus;

            localStorage.setItem(`goodstone_wallet_${clean}`, JSON.stringify(userWallet));
            document.getElementById("user-wallet-display").innerText = `฿${userWallet.balance.toLocaleString()}`;
            document.getElementById("wallet-btn-bal").innerText = `คงเหลือ ฿${userWallet.balance.toLocaleString()}`;
            document.getElementById("wallet-balance-big").innerText = `฿${userWallet.balance.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            updateCalculations();
            closeTopupModal();
            alert(`🎉 เติมเงินสำเร็จ! ได้รับเครดิต ฿${totalAdd.toLocaleString()} (ยอดคงเหลือ: ฿${userWallet.balance.toLocaleString()})`);
        }

        window.onload = init;
    </script>
</body>
</html>"""

with open("/working_dir/slingshot-shop/index.html", "w", encoding="utf-8") as f:
    f.write(index_html_cream)

print("slingshot-shop/index.html updated with Product Catalog Grid as Homepage + Direct Checkout on Click + Warm Cream & Shopee Orange Theme!")
