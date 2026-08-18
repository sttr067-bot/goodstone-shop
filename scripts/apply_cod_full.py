import json
import re

# 1. Update index.html
with open("/working_dir/slingshot-shop/index.html", "r", encoding="utf-8") as f:
    idx_code = f.read()

# Add summary-cod-row to summary table
old_summary_ship = """                        <div class="flex justify-between">
                            <span class="text-slate-500">ค่าจัดส่ง:</span>
                            <span id="summary-shipping" class="font-bold text-emerald-700">ฟรี (฿0)</span>
                        </div>"""

new_summary_ship = """                        <div class="flex justify-between">
                            <span class="text-slate-500">ค่าจัดส่ง:</span>
                            <span id="summary-shipping" class="font-bold text-emerald-700">ฟรี (฿0)</span>
                        </div>
                        <div id="summary-cod-row" class="flex justify-between text-[#EE4D2D] hidden">
                            <span>ค่าบริการเก็บเงินปลายทาง (+3%):</span>
                            <span id="summary-cod-fee" class="font-bold">+฿0.00</span>
                        </div>"""

if old_summary_ship in idx_code:
    idx_code = idx_code.replace(old_summary_ship, new_summary_ship)

# Update updateCalculations() in index.html
old_calc_block = """        function updateCalculations() {
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
            document.getElementById("wallet-order-amt").innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}` THREE"""

new_calc_func = """        function updateCalculations() {
            const activeV = selectedProduct.variants[selectedVariantIdx] || { name: "รุ่นมาตรฐาน", price: selectedProduct.price };
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
            document.getElementById("summary-shipping").innerText = isFreeShipping ? "ฟรี (฿0)" : "฿25.00";
            
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
            document.getElementById("promptpay-qr-img").src = `https://api.qrserver.com/v1/create-qr-code/?size=260x260&margin=12&data=${encodeURIComponent(ppPayload)}`;
        }

        function setPaymentMethod(method) {
            paymentMethod = method;
            const btnPP = document.getElementById("btn-pay-promptpay");
            const btnCOD = document.getElementById("btn-pay-cod");
            const btnW = document.getElementById("btn-pay-wallet");
            const panelPP = document.getElementById("panel-promptpay");
            const panelCOD = document.getElementById("panel-cod");
            const panelW = document.getElementById("panel-wallet");

            btnPP.className = "p-2.5 rounded-2xl border-2 border-[#EBE3D5] bg-[#F9F6F0] text-slate-700 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";
            if (btnCOD) btnCOD.className = "p-2.5 rounded-2xl border-2 border-[#EBE3D5] bg-[#F9F6F0] text-slate-700 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";
            btnW.className = "p-2.5 rounded-2xl border-2 border-[#EBE3D5] bg-[#F9F6F0] text-slate-700 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";

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
        }"""

# Replace old updateCalculations and setPaymentMethod
target_pattern = r"function updateCalculations\(\) \{[\s\S]*?function onPhoneChange"
match = re.search(target_pattern, idx_code)
if match:
    idx_code = idx_code[:match.start()] + new_calc_func + "\n\n        function onPhoneChange" + idx_code[match.end():]
    print("Replaced updateCalculations & setPaymentMethod in index.html!")

# Update submitDirectOrder in index.html
old_submit_start = "        function submitDirectOrder() {"
new_submit_func = """        function submitDirectOrder() {
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
        }"""

submit_pattern = r"function submitDirectOrder\(\) \{[\s\S]*?function openGalleryModal"
match_sub = re.search(submit_pattern, idx_code)
if match_sub:
    idx_code = idx_code[:match_sub.start()] + new_submit_func + "\n\n        // ================= GALLERY LIGHTBOX =================\n        function openGalleryModal" + idx_code[match_sub.end():]
    print("Replaced submitDirectOrder in index.html!")

with open("/working_dir/slingshot-shop/index.html", "w", encoding="utf-8") as f:
    f.write(idx_code)

# 2. Update admin.html (Orders card & 4x6 Thermal Label COD)
with open("/working_dir/slingshot-shop/admin.html", "r", encoding="utf-8") as f:
    adm_code = f.read()

