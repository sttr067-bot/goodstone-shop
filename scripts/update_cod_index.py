import json

with open("/working_dir/slingshot-shop/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Payment Method Buttons in HTML
old_payment_buttons = """                        <div class="grid grid-cols-2 gap-3">
                            <button type="button" onclick="setPaymentMethod('PROMPTPAY')" id="btn-pay-promptpay" class="p-3 rounded-2xl border-2 border-[#EE4D2D] bg-[#FFF2EE] text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-1 shadow-sm transition-all">
                                <span class="text-lg">📱</span>
                                <span>PromptPay QR Code</span>
                                <span class="text-[10px] font-normal text-slate-500">สแกนจ่าย + แนบสลิป</span>
                            </button>

                            <button type="button" onclick="setPaymentMethod('STORE_CREDIT')" id="btn-pay-wallet" class="p-3 rounded-2xl border-2 border-[#EBE3D5] bg-[#F9F6F0] text-slate-700 text-xs font-bold flex flex-col items-center gap-1 transition-all">
                                <span class="text-lg">👛</span>
                                <span>กระเป๋าเครดิต (Store Credit)</span>
                                <span id="wallet-btn-bal" class="text-[10px] font-bold text-emerald-700">คงเหลือ ฿530.00</span>
                            </button>
                        </div>"""

new_payment_buttons = """                        <div class="grid grid-cols-3 gap-2">
                            <button type="button" onclick="setPaymentMethod('PROMPTPAY')" id="btn-pay-promptpay" class="p-2.5 rounded-2xl border-2 border-[#EE4D2D] bg-[#FFF2EE] text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-0.5 shadow-sm transition-all text-center">
                                <span class="text-base">📱</span>
                                <span class="text-[11px] sm:text-xs">พร้อมเพย์</span>
                                <span class="text-[9px] text-emerald-700 font-normal">ฟรีค่าธรรมเนียม</span>
                            </button>

                            <button type="button" onclick="setPaymentMethod('COD')" id="btn-pay-cod" class="p-2.5 rounded-2xl border-2 border-[#EBE3D5] bg-[#F9F6F0] text-slate-700 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center">
                                <span class="text-base">💵</span>
                                <span class="text-[11px] sm:text-xs">เก็บปลายทาง</span>
                                <span class="text-[9px] text-[#EE4D2D] font-bold">บวก 3%</span>
                            </button>

                            <button type="button" onclick="setPaymentMethod('STORE_CREDIT')" id="btn-pay-wallet" class="p-2.5 rounded-2xl border-2 border-[#EBE3D5] bg-[#F9F6F0] text-slate-700 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center">
                                <span class="text-base">👛</span>
                                <span class="text-[11px] sm:text-xs">กระเป๋าเครดิต</span>
                                <span id="wallet-btn-bal" class="text-[9px] text-emerald-700 font-normal">฿530.00</span>
                            </button>
                        </div>"""

# 2. Add COD Panel
old_promptpay_panel = """                        <!-- PROMPTPAY PANEL -->"""

cod_panel_html = """                        <!-- COD PANEL (เก็บเงินปลายทาง) -->
                        <div id="panel-cod" class="bg-[#FFF8F5] border-2 border-[#FFD5CC] rounded-2xl p-4 sm:p-5 space-y-3 hidden text-[#2C241E]">
                            <div class="flex items-center gap-3">
                                <div class="w-10 h-10 rounded-xl bg-[#EE4D2D] text-white flex items-center justify-center text-xl flex-shrink-0">
                                    💵
                                </div>
                                <div>
                                    <h4 class="font-bold text-xs sm:text-sm text-[#2C241E]">บริการเก็บเงินปลายทาง (Cash on Delivery)</h4>
                                    <p class="text-[11px] text-slate-600">มีค่าบริการเก็บเงินปลายทาง +3% ของยอดรวม</p>
                                </div>
                            </div>
                            <div class="bg-white p-3 rounded-xl border border-[#FFD5CC] text-xs space-y-1 text-slate-700">
                                <p class="flex justify-between"><span>ราคาสินค้า + ค่าส่ง:</span> <span id="cod-base-amount" class="font-bold">฿0.00</span></p>
                                <p class="flex justify-between text-[#EE4D2D]"><span>ค่าบริการ COD (+3%):</span> <span id="cod-fee-amount" class="font-bold">+฿0.00</span></p>
                                <div class="border-t border-slate-100 pt-1 flex justify-between font-black text-sm text-[#2C241E]">
                                    <span>ยอดชำระเมื่อรับพัสดุ:</span>
                                    <span id="cod-total-amount" class="text-[#EE4D2D]">฿0.00</span>
                                </div>
                            </div>
                            <p class="text-[10px] text-slate-500 bg-orange-50/60 p-2 rounded-lg border border-orange-100">
                                💡 ไม่ต้องโอนเงินล่วงหน้า กรุณาเตรียมเงินสดพอดีให้กับพนักงานขนส่งเมื่อพัสดุไปถึงครับ
                            </p>
                        </div>

                        <!-- PROMPTPAY PANEL -->"""

if old_payment_buttons in content:
    content = content.replace(old_payment_buttons, new_payment_buttons)
    print("Replaced payment buttons!")

if old_promptpay_panel in content:
    content = content.replace(old_promptpay_panel, cod_panel_html)
    print("Added COD panel!")

# 3. Update JS Logic for COD in index.html
old_js_update_totals = """            const subtotal = activeV.price * quantity;
            const isFreeShipping = (subtotal >= 200);
            const shippingCost = isFreeShipping ? 0 : 25;
            const total = subtotal + shippingCost;"""

new_js_update_totals = """            const subtotal = activeV.price * quantity;
            const isFreeShipping = (subtotal >= 200);
            const shippingCost = isFreeShipping ? 0 : 25;
            const baseTotal = subtotal + shippingCost;
            const codFee = (paymentMethod === "COD") ? Number((baseTotal * 0.03).toFixed(2)) : 0;
            const total = Number((baseTotal + codFee).toFixed(2));"""

if old_js_update_totals in content:
    content = content.replace(old_js_update_totals, new_js_update_totals)
    print("Updated calculate totals in JS!")

# 4. Update setPaymentMethod in JS
old_set_payment_method = """        function setPaymentMethod(method) {
            paymentMethod = method;
            const btnPP = document.getElementById("btn-pay-promptpay");
            const btnW = document.getElementById("btn-pay-wallet");
            const panelPP = document.getElementById("panel-promptpay");
            const panelW = document.getElementById("panel-wallet");

            if (method === "PROMPTPAY") {
                btnPP.className = "p-3 rounded-2xl border-2 border-[#EE4D2D] bg-[#FFF2EE] text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-1 shadow-sm transition-all";
                btnW.className = "p-3 rounded-2xl border-2 border-[#EBE3D5] bg-[#F9F6F0] text-slate-700 text-xs font-bold flex flex-col items-center gap-1 transition-all";
                panelPP.classList.remove("hidden");
                panelW.classList.add("hidden");
            } else {
                btnW.className = "p-3 rounded-2xl border-2 border-[#EE4D2D] bg-[#FFF2EE] text-[#EE4D2D] text-xs font-bold flex flex-col items-center gap-1 shadow-sm transition-all";
                btnPP.className = "p-3 rounded-2xl border-2 border-[#EBE3D5] bg-[#F9F6F0] text-slate-700 text-xs font-bold flex flex-col items-center gap-1 transition-all";
                panelW.classList.remove("hidden");
                panelPP.classList.add("hidden");
            }
            updateCheckoutTotals();
        }"""

new_set_payment_method = """        function setPaymentMethod(method) {
            paymentMethod = method;
            const btnPP = document.getElementById("btn-pay-promptpay");
            const btnCOD = document.getElementById("btn-pay-cod");
            const btnW = document.getElementById("btn-pay-wallet");
            const panelPP = document.getElementById("panel-promptpay");
            const panelCOD = document.getElementById("panel-cod");
            const panelW = document.getElementById("panel-wallet");

            btnPP.className = "p-2.5 rounded-2xl border-2 border-[#EBE3D5] bg-[#F9F6F0] text-slate-700 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";
            btnCOD.className = "p-2.5 rounded-2xl border-2 border-[#EBE3D5] bg-[#F9F6F0] text-slate-700 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";
            btnW.className = "p-2.5 rounded-2xl border-2 border-[#EBE3D5] bg-[#F9F6F0] text-slate-700 text-xs font-bold flex flex-col items-center gap-0.5 transition-all text-center";

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
            updateCheckoutTotals();
        }"""

if old_set_payment_method in content:
    content = content.replace(old_set_payment_method, new_set_payment_method)
    print("Updated setPaymentMethod in JS!")

# 5. Update updateCheckoutTotals DOM update
old_totals_dom = """            document.getElementById("checkout-subtotal").innerText = `฿${subtotal.toFixed(2)}`;
            document.getElementById("checkout-shipping").innerText = isFreeShipping ? "ฟรี (฿0.00)" : `฿${shippingCost.toFixed(2)}`;
            document.getElementById("checkout-total").innerText = `฿${total.toFixed(2)}`;
            document.getElementById("promptpay-amount-display").innerText = `฿${total.toFixed(2)}`;
            document.getElementById("wallet-pay-amount").innerText = `฿${total.toFixed(2)}`;"""

new_totals_dom = """            document.getElementById("checkout-subtotal").innerText = `฿${subtotal.toFixed(2)}`;
            document.getElementById("checkout-shipping").innerText = isFreeShipping ? "ฟรี (฿0.00)" : `฿${shippingCost.toFixed(2)}`;
            
            // COD fee row in summary
            const codFeeRow = document.getElementById("checkout-cod-fee-row");
            if (codFeeRow) {
                if (paymentMethod === "COD") {
                    codFeeRow.classList.remove("hidden");
                    document.getElementById("checkout-cod-fee").innerText = `+฿${codFee.toFixed(2)}`;
                } else {
                    codFeeRow.classList.add("hidden");
                }
            }

            document.getElementById("checkout-total").innerText = `฿${total.toFixed(2)}`;
            document.getElementById("promptpay-amount-display").innerText = `฿${total.toFixed(2)}`;
            document.getElementById("wallet-pay-amount").innerText = `฿${total.toFixed(2)}`;

            const codBaseEl = document.getElementById("cod-base-amount");
            if (codBaseEl) {
                codBaseEl.innerText = `฿${baseTotal.toFixed(2)}`;
                document.getElementById("cod-fee-amount").innerText = `+฿${codFee.toFixed(2)}`;
                document.getElementById("cod-total-amount").innerText = `฿${total.toFixed(2)}`;
            }"""

if old_totals_dom in content:
    content = content.replace(old_totals_dom, new_totals_dom)
    print("Updated totals DOM in JS!")

# 6. Add COD Fee row in summary table
old_summary_shipping_row = """                        <div class="flex justify-between">
                            <span class="text-slate-500">ค่าจัดส่ง:</span>
                            <span id="checkout-shipping" class="font-bold text-emerald-700">ฟรี (฿0.00)</span>
                        </div>"""

new_summary_shipping_row = """                        <div class="flex justify-between">
                            <span class="text-slate-500">ค่าจัดส่ง:</span>
                            <span id="checkout-shipping" class="font-bold text-emerald-700">ฟรี (฿0.00)</span>
                        </div>
                        <div id="checkout-cod-fee-row" class="flex justify-between text-[#EE4D2D] hidden">
                            <span>ค่าบริการเก็บปลายทาง (COD +3%):</span>
                            <span id="checkout-cod-fee" class="font-bold">+฿0.00</span>
                        </div>"""

if old_summary_shipping_row in content:
    content = content.replace(old_summary_shipping_row, new_summary_shipping_row)
    print("Added COD Fee row in summary box!")

# 7. Update submitOrder in JS to handle COD
old_submit_validation = """            if (paymentMethod === "PROMPTPAY" && !slipImageBase64) {
                alert("กรุณาแนบสลิปหลักฐานการโอนเงินก่อนยืนยันสั่งซื้อครับ");
                return;
            }"""

new_submit_validation = """            if (paymentMethod === "PROMPTPAY" && !slipImageBase64) {
                alert("กรุณาแนบสลิปหลักฐานการโอนเงินก่อนยืนยันสั่งซื้อครับ");
                return;
            }"""

old_order_create = """            const newOrder = {
                id: orderId,
                customer_name: name,
                phone: phone,
                address: fullAddress,
                postal_code: postCode,
                shipping_provider: routing.provider,
                carrier_type: routing.carrier,
                shipping_cost: shippingCost,
                subtotal: subtotal,
                total_amount: total,
                status: "PAID",
                payment_method: paymentMethod,
                slip_image: slipImageBase64,
                items: [{
                    product_id: selectedProduct.id,
                    name: `${selectedProduct.name} (${activeV.name})`,
                    base_name: selectedProduct.name,
                    variant: activeV.name,
                    price: activeV.price,
                    quantity: quantity,
                    image: selectedProduct.image_file || selectedProduct.fallback_image
                }],
                created_at: new Date().toLocaleString("th-TH")
            };"""

new_order_create = """            const newOrder = {
                id: orderId,
                customer_name: name,
                phone: phone,
                address: fullAddress,
                postal_code: postCode,
                shipping_provider: routing.provider,
                carrier_type: routing.carrier,
                shipping_cost: shippingCost,
                subtotal: subtotal,
                cod_fee: codFee,
                total_amount: total,
                status: (paymentMethod === "COD") ? "COD_PENDING" : "PAID",
                payment_method: paymentMethod,
                slip_image: slipImageBase64,
                items: [{
                    product_id: selectedProduct.id,
                    name: `${selectedProduct.name} (${activeV.name})`,
                    base_name: selectedProduct.name,
                    variant: activeV.name,
                    price: activeV.price,
                    quantity: quantity,
                    image: selectedProduct.image_file || selectedProduct.fallback_image
                }],
                created_at: new Date().toLocaleString("th-TH")
            };"""

if old_order_create in content:
    content = content.replace(old_order_create, new_order_create)
    print("Updated order creation for COD!")

with open("/working_dir/slingshot-shop/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("index.html successfully updated with COD +3%!")
