import json

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))
products_json = json.dumps(data["products"], ensure_ascii=False)
orders_json = json.dumps(data["orders"], ensure_ascii=False)

admin_html_code = """<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GOODSTONE ADMIN - ระบบจัดการร้านค้า สต็อก และภาษี</title>
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
        body { font-family: "Prompt", sans-serif; background-color: #F9F6F0; color: #2C241E; }
    </style>
</head>
<body class="bg-[#F9F6F0] text-[#2C241E] min-h-screen flex flex-col font-sans">

    <!-- ADMIN HEADER (CREAM WHITE & SHOPEE ORANGE) -->
    <header class="sticky top-0 z-40 bg-white border-b-2 border-[#EBE3D5] shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <!-- Logo -->
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-2xl bg-[#EE4D2D] text-white font-black text-xl flex items-center justify-center shadow-md shadow-orange-500/20">
                        🛡️
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="font-black text-base sm:text-lg text-[#2C241E]">GOODSTONE ADMIN</span>
                            <span class="bg-[#FFF2EE] text-[#EE4D2D] border border-[#FFD5CC] text-[10px] px-2 py-0.5 rounded font-black uppercase">
                                Pro Portal
                            </span>
                        </div>
                        <span class="text-[11px] text-slate-500 font-medium">เจ้าของร้าน: คุณสุเมธา แท่นธรรมโรจน์ (061-537-2239)</span>
                    </div>
                </div>

                <!-- Navigation Tabs -->
                <div class="flex items-center gap-2 sm:gap-3">
                    <div class="flex bg-[#F2EDE4] p-1 rounded-2xl border border-[#EBE3D5] text-xs font-bold">
                        <button onclick="switchTab('ORDERS')" id="tab-btn-orders" class="px-3.5 py-1.5 rounded-xl transition-all bg-[#EE4D2D] text-white shadow-md">
                            📦 คำสั่งซื้อ
                        </button>
                        <button onclick="switchTab('INVENTORY')" id="tab-btn-inventory" class="px-3.5 py-1.5 rounded-xl transition-all text-slate-700 hover:text-[#EE4D2D]">
                            📊 สต็อก & ตัวเลือก
                        </button>
                        <button onclick="switchTab('VAT')" id="tab-btn-vat" class="px-3.5 py-1.5 rounded-xl transition-all text-slate-700 hover:text-[#EE4D2D]">
                            📈 เพดานภาษี (1.8M)
                        </button>
                    </div>

                    <a href="index.html" target="_blank" class="hidden sm:inline-flex bg-white hover:bg-orange-50 text-slate-700 hover:text-[#EE4D2D] text-xs px-3.5 py-2 rounded-xl border border-[#EBE3D5] font-bold items-center gap-1.5 shadow-sm">
                        <span>หน้าร้านค้า ↗</span>
                    </a>
                </div>
            </div>
        </div>
    </header>

    <!-- MAIN CONTAINER -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">

        <!-- ================= TAB 1: ORDERS ================= -->
        <div id="tab-orders" class="space-y-6">
            <!-- Action Bar -->
            <div class="bg-white p-5 sm:p-6 rounded-3xl border-2 border-[#EBE3D5] flex flex-col sm:flex-row sm:items-center justify-between gap-4 shadow-sm">
                <div class="space-y-1">
                    <h2 class="text-lg font-black text-[#2C241E] flex items-center gap-2">
                        <span>📦</span> รายการคำสั่งซื้อที่ชำระเงินแล้ว
                    </h2>
                    <p class="text-xs text-slate-500">ระบบคัดแยกขนส่งอัตโนมัติ (SPX Express และ ไปรษณีย์ไทย EMS สำหรับพื้นที่ห่างไกล/เกาะ)</p>
                </div>
                <div class="flex flex-wrap gap-2.5">
                    <button onclick="bulkConfirmOrders()" class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold px-4 py-2.5 rounded-2xl text-xs sm:text-sm flex items-center gap-1.5 shadow-md active:scale-95">
                        <span>⚡ กดยืนยันออเดอร์ทั้งหมด</span>
                    </button>
                    <button onclick="printLabels()" class="bg-[#EE4D2D] hover:bg-[#d73211] text-white font-black px-4 py-2.5 rounded-2xl text-xs sm:text-sm flex items-center gap-1.5 shadow-lg active:scale-95">
                        <span>🖨️ พิมพ์ใบปะหน้าพัสดุ (4x6 นิ้ว)</span>
                    </button>
                </div>
            </div>

            <!-- Table Card -->
            <div class="bg-white rounded-3xl border-2 border-[#EBE3D5] overflow-hidden shadow-sm">
                <div class="p-4 border-b border-[#EBE3D5] flex justify-between items-center bg-[#FAF7F2]">
                    <div class="flex items-center gap-2">
                        <h3 class="font-bold text-[#2C241E] text-sm sm:text-base">ตารางคำสั่งซื้อ</h3>
                        <span id="order-count-badge" class="bg-[#FFF2EE] text-[#EE4D2D] border border-[#FFD5CC] text-xs px-2.5 py-0.5 rounded-full font-bold">0 รายการ</span>
                    </div>
                    <select id="status-filter" onchange="renderOrdersTable()" class="bg-white border border-[#EBE3D5] text-[#2C241E] text-xs rounded-xl px-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-[#EE4D2D]">
                        <option value="ALL">ทั้งหมด (All Orders)</option>
                        <option value="PAID">ชำระแล้ว (รอแพ็ก)</option>
                        <option value="SHIPPED">จัดส่งแล้ว (มีเลขพัสดุ)</option>
                    </select>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs text-slate-700">
                        <thead class="bg-[#F9F6F0] text-slate-500 uppercase text-[11px] font-bold border-b border-[#EBE3D5]">
                            <tr>
                                <th class="p-4 w-10 text-center">
                                    <input type="checkbox" onchange="toggleSelectAll(this)" class="rounded border-slate-300">
                                </th>
                                <th class="p-4">รหัส / เวลา</th>
                                <th class="p-4">ลูกค้า & ที่อยู่</th>
                                <th class="p-4">รายการสินค้า</th>
                                <th class="p-4">ยอดเงิน</th>
                                <th class="p-4">สลิป</th>
                                <th class="p-4">ขนส่ง & เลขพัสดุ</th>
                                <th class="p-4 text-center">พิมพ์</th>
                            </tr>
                        </thead>
                        <tbody id="orders-tbody" class="divide-y divide-[#EBE3D5]"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- ================= TAB 2: INVENTORY & SHOPEE AFFILIATE ================= -->
        <div id="tab-inventory" class="hidden space-y-6">
            <div class="bg-white p-5 rounded-3xl border-2 border-[#EBE3D5] flex flex-col sm:flex-row sm:items-center justify-between gap-4 shadow-sm">
                <div class="space-y-1">
                    <h2 class="text-lg font-black text-[#2C241E] flex items-center gap-2">
                        <span>📊</span> จัดการสต็อกสินค้า & ใส่ลิงก์รีวิว Shopee Affiliate รายชิ้น
                    </h2>
                    <p class="text-xs text-slate-500">ใส่ลิงก์รีวิว Shopee ในแต่ละสินค้าเพื่อให้ลูกค้ากดดูรีวิวผู้ใช้จริงได้ทันที</p>
                </div>
            </div>

            <div class="bg-white rounded-3xl border-2 border-[#EBE3D5] overflow-hidden shadow-sm">
                <div class="p-4 border-b border-[#EBE3D5] bg-[#FAF7F2] flex justify-between items-center">
                    <h3 class="font-bold text-[#2C241E] text-base">รายการสินค้าในระบบ</h3>
                    <span id="product-count-badge" class="bg-[#FFF2EE] text-[#EE4D2D] border border-[#FFD5CC] text-xs px-2.5 py-0.5 rounded-full font-bold">8 รายการ</span>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs text-slate-700">
                        <thead class="bg-[#F9F6F0] text-slate-500 uppercase text-[11px] font-bold border-b border-[#EBE3D5]">
                            <tr>
                                <th class="p-4">สินค้า</th>
                                <th class="p-4">หมวดหมู่</th>
                                <th class="p-4">ราคาเริ่มต้น</th>
                                <th class="p-4">ตัวเลือก / สเปก</th>
                                <th class="p-4">ลิงก์รีวิว Shopee Affiliate</th>
                                <th class="p-4">สต็อก</th>
                                <th class="p-4 text-center">เติมสต็อกด่วน</th>
                                <th class="p-4 text-center">แก้ไข</th>
                            </tr>
                        </thead>
                        <tbody id="inventory-tbody" class="divide-y divide-[#EBE3D5]"></tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- ================= TAB 3: VAT 1.8M THRESHOLD MONITOR ================= -->
        <div id="tab-vat" class="hidden space-y-6">
            <div class="bg-white p-6 sm:p-8 rounded-3xl border-2 border-[#EBE3D5] space-y-6 shadow-sm">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                    <div>
                        <h2 class="text-xl font-black text-[#2C241E] flex items-center gap-2">
                            <span>📈</span> มอนิเตอร์เพดานภาษีมูลค่าเพิ่ม (VAT Threshold Monitor 1.8 ล้านบาท)
                        </h2>
                        <p class="text-xs sm:text-sm text-slate-500">
                            ติดตามยอดขายสะสมรายปี เพื่อวางแผนจดทะเบียนภาษีมูลค่าเพิ่มล่วงหน้าก่อนเกินเพดาน 1,800,000 บาท/ปี
                        </p>
                    </div>
                    <span id="vat-status-badge" class="px-4 py-1.5 rounded-2xl text-xs font-black self-start sm:self-auto bg-emerald-50 text-emerald-700 border border-emerald-300">
                        สถานะ: 🟢 ปลอดภัย (ห่างจากเพดาน)
                    </span>
                </div>

                <!-- Progress Bar -->
                <div class="space-y-2">
                    <div class="flex justify-between text-xs font-bold text-slate-700">
                        <span id="vat-rev-text">ยอดขายสะสมปีปัจจุบัน: ฿0.00</span>
                        <span>เพดานภาษี: ฿1,800,000.00</span>
                    </div>
                    <div class="w-full h-5 bg-[#F2EDE4] rounded-full overflow-hidden border border-[#EBE3D5] p-0.5">
                        <div id="vat-progress-bar" class="h-full bg-gradient-to-r from-emerald-500 via-amber-500 to-[#EE4D2D] rounded-full transition-all duration-500" style="width: 5%;"></div>
                    </div>
                    <div class="flex justify-between text-[11px] text-slate-500">
                        <span id="vat-percent-text">คิดเป็น 0.00% ของเพดาน</span>
                        <span id="vat-headroom-text" class="font-bold text-[#EE4D2D]">เหลือพื้นที่รองรับยอดขายอีก: ฿1,800,000.00</span>
                    </div>
                </div>
            </div>
        </div>

    </main>

    <!-- ================= EDIT PRODUCT MODAL (WITH SHOPEE AFFILIATE FIELD) ================= -->
    <div id="edit-prod-modal" class="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-slate-950/70 backdrop-blur-sm hidden overflow-y-auto">
        <div class="bg-white border-2 border-[#EBE3D5] rounded-3xl max-w-2xl w-full p-6 space-y-4 shadow-2xl my-8 text-[#2C241E]">
            <div class="flex justify-between items-center border-b border-[#EBE3D5] pb-3">
                <h3 class="text-base font-black text-[#2C241E]">✏️ แก้ไขสินค้า & ลิงก์รีวิว Shopee Affiliate</h3>
                <button onclick="closeProductModal()" class="text-slate-400 hover:text-slate-600 font-bold text-lg">✕</button>
            </div>

            <div class="space-y-4 max-h-[75vh] overflow-y-auto pr-1">
                <input type="hidden" id="edit-prod-id">
                
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">ชื่อสินค้า *</label>
                    <input type="text" id="edit-prod-name" class="w-full bg-[#FAF7F2] border border-[#EBE3D5] rounded-xl px-3.5 py-2 text-xs sm:text-sm text-[#2C241E] focus:ring-2 focus:ring-[#EE4D2D] focus:bg-white">
                </div>

                <!-- PROMINENT SHOPEE AFFILIATE LINK FIELD -->
                <div class="bg-[#FFF2EE] p-4 rounded-2xl border-2 border-[#FFD5CC] space-y-1.5">
                    <label class="block text-xs font-black text-[#EE4D2D] flex items-center gap-1.5">
                        <span>⭐</span> ลิงก์รีวิวสินค้าบน Shopee (Shopee Affiliate Link) ของสินค้านี้:
                    </label>
                    <input type="url" id="edit-prod-shopee-url" placeholder="https://th.shp.ee/..." class="w-full bg-white border-2 border-[#FFD5CC] rounded-xl px-3.5 py-2 text-xs font-mono text-[#2C241E] focus:ring-2 focus:ring-[#EE4D2D]">
                    <span class="text-[11px] text-slate-600 block">
                        💡 <strong>คำแนะนำ:</strong> เมื่อใส่ลิงก์นี้แล้ว ปุ่ม <em>"⭐ ดูรีวิวใน Shopee &gt;"</em> บนการ์ดสินค้านี้จะพาไปยังลิงก์นี้ทันที
                    </span>
                </div>

                <!-- Multi-Image Gallery Manager -->
                <div class="bg-[#FAF7F2] p-4 rounded-2xl border border-[#EBE3D5] space-y-2.5">
                    <div class="flex justify-between items-center">
                        <label class="text-xs font-bold text-slate-800">🖼️ คลังรูปภาพสินค้า:</label>
                        <label class="bg-[#EE4D2D] hover:bg-[#d73211] text-white text-xs px-3 py-1.5 rounded-xl font-bold cursor-pointer transition-all">
                            + เพิ่มรูปภาพ
                            <input type="file" id="multi-img-upload-input" multiple accept="image/*" onchange="handleMultiImageUpload(this)" class="hidden">
                        </label>
                    </div>
                    <div id="modal-imgs-grid" class="grid grid-cols-4 sm:grid-cols-5 gap-2 max-h-36 overflow-y-auto"></div>
                </div>

                <!-- Interactive Variant Rows Table -->
                <div class="space-y-2 pt-2 border-t border-slate-100">
                    <div class="flex justify-between items-center">
                        <label class="text-xs font-bold text-slate-800">ตัวเลือกสเปกสินค้า & ตั้งราคาแยกช่อง:</label>
                        <button type="button" onclick="addVariantRow()" class="bg-[#2C241E] text-white font-bold text-xs px-3 py-1 rounded-lg">
                            + เพิ่มแถว
                        </button>
                    </div>
                    <div id="modal-variants-container" class="space-y-2 max-h-40 overflow-y-auto"></div>
                </div>
            </div>

            <div class="flex gap-2 pt-3 border-t border-[#EBE3D5]">
                <button type="button" onclick="saveProductModal()" class="flex-grow bg-[#EE4D2D] hover:bg-[#d73211] text-white font-black py-2.5 rounded-2xl shadow-lg transition-all text-sm cursor-pointer">
                    💾 บันทึกข้อมูลสินค้า & ลิงก์ Shopee
                </button>
                <button type="button" onclick="closeProductModal()" class="bg-[#F2EDE4] hover:bg-slate-200 text-slate-700 px-4 py-2.5 rounded-2xl text-sm font-bold">
                    ยกเลิก
                </button>
            </div>
        </div>
    </div>

    <!-- ================= VIEW SLIP MODAL ================= -->
    <div id="slip-modal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/70 backdrop-blur-sm hidden">
        <div class="bg-white rounded-3xl border-2 border-[#EBE3D5] max-w-md w-full p-5 space-y-3 shadow-2xl">
            <div class="flex justify-between items-center border-b border-[#EBE3D5] pb-2">
                <h4 id="slip-modal-title" class="text-sm font-bold text-[#2C241E]">สลิปโอนเงิน</h4>
                <button onclick="closeSlipModal()" class="text-slate-400 hover:text-slate-600 font-bold">✕</button>
            </div>
            <div class="max-h-[60vh] overflow-y-auto flex items-center justify-center bg-[#FAF7F2] rounded-2xl p-2 border border-[#EBE3D5]">
                <img id="slip-modal-img" src="" class="max-w-full h-auto rounded-xl">
            </div>
            <div id="slip-modal-info" class="text-xs text-slate-700 space-y-1 bg-[#FFF5F2] p-3 rounded-2xl border border-[#FFD5CC]"></div>
        </div>
    </div>

    <!-- LOGIC SCRIPT -->
    <script>
        const DEFAULT_PRODUCTS = """ + products_json + """;
        const DEFAULT_ORDERS = """ + orders_json + """;

        let products = DEFAULT_PRODUCTS;
        let orders = DEFAULT_ORDERS;
        let selectedOrderIds = [];
        let modalImages = [];
        let modalVariants = [];

        function init() {
            lucide.createIcons();

            const savedProds = localStorage.getItem("goodstone_products");
            if (savedProds) {
                try { products = JSON.parse(savedProds); } catch(e) {}
            } else {
                localStorage.setItem("goodstone_products", JSON.stringify(DEFAULT_PRODUCTS));
            }

            const savedOrders = localStorage.getItem("goodstone_orders");
            if (savedOrders) {
                try { orders = JSON.parse(savedOrders); } catch(e) {}
            } else {
                localStorage.setItem("goodstone_orders", JSON.stringify(DEFAULT_ORDERS));
            }

            renderOrdersTable();
            renderInventoryTable();
            updateVATMonitor();
        }

        function switchTab(tab) {
            document.getElementById("tab-orders").classList.add("hidden");
            document.getElementById("tab-inventory").classList.add("hidden");
            document.getElementById("tab-vat").classList.add("hidden");

            document.getElementById("tab-btn-orders").className = "px-3.5 py-1.5 rounded-xl transition-all text-slate-700 hover:text-[#EE4D2D]";
            document.getElementById("tab-btn-inventory").className = "px-3.5 py-1.5 rounded-xl transition-all text-slate-700 hover:text-[#EE4D2D]";
            document.getElementById("tab-btn-vat").className = "px-3.5 py-1.5 rounded-xl transition-all text-slate-700 hover:text-[#EE4D2D]";

            if (tab === "ORDERS") {
                document.getElementById("tab-orders").classList.remove("hidden");
                document.getElementById("tab-btn-orders").className = "px-3.5 py-1.5 rounded-xl transition-all bg-[#EE4D2D] text-white shadow-md";
                renderOrdersTable();
            } else if (tab === "INVENTORY") {
                document.getElementById("tab-inventory").classList.remove("hidden");
                document.getElementById("tab-btn-inventory").className = "px-3.5 py-1.5 rounded-xl transition-all bg-[#EE4D2D] text-white shadow-md";
                renderInventoryTable();
            } else if (tab === "VAT") {
                document.getElementById("tab-vat").classList.remove("hidden");
                document.getElementById("tab-btn-vat").className = "px-3.5 py-1.5 rounded-xl transition-all bg-[#EE4D2D] text-white shadow-md";
                updateVATMonitor();
            }
        }

        function renderOrdersTable() {
            const filter = document.getElementById("status-filter").value;
            const list = filter === "ALL" ? orders : orders.filter(o => o.status === filter);
            const tbody = document.getElementById("orders-tbody");
            tbody.innerHTML = "";
            document.getElementById("order-count-badge").innerText = `${list.length} รายการ`;

            if (list.length === 0) {
                tbody.innerHTML = `<tr><td colspan="8" class="p-8 text-center text-slate-400">ไม่พบคำสั่งซื้อในสถานะนี้</td></tr>`;
                return;
            }

            list.forEach(o => {
                const tr = document.createElement("tr");
                tr.className = "hover:bg-[#FFF9F5] transition-colors";
                const isEMS = o.carrier_type === "THAILAND_POST_EMS" || (o.shipping_provider && o.shipping_provider.includes("ไปรษณีย์"));
                const itemsSummary = o.items.map(i => `<div class="text-slate-800">• ${i.name} <span class="text-[#EE4D2D] font-bold">x${i.quantity}</span></div>`).join("");

                const slipBtn = o.slip_image
                    ? `<button onclick="viewSlip('${o.id}')" class="bg-emerald-50 hover:bg-emerald-100 border border-emerald-300 text-emerald-700 px-2 py-0.5 rounded text-[11px] font-bold">🧾 ดูสลิป</button>`
                    : `<span class="text-slate-400 text-[10px]">Credit / ไม่มีสลิป</span>`;

                tr.innerHTML = `
                    <td class="p-4 text-center">
                        <input type="checkbox" ${selectedOrderIds.includes(o.id) ? "checked" : ""} onchange="toggleSelectOrder('${o.id}', this)" class="rounded border-slate-300">
                    </td>
                    <td class="p-4">
                        <span class="font-bold text-[#2C241E] block">${o.id}</span>
                        <span class="text-[10px] text-slate-400">${o.created_at}</span>
                    </td>
                    <td class="p-4 max-w-xs">
                        <span class="font-bold text-[#2C241E] block">${o.customer_name} (${o.phone})</span>
                        <span class="text-slate-500 line-clamp-1 text-[11px]">${o.address}</span>
                    </td>
                    <td class="p-4">${itemsSummary}</td>
                    <td class="p-4 font-black text-[#EE4D2D] text-sm">
                        ฿${Number(o.total_amount).toLocaleString(undefined, {minimumFractionDigits: 2})}
                    </td>
                    <td class="p-4">${slipBtn}</td>
                    <td class="p-4">
                        <span class="text-[10px] px-2 py-0.5 rounded font-bold ${isEMS ? 'bg-red-50 text-red-600 border border-red-200' : 'bg-orange-50 text-[#EE4D2D] border border-orange-200'}">
                            ${o.shipping_provider}
                        </span>
                        <span class="font-mono font-bold text-slate-600 block text-xs mt-1">
                            ${o.tracking_number || '(ยังไม่ออกเลข)'}
                        </span>
                    </td>
                    <td class="p-4 text-center">
                        <button onclick="printSingleLabel('${o.id}')" class="bg-[#F2EDE4] hover:bg-[#EE4D2D] hover:text-white text-slate-700 p-2 rounded-xl transition-all shadow-sm" title="พิมพ์ใบปะหน้า">
                            🖨️
                        </button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        function toggleSelectOrder(id, cb) {
            if (cb.checked) selectedOrderIds.push(id);
            else selectedOrderIds = selectedOrderIds.filter(x => x !== id);
        }

        function toggleSelectAll(master) {
            if (master.checked) selectedOrderIds = orders.map(o => o.id);
            else selectedOrderIds = [];
            renderOrdersTable();
        }

        function bulkConfirmOrders() {
            const targetIds = selectedOrderIds.length > 0 ? selectedOrderIds : orders.filter(o => o.status === "PAID").map(o => o.id);
            if (targetIds.length === 0) {
                alert("ไม่มีออเดอร์ที่ต้องกดยืนยันครับ");
                return;
            }

            if (!confirm(`ต้องการกดยืนยันและออกเลขพัสดุอัตโนมัติ ${targetIds.length} รายการใช่หรือไม่?`)) return;

            orders.forEach(o => {
                if (targetIds.includes(o.id)) {
                    o.status = "SHIPPED";
                    if (!o.tracking_number) {
                        const isEMS = o.carrier_type === "THAILAND_POST_EMS" || (o.shipping_provider && o.shipping_provider.includes("ไปรษณีย์"));
                        o.tracking_number = isEMS
                            ? `ED${Math.floor(100000000 + Math.random()*900000000)}TH`
                            : `SPXTH${Math.floor(1000000000 + Math.random()*9000000000)}`;
                    }
                }
            });

            localStorage.setItem("goodstone_orders", JSON.stringify(orders));
            selectedOrderIds = [];
            renderOrdersTable();
            updateVATMonitor();
            alert(`✅ ยืนยันสำเร็จ ${targetIds.length} ออเดอร์! พร้อมสั่งพิมพ์ใบปะหน้าได้ทันที`);
        }

        function renderInventoryTable() {
            const tbody = document.getElementById("inventory-tbody");
            tbody.innerHTML = "";
            products.forEach(p => {
                const tr = document.createElement("tr");
                tr.className = "hover:bg-[#FFF9F5] transition-colors";

                const variantsHtml = p.variants.map(v => `<span class="inline-block bg-[#FAF7F2] border border-[#EBE3D5] px-2 py-0.5 rounded text-[11px] text-slate-700 mr-1 mb-1">${v.name} (฿${v.price}) [${v.stock}ชิ้น]</span>`).join("");
                const affiliateHtml = p.shopee_affiliate_url
                    ? `<a href="${p.shopee_affiliate_url}" target="_blank" class="text-[#EE4D2D] underline font-bold truncate block">⭐ ${p.shopee_affiliate_url}</a>`
                    : `<span class="text-slate-400">(ยังไม่ใส่ลิงก์)</span>`;

                tr.innerHTML = `
                    <td class="p-4">
                        <div class="flex items-center gap-3">
                            <img src="${p.image_file || p.fallback_image}" class="w-11 h-11 object-contain bg-[#FAF7F2] rounded-xl border border-[#EBE3D5] p-0.5">
                            <div>
                                <span class="font-bold text-[#2C241E] block text-sm">${p.name}</span>
                                <span class="text-[10px] text-slate-400 font-mono">ID: ${p.id} (${p.images ? p.images.length : 1} ภาพ)</span>
                            </div>
                        </div>
                    </td>
                    <td class="p-4">
                        <span class="bg-[#FAF7F2] text-slate-700 border border-[#EBE3D5] text-xs px-2.5 py-0.5 rounded-lg font-bold">${p.category}</span>
                    </td>
                    <td class="p-4 font-black text-[#EE4D2D] text-sm">
                        ฿${p.price.toLocaleString()}
                    </td>
                    <td class="p-4 max-w-xs">${variantsHtml}</td>
                    <td class="p-4 max-w-xs truncate text-[11px]">${affiliateHtml}</td>
                    <td class="p-4">
                        <span class="text-xs px-2.5 py-1 rounded-full font-bold ${p.stock <= 0 ? 'bg-red-50 text-red-600' : p.stock < 10 ? 'bg-amber-50 text-amber-600' : 'bg-emerald-50 text-emerald-700'}">
                            ${p.stock} ชิ้น
                        </span>
                    </td>
                    <td class="p-4 text-center">
                        <div class="inline-flex gap-1">
                            <button onclick="quickRefill('${p.id}', 10)" class="bg-[#F2EDE4] hover:bg-emerald-600 hover:text-white text-slate-700 px-2 py-1 rounded font-bold text-xs">+10</button>
                            <button onclick="quickRefill('${p.id}', 50)" class="bg-[#F2EDE4] hover:bg-emerald-600 hover:text-white text-slate-700 px-2 py-1 rounded font-bold text-xs">+50</button>
                            <button onclick="quickRefill('${p.id}', 100)" class="bg-[#F2EDE4] hover:bg-emerald-600 hover:text-white text-slate-700 px-2 py-1 rounded font-bold text-xs">+100</button>
                        </div>
                    </td>
                    <td class="p-4 text-center">
                        <button onclick="openEditModal('${p.id}')" class="bg-[#EE4D2D] hover:bg-[#d73211] text-white px-3 py-1.5 rounded-xl font-bold transition-all text-xs shadow-sm">
                            ✏️ แก้ไข
                        </button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        function quickRefill(id, amt) {
            const p = products.find(x => x.id === id);
            if (p) {
                p.stock += amt;
                localStorage.setItem("goodstone_products", JSON.stringify(products));
                renderInventoryTable();
            }
        }

        function openEditModal(id) {
            const p = products.find(x => x.id === id);
            if (!p) return;

            document.getElementById("edit-prod-id").value = p.id;
            document.getElementById("edit-prod-name").value = p.name;
            document.getElementById("edit-prod-shopee-url").value = p.shopee_affiliate_url || "";

            modalImages = p.images ? JSON.parse(JSON.stringify(p.images)) : [{ file: p.image_file, name: `${p.id}_main.jpg` }];
            modalVariants = p.variants ? JSON.parse(JSON.stringify(p.variants)) : [];

            renderModalImages();
            renderModalVariants();
            document.getElementById("edit-prod-modal").classList.remove("hidden");
        }

        function closeProductModal() {
            document.getElementById("edit-prod-modal").classList.add("hidden");
        }

        function renderModalImages() {
            const grid = document.getElementById("modal-imgs-grid");
            grid.innerHTML = "";
            modalImages.forEach((img, idx) => {
                const div = document.createElement("div");
                div.className = "relative h-18 bg-[#FAF7F2] rounded-xl border border-[#EBE3D5] p-1 flex items-center justify-center";
                div.innerHTML = `
                    <img src="${img.file}" class="w-full h-full object-contain">
                    ${idx === 0 ? '<span class="absolute bottom-1 left-1 bg-[#EE4D2D] text-white text-[9px] px-1 rounded font-black">หน้าปก</span>' : ''}
                    <button type="button" onclick="removeModalImage(${idx})" class="absolute top-1 right-1 bg-red-600 text-white rounded-full p-0.5 text-[10px]">✕</button>
                `;
                grid.appendChild(div);
            });
        }

        function handleMultiImageUpload(input) {
            const files = Array.from(input.files);
            files.forEach(f => {
                const r = new FileReader();
                r.onload = e => {
                    modalImages.push({ file: e.target.result, name: f.name, fallback: e.target.result });
                    renderModalImages();
                };
                r.readAsDataURL(f);
            });
        }

        function removeModalImage(idx) {
            modalImages.splice(idx, 1);
            renderModalImages();
        }

        function renderModalVariants() {
            const container = document.getElementById("modal-variants-container");
            container.innerHTML = "";
            modalVariants.forEach((v, idx) => {
                const div = document.createElement("div");
                div.className = "grid grid-cols-12 gap-2 bg-[#FAF7F2] p-2 rounded-xl border border-[#EBE3D5] items-center";
                div.innerHTML = `
                    <div class="col-span-6">
                        <input type="text" value="${v.name}" oninput="modalVariants[${idx}].name=this.value" placeholder="ชื่อตัวเลือก" class="w-full bg-white border border-[#EBE3D5] rounded-lg px-2 py-1 text-xs text-[#2C241E]">
                    </div>
                    <div class="col-span-3">
                        <input type="number" value="${v.price}" oninput="modalVariants[${idx}].price=Number(this.value)" placeholder="ราคา" class="w-full bg-white border border-[#EBE3D5] rounded-lg px-2 py-1 text-xs text-[#EE4D2D] font-bold">
                    </div>
                    <div class="col-span-2">
                        <input type="number" value="${v.stock}" oninput="modalVariants[${idx}].stock=Number(this.value)" placeholder="สต็อก" class="w-full bg-white border border-[#EBE3D5] rounded-lg px-2 py-1 text-xs text-[#2C241E]">
                    </div>
                    <div class="col-span-1 text-center">
                        <button type="button" onclick="modalVariants.splice(${idx},1);renderModalVariants();" class="text-red-500 hover:text-red-700 font-bold">✕</button>
                    </div>
                `;
                container.appendChild(div);
            });
        }

        function addVariantRow() {
            modalVariants.push({ name: "ตัวเลือกใหม่", price: 100, stock: 20 });
            renderModalVariants();
        }

        function saveProductModal() {
            const id = document.getElementById("edit-prod-id").value;
            const p = products.find(x => x.id === id);
            if (!p) return;

            p.name = document.getElementById("edit-prod-name").value.trim();
            p.shopee_affiliate_url = document.getElementById("edit-prod-shopee-url").value.trim();
            p.variants = modalVariants;

            const totalStock = modalVariants.reduce((sum, v) => sum + Number(v.stock || 0), 0);
            const minPrice = modalVariants.length > 0 ? Math.min(...modalVariants.map(v => Number(v.price || 0))) : p.price;

            p.price = minPrice > 0 ? minPrice : p.price;
            p.stock = totalStock > 0 ? totalStock : p.stock;

            if (modalImages.length > 0) {
                p.images = modalImages;
                p.image_file = modalImages[0].file;
            }

            localStorage.setItem("goodstone_products", JSON.stringify(products));
            closeProductModal();
            renderInventoryTable();
            alert("💾 บันทึกข้อมูลสินค้า ตัวเลือก และลิงก์ Shopee Affiliate เรียบร้อยแล้วครับ!");
        }

        function updateVATMonitor() {
            const totalRev = orders.reduce((sum, o) => sum + (o.status !== "CANCELLED" ? Number(o.total_amount || 0) : 0), 0);
            const threshold = 1800000;
            const pct = Math.min(100, (totalRev / threshold) * 100);
            const headroom = Math.max(0, threshold - totalRev);

            document.getElementById("vat-rev-text").innerText = `ยอดขายสะสมปีปัจจุบัน: ฿${totalRev.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("vat-percent-text").innerText = `คิดเป็น ${pct.toFixed(2)}% ของเพดาน`;
            document.getElementById("vat-headroom-text").innerText = `เหลือพื้นที่รองรับยอดขายอีก: ฿${headroom.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("vat-progress-bar").style.width = `${Math.max(3, pct)}%`;

            const badge = document.getElementById("vat-status-badge");
            if (totalRev >= threshold) {
                badge.className = "px-4 py-1.5 rounded-2xl text-xs font-black self-start sm:self-auto bg-red-50 text-red-600 border border-red-300";
                badge.innerText = "สถานะ: 🔴 เกินเพดาน 1.8 ล้านบาท (ต้องยื่นจด VAT)";
            } else if (pct >= 70) {
                badge.className = "px-4 py-1.5 rounded-2xl text-xs font-black self-start sm:self-auto bg-amber-50 text-amber-600 border border-amber-300";
                badge.innerText = "สถานะ: 🟡 เฝ้าระวัง (เกิน 70% ของเพดาน)";
            } else {
                badge.className = "px-4 py-1.5 rounded-2xl text-xs font-black self-start sm:self-auto bg-emerald-50 text-emerald-700 border border-emerald-300";
                badge.innerText = "สถานะ: 🟢 ปลอดภัย (ห่างจากเพดาน)";
            }
        }

        function viewSlip(id) {
            const o = orders.find(x => x.id === id);
            if (!o || !o.slip_image) return;
            document.getElementById("slip-modal-title").innerText = `สลิปโอนเงิน: ${o.id}`;
            document.getElementById("slip-modal-img").src = o.slip_image;
            document.getElementById("slip-modal-info").innerHTML = `<p><strong>ผู้สั่งซื้อ:</strong> ${o.customer_name} (${o.phone})</p><p><strong>ยอดชำระ:</strong> <span class="text-[#EE4D2D] font-bold">฿${Number(o.total_amount).toLocaleString(undefined, {minimumFractionDigits: 2})}</span></p>`;
            document.getElementById("slip-modal").classList.remove("hidden");
        }

        function closeSlipModal() {
            document.getElementById("slip-modal").classList.add("hidden");
        }

        function printSingleLabel(id) {
            const o = orders.find(x => x.id === id);
            if (o) printLabels([o]);
        }

        function printLabels(targetList) {
            const targetOrders = targetList || (selectedOrderIds.length > 0 ? orders.filter(o => selectedOrderIds.includes(o.id)) : orders.filter(o => o.status === "PAID" || o.status === "SHIPPED"));
            if (targetOrders.length === 0) {
                alert("กรุณาเลือกออเดอร์ก่อนครับ");
                return;
            }

            const labelsHtml = targetOrders.map(o => {
                const barcodeNum = o.tracking_number || o.id;
                const isEMS = o.carrier_type === "THAILAND_POST_EMS" || (o.shipping_provider && o.shipping_provider.includes("ไปรษณีย์"));
                const carrierName = isEMS ? "THAILAND POST (EMS)" : "SPX EXPRESS";
                const badgeText = isEMS ? "EMS ด่วนพิเศษ" : "SPX STANDARD";

                const itemsRows = o.items.map((i, idx) => `
                    <tr style="border-bottom: 1px dashed #ccc;">
                        <td style="padding: 2px 4px; text-align: center;">${idx+1}</td>
                        <td style="padding: 2px 4px; font-weight: bold;">${i.name}</td>
                        <td style="padding: 2px 4px; text-align: center; font-weight: bold; font-size: 13px;">x${i.quantity}</td>
                    </tr>
                `).join("");

                return `
                <div class="label-page">
                    <div class="label-header">
                        <div class="carrier-name">${carrierName}</div>
                        <div class="header-right">
                            <div class="delivery-type">${badgeText}</div>
                            <div class="cod-tag">ชำระแล้ว (NON-COD)</div>
                        </div>
                    </div>

                    <div class="barcode-box">
                        <div class="tracking-title">${barcodeNum}</div>
                        <div class="barcode-lines">
                            ${Array(60).fill(0).map(() => `<div class="bar ${Math.random() > 0.45 ? 'thick' : 'thin'}"></div>`).join('')}
                        </div>
                        <div class="order-id-sub">Order: ${o.id} | วันที่: ${o.created_at}</div>
                    </div>

                    <div class="address-section receiver-section">
                        <div class="to-header">
                            <span class="to-label">ผู้รับ (TO):</span>
                            <span class="to-name">${o.customer_name}</span>
                        </div>
                        <div class="to-phone">โทร: ${o.phone}</div>
                        <div class="to-address">${o.address}</div>
                        <div class="postal-box">${o.postal_code || '10150'}</div>
                    </div>

                    <div class="address-section sender-section">
                        <span class="from-label">ผู้ส่ง (FROM):</span> <strong>GOODSTONE SHOP</strong> (คุณสุเมธา แท่นธรรมโรจน์ โทร. 061-537-2239)<br>
                        123/45 ถนนพระราม 2 แขวงท่าข้าม เขตบางขุนเทียน กรุงเทพฯ 10150
                    </div>

                    <div class="packing-list-section">
                        <div class="packing-title">📦 รายการสินค้าในพัสดุ (PACKING LIST):</div>
                        <table class="packing-table">
                            <thead>
                                <tr style="background: #eee; border-bottom: 1px solid #000;">
                                    <th style="width: 25px; padding: 2px;">#</th>
                                    <th style="text-align: left; padding: 2px 4px;">ชื่อสินค้า / สเปก</th>
                                    <th style="width: 40px; padding: 2px;">จำนวน</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${itemsRows}
                            </tbody>
                        </table>
                    </div>

                    <div class="label-footer">
                        <div>ลายเซ็นผู้รับ: ____________________ วันที่: _____/_____/________</div>
                        <div style="font-weight: bold; font-family: monospace; font-size: 11px;">${carrierName}</div>
                    </div>
                </div>`;
            }).join("");

            const printHtml = `<!DOCTYPE html>
            <html lang="th">
            <head>
                <meta charset="UTF-8">
                <title>พิมพ์ใบปะหน้าพัสดุ (${targetOrders.length} รายการ)</title>
                <style>
                    * { box-sizing: border-box; margin: 0; padding: 0; }
                    body { font-family: sans-serif; background: #333; color: #000; padding: 10px 0; }
                    .print-toolbar { max-width: 100mm; margin: 0 auto 15px auto; display: flex; gap: 10px; justify-content: space-between; align-items: center; background: #fff; padding: 10px 15px; border-radius: 8px; }
                    .print-btn { background: #EE4D2D; color: #fff; border: none; padding: 8px 18px; font-weight: bold; font-size: 14px; border-radius: 6px; cursor: pointer; }
                    .close-btn { background: #e2e8f0; color: #1e293b; border: none; padding: 8px 14px; font-weight: bold; font-size: 14px; border-radius: 6px; cursor: pointer; }
                    .label-page { width: 100mm; height: 146mm; margin: 0 auto 15mm auto; padding: 5mm; background: #fff; border: 2px solid #000; display: flex; flex-direction: column; justify-content: space-between; page-break-after: always; position: relative; }
                    .label-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #000; padding-bottom: 4px; }
                    .carrier-name { font-size: 18px; font-weight: 900; }
                    .delivery-type { background: #000; color: #fff; padding: 2px 6px; border-radius: 4px; font-size: 12px; font-weight: 900; }
                    .cod-tag { font-size: 10px; font-weight: bold; color: #047857; margin-top: 2px; }
                    .barcode-box { text-align: center; border-bottom: 2px solid #000; padding: 4px 0; }
                    .tracking-title { font-family: monospace; font-size: 16px; font-weight: 900; letter-spacing: 2px; }
                    .barcode-lines { height: 42px; display: flex; align-items: center; justify-content: center; gap: 1px; margin: 3px 0; }
                    .bar.thick { width: 3px; height: 100%; background: #000; }
                    .bar.thin { width: 1.5px; height: 100%; background: #000; }
                    .order-id-sub { font-size: 9px; color: #555; }
                    .address-section { border-bottom: 1.5px solid #000; padding: 4px 0; font-size: 11px; line-height: 1.3; }
                    .receiver-section { background: #fafafa; padding: 4px; position: relative; }
                    .to-header { display: flex; align-items: baseline; gap: 6px; }
                    .to-label { font-weight: 900; font-size: 12px; }
                    .to-name { font-size: 13px; font-weight: 900; }
                    .to-phone { font-size: 13px; font-weight: 900; margin: 2px 0; }
                    .to-address { font-size: 10.5px; padding-right: 55px; }
                    .postal-box { position: absolute; right: 4px; top: 12px; border: 2px solid #000; padding: 3px 6px; font-size: 15px; font-weight: 900; font-family: monospace; background: #fff; }
                    .sender-section { font-size: 9.5px; color: #333; }
                    .from-label { font-weight: bold; color: #000; }
                    .packing-list-section { flex-grow: 1; padding-top: 4px; }
                    .packing-title { font-size: 9.5px; font-weight: 800; margin-bottom: 2px; }
                    .packing-table { width: 100%; border-collapse: collapse; font-size: 9.5px; }
                    .label-footer { border-top: 1.5px solid #000; padding-top: 3px; display: flex; justify-content: space-between; font-size: 8.5px; }
                    @media print {
                        body { background: #fff; padding: 0; }
                        .print-toolbar { display: none; }
                        .label-page { margin: 0; box-shadow: none; page-break-after: always; }
                        @page { size: 100mm 150mm; margin: 0; }
                    }
                </style>
            </head>
            <body>
                <div class="print-toolbar">
                    <span style="font-size: 13px; font-weight: bold;">🖨️ ใบปะหน้าพัสดุพร้อมพิมพ์ (${targetOrders.length} รายการ)</span>
                    <div style="display: flex; gap: 8px;">
                        <button onclick="window.print()" class="print-btn">สั่งพิมพ์ทันที (Print)</button>
                        <button onclick="window.close()" class="close-btn">ปิด</button>
                    </div>
                </div>
                ${labelsHtml}
                <script>window.onload = function() { setTimeout(() => window.print(), 500); };<\/script>
            </body>
            </html>`;

            const win = window.open("", "_blank");
            if (win) {
                win.document.open();
                win.document.write(printHtml);
                win.document.close();
            }
        }

        window.onload = init;
    </script>
</body>
</html>"""

with open("/working_dir/slingshot-shop/admin.html", "w", encoding="utf-8") as f:
    f.write(admin_html_code)

print("slingshot-shop/admin.html created with Cream-Shopee theme & Shopee Affiliate link field!")
