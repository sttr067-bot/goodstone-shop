import json

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))
products_json = json.dumps(data["products"], ensure_ascii=False)
orders_json = json.dumps(data["orders"], ensure_ascii=False)

admin_code = """<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
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
                        },
                        cream: {
                            bg: "#F9F6F0",
                            card: "#FFFFFF",
                            border: "#EBE3D5",
                            darkText: "#2C241E"
                        }
                    }
                }
            }
        }
    </script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        body { font-family: "Prompt", sans-serif; background-color: #F9F6F0; color: #2C241E; margin: 0; padding: 0; }
    </style>
</head>
<body class="bg-[#F9F6F0] text-[#2C241E] min-h-screen flex flex-col font-sans">

    <!-- ADMIN HEADER (RESPONSIVE FOR MOBILE & DESKTOP) -->
    <header class="sticky top-0 z-40 bg-white border-b-2 border-[#EBE3D5] shadow-sm">
        <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <!-- Logo & Store Info -->
                <div class="flex items-center gap-2.5 sm:gap-3">
                    <div class="w-10 h-10 rounded-2xl bg-[#EE4D2D] flex items-center justify-center text-white font-black text-xl shadow-md shadow-orange-500/20 flex-shrink-0">
                        🛡️
                    </div>
                    <div>
                        <div class="flex items-center gap-1.5">
                            <span class="font-black text-sm sm:text-lg text-[#2C241E] tracking-tight">GOODSTONE ADMIN</span>
                            <span class="bg-[#FFF2EE] text-[#EE4D2D] border border-[#FFD5CC] text-[9px] sm:text-[10px] px-1.5 py-0.2 rounded font-black uppercase">PRO</span>
                        </div>
                        <span class="text-[10px] sm:text-xs text-slate-500 block font-medium truncate max-w-[180px] sm:max-w-none">คุณสุเมธา (061-537-2239)</span>
                    </div>
                </div>

                <!-- Navigation Action -->
                <div class="flex items-center gap-2">
                    <a href="index.html" target="_blank" class="bg-[#FFF2EE] hover:bg-[#FFE3DC] text-[#EE4D2D] border border-[#FFD5CC] text-xs px-3 py-1.5 rounded-xl font-bold flex items-center gap-1 shadow-sm transition-all">
                        <span>หน้าร้าน ↗</span>
                    </a>
                </div>
            </div>

            <!-- Mobile Navigation Tab Buttons -->
            <div class="grid grid-cols-3 gap-1.5 pb-2.5 pt-0.5">
                <button onclick="switchTab('ORDERS')" id="tab-btn-orders" class="py-2 px-1 rounded-xl text-xs font-bold transition-all text-center bg-[#EE4D2D] text-white shadow-md">
                    📦 คำสั่งซื้อ
                </button>
                <button onclick="switchTab('INVENTORY')" id="tab-btn-inventory" class="py-2 px-1 rounded-xl text-xs font-bold transition-all text-center bg-[#F2EDE4] text-slate-700 hover:text-[#EE4D2D]">
                    📊 สต็อก & สินค้า
                </button>
                <button onclick="switchTab('VAT')" id="tab-btn-vat" class="py-2 px-1 rounded-xl text-xs font-bold transition-all text-center bg-[#F2EDE4] text-slate-700 hover:text-[#EE4D2D]">
                    📈 เพดานภาษี (1.8M)
                </button>
            </div>
        </div>
    </header>

    <!-- MAIN CONTAINER -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-3 sm:px-6 lg:px-8 py-4 sm:py-6 space-y-6">

        <!-- ================= TAB 1: ORDERS ================= -->
        <div id="tab-orders" class="space-y-4">
            
            <!-- Top Controls -->
            <div class="bg-white p-4 sm:p-5 rounded-3xl border-2 border-[#EBE3D5] flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-sm">
                <div>
                    <h2 class="text-base sm:text-lg font-black text-[#2C241E] flex items-center gap-2">
                        <span>📦</span> รายการคำสั่งซื้อที่ชำระเงินแล้ว
                    </h2>
                    <p class="text-xs text-slate-500">คัดแยกขนส่ง SPX Express / ไปรษณีย์ไทย EMS อัตโนมัติ</p>
                </div>

                <div class="flex gap-2">
                    <button onclick="bulkConfirmOrders()" class="flex-grow sm:flex-grow-0 bg-emerald-600 hover:bg-emerald-500 text-white font-bold px-3.5 py-2.5 rounded-2xl text-xs flex items-center justify-center gap-1 shadow-md active:scale-95">
                        <span>⚡ กดยืนยันทั้งหมด</span>
                    </button>
                    <button onclick="printLabels()" class="flex-grow sm:flex-grow-0 bg-[#EE4D2D] hover:bg-[#d73211] text-white font-black px-3.5 py-2.5 rounded-2xl text-xs flex items-center justify-center gap-1 shadow-md active:scale-95">
                        <span>🖨️ พิมพ์ใบปะหน้า</span>
                    </button>
                </div>
            </div>

            <!-- Orders Filter & Cards Container -->
            <div class="flex justify-between items-center px-1">
                <span id="order-count-badge" class="text-xs font-black text-[#EE4D2D] bg-[#FFF2EE] border border-[#FFD5CC] px-3 py-1 rounded-full">
                    0 รายการ
                </span>
                <select id="status-filter" onchange="renderOrdersView()" class="bg-white border border-[#EBE3D5] text-xs font-bold rounded-xl px-3 py-1.5 text-slate-700">
                    <option value="ALL">ทั้งหมด (All Orders)</option>
                    <option value="PAID">ชำระแล้ว (รอแพ็ก)</option>
                    <option value="SHIPPED">จัดส่งแล้ว (มีเลขพัสดุ)</option>
                </select>
            </div>

            <!-- Mobile Responsive Orders List -->
            <div id="orders-list-container" class="space-y-3">
                <!-- Loaded dynamically -->
            </div>
        </div>

        <!-- ================= TAB 2: INVENTORY & SHOPEE AFFILIATE ================= -->
        <div id="tab-inventory" class="hidden space-y-4">
            
            <div class="bg-white p-4 sm:p-5 rounded-3xl border-2 border-[#EBE3D5] flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-sm">
                <div>
                    <h2 class="text-base sm:text-lg font-black text-[#2C241E] flex items-center gap-2">
                        <span>📊</span> จัดการสต็อก & ลิงก์ Shopee Affiliate
                    </h2>
                    <p class="text-xs text-slate-500">เติมสต็อกด่วน +10/+50/+100 หรือกดแก้ไขเพื่อเพิ่มรูปและใส่ลิงก์รีวิว Shopee</p>
                </div>
                <span id="product-count-badge" class="self-start sm:self-auto text-xs font-black text-[#EE4D2D] bg-[#FFF2EE] border border-[#FFD5CC] px-3 py-1 rounded-full">
                    8 รายการ
                </span>
            </div>

            <!-- Mobile-First Product Inventory Cards List -->
            <div id="inventory-cards-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                <!-- Loaded dynamically -->
            </div>
        </div>

        <!-- ================= TAB 3: VAT THRESHOLD MONITOR ================= -->
        <div id="tab-vat" class="hidden space-y-4">
            <div class="bg-white p-5 sm:p-7 rounded-3xl border-2 border-[#EBE3D5] space-y-5 shadow-sm">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                    <div>
                        <h2 class="text-base sm:text-lg font-black text-[#2C241E] flex items-center gap-2">
                            <span>📈</span> มอนิเตอร์เพดานภาษีมูลค่าเพิ่ม (VAT 1.8M)
                        </h2>
                        <p class="text-xs text-slate-500">
                            ติดตามยอดขายสะสมรายปี เพื่อวางแผนจดทะเบียนภาษีมูลค่าเพิ่มล่วงหน้าก่อนเกินเพดาน 1,800,000 บาท/ปี
                        </p>
                    </div>
                    <span id="vat-status-badge" class="px-3.5 py-1.5 rounded-2xl text-xs font-black self-start sm:self-auto bg-emerald-50 text-emerald-700 border border-emerald-300">
                        สถานะ: 🟢 ปลอดภัย (ห่างจากเพดาน)
                    </span>
                </div>

                <div class="space-y-2 pt-2">
                    <div class="flex justify-between text-xs font-bold text-slate-700">
                        <span id="vat-rev-text">ยอดขายสะสมปีปัจจุบัน: ฿0.00</span>
                        <span>เพดาน: ฿1,800,000.00</span>
                    </div>
                    <div class="w-full h-4 bg-[#F2EDE4] rounded-full overflow-hidden border border-[#EBE3D5] p-0.5">
                        <div id="vat-progress-bar" class="h-full bg-gradient-to-r from-emerald-500 via-amber-500 to-[#EE4D2D] rounded-full transition-all duration-500" style="width: 5%;"></div>
                    </div>
                    <div class="flex justify-between text-[11px] text-slate-500">
                        <span id="vat-percent-text">คิดเป็น 0.00% ของเพดาน</span>
                        <span id="vat-headroom-text" class="font-bold text-[#EE4D2D]">เหลือยอดขายอีก: ฿1,800,000.00</span>
                    </div>
                </div>
            </div>
        </div>

    </main>

    <!-- ================= EDIT PRODUCT MODAL (MOBILE TOUCH FRIENDLY) ================= -->
    <div id="edit-prod-modal" class="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4 bg-slate-950/70 backdrop-blur-sm hidden overflow-y-auto">
        <div class="bg-white border-2 border-[#EBE3D5] rounded-3xl max-w-xl w-full p-4 sm:p-6 space-y-4 shadow-2xl my-4 text-[#2C241E]">
            <div class="flex justify-between items-center border-b border-[#EBE3D5] pb-3">
                <h3 class="text-sm sm:text-base font-black text-[#2C241E]">✏️ แก้ไขสินค้า & ลิงก์ Shopee</h3>
                <button onclick="closeProductModal()" class="text-slate-400 hover:text-slate-700 font-bold text-xl px-2">✕</button>
            </div>

            <div class="space-y-4 max-h-[72vh] overflow-y-auto pr-1">
                <input type="hidden" id="edit-prod-id">
                
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">ชื่อสินค้า *</label>
                    <input type="text" id="edit-prod-name" class="w-full bg-[#FAF7F2] border border-[#EBE3D5] rounded-xl px-3 py-2 text-xs sm:text-sm text-[#2C241E] focus:ring-2 focus:ring-[#EE4D2D] focus:bg-white">
                </div>

                <!-- SHOPEE AFFILIATE LINK -->
                <div class="bg-[#FFF2EE] p-3.5 rounded-2xl border-2 border-[#FFD5CC] space-y-1">
                    <label class="block text-xs font-black text-[#EE4D2D] flex items-center gap-1">
                        <span>⭐</span> ลิงก์รีวิวสินค้าบน Shopee (Shopee Affiliate Link):
                    </label>
                    <input type="url" id="edit-prod-shopee-url" placeholder="https://th.shp.ee/..." class="w-full bg-white border-2 border-[#FFD5CC] rounded-xl px-3 py-2 text-xs font-mono text-[#2C241E] focus:ring-2 focus:ring-[#EE4D2D]">
                    <span class="text-[10px] text-slate-500 block">ปุ่ม "⭐ ดูรีวิวใน Shopee >" บนการ์ดสินค้านี้จะพาไปที่ลิงก์นี้</span>
                </div>

                <!-- MOBILE MULTI-IMAGE UPLOADER (RELIABLE TOUCH COMPATIBLE WITH AUTO-COMPRESSION) -->
                <div class="bg-[#FAF7F2] p-3.5 rounded-2xl border border-[#EBE3D5] space-y-2.5">
                    <div class="flex justify-between items-center">
                        <div>
                            <label class="text-xs font-bold text-slate-800 block">🖼️ รูปภาพสินค้า (<span id="modal-imgs-count-text">0 รูป</span>):</label>
                            <span class="text-[10px] text-slate-500">รูปแรกคือรูปหน้าปก</span>
                        </div>
                        
                        <!-- Direct Visible Upload Button for Phones -->
                        <label class="bg-[#EE4D2D] hover:bg-[#d73211] text-white text-xs px-3.5 py-2 rounded-xl font-bold cursor-pointer shadow-md flex items-center gap-1 active:scale-95">
                            <span>📷 + เพิ่มรูปภาพ</span>
                            <input type="file" id="phone-img-input" accept="image/*" multiple onchange="handlePhoneImageUpload(this)" class="hidden">
                        </label>
                    </div>

                    <!-- Images Thumbnails Grid -->
                    <div id="modal-imgs-grid" class="grid grid-cols-3 sm:grid-cols-4 gap-2 max-h-36 overflow-y-auto p-1 bg-white rounded-xl border border-[#EBE3D5]"></div>
                </div>

                <!-- VARIANT ROWS -->
                <div class="space-y-2 pt-2 border-t border-slate-100">
                    <div class="flex justify-between items-center">
                        <label class="text-xs font-bold text-slate-800">ตัวเลือกสเปกสินค้า & ตั้งราคาแยกช่อง:</label>
                        <button type="button" onclick="addVariantRow()" class="bg-[#2C241E] text-white font-bold text-xs px-2.5 py-1 rounded-lg">
                            + เพิ่มแถว
                        </button>
                    </div>
                    <div id="modal-variants-container" class="space-y-2 max-h-40 overflow-y-auto"></div>
                </div>
            </div>

            <div class="flex gap-2 pt-3 border-t border-[#EBE3D5]">
                <button type="button" onclick="saveProductModal()" class="flex-grow bg-[#EE4D2D] hover:bg-[#d73211] text-white font-black py-2.5 rounded-2xl shadow-lg transition-all text-xs sm:text-sm cursor-pointer active:scale-95">
                    💾 บันทึกข้อมูลสินค้า & ลิงก์ Shopee
                </button>
                <button type="button" onclick="closeProductModal()" class="bg-[#F2EDE4] hover:bg-slate-200 text-slate-700 px-4 py-2.5 rounded-2xl text-xs sm:text-sm font-bold">
                    ยกเลิก
                </button>
            </div>
        </div>
    </div>

    <!-- ================= VIEW SLIP MODAL ================= -->
    <div id="slip-modal" class="fixed inset-0 z-50 flex items-center justify-center p-3 bg-slate-950/70 backdrop-blur-sm hidden">
        <div class="bg-white rounded-3xl border-2 border-[#EBE3D5] max-w-sm w-full p-4 space-y-3 shadow-2xl">
            <div class="flex justify-between items-center border-b border-[#EBE3D5] pb-2">
                <h4 id="slip-modal-title" class="text-xs sm:text-sm font-bold text-[#2C241E]">สลิปโอนเงิน</h4>
                <button onclick="closeSlipModal()" class="text-slate-400 hover:text-slate-600 font-bold text-lg">✕</button>
            </div>
            <div class="max-h-[55vh] overflow-y-auto flex items-center justify-center bg-[#FAF7F2] rounded-2xl p-2 border border-[#EBE3D5]">
                <img id="slip-modal-img" src="" class="max-w-full h-auto rounded-xl">
            </div>
            <div id="slip-modal-info" class="text-xs text-slate-700 space-y-1 bg-[#FFF5F2] p-2.5 rounded-2xl border border-[#FFD5CC]"></div>
        </div>
    </div>

    <!-- JAVASCRIPT LOGIC -->
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

            renderOrdersView();
            renderInventoryView();
            updateVATMonitor();
        }

        function switchTab(tab) {
            document.getElementById("tab-orders").classList.add("hidden");
            document.getElementById("tab-inventory").classList.add("hidden");
            document.getElementById("tab-vat").classList.add("hidden");

            document.getElementById("tab-btn-orders").className = "py-2 px-1 rounded-xl text-xs font-bold transition-all text-center bg-[#F2EDE4] text-slate-700 hover:text-[#EE4D2D]";
            document.getElementById("tab-btn-inventory").className = "py-2 px-1 rounded-xl text-xs font-bold transition-all text-center bg-[#F2EDE4] text-slate-700 hover:text-[#EE4D2D]";
            document.getElementById("tab-btn-vat").className = "py-2 px-1 rounded-xl text-xs font-bold transition-all text-center bg-[#F2EDE4] text-slate-700 hover:text-[#EE4D2D]";

            if (tab === "ORDERS") {
                document.getElementById("tab-orders").classList.remove("hidden");
                document.getElementById("tab-btn-orders").className = "py-2 px-1 rounded-xl text-xs font-bold transition-all text-center bg-[#EE4D2D] text-white shadow-md";
                renderOrdersView();
            } else if (tab === "INVENTORY") {
                document.getElementById("tab-inventory").classList.remove("hidden");
                document.getElementById("tab-btn-inventory").className = "py-2 px-1 rounded-xl text-xs font-bold transition-all text-center bg-[#EE4D2D] text-white shadow-md";
                renderInventoryView();
            } else if (tab === "VAT") {
                document.getElementById("tab-vat").classList.remove("hidden");
                document.getElementById("tab-btn-vat").className = "py-2 px-1 rounded-xl text-xs font-bold transition-all text-center bg-[#EE4D2D] text-white shadow-md";
                updateVATMonitor();
            }
        }

        // ================= MOBILE RESPONSIVE ORDERS VIEW =================
        function renderOrdersView() {
            const filter = document.getElementById("status-filter").value;
            const list = filter === "ALL" ? orders : orders.filter(o => o.status === filter);
            const container = document.getElementById("orders-list-container");
            container.innerHTML = "";
            document.getElementById("order-count-badge").innerText = `${list.length} รายการ`;

            if (list.length === 0) {
                container.innerHTML = `<div class="bg-white p-8 rounded-3xl border-2 border-[#EBE3D5] text-center text-slate-400 text-xs">ไม่พบคำสั่งซื้อในสถานะนี้</div>`;
                return;
            }

            list.forEach(o => {
                const isEMS = o.carrier_type === "THAILAND_POST_EMS" || (o.shipping_provider && o.shipping_provider.includes("ไปรษณีย์"));
                const itemsHtml = o.items.map(i => `<div class="text-xs text-slate-800">• ${i.name} <span class="text-[#EE4D2D] font-bold">x${i.quantity}</span></div>`).join("");

                const card = document.createElement("div");
                card.className = "bg-white p-4 sm:p-5 rounded-3xl border-2 border-[#EBE3D5] shadow-sm space-y-3";
                card.innerHTML = `
                    <div class="flex justify-between items-center pb-2 border-b border-slate-100">
                        <div class="flex items-center gap-2">
                            <input type="checkbox" ${selectedOrderIds.includes(o.id) ? "checked" : ""} onchange="toggleSelectOrder('${o.id}', this)" class="rounded border-slate-300 w-4 h-4">
                            <div>
                                <span class="font-black text-sm text-[#2C241E] block">${o.id}</span>
                                <span class="text-[10px] text-slate-400">${o.created_at}</span>
                            </div>
                        </div>
                        <span class="text-[10px] font-bold px-2.5 py-1 rounded-full ${o.status === 'SHIPPED' ? 'bg-emerald-50 text-emerald-700 border border-emerald-300' : 'bg-orange-50 text-[#EE4D2D] border border-orange-200'}">
                            ${o.status === 'SHIPPED' ? '✓ จัดส่งแล้ว' : 'ชำระแล้ว (รอแพ็ก)'}
                        </span>
                    </div>

                    <div class="text-xs text-slate-700 space-y-1">
                        <p><strong>ผู้รับ:</strong> ${o.customer_name} (${o.phone})</p>
                        <p class="text-slate-500 text-[11px] line-clamp-1"><strong>ที่อยู่:</strong> ${o.address}</p>
                        <div class="py-1 border-t border-slate-100">${itemsHtml}</div>
                    </div>

                    <div class="bg-[#FAF7F2] p-2.5 rounded-2xl border border-[#EBE3D5] flex items-center justify-between text-xs">
                        <div>
                            <span class="text-[10px] px-2 py-0.5 rounded font-bold ${isEMS ? 'bg-red-50 text-red-600 border border-red-200' : 'bg-orange-50 text-[#EE4D2D] border border-orange-200'}">
                                ${o.shipping_provider}
                            </span>
                            <span class="font-mono font-bold text-slate-600 block text-[11px] mt-1">${o.tracking_number || '(ยังไม่ออกเลข)'}</span>
                        </div>
                        <div class="text-right">
                            <span class="text-[10px] text-slate-400 block">ยอดชำระสุทธิ</span>
                            <span class="text-sm font-black text-[#EE4D2D]">฿${Number(o.total_amount).toLocaleString(undefined, {minimumFractionDigits: 2})}</span>
                        </div>
                    </div>

                    <div class="flex gap-2 pt-1">
                        ${o.slip_image ? `<button onclick="viewSlip('${o.id}')" class="flex-1 bg-emerald-50 hover:bg-emerald-100 border border-emerald-300 text-emerald-700 py-1.5 rounded-xl text-xs font-bold">🧾 ดูสลิป</button>` : `<span class="flex-1 text-center text-[10px] text-slate-400 py-1.5">Credit Wallet</span>`}
                        <button onclick="printSingleLabel('${o.id}')" class="flex-1 bg-[#EE4D2D] hover:bg-[#d73211] text-white py-1.5 rounded-xl text-xs font-bold shadow-sm">🖨️ พิมพ์ใบปะหน้า</button>
                    </div>
                `;
                container.appendChild(card);
            });
        }

        function toggleSelectOrder(id, cb) {
            if (cb.checked) selectedOrderIds.push(id);
            else selectedOrderIds = selectedOrderIds.filter(x => x !== id);
        }

        function bulkConfirmOrders() {
            const targetIds = selectedOrderIds.length > 0 ? selectedOrderIds : orders.filter(o => o.status === "PAID").map(o => o.id);
            if (targetIds.length === 0) { alert("ไม่มีออเดอร์ที่ต้องกดยืนยันครับ"); return; }
            if (!confirm(`ต้องการกดยืนยันและออกเลขพัสดุ ${targetIds.length} รายการใช่หรือไม่?`)) return;

            orders.forEach(o => {
                if (targetIds.includes(o.id)) {
                    o.status = "SHIPPED";
                    if (!o.tracking_number) {
                        const isEMS = o.carrier_type === "THAILAND_POST_EMS" || (o.shipping_provider && o.shipping_provider.includes("ไปรษณีย์"));
                        o.tracking_number = isEMS ? `ED${Math.floor(100000000 + Math.random()*900000000)}TH` : `SPXTH${Math.floor(1000000000 + Math.random()*9000000000)}`;
                    }
                }
            });

            localStorage.setItem("goodstone_orders", JSON.stringify(orders));
            selectedOrderIds = [];
            renderOrdersView();
            updateVATMonitor();
            alert(`✅ ยืนยันสำเร็จ ${targetIds.length} ออเดอร์!`);
        }

        // ================= MOBILE-FIRST INVENTORY CARDS VIEW =================
        function renderInventoryView() {
            const container = document.getElementById("inventory-cards-container");
            container.innerHTML = "";

            products.forEach(p => {
                const imgCount = (p.images && p.images.length > 0) ? p.images.length : 1;
                const imgSrc = p.image_file || p.fallback_image;
                const shopeeUrl = p.shopee_affiliate_url || "https://th.shp.ee/sdFv2cS1";
                const variantsHtml = p.variants.map(v => `<span class="inline-block bg-[#FAF7F2] border border-[#EBE3D5] px-2 py-0.5 rounded text-[10px] text-slate-700 mr-1 mb-1 font-medium">${v.name} (฿${v.price}) [${v.stock}ชิ้น]</span>`).join("");

                const card = document.createElement("div");
                card.className = "bg-white p-4 sm:p-5 rounded-3xl border-2 border-[#EBE3D5] shadow-sm space-y-3.5 flex flex-col justify-between";
                card.innerHTML = `
                    <div class="space-y-2.5">
                        <div class="flex gap-3 items-center">
                            <div class="w-16 h-16 bg-[#FAF7F2] rounded-2xl border border-[#EBE3D5] p-1 flex items-center justify-center flex-shrink-0 overflow-hidden">
                                <img src="${imgSrc}" onerror="this.onerror=null; this.src='${p.fallback_image}';" class="w-full h-full object-contain">
                            </div>
                            <div class="flex-grow min-w-0">
                                <span class="bg-[#FFF2EE] text-[#EE4D2D] border border-[#FFD5CC] text-[9px] px-2 py-0.5 rounded-full font-black uppercase inline-block mb-0.5">${p.category}</span>
                                <h3 class="font-bold text-[#2C241E] text-xs sm:text-sm line-clamp-2 leading-snug">${p.name}</h3>
                                <div class="flex items-center gap-2 mt-1">
                                    <span class="text-xs font-black text-[#EE4D2D]">฿${p.price.toLocaleString()}</span>
                                    <span class="text-[10px] px-2 py-0.2 rounded-full font-bold ${p.stock <= 0 ? 'bg-red-50 text-red-600' : p.stock < 10 ? 'bg-amber-50 text-amber-600' : 'bg-emerald-50 text-emerald-700'}">
                                        สต็อก: ${p.stock} ชิ้น
                                    </span>
                                </div>
                            </div>
                        </div>

                        <!-- Variants Display -->
                        <div class="pt-1.5 border-t border-slate-100">
                            <span class="text-[10px] font-bold text-slate-500 block mb-1">ตัวเลือกสเปกสินค้า:</span>
                            <div>${variantsHtml}</div>
                        </div>

                        <!-- Shopee Affiliate Display & Link -->
                        <div class="bg-[#FFF5F2] p-2 rounded-xl border border-[#FFD5CC] flex items-center justify-between text-xs">
                            <span class="text-[10px] text-slate-600 truncate mr-2"><strong>Shopee:</strong> ${shopeeUrl}</span>
                            <a href="${shopeeUrl}" target="_blank" class="text-[10px] bg-[#EE4D2D] text-white px-2 py-0.5 rounded font-bold flex-shrink-0">ดู ↗</a>
                        </div>
                    </div>

                    <!-- Bottom Controls: Quick Refill + Edit Button -->
                    <div class="pt-2 border-t border-slate-100 space-y-2">
                        <div class="flex items-center justify-between text-xs">
                            <span class="text-[10px] font-bold text-slate-500">เติมสต็อกด่วน:</span>
                            <div class="inline-flex gap-1">
                                <button onclick="quickRefill('${p.id}', 10)" class="bg-[#F2EDE4] hover:bg-emerald-600 hover:text-white text-slate-700 px-2.5 py-1 rounded-lg font-bold text-xs">+10</button>
                                <button onclick="quickRefill('${p.id}', 50)" class="bg-[#F2EDE4] hover:bg-emerald-600 hover:text-white text-slate-700 px-2.5 py-1 rounded-lg font-bold text-xs">+50</button>
                                <button onclick="quickRefill('${p.id}', 100)" class="bg-[#F2EDE4] hover:bg-emerald-600 hover:text-white text-slate-700 px-2.5 py-1 rounded-lg font-bold text-xs">+100</button>
                            </div>
                        </div>

                        <button onclick="openEditModal('${p.id}')" class="w-full bg-[#2C241E] hover:bg-[#EE4D2D] text-white py-2 rounded-xl font-bold text-xs transition-all shadow-sm flex items-center justify-center gap-1 active:scale-95">
                            <span>✏️ แก้ไขข้อมูล, สต็อก & ลิงก์ Shopee (${imgCount} รูป)</span>
                        </button>
                    </div>
                `;
                container.appendChild(card);
            });
        }

        function quickRefill(id, amt) {
            const p = products.find(x => x.id === id);
            if (p) {
                p.stock += amt;
                localStorage.setItem("goodstone_products", JSON.stringify(products));
                renderInventoryView();
            }
        }

        // ================= EDIT MODAL WITH PHONE COMPRESSION =================
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
            document.getElementById("modal-imgs-count-text").innerText = `${modalImages.length} รูป`;

            if (modalImages.length === 0) {
                grid.innerHTML = `<div class="col-span-full py-4 text-center text-slate-400 text-xs">ยังไม่มีรูปภาพ กดปุ่ม "+ เพิ่มรูปภาพ" เพื่อเลือกรูป</div>`;
                return;
            }

            modalImages.forEach((img, idx) => {
                const div = document.createElement("div");
                div.className = `relative h-16 bg-[#FAF7F2] rounded-xl border-2 p-1 flex items-center justify-center ${idx === 0 ? 'border-[#EE4D2D]' : 'border-[#EBE3D5]'}`;
                div.innerHTML = `
                    <img src="${img.file}" class="w-full h-full object-contain">
                    ${idx === 0 ? '<span class="absolute bottom-0.5 left-0.5 bg-[#EE4D2D] text-white text-[8px] px-1 rounded font-black">หน้าปก</span>' : ''}
                    <button type="button" onclick="removeModalImage(${idx})" class="absolute top-0.5 right-0.5 bg-red-600 text-white rounded-full w-4 h-4 flex items-center justify-center text-[9px] font-bold shadow-md">✕</button>
                `;
                grid.appendChild(div);
            });
        }

        // Phone Touch Friendly & Auto-Compress to 800px Canvas
        function handlePhoneImageUpload(input) {
            const files = Array.from(input.files || []);
            if (files.length === 0) return;

            let loaded = 0;
            files.forEach(file => {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const img = new Image();
                    img.onload = function() {
                        // Compress via canvas to max 800px width/height for fast mobile rendering
                        const canvas = document.createElement("canvas");
                        let w = img.width;
                        let h = img.height;
                        const maxDim = 800;
                        if (w > maxDim || h > maxDim) {
                            if (w > h) { h = Math.round(h * maxDim / w); w = maxDim; }
                            else { w = Math.round(w * maxDim / h); h = maxDim; }
                        }
                        canvas.width = w;
                        canvas.height = h;
                        const ctx = canvas.getContext("2d");
                        ctx.drawImage(img, 0, 0, w, h);
                        const compressedBase64 = canvas.toDataURL("image/jpeg", 0.82);

                        modalImages.push({
                            file: compressedBase64,
                            name: file.name,
                            fallback: compressedBase64
                        });
                        loaded++;
                        if (loaded === files.length) {
                            renderModalImages();
                        }
                    };
                    img.src = e.target.result;
                };
                reader.readAsDataURL(file);
            });
            input.value = "";
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
                div.className = "grid grid-cols-12 gap-1.5 bg-[#FAF7F2] p-2 rounded-xl border border-[#EBE3D5] items-center";
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
                        <button type="button" onclick="modalVariants.splice(${idx},1);renderModalVariants();" class="text-red-500 font-bold text-sm">✕</button>
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
                p.fallback_image = modalImages[0].fallback || modalImages[0].file;
            }

            localStorage.setItem("goodstone_products", JSON.stringify(products));
            closeProductModal();
            renderInventoryView();
            alert("💾 บันทึกรูปภาพ ตัวเลือก และลิงก์ Shopee เรียบร้อยแล้วครับ!");
        }

        function updateVATMonitor() {
            const totalRev = orders.reduce((sum, o) => sum + (o.status !== "CANCELLED" ? Number(o.total_amount || 0) : 0), 0);
            const threshold = 1800000;
            const pct = Math.min(100, (totalRev / threshold) * 100);
            const headroom = Math.max(0, threshold - totalRev);

            document.getElementById("vat-rev-text").innerText = `ยอดขายสะสมปีปัจจุบัน: ฿${totalRev.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("vat-percent-text").innerText = `คิดเป็น ${pct.toFixed(2)}% ของเพดาน`;
            document.getElementById("vat-headroom-text").innerText = `เหลือยอดขายอีก: ฿${headroom.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("vat-progress-bar").style.width = `${Math.max(3, pct)}%`;

            const badge = document.getElementById("vat-status-badge");
            if (totalRev >= threshold) {
                badge.className = "px-3.5 py-1.5 rounded-2xl text-xs font-black self-start sm:self-auto bg-red-50 text-red-600 border border-red-300";
                badge.innerText = "สถานะ: 🔴 เกินเพดาน 1.8M (ต้องยื่นจด VAT)";
            } else if (pct >= 70) {
                badge.className = "px-3.5 py-1.5 rounded-2xl text-xs font-black self-start sm:self-auto bg-amber-50 text-amber-600 border border-amber-300";
                badge.innerText = "สถานะ: 🟡 เฝ้าระวัง (เกิน 70%)";
            } else {
                badge.className = "px-3.5 py-1.5 rounded-2xl text-xs font-black self-start sm:self-auto bg-emerald-50 text-emerald-700 border border-emerald-300";
                badge.innerText = "สถานะ: 🟢 ปลอดภัย (ห่างจากเพดาน)";
            }
        }

        function viewSlip(id) {
            const o = orders.find(x => x.id === id);
            if (!o || !o.slip_image) return;
            document.getElementById("slip-modal-title").innerText = `สลิป: ${o.id}`;
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
            if (targetOrders.length === 0) { alert("กรุณาเลือกออเดอร์ก่อนครับ"); return; }

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
                <div class="label-page" style="width: 100mm; height: 146mm; margin: 0 auto 15mm auto; padding: 5mm; background: #fff; border: 2px solid #000; display: flex; flex-direction: column; justify-content: space-between; page-break-after: always;">
                    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #000; padding-bottom: 4px;">
                        <div style="font-size: 18px; font-weight: 900;">${carrierName}</div>
                        <div style="text-align: right;">
                            <div style="background: #000; color: #fff; padding: 2px 6px; border-radius: 4px; font-size: 12px; font-weight: 900;">${badgeText}</div>
                            <div style="font-size: 10px; font-weight: bold; color: #047857; margin-top: 2px;">ชำระแล้ว (NON-COD)</div>
                        </div>
                    </div>
                    <div style="text-align: center; border-bottom: 2px solid #000; padding: 4px 0;">
                        <div style="font-family: monospace; font-size: 16px; font-weight: 900; letter-spacing: 2px;">${barcodeNum}</div>
                        <div style="font-size: 9px; color: #555;">Order: ${o.id} | วันที่: ${o.created_at}</div>
                    </div>
                    <div style="border-bottom: 1.5px solid #000; padding: 4px 0; font-size: 11px; line-height: 1.3; background: #fafafa; position: relative;">
                        <div><strong style="font-size: 12px;">ผู้รับ (TO):</strong> <span style="font-size: 13px; font-weight: 900;">${o.customer_name}</span></div>
                        <div style="font-size: 13px; font-weight: 900;">โทร: ${o.phone}</div>
                        <div style="font-size: 10.5px; padding-right: 55px;">${o.address}</div>
                        <div style="position: absolute; right: 4px; top: 10px; border: 2px solid #000; padding: 2px 5px; font-size: 14px; font-weight: 900; font-family: monospace; background: #fff;">${o.postal_code || '10150'}</div>
                    </div>
                    <div style="font-size: 9.5px; color: #333; border-bottom: 1.5px solid #000; padding: 3px 0;">
                        <strong>ผู้ส่ง (FROM):</strong> GOODSTONE SHOP (คุณสุเมธา แท่นธรรมโรจน์ โทร. 061-537-2239)<br>
                        123/45 ถนนพระราม 2 แขวงท่าข้าม เขตบางขุนเทียน กรุงเทพฯ 10150
                    </div>
                    <div style="flex-grow: 1; padding-top: 4px;">
                        <div style="font-size: 9.5px; font-weight: 800; margin-bottom: 2px;">📦 รายการสินค้าในพัสดุ (PACKING LIST):</div>
                        <table style="width: 100%; border-collapse: collapse; font-size: 9.5px;">
                            <thead>
                                <tr style="background: #eee; border-bottom: 1px solid #000;">
                                    <th style="width: 25px; padding: 2px;">#</th>
                                    <th style="text-align: left; padding: 2px 4px;">ชื่อสินค้า / สเปก</th>
                                    <th style="width: 40px; padding: 2px;">จำนวน</th>
                                </tr>
                            </thead>
                            <tbody>${itemsRows}</tbody>
                        </table>
                    </div>
                    <div style="border-top: 1.5px solid #000; padding-top: 3px; display: flex; justify-content: space-between; font-size: 8.5px;">
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
                    @media print {
                        body { background: #fff; padding: 0; }
                        .print-toolbar { display: none; }
                        .label-page { margin: 0 !important; border: 2px solid #000 !important; box-shadow: none !important; page-break-after: always !important; }
                        @page { size: 100mm 150mm; margin: 0; }
                    }
                </style>
            </head>
            <body>
                <div class="print-toolbar">
                    <span style="font-size: 13px; font-weight: bold;">🖨️ ใบปะหน้า (${targetOrders.length} รายการ)</span>
                    <div style="display: flex; gap: 8px;">
                        <button onclick="window.print()" class="print-btn">สั่งพิมพ์</button>
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
    f.write(admin_code)

print("slingshot-shop/admin.html updated with Mobile-First Card Layout & Reliable Mobile Image Uploader!")
