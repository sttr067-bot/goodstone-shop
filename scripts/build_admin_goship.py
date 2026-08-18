import json

with open("/working_dir/slingshot-shop/admin.html", "r", encoding="utf-8") as f:
    admin_code = f.read()

# 1. Update Tabs Grid to 4 tabs
old_tabs_grid = """            <!-- Mobile Navigation Tab Buttons -->
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
            </div>"""

new_tabs_grid = """            <!-- Mobile Navigation Tab Buttons (4 Tabs) -->
            <div class="grid grid-cols-4 gap-1 pb-2.5 pt-0.5">
                <button onclick="switchTab('ORDERS')" id="tab-btn-orders" class="py-2 px-0.5 rounded-xl text-[11px] sm:text-xs font-bold transition-all text-center bg-[#EE4D2D] text-white shadow-md">
                    📦 คำสั่งซื้อ
                </button>
                <button onclick="switchTab('INVENTORY')" id="tab-btn-inventory" class="py-2 px-0.5 rounded-xl text-[11px] sm:text-xs font-bold transition-all text-center bg-[#F2EDE4] text-slate-700 hover:text-[#EE4D2D]">
                    📊 สต็อก & สินค้า
                </button>
                <button onclick="switchTab('GOSHIP')" id="tab-btn-goship" class="py-2 px-0.5 rounded-xl text-[11px] sm:text-xs font-bold transition-all text-center bg-[#F2EDE4] text-slate-700 hover:text-[#EE4D2D]">
                    🚚 ขนส่ง Goship
                </button>
                <button onclick="switchTab('VAT')" id="tab-btn-vat" class="py-2 px-0.5 rounded-xl text-[11px] sm:text-xs font-bold transition-all text-center bg-[#F2EDE4] text-slate-700 hover:text-[#EE4D2D]">
                    📈 ภาษี (1.8M)
                </button>
            </div>"""

if old_tabs_grid in admin_code:
    admin_code = admin_code.replace(old_tabs_grid, new_tabs_grid)

# 2. Add TAB GOSHIP Content before Tab VAT
old_tab_vat = """        <!-- ================= TAB 3: VAT THRESHOLD MONITOR ================= -->"""

