import re

with open("/working_dir/slingshot-shop/index.html", "r", encoding="utf-8") as f:
    code = f.read()

# Replace updateCalculations and renderProductCheckoutDetail and openProductDirectCheckout and init
new_checkout_engine = """        function init() {
            lucide.createIcons();
            
            const savedProducts = localStorage.getItem("goodstone_products");
            if (savedProducts) {
                try { 
                    const parsed = JSON.parse(savedProducts);
                    if (Array.isArray(parsed) && parsed.length > 0) {
                        products = parsed;
                    }
                } catch(e) {}
            } else {
                localStorage.setItem("goodstone_products", JSON.stringify(DEFAULT_PRODUCTS));
            }

            selectedProduct = (products && products.length > 0) ? products[0] : DEFAULT_PRODUCTS[0];
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
                    const cookieBadge = document.getElementById("auto-cookie-badge");
                    if (cookieBadge) cookieBadge.classList.remove("hidden");
                } catch(e) {}
            }

            renderCatalogGrid();
            renderProductCheckoutDetail();
            updateCalculations();
            applyTheme(currentTheme);
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

        // ================= CATALOG GRID =================
        function renderCatalogGrid() {
            const grid = document.getElementById("product-grid");
            if (!grid) return;
            grid.innerHTML = "";

            const list = selectedCategory === "all" ? products : products.filter(p => p.category === selectedCategory);

            if (list.length === 0) {
                grid.innerHTML = `<div class="col-span-full text-center py-12 text-slate-400">ไม่พบสินค้าในหมวดหมู่นี้</div>`;
                return;
            }

            list.forEach(p => {
                const imageCount = (p.images && p.images.length > 0) ? p.images.length : 1;
                const imgSrc = p.image_file || p.fallback_image;
                const shopeeUrl = p.shopee_affiliate_url || "https://th.shp.ee/sdFv2cS1";
                const displayPrice = Number(p.price) || 390;

                const card = document.createElement("div");
                card.className = "theme-card rounded-3xl border-2 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group";

                card.innerHTML = `
                    <div onclick="openProductDirectCheckout('${p.id}')" class="h-48 sm:h-52 overflow-hidden theme-card-subtle relative flex items-center justify-center cursor-pointer group/img border-b theme-border">
                        <img src="${imgSrc}" onerror="this.onerror=null; this.src='${p.fallback_image}';" alt="${p.name}" class="w-full h-full object-contain group-hover/img:scale-105 transition-transform duration-300">
                        <span class="absolute top-3 right-3 bg-white/95 dark:bg-black/80 text-[#EE4D2D] border border-orange-200 text-[11px] px-2.5 py-1 rounded-full font-black shadow-sm">
                            คงเหลือ ${p.stock || 20}
                        </span>
                        <div class="absolute bottom-2 left-2 bg-white/95 dark:bg-black/80 theme-text-main border border-slate-200 dark:border-slate-700 text-[10px] px-2.5 py-1 rounded-xl flex items-center gap-1 group-hover/img:bg-[#EE4D2D] group-hover/img:text-white group-hover/img:border-[#EE4D2D] font-bold transition-all shadow-sm">
                            <span>⚡ แตะรูปเพื่อซื้อด่วน (${imageCount} รูป)</span>
                        </div>
                    </div>

                    <div class="p-4 sm:p-5 flex flex-col flex-grow justify-between space-y-3">
                        <div class="space-y-1.5">
                            <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full theme-badge border">
                                ${p.category}
                            </span>
                            <h3 onclick="openProductDirectCheckout('${p.id}')" class="font-bold theme-text-main text-sm sm:text-base line-clamp-2 cursor-pointer hover:text-[#EE4D2D] transition-colors">
                                ${p.name}
                            </h3>
                            <p class="text-xs theme-text-muted line-clamp-2 leading-relaxed">
                                ${p.description}
                            </p>
                        </div>

                        <div class="pt-2 border-t theme-border space-y-2">
                            <div class="flex items-center justify-between">
                                <div>
                                    <span class="text-[10px] theme-text-muted block">ราคาเริ่มต้น</span>
                                    <span class="text-lg sm:text-xl font-extrabold text-[#EE4D2D]">฿${displayPrice.toLocaleString()}</span>
                                </div>
                                <button onclick="openProductDirectCheckout('${p.id}')" class="bg-[#EE4D2D] hover:bg-[#d73211] text-white px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1 shadow-md active:scale-95 cursor-pointer">
                                    <span>⚡ ซื้อด่วน</span>
                                </button>
                            </div>

                            <a href="${shopeeUrl}" target="_blank" rel="noopener noreferrer" class="w-full text-center block theme-badge py-1.5 rounded-xl border text-xs font-bold transition-colors">
                                ⭐ ดูรีวิวใน Shopee &gt;
                            </a>
                        </div>
                    </div>
                `;
                grid.appendChild(card);
            });
            lucide.createIcons();
        }

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
                thumb.className = `w-14 h-14 rounded-xl p-1 theme-card-subtle border-2 cursor-pointer transition-all flex-shrink-0 flex items-center justify-center ${idx === 0 ? "border-[#EE4D2D] scale-105 shadow-md" : "theme-border opacity-70"}`;
                thumb.innerHTML = `<img src="${img.file}" class="w-full h-full object-contain">`;
                thumb.onclick = () => {
                    document.getElementById("detail-main-img").src = img.file;
                    Array.from(thumbsStrip.children).forEach((c, i) => {
                        c.className = `w-14 h-14 rounded-xl p-1 theme-card-subtle border-2 cursor-pointer transition-all flex-shrink-0 flex items-center justify-center ${i === idx ? "border-[#EE4D2D] scale-105 shadow-md" : "theme-border opacity-70"}`;
                    });
                };
                thumbsStrip.appendChild(thumb);
            });

            // Shopee Affiliate Button in Checkout View
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

            // Variant Pills (Shopee Style)
            const pillsContainer = document.getElementById("detail-variant-pills");
            pillsContainer.innerHTML = "";
            p.variants.forEach((v, idx) => {
                const isSel = (idx === selectedVariantIdx);
                const vPrice = Number(v.price) || Number(p.price) || 390;
                const btn = document.createElement("button");
                btn.type = "button";
                btn.className = `px-3.5 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 ${isSel ? "bg-[#EE4D2D] text-white border-2 border-[#d73211] shadow-md scale-105" : "theme-card-subtle hover:border-[#EE4D2D] theme-text-main border theme-border"}`;
                btn.innerHTML = `${isSel ? "<span>✓</span>" : ""}<span>${v.name}</span><span class="${isSel ? "bg-black/30 text-amber-300" : "theme-badge"} text-[11px] px-1.5 py-0.5 rounded font-black">฿${vPrice.toLocaleString()}</span>`;
                btn.onclick = () => {
                    selectedVariantIdx = idx;
                    renderProductCheckoutDetail();
                    updateCalculations();
                };
                pillsContainer.appendChild(btn);
            });
        }

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
            const unitPrice = Number(activeV.price) || Number(p.price) || 390;
            const qty = Math.max(1, Number(quantity) || 1);

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
        }"""

# Find and replace the whole block from function init() down to function setPaymentMethod
pattern = r"function init\(\) \{[\s\S]*?function setPaymentMethod"
match = re.search(pattern, code)
if match:
    code = code[:match.start()] + new_checkout_engine + "\n\n        function setPaymentMethod" + code[match.end():]
    print("Replaced checkout engine with bulletproof NaN protection!")

with open("/working_dir/slingshot-shop/index.html", "w", encoding="utf-8") as f:
    f.write(code)