# Update status filter in admin.html
old_status_filter = """                    <option value="ALL">ทั้งหมด (All Orders)</option>
                    <option value="PAID">ชำระแล้ว (รอแพ็ก)</option>
                    <option value="SHIPPED">จัดส่งแล้ว (มีเลขพัสดุ)</option>"""

new_status_filter = """                    <option value="ALL">ทั้งหมด (All Orders)</option>
                    <option value="PAID">ชำระแล้ว (รอแพ็ก)</option>
                    <option value="COD_PENDING">เก็บเงินปลายทาง (COD)</option>
                    <option value="SHIPPED">จัดส่งแล้ว (มีเลขพัสดุ)</option>"""

if old_status_filter in adm_code:
    adm_code = adm_code.replace(old_status_filter, new_status_filter)

# Update order card status badge in admin.html
old_card_badge = """                        <span class="text-[10px] font-bold px-2.5 py-1 rounded-full ${o.status === 'SHIPPED' ? 'bg-emerald-50 text-emerald-700 border border-emerald-300' : 'bg-orange-50 text-[#EE4D2D] border border-orange-200'}">
                            ${o.status === 'SHIPPED' ? '✓ จัดส่งแล้ว' : 'ชำระแล้ว (รอแพ็ก)'}
                        </span>"""

new_card_badge = """                        <span class="text-[10px] font-bold px-2.5 py-1 rounded-full ${o.status === 'SHIPPED' ? 'bg-emerald-50 text-emerald-700 border border-emerald-300' : o.payment_method === 'COD' || o.status === 'COD_PENDING' ? 'bg-amber-50 text-amber-800 border border-amber-300' : 'bg-orange-50 text-[#EE4D2D] border border-orange-200'}">
                            ${o.status === 'SHIPPED' ? '✓ จัดส่งแล้ว' : o.payment_method === 'COD' || o.status === 'COD_PENDING' ? '💵 COD รอส่ง' : 'ชำระแล้ว (รอแพ็ก)'}
                        </span>"""

if old_card_badge in adm_code:
    adm_code = adm_code.replace(old_card_badge, new_card_badge)

# Update printLabels in admin.html to display COD box on 4x6 thermal label
old_header_right = """                        <div class="header-right">
                            <div class="delivery-type">${badgeText}</div>
                            <div class="cod-tag">ชำระแล้ว (NON-COD)</div>
                        </div>"""

new_header_right = """                        <div class="header-right">
                            <div class="delivery-type">${badgeText}</div>
                            ${(o.payment_method === 'COD' || o.status === 'COD_PENDING') 
                                ? `<div style="background: #EE4D2D; color: #fff; padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: 900; margin-top: 2px; border: 1.5px solid #000;">💵 ยอดเก็บเงิน COD: ฿${Number(o.total_amount).toLocaleString(undefined, {minimumFractionDigits: 2})}</div>`
                                : `<div class="cod-tag">ชำระแล้ว (NON-COD)</div>`
                            }
                        </div>"""

if old_header_right in adm_code:
    adm_code = adm_code.replace(old_header_right, new_header_right)
    print("Updated printLabels COD amount box in admin.html!")

# Update slip button in admin.html
old_slip_btn = """${o.slip_image ? `<button onclick="viewSlip('${o.id}')" class="flex-1 bg-emerald-50 hover:bg-emerald-100 border border-emerald-300 text-emerald-700 py-1.5 rounded-xl text-xs font-bold">🧾 ดูสลิป</button>` : `<span class="flex-1 text-center text-[10px] text-slate-400 py-1.5">Credit Wallet</span>` THREE"""

new_slip_btn = """${o.slip_image ? `<button onclick="viewSlip('${o.id}')" class="flex-1 bg-emerald-50 hover:bg-emerald-100 border border-emerald-300 text-emerald-700 py-1.5 rounded-xl text-xs font-bold">🧾 ดูสลิป</button>` : `<span class="flex-1 text-center text-[10px] font-bold text-slate-500 py-1.5">${o.payment_method === 'COD' ? '💵 เก็บปลายทาง (COD)' : 'Credit Wallet'}</span>` THREE"""

with open("/working_dir/slingshot-shop/admin.html", "w", encoding="utf-8") as f:
    f.write(adm_code)

print("slingshot-shop files successfully updated for COD +3%!")