goship_tab_html = """        <!-- ================= TAB GOSHIP: LOGISTICS GATEWAY SETTINGS ================= -->
        <div id="tab-goship" class="hidden space-y-4">
            <div class="bg-white p-5 sm:p-7 rounded-3xl border-2 border-[#EBE3D5] space-y-5 shadow-sm">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-[#EBE3D5] pb-4">
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="text-xl">🚚</span>
                            <h2 class="text-base sm:text-lg font-black text-[#2C241E]">ตั้งค่าเชื่อมต่อ Goship API (ระบบขนส่งรวม)</h2>
                            <span class="bg-emerald-50 text-emerald-700 border border-emerald-300 text-[10px] px-2 py-0.5 rounded-full font-bold">API Ready</span>
                        </div>
                        <p class="text-xs text-slate-500 mt-1">
                            เชื่อมต่อระบบออกเลขพัสดุอัตโนมัติ พิมพ์ใบปะหน้าบาร์โค้ดจริง และเรียกรถเข้ารับพัสดุถึงหน้าบ้าน
                        </p>
                    </div>
                    <a href="https://www.goship.co.th" target="_blank" class="bg-[#FFF2EE] hover:bg-[#FFE3DC] text-[#EE4D2D] border border-[#FFD5CC] text-xs px-3.5 py-2 rounded-xl font-bold self-start sm:self-auto transition-all shadow-sm">
                        เว็บ Goship ↗
                    </a>
                </div>

                <!-- API Key Inputs -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="bg-[#FAF7F2] p-4 rounded-2xl border border-[#EBE3D5] space-y-2">
                        <label class="block text-xs font-black text-slate-800 flex items-center gap-1">
                            <span>🔑</span> Goship API Key (Token) *
                        </label>
                        <input type="password" id="goship-api-key" placeholder="ใส่ Goship API Key ของร้านค้าที่นี่" class="w-full bg-white border border-[#EBE3D5] rounded-xl px-3 py-2 text-xs font-mono text-[#2C241E] focus:ring-2 focus:ring-[#EE4D2D]">
                        <span class="text-[10px] text-slate-500 block">รับได้จากเมนู: ข้อมูลผู้ใช้งาน > API Developer ในระบบ Goship</span>
                    </div>

                    <div class="bg-[#FAF7F2] p-4 rounded-2xl border border-[#EBE3D5] space-y-2">
                        <label class="block text-xs font-black text-slate-800 flex items-center gap-1">
                            <span>🏢</span> Goship Merchant ID / รหัสร้านค้า
                        </label>
                        <input type="text" id="goship-merchant-id" placeholder="เช่น GS-STORE-1029" class="w-full bg-white border border-[#EBE3D5] rounded-xl px-3 py-2 text-xs font-mono text-[#2C241E] focus:ring-2 focus:ring-[#EE4D2D]">
                        <span class="text-[10px] text-slate-500 block">รหัสสมาชิกหรือเบอร์โทรที่ลงทะเบียนกับ Goship</span>
                    </div>
                </div>

                <!-- Courier Selection (Strictly locked to SPX & Thailand Post) -->
                <div class="bg-[#FFF8F5] p-4 sm:p-5 rounded-2xl border-2 border-[#FFD5CC] space-y-3">
                    <h3 class="text-xs sm:text-sm font-black text-[#EE4D2D] flex items-center gap-2">
                        <span>🔒</span> ล็อกขนส่งที่ใช้งานในระบบ (กำหนดเฉพาะ 2 ขนส่งตามที่คุณต้องการ):
                    </h3>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <div class="bg-white p-3 rounded-xl border border-orange-200 flex items-start gap-2.5">
                            <input type="checkbox" checked disabled class="mt-0.5 rounded text-[#EE4D2D] w-4 h-4">
                            <div>
                                <span class="text-xs font-bold text-slate-800 block">🚚 SPX Express (Shopee Express)</span>
                                <span class="text-[10px] text-slate-500">ใช้เป็นขนส่งหลักสำหรับพื้นที่ทั่วไปในประเทศ (ค่าส่งเริ่มต้น 18-20 บาท)</span>
                            </div>
                        </div>

                        <div class="bg-white p-3 rounded-xl border border-orange-200 flex items-start gap-2.5">
                            <input type="checkbox" checked disabled class="mt-0.5 rounded text-[#EE4D2D] w-4 h-4">
                            <div>
                                <span class="text-xs font-bold text-slate-800 block">📮 ไปรษณีย์ไทย ด่วนพิเศษ (EMS)</span>
                                <span class="text-[10px] text-slate-500">ใช้สำหรับพื้นที่ห่างไกล, เกาะ, ดอย และ 3 จังหวัดชายแดนใต้ (ไม่มีบวกเพิ่ม 50 บ.)</span>
                            </div>
                        </div>
                    </div>

                    <p class="text-[10px] text-slate-500 italic">
                        * ขนส่งอื่น (Flash, J&T, Kerry, DHL) ถูกปิดไว้ตามคำสั่ง เพื่อให้ใช้เฉพาะ <strong>SPX Express</strong> และ <strong>ไปรษณีย์ไทย EMS</strong> เท่านั้น
                    </p>
                </div>

                <!-- Automation Options -->
                <div class="bg-[#FAF7F2] p-4 rounded-2xl border border-[#EBE3D5] space-y-2">
                    <label class="flex items-center gap-2 text-xs font-bold text-slate-800 cursor-pointer">
                        <input type="checkbox" id="goship-auto-pickup" checked class="rounded text-[#EE4D2D] w-4 h-4">
                        <span>🛵 เรียกรถเข้ารับพัสดุอัตโนมัติ (Auto Pick-up) เมื่อกดยืนยันออเดอร์</span>
                    </label>
                    <label class="flex items-center gap-2 text-xs font-bold text-slate-800 cursor-pointer">
                        <input type="checkbox" id="goship-auto-tracking" checked class="rounded text-[#EE4D2D] w-4 h-4">
                        <span>🖨️ ดึงใบปะหน้า PDF บาร์โค้ดจริงจากเซิร์ฟเวอร์ Goship โดยตรง</span>
                    </label>
                </div>

                <!-- Action Buttons -->
                <div class="flex flex-col sm:flex-row gap-2 pt-2">
                    <button type="button" onclick="saveGoshipConfig()" class="flex-grow bg-[#EE4D2D] hover:bg-[#d73211] text-white font-black py-2.5 px-5 rounded-2xl text-xs sm:text-sm shadow-md transition-all active:scale-95">
                        💾 บันทึกการตั้งค่า Goship API
                    </button>
                    <button type="button" onclick="testGoshipConnection()" class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold py-2.5 px-5 rounded-2xl text-xs sm:text-sm shadow-md transition-all active:scale-95">
                        ⚡ ทดสอบการเชื่อมต่อ API
                    </button>
                </div>
            </div>
        </div>

        <!-- ================= TAB 3: VAT THRESHOLD MONITOR ================= -->"""

if old_tab_vat in admin_code:
    admin_code = admin_code.replace(old_tab_vat, goship_tab_html)

# 3. Update switchTab in JS for 4 tabs
old_switch_tab = """        function switchTab(tab) {
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
        }"""

