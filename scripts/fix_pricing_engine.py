with open("/working_dir/slingshot-shop/index.html", "r", encoding="utf-8") as f:
    code = f.read()

# Replace pricing and variant helpers in index.html
safe_helpers = """
        // ================= BULLETPROOF PRODUCT & VARIANT RESOLVER =================
        function getSafeProduct(prodOrId) {
            if (!prodOrId) return products[0] || DEFAULT_PRODUCTS[0];
            if (typeof prodOrId === "string") {
                const found = products.find(p => p.id === prodOrId);
                return found || products[0] || DEFAULT_PRODUCTS[0];
            }
            return prodOrId;
        }

        function getSafeVariant(product, variantIdx) {
            const p = getSafeProduct(product);
            const defaultPrice = !isNaN(Number(p.price)) ? Number(p.price) : 390;
            const defaultStock = !isNaN(Number(p.stock)) ? Number(p.stock) : 20;

            if (p.variants && Array.isArray(p.variants) && p.variants.length > 0) {
                const idx = (typeof variantIdx === "number" && variantIdx >= 0 && variantIdx < p.variants.length) ? variantIdx : 0;
                const v = p.variants[idx] || p.variants[0];
                if (v) {
                    return {
                        name: (v.name && String(v.name).trim()) ? String(v.name).trim() : "รุ่นมาตรฐาน",
                        price: (!isNaN(Number(v.price)) && Number(v.price) > 0) ? Number(v.price) : defaultPrice,
                        stock: (!isNaN(Number(v.stock))) ? Number(v.stock) : defaultStock
                    };
                }
            }

            return {
                name: "รุ่นมาตรฐาน",
                price: defaultPrice,
                stock: defaultStock
            };
        }
"""

old_open_checkout = """        function openProductDirectCheckout(productId) {
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
        }"""

new_open_checkout = """        function openProductDirectCheckout(productId) {
            selectedProduct = getSafeProduct(productId);
            selectedVariantIdx = 0;
            quantity = 1;
            currentGalleryIdx = 0;

            document.getElementById("view-catalog").classList.add("hidden");
            document.getElementById("view-checkout").classList.remove("hidden");

            renderProductCheckoutDetail();
            updateCalculations();
            window.scrollTo({ top: 0, behavior: "smooth" });
        }"""

new_render_checkout = """        function renderProductCheckoutDetail() {
            const p = getSafeProduct(selectedProduct);
            selectedProduct = p;

            const images = (p.images && Array.isArray(p.images) && p.images.length > 0)
                ? p.images
                : [{ file: p.image_file || p.fallback_image, name: `${p.id}_main.jpg` }];

            const mainImg = document.getElementById("checkout-main-img");
            if (mainImg) mainImg.src = images[0].file || p.fallback_image;

            document.getElementById("checkout-prod-category").innerText = p.category || "slingshot";
            document.getElementById("checkout-prod-title").innerText = p.name || "หนังสติ๊กยุทธวิธี";
            document.getElementById("checkout-prod-desc").innerText = p.description || "";

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
                thumbsContainer.appendChild(btn);\n            });

            // Variant Selector Buttons
            const variantsContainer = document.getElementById("checkout-variants-container");
            variantsContainer.innerHTML = "";
            const variantsList = (p.variants && Array.isArray(p.variants) && p.variants.length > 0)
                ? p.variants
                : [{ name: "รุ่นมาตรฐาน", price: Number(p.price || 390), stock: Number(p.stock || 20) }];

            variantsList.forEach((v, idx) => {
                const safeV = getSafeVariant(p, idx);
                const btn = document.createElement("button");
                btn.type = "button";
                btn.className = `px-3 py-1.5 rounded-xl text-xs font-bold border-2 transition-all cursor-pointer ${idx === selectedVariantIdx ? 'border-[#EE4D2D] bg-[#EE4D2D] text-white shadow-sm' : 'theme-card-subtle theme-text-main hover:border-[#EE4D2D]'}`;
                btn.innerText = `${safeV.name} (฿${safeV.price.toLocaleString()})`;
                btn.onclick = () => {
                    selectedVariantIdx = idx;
                    renderProductCheckoutDetail();
                    updateCalculations();
                };
                variantsContainer.appendChild(btn);
            });

            const activeV = getSafeVariant(p, selectedVariantIdx);
            document.getElementById("checkout-prod-price").innerText = `฿${activeV.price.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            document.getElementById("checkout-prod-stock").innerText = `สต็อกคงเหลือ ${activeV.stock} ชิ้น`;
            document.getElementById("checkout-qty-display").innerText = quantity;
        }"""

new_update_calc = """        function updateCalculations() {
            const p = getSafeProduct(selectedProduct);
            selectedProduct = p;
            const activeV = getSafeVariant(p, selectedVariantIdx);
            const unitPrice = activeV.price;
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
        }"""

# Insert safe_helpers right before function showCatalogView
if "function showCatalogView() {" in code:
    code = code.replace("function showCatalogView() {", safe_helpers + "\n        function showCatalogView() {")

# Replace openProductDirectCheckout, renderProductCheckoutDetail, and updateCalculations
import re
target_block = r"function openProductDirectCheckout\(productId\) \{[\s\S]*?function setPaymentMethod"
match = re.search(target_block, code)
if match:
    replacement = new_open_checkout + "\n\n" + new_render_checkout + "\n\n" + new_update_calc + "\n\n        function setPaymentMethod"
    code = code[:match.start()] + replacement + code[match.end():]
    print("Replaced checkout & pricing calculation functions!")

# Also fix submitDirectOrder
new_submit_order = """        function submitDirectOrder() {
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
            const unitPrice = activeV.price;
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
        }"""

submit_match = re.search(r"function submitDirectOrder\(\) \{[\s\S]*?function openGalleryModal", code)
if submit_match:
    code = code[:submit_match.start()] + new_submit_order + "\n\n        // ================= GALLERY LIGHTBOX =================\n        function openGalleryModal" + code[submit_match.end():]
    print("Replaced submitDirectOrder!")

with open("/working_dir/slingshot-shop/index.html", "w", encoding="utf-8") as f:
    f.write(code)

print("Saved slingshot-shop/index.html successfully!")
