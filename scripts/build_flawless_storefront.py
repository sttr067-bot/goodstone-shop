import json
import re

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))
products_json = json.dumps(data["products"], ensure_ascii=False)

# Let's inspect the entire index.html and rebuild the theme CSS and calculation engine cleanly
with open("/working_dir/slingshot-shop/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. CSS Theme Engine
clean_theme_css = """    <style>
        body { font-family: "Prompt", sans-serif; transition: background-color 0.2s ease, color 0.2s ease; margin: 0; padding: 0; }
        
        /* ---------------- DARK THEME (DEFAULT) ---------------- */
        :root, html[data-theme="dark"], body[data-theme="dark"] {
            --bg-page: #121215;
            --bg-header: #191920;
            --bg-card: #1F1F26;
            --bg-subtle: #272732;
            --bg-input: #17171E;
            --border-card: #333342;
            --border-subtle: #2A2A38;
            --text-main: #F4F0EA;
            --text-muted: #A1A1B0;
            --text-sub: #787888;
            --badge-bg: #2E1B17;
            --badge-border: #5C2B1F;
            --badge-text: #FF6E4E;
            --hero-bg: linear-gradient(135deg, #261B18 0%, #201C22 50%, #191922 100%);
            --summary-box-bg: #191920;
            --btn-ghost-bg: #272732;
            --btn-ghost-border: #383848;
            --btn-ghost-text: #DCD8D0;
        }

        /* ---------------- LIGHT THEME (WARM CREAM & SHOPEE ORANGE) ---------------- */
        html[data-theme="light"], body[data-theme="light"] {
            --bg-page: #F9F6F0;
            --bg-header: #FFFFFF;
            --bg-card: #FFFFFF;
            --bg-subtle: #FAF7F2;
            --bg-input: #FAF7F2;
            --border-card: #EBE3D5;
            --border-subtle: #F0EAE1;
            --text-main: #2C241E;
            --text-muted: #64748B;
            --text-sub: #94A3B8;
            --badge-bg: #FFF2EE;
            --badge-border: #FFD5CC;
            --badge-text: #EE4D2D;
            --hero-bg: linear-gradient(135deg, #FFF6F2 0%, #FDF3EA 50%, #FBF0E4 100%);
            --summary-box-bg: #FAF7F2;
            --btn-ghost-bg: #FAF7F2;
            --btn-ghost-border: #EBE3D5;
            --btn-ghost-text: #2C241E;
        }

        /* Core Theme Classes */
        .app-bg { background-color: var(--bg-page) !important; color: var(--text-main) !important; }
        .app-header { background-color: var(--bg-header) !important; border-color: var(--border-card) !important; }
        .app-card { background-color: var(--bg-card) !important; border-color: var(--border-card) !important; color: var(--text-main) !important; }
        .app-card-subtle { background-color: var(--bg-subtle) !important; border-color: var(--border-subtle) !important; }
        .app-input { background-color: var(--bg-input) !important; border-color: var(--border-card) !important; color: var(--text-main) !important; }
        .app-hero { background: var(--hero-bg) !important; border-color: var(--border-card) !important; }
        .app-summary { background-color: var(--summary-box-bg) !important; border-color: var(--border-card) !important; }
        .app-badge { background-color: var(--badge-bg) !important; border-color: var(--badge-border) !important; color: var(--badge-text) !important; }
        .app-text-main { color: var(--text-main) !important; }
        .app-text-muted { color: var(--text-muted) !important; }
        .app-border { border-color: var(--border-card) !important; }
    </style>"""

# Replace <style> block
html = re.sub(r"<style>[\s\S]*?<\/style>", clean_theme_css, html)

# 2. Ensure body tag uses app-bg and data-theme="dark"
html = re.sub(r"<body[^>]*>", '<body class="app-bg min-h-screen flex flex-col font-sans" data-theme="dark">', html)

# 3. Update Header
old_header_pattern = r"<header[\s\S]*?<\/header>"
new_header_html = """<header class="sticky top-0 z-40 app-header border-b-2 shadow-sm">
        <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16">
                <!-- Logo -->
                <div class="flex items-center gap-2.5 sm:gap-3 cursor-pointer" onclick="showCatalogView()">
                    <div class="w-10 h-10 rounded-2xl bg-[#EE4D2D] flex items-center justify-center text-white font-black text-xl shadow-md shadow-orange-500/20 flex-shrink-0">
                        🎯
                    </div>
                    <div>
                        <div class="flex items-center gap-1.5">
                            <span class="font-black text-base sm:text-lg tracking-wide app-text-main">GOODSTONE</span>
                            <span class="app-badge text-[9px] px-1.5 py-0.2 rounded font-black border uppercase">SHOP</span>
                        </div>
                        <span class="text-[10px] sm:text-[11px] block app-text-muted font-medium">ร้านหนังสติ๊กยุทธวิธีและอุปกรณ์</span>
                    </div>
                </div>

                <!-- Nav Menu & Theme Toggle -->
                <div class="flex items-center gap-2 sm:gap-4">
                    <button onclick="showCatalogView()" class="app-text-main hover:text-[#EE4D2D] text-xs sm:text-sm font-bold flex items-center gap-1">
                        <span>🏪</span> <span class="hidden sm:inline">หน้าร้านค้า</span>
                    </button>
                    <a href="track.html" class="app-text-muted hover:text-[#EE4D2D] text-xs sm:text-sm font-bold flex items-center gap-1">
                        <span>🚚</span> <span class="hidden sm:inline">เช็คพัสดุ</span>
                    </a>

                    <!-- Theme Toggle Switcher Button (Default: Dark) -->
                    <button type="button" onclick="toggleTheme()" id="theme-toggle-btn" class="flex items-center gap-1.5 px-3 py-1.5 rounded-xl border text-xs font-bold transition-all shadow-sm active:scale-95 cursor-pointer" title="สลับโหมดมืด / โหมดสว่าง (ครีม-ส้ม)">
                        <span id="theme-toggle-icon">🌙</span>
                        <span id="theme-toggle-text" class="text-[11px] sm:text-xs">โหมดมืด</span>
                    </button>

                    <!-- Customer Wallet Badge -->
                    <div id="header-wallet-badge" class="hidden sm:flex items-center gap-1.5 app-badge px-3 py-1.5 rounded-xl text-xs font-bold border">
                        <span>👛</span>
                        <span id="user-wallet-display" class="font-black text-[#EE4D2D]">฿0.00</span>
                    </div>
                </div>
            </div>
        </div>
    </header>"""

html = re.sub(old_header_pattern, new_header_html, html)

# 4. Update Hero Banner
html = html.replace(
    'class="rounded-3xl theme-hero p-6 sm:p-10 border-2 shadow-sm space-y-3"',
    'class="rounded-3xl app-hero p-5 sm:p-8 border-2 shadow-sm space-y-3"'
)

# 5. Replace Javascript engine with 100% NaN-proof calculations and responsive theme switcher
js_engine = """
    <!-- JAVASCRIPT LOGIC ENGINE -->
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
        let currentTheme = localStorage.getItem("goodstone_theme") || "dark";

        let userWallet = {
            balance: 530,
            total_topup: 500,
            total_bonus: 30
        };

        // ================= THEME CONTROLLER (LOCKED DEFAULT TO DARK) =================
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
                if (btn) {
                    btn.className = "flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-[#333342] bg-[#272732] text-[#F4F0EA] hover:border-[#FF6E4E] text-xs font-bold transition-all shadow-sm active:scale-95 cursor-pointer";
                }
            } else {
                if (icon) icon.innerText = "☀️";
                if (text) text.innerText = "โหมดสว่าง (ครีม)";
                if (btn) {
                    btn.className = "flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-[#EBE3D5] bg-[#FFFFFF] text-[#2C241E] hover:border-[#EE4D2D] text-xs font-bold transition-all shadow-sm active:scale-95 cursor-pointer";
                }
            }

            if (typeof renderCatalogGrid === "function") {
                renderCatalogGrid();
            }
        }

        function toggleTheme() {
            const nextTheme = currentTheme === "dark" ? "light" : "dark";
            applyTheme(nextTheme);
        }

        // ================= INIT =================
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
            const p = products.find(x => x.id === productId) || products[0] || DEFAULT_PRODUCTS[0];
            selectedProduct = p;
            selectedVariantIdx = 0;
            quantity = 1;

            document.getElementById("view-catalog").classList.add("hidden");
            document.getElementById("view-checkout").classList.remove("hidden");
            window.scrollTo({ top: 0, behavior: "smooth" });

            renderProductCheckoutDetail();
            updateCalculations();
        }

        function filterCategory(cat) {
            selectedCategory = cat;
            renderCatalogGrid();
        }

        function searchProducts() {
            renderCatalogGrid();
        }

        // ================= CATALOG GRID RENDER =================
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
                    btn.className = "cat-filter-btn px-4 py-2 rounded-2xl text-xs font-bold bg-[#EE4D2D] text-white shadow-md transition-all scale-105";
                } else {
                    btn.className = "cat-filter-btn px-4 py-2 rounded-2xl text-xs font-bold app-card-subtle app-text-main border app-border hover:border-[#EE4D2D] transition-all";
                }
            });

            const filtered = products.filter(p => {
                const matchCat = (selectedCategory === "all" || p.category === selectedCategory);
                const matchQuery = !query || p.name.toLowerCase().includes(query) || p.description.toLowerCase().includes(query);
                return matchCat && matchQuery;
            });

            if (filtered.length === 0) {
                container.innerHTML = `<div class="col-span-full py-12 text-center app-text-muted text-sm">ไม่พบสินค้าที่ตรงกับการค้นหา</div>`;
                return;
            }

            filtered.forEach(p => {
                const minPrice = (p.variants && p.variants.length > 0)
                    ? Math.min(...p.variants.map(v => Number(v.price) || Number(p.price) || 390))
                    : (Number(p.price) || 390);

                const imgCount = (p.images && p.images.length > 0) ? p.images.length : 1;
                const imgSrc = p.image_file || p.fallback_image;
                const shopeeUrl = p.shopee_affiliate_url || "https://th.shp.ee/sdFv2cS1";

                const card = document.createElement("div");
                card.className = "app-card rounded-3xl border-2 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group";
                card.innerHTML = `
                    <div>
                        <!-- Clickable Product Image triggers Direct Checkout -->
                        <div onclick="openProductDirectCheckout('${p.id}')" class="h-48 sm:h-52 overflow-hidden app-card-subtle relative flex items-center justify-center cursor-pointer group/img border-b app-border">
                            <img src="${imgSrc}" onerror="this.onerror=null; this.src='${p.fallback_image}';" alt="${p.name}" class="w-full h-full object-contain p-4 group-hover/img:scale-105 transition-transform duration-300">
                            
                            <div class="absolute top-3 left-3 bg-black/70 text-white text-[10px] px-2.5 py-1 rounded-full font-bold backdrop-blur-sm flex items-center gap-1">
                                <span>⚡ แตะรูปเพื่อซื้อด่วน (${imgCount} รูป)</span>
                            </div>

                            <div class="absolute top-3 right-3 bg-emerald-500/90 text-white text-[10px] px-2.5 py-1 rounded-full font-black shadow-sm">
                                คงเหลือ ${p.stock || 20}
                            </div>
                        </div>

                        <!-- Product Info -->
                        <div class="p-4 sm:p-5 space-y-2">
                            <span class="app-badge text-[9px] px-2 py-0.5 rounded-full font-black uppercase inline-block border">${p.category}</span>
                            <h3 onclick="openProductDirectCheckout('${p.id}')" class="font-bold app-text-main text-sm sm:text-base line-clamp-2 cursor-pointer hover:text-[#EE4D2D] transition-colors leading-snug">
                                ${p.name}
                            </h3>
                            <p class="app-text-muted text-xs line-clamp-2 leading-relaxed font-normal">
                                ${p.description}
                            </p>
                        </div>
                    </div>

                    <!-- Actions Area -->
                    <div class="p-4 sm:p-5 pt-0 space-y-2">
                        <div class="flex items-center justify-between pt-2 border-t app-border">
                            <div>
                                <span class="text-[10px] app-text-muted block">ราคาเริ่มต้น</span>
                                <span class="text-base sm:text-lg font-black text-[#EE4D2D]">฿${minPrice.toLocaleString()}</span>
                            </div>
                            <button onclick="openProductDirectCheckout('${p.id}')" class="bg-[#EE4D2D] hover:bg-[#d73211] text-white px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1 shadow-md active:scale-95 cursor-pointer">
                                <span>⚡ ซื้อด่วน</span>
                            </button>
                        </div>

                        <!-- Shopee Review Button -->
                        <a href="${shopeeUrl}" target="_blank" class="w-full bg-[#FFF2EE] hover:bg-[#FFE5DC] text-[#EE4D2D] border border-[#FFD5CC] py-2 rounded-xl text-xs font-bold flex items-center justify-center gap-1 transition-all shadow-sm">
                            <span>⭐ ดูรีวิวใน Shopee ></span>
                        </a>
                    </div>
                `;
                container.appendChild(card);
            });
        }

        // ================= PRODUCT DETAIL & VARIANT RENDER =================
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
        }

        // ================= 100% NaN-PROOF CALCULATION ENGINE =================
        function updateCalculations() {
            if (!selectedProduct) {
                selectedProduct = (products && products.length > 0) ? products[0] : DEFAULT_PRODUCTS[0];
            }
            const p = selectedProduct;
            const variants = (p.variants && Array.isArray(p.variants) && p.variants.length > 0) 
                ? p.variants 
                : [{ name: "รุ่นมาตรฐาน", price: Number(p.price) || 390, stock: Number(p.stock) || 20 }];

            if (selectedVariantIdx < 0 || selectedVariantIdx >= variants.length) {
                selectedVariantIdx = 0;
            }

            const activeV = variants[selectedVariantIdx] || variants[0];
            const rawPrice = Number(activeV.price);
            const unitPrice = (!isNaN(rawPrice) && rawPrice > 0) ? rawPrice : (Number(p.price) || 390);
            const qty = Math.max(1, parseInt(quantity) || 1);

            const subtotal = unitPrice * qty;
            const isFreeShipping = (subtotal >= 200);
            const shippingCost = isFreeShipping ? 0 : 25;
            const baseTotal = subtotal + shippingCost;
            const codFee = (paymentMethod === "COD") ? Number((baseTotal * 0.03).toFixed(2)) : 0;
            const total = Number((baseTotal + codFee).toFixed(2));

            const varNameEl = document.getElementById("summary-variant-name");
            if (varNameEl) varNameEl.innerText = activeV.name || "รุ่นมาตรฐาน";
            
            const qtyEl = document.getElementById("summary-qty");
            if (qtyEl) qtyEl.innerText = qty;
            
            const subtotalEl = document.getElementById("summary-subtotal");
            if (subtotalEl) subtotalEl.innerText = `฿${subtotal.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            
            const shipEl = document.getElementById("summary-shipping");
            if (shipEl) shipEl.innerText = isFreeShipping ? "ฟรี (฿0.00)" : "฿25.00";
            
            const codRow = document.getElementById("summary-cod-row");
            if (codRow) {
                if (paymentMethod === "COD") {
                    codRow.classList.remove("hidden");
                    const codFeeEl = document.getElementById("summary-cod-fee");
                    if (codFeeEl) codFeeEl.innerText = `+฿${codFee.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
                } else {
                    codRow.classList.add("hidden");
                }
            }

            const totalEl = document.getElementById("summary-total");
            if (totalEl) totalEl.innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            
            const ppDisplayEl = document.getElementById("promptpay-amount-display");
            if (ppDisplayEl) ppDisplayEl.innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            
            const submitBtnTextEl = document.getElementById("submit-btn-text");
            if (submitBtnTextEl) {
                if (paymentMethod === "COD") {
                    submitBtnTextEl.innerText = `📦 สั่งซื้อแบบเก็บเงินปลายทาง (฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})})`;
                } else {
                    submitBtnTextEl.innerText = `⚡ สั่งซื้อและชำระเงิน (฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})})`;
                }
            }

            const carrierBadgeEl = document.getElementById("carrier-fee-badge");
            if (carrierBadgeEl) carrierBadgeEl.innerText = isFreeShipping ? "ส่งฟรี (฿0)" : "฿25";
            
            const walletOrderAmtEl = document.getElementById("wallet-order-amt");
            if (walletOrderAmtEl) walletOrderAmtEl.innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            
            const walletAfterBalEl = document.getElementById("wallet-after-bal");
            if (walletAfterBalEl) walletAfterBalEl.innerText = `฿${Math.max(0, userWallet.balance - total).toLocaleString(undefined, {minimumFractionDigits: 2})}`;

            const codBaseEl = document.getElementById("cod-base-amount");
            if (codBaseEl) {
                codBaseEl.innerText = `฿${baseTotal.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
                const codFeeAmtEl = document.getElementById("cod-fee-amount");
                if (codFeeAmtEl) codFeeAmtEl.innerText = `+฿${codFee.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
                const codTotAmtEl = document.getElementById("cod-total-amount");
                if (codTotAmtEl) codTotAmtEl.innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            }

            // Update Dynamic PromptPay QR
            const ppPayload = generatePromptPayQR(total);
            const ppImgEl = document.getElementById("promptpay-qr-img");
            if (ppImgEl) ppImgEl.src = `https://api.qrserver.com/v1/create-qr-code/?size=260x260&margin=12&data=${encodeURIComponent(ppPayload)}`;
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
            if (btnCOD) btnCOD.className = "p-2.5 rounded-2xl border-2 app-border app-card-subtle app-text-main text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";
            btnW.className = "p-2.5 rounded-2xl border-2 app-border app-card-subtle app-text-main text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";

            panelPP.classList.add("hidden");
            if (panelCOD) panelCOD.classList.add("hidden");
            panelW.classList.add("hidden");

            if (method === "PROMPTPAY") {
                btnPP.className = "p-2.5 rounded-2xl border-2 border-[#EE4D2D] bg-[#FFF2EE] text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-0.5 shadow-sm transition-all text-center";
                panelPP.classList.remove("hidden");
            } else if (method === "COD") {
                if (btnCOD) btnCOD.className = "p-2.5 rounded-2xl border-2 border-[#EE4D2D] bg-[#FFF2EE] text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-0.5 shadow-sm transition-all text-center";
                if (panelCOD) panelCOD.classList.remove("hidden");
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
                const disp = document.getElementById("user-wallet-display");
                if (disp) disp.innerText = `฿${userWallet.balance.toLocaleString()}`;
                const btnBal = document.getElementById("wallet-btn-bal");
                if (btnBal) btnBal.innerText = `฿${userWallet.balance.toLocaleString()}`;
                const balBig = document.getElementById("wallet-balance-big");
                if (balBig) balBig.innerText = `฿${userWallet.balance.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
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

            const p = selectedProduct || DEFAULT_PRODUCTS[0];
            const variants = (p.variants && p.variants.length > 0) ? p.variants : [{ name: "รุ่นมาตรฐาน", price: Number(p.price) || 390, stock: 20 }];
            const activeV = variants[selectedVariantIdx] || variants[0];
            const unitPrice = Number(activeV.price) || Number(p.price) || 390;
            const qty = Math.max(1, parseInt(quantity) || 1);

            const subtotal = unitPrice * qty;
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
                        price: unitPrice,
                        quantity: qty,
                        image: p.image_file || p.fallback_image
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
                alert(`🎉 สั่งซื้อและชำระเงินสำเร็จ!\\nรหัสคำสั่งซื้อ: ${newOrder.id}\\nขนส่งที่จัดสรร: ${newOrder.shipping_provider}\\nเลขพัสดุ: ${newOrder.tracking_number}`);
            }
            window.location.href = "track.html";
        }

        // ================= GALLERY LIGHTBOX =================
        function openGalleryModal() {
            const p = selectedProduct || DEFAULT_PRODUCTS[0];
            const images = (p.images && p.images.length > 0)
                ? p.images
                : [{ file: p.image_file || p.fallback_image, name: `${p.id}_main.jpg` }];
            currentGalleryIdx = 0;
            renderGalleryModal(images);
            document.getElementById("gallery-lightbox-modal").classList.remove("hidden");
        }

        function closeGalleryModal() {
            document.getElementById("gallery-lightbox-modal").classList.add("hidden");
        }

        function renderGalleryModal(images) {
            document.getElementById("gallery-active-img").src = images[currentGalleryIdx].file;
            document.getElementById("gallery-counter").innerText = `${currentGalleryIdx + 1} / ${images.length}`;

            const thumbsGrid = document.getElementById("gallery-modal-thumbs");
            thumbsGrid.innerHTML = "";
            images.forEach((img, idx) => {
                const div = document.createElement("div");
                div.className = `w-16 h-16 rounded-xl border-2 p-1 bg-black cursor-pointer overflow-hidden ${idx === currentGalleryIdx ? "border-[#EE4D2D]" : "border-slate-700 opacity-60"}`;
                div.innerHTML = `<img src="${img.file}" class="w-full h-full object-contain">`;
                div.onclick = () => {
                    currentGalleryIdx = idx;
                    renderGalleryModal(images);
                };
                thumbsGrid.appendChild(div);
            });
        }

        function prevGalleryImage() {
            const p = selectedProduct || DEFAULT_PRODUCTS[0];
            const images = (p.images && p.images.length > 0) ? p.images : [{ file: p.image_file || p.fallback_image, name: "img" }];
            currentGalleryIdx = (currentGalleryIdx - 1 + images.length) % images.length;
            renderGalleryModal(images);
        }

        function nextGalleryImage() {
            const p = selectedProduct || DEFAULT_PRODUCTS[0];
            const images = (p.images && p.images.length > 0) ? p.images : [{ file: p.image_file || p.fallback_image, name: "img" }];
            currentGalleryIdx = (currentGalleryIdx + 1) % images.length;
            renderGalleryModal(images);
        }

        // ================= WALLET TOPUP MODAL =================
        function openTopupModal() {
            document.getElementById("topup-modal").classList.remove("hidden");
        }

        function closeTopupModal() {
            document.getElementById("topup-modal").classList.add("hidden");
        }

        function selectTopupTier(amt, bonus) {
            const phone = document.getElementById("cust-phone").value.replace(/[^0-9]/g, "") || "0615372239";
            userWallet.balance += (amt + bonus);
            userWallet.total_topup += amt;
            userWallet.total_bonus += bonus;

            localStorage.setItem(`goodstone_wallet_${phone}`, JSON.stringify(userWallet));
            alert(`🎉 เติมเงิน ฿${amt} รับโบนัสฟรี ฿${bonus} สำเร็จ!\\nยอดเครดิตคงเหลือปัจจุบัน: ฿${userWallet.balance}`);
            
            closeTopupModal();
            onPhoneChange(phone);
        }

        // ================= PROMPTPAY CRC16 GENERATOR =================
        function generatePromptPayQR(amount) {
            const target = "0615372239";
            const formattedTarget = "0066" + target.substring(1);
            const targetField = "0113" + formattedTarget;
            const aid = "0016A000000677010111";
            const merchantInfo = aid + targetField;
            const merchantField = "29" + String(merchantInfo.length).padStart(2, "0") + merchantInfo;
            const amountStr = Number(amount).toFixed(2);
            const amountField = "54" + String(amountStr.length).padStart(2, "0") + amountStr;
            const rawPayload = "000201010212" + merchantField + "5303764" + amountField + "5802TH6304";

            function crc16(str) {
                let crc = 0xFFFF;
                for (let c = 0; c < str.length; c++) {
                    crc ^= str.charCodeAt(c) << 8;
                    for (let i = 0; i < 8; i++) {
                        if (crc & 0x8000) crc = (crc << 1) ^ 0x1021;
                        else crc = crc << 1;
                        crc &= 0xFFFF;
                    }
                }
                return crc.toString(16).toUpperCase().padStart(4, "0");
            }

            return rawPayload + crc16(rawPayload);
        }

        window.onload = init;
    </script>
"""

# Replace the script block at the bottom
script_pattern = r"<script>\s*const DEFAULT_PRODUCTS = [\s\S]*?<\/script>"
html = re.sub(script_pattern, js_engine, html)

with open("/working_dir/slingshot-shop/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Flawless storefront built!")