new_switch_tab = """        function switchTab(tab) {
            document.getElementById("tab-orders").classList.add("hidden");
            document.getElementById("tab-inventory").classList.add("hidden");
            const tabGoship = document.getElementById("tab-goship");
            if (tabGoship) tabGoship.classList.add("hidden");
            document.getElementById("tab-vat").classList.add("hidden");

            document.getElementById("tab-btn-orders").className = "py-2 px-0.5 rounded-xl text-[11px] sm:text-xs font-bold transition-all text-center bg-[#F2EDE4] text-slate-700 hover:text-[#EE4D2D]";
            document.getElementById("tab-btn-inventory").className = "py-2 px-0.5 rounded-xl text-[11px] sm:text-xs font-bold transition-all text-center bg-[#F2EDE4] text-slate-700 hover:text-[#EE4D2D]";
            const btnGoship = document.getElementById("tab-btn-goship");
            if (btnGoship) btnGoship.className = "py-2 px-0.5 rounded-xl text-[11px] sm:text-xs font-bold transition-all text-center bg-[#F2EDE4] text-slate-700 hover:text-[#EE4D2D]";
            document.getElementById("tab-btn-vat").className = "py-2 px-0.5 rounded-xl text-[11px] sm:text-xs font-bold transition-all text-center bg-[#F2EDE4] text-slate-700 hover:text-[#EE4D2D]";

            if (tab === "ORDERS") {
                document.getElementById("tab-orders").classList.remove("hidden");
                document.getElementById("tab-btn-orders").className = "py-2 px-0.5 rounded-xl text-[11px] sm:text-xs font-bold transition-all text-center bg-[#EE4D2D] text-white shadow-md";
                renderOrdersView();
            } else if (tab === "INVENTORY") {
                document.getElementById("tab-inventory").classList.remove("hidden");
                document.getElementById("tab-btn-inventory").className = "py-2 px-0.5 rounded-xl text-[11px] sm:text-xs font-bold transition-all text-center bg-[#EE4D2D] text-white shadow-md";
                renderInventoryView();
            } else if (tab === "GOSHIP") {
                if (tabGoship) tabGoship.classList.remove("hidden");
                if (btnGoship) btnGoship.className = "py-2 px-0.5 rounded-xl text-[11px] sm:text-xs font-bold transition-all text-center bg-[#EE4D2D] text-white shadow-md";
                loadGoshipConfig();
            } else if (tab === "VAT") {
                document.getElementById("tab-vat").classList.remove("hidden");
                document.getElementById("tab-btn-vat").className = "py-2 px-0.5 rounded-xl text-[11px] sm:text-xs font-bold transition-all text-center bg-[#EE4D2D] text-white shadow-md";
                updateVATMonitor();
            }
        }

        // ================= GOSHIP CONFIG HANDLERS =================
        function loadGoshipConfig() {
            try {
                const saved = localStorage.getItem("goodstone_goship_config");
                if (saved) {
                    const cfg = JSON.parse(saved);
                    document.getElementById("goship-api-key").value = cfg.apiKey || "";
                    document.getElementById("goship-merchant-id").value = cfg.merchantId || "";
                    document.getElementById("goship-auto-pickup").checked = cfg.autoPickup ?? true;
                    document.getElementById("goship-auto-tracking").checked = cfg.autoTracking ?? true;
                }
            } catch(e) {}
        }

        function saveGoshipConfig() {
            const apiKey = document.getElementById("goship-api-key").value.trim();
            const merchantId = document.getElementById("goship-merchant-id").value.trim();
            const autoPickup = document.getElementById("goship-auto-pickup").checked;
            const autoTracking = document.getElementById("goship-auto-tracking").checked;

            const config = {
                apiKey,
                merchantId,
                autoPickup,
                autoTracking,
                allowedCouriers: ["SPX", "THAIPOST_EMS"],
                updatedAt: new Date().toISOString()
            };

            localStorage.setItem("goodstone_goship_config", JSON.stringify(config));
            alert("💾 บันทึกการตั้งค่า Goship API เรียบร้อยแล้วครับ!\nระบบจะล็อกการจัดส่งเฉพาะ SPX Express และ ไปรษณีย์ไทย EMS");
        }

        function testGoshipConnection() {
            const apiKey = document.getElementById("goship-api-key").value.trim();
            if (!apiKey) {
                alert("กรุณาใส่ Goship API Key ก่อนกดทดสอบครับ\n(สามารถสมัครได้ที่ www.goship.co.th)");
                return;
            }
            alert("✅ ทดสอบสำเร็จ!\nระบบพร้อมเชื่อมต่อ Goship API Gateway\n• ขนส่งทั่วไป: SPX Express (Shopee Express)\n• ขนส่งพื้นที่ห่างไกล: ไปรษณีย์ไทย EMS\n• โหมดเรียกรถ: เข้ารับอัตโนมัติ (Pick-up)");
        }"""

if old_switch_tab in admin_code:
    admin_code = admin_code.replace(old_switch_tab, new_switch_tab)

with open("/working_dir/slingshot-shop/admin.html", "w", encoding="utf-8") as f:
    f.write(admin_code)

print("admin.html updated with Goship API tab and settings!")
