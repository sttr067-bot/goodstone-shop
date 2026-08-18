import json

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))

# Check orders data to ensure sample orders have correct matching postal codes
for o in data["orders"]:
    if "10270" in o.get("address", ""):
        o["postal_code"] = "10270"

with open("/working_dir/slingshot-shop/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("/working_dir/slingshot-shop/admin.html", "r", encoding="utf-8") as f:
    admin_content = f.read()

# Replace printLabels in admin.html with real JsBarcode + QR Code implementation
old_print_function_start = "        function printLabels(targetList) {"
old_print_function_end = "        window.onload = init;"

new_print_function = """        function printSingleLabel(id) {
            const o = orders.find(x => x.id === id);
            if (o) printLabels([o]);
        }

        function extractPostcode(order) {
            if (order.postal_code && order.postal_code.trim().length === 5) return order.postal_code.trim();
            const match = (order.address || "").match(/\\b\\d{5}\\b/);
            return match ? match[0] : (order.postal_code || "10150");
        }

        function printLabels(targetList) {
            const targetOrders = targetList || (selectedOrderIds.length > 0 ? orders.filter(o => selectedOrderIds.includes(o.id)) : orders.filter(o => o.status === "PAID" || o.status === "SHIPPED"));
            if (targetOrders.length === 0) { alert("กรุณาเลือกออเดอร์ก่อนครับ"); return; }

            const labelsHtml = targetOrders.map((o, index) => {
                const barcodeNum = o.tracking_number || o.id;
                const isEMS = o.carrier_type === "THAILAND_POST_EMS" || (o.shipping_provider && o.shipping_provider.includes("ไปรษณีย์"));
                const carrierName = isEMS ? "THAILAND POST (EMS)" : "SPX EXPRESS";
                const badgeText = isEMS ? "EMS ด่วนพิเศษ" : "SPX STANDARD";
                const recipientPostcode = extractPostcode(o);

                const itemsRows = o.items.map((i, idx) => `
                    <tr style="border-bottom: 1px dashed #ccc;">
                        <td style="padding: 2px 4px; text-align: center; font-size: 10px;">${idx+1}</td>
                        <td style="padding: 2px 4px; font-weight: bold; font-size: 10.5px;">${i.name}</td>
                        <td style="padding: 2px 4px; text-align: center; font-weight: bold; font-size: 12px;">x${i.quantity}</td>
                    </tr>
                `).join("");

                return `
                <div class="label-page">
                    <!-- 1. Header -->
                    <div class="label-header">
                        <div class="carrier-name">${carrierName}</div>
                        <div class="header-right">
                            <div class="delivery-type">${badgeText}</div>
                            <div class="cod-tag">ชำระแล้ว (NON-COD)</div>
                        </div>
                    </div>

                    <!-- 2. Real Scannable Barcode (Code 128) & 2D QR Code Row -->
                    <div class="barcode-qr-row">
                        <div class="barcode-col">
                            <svg id="barcode-svg-${index}" class="barcode-svg" jsbarcode-format="CODE128" jsbarcode-value="${barcodeNum}" jsbarcode-text="${barcodeNum}" jsbarcode-width="1.8" jsbarcode-height="40" jsbarcode-fontsize="13" jsbarcode-font="monospace" jsbarcode-margin="2"></svg>
                            <div class="order-ref-text">Order ID: ${o.id} | วันที่: ${o.created_at}</div>
                        </div>
                        <div class="qr-col">
                            <img src="https://api.qrserver.com/v1/create-qr-code/?size=95x95&margin=0&data=${encodeURIComponent(barcodeNum)}" class="qr-img" alt="QR">
                            <span class="qr-subtext">SCAN QR</span>
                        </div>
                    </div>

                    <!-- 3. Receiver Section (TO) -->
                    <div class="address-section receiver-section">
                        <div class="to-header">
                            <span class="to-label">ผู้รับ (TO):</span>
                            <span class="to-name">${o.customer_name}</span>
                        </div>
                        <div class="to-phone">โทร: ${o.phone}</div>
                        <div class="to-address">${o.address}</div>
                        <div class="postal-box">${recipientPostcode}</div>
                    </div>

                    <!-- 4. Sender Section (FROM) -->
                    <div class="address-section sender-section">
                        <span class="from-label">ผู้ส่ง (FROM):</span> <strong>GOODSTONE SHOP</strong> (คุณสุเมธา แท่นธรรมโรจน์ โทร. 061-537-2239)<br>
                        123/45 ถนนพระราม 2 แขวงท่าข้าม เขตบางขุนเทียน กรุงเทพฯ 10150
                    </div>

                    <!-- 5. Packing List Section -->
                    <div class="packing-list-section">
                        <div class="packing-title">📦 รายการสินค้าในพัสดุ (PACKING LIST):</div>
                        <table class="packing-table">
                            <thead>
                                <tr style="background: #f0f0f0; border-bottom: 1px solid #000;">
                                    <th style="width: 25px; padding: 2px; text-align: center;">#</th>
                                    <th style="text-align: left; padding: 2px 4px;">ชื่อสินค้า / สเปก</th>
                                    <th style="width: 40px; padding: 2px; text-align: center;">จำนวน</th>
                                </tr>
                            </thead>
                            <tbody>${itemsRows}</tbody>
                        </table>
                    </div>

                    <!-- 6. Footer -->
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
                <!-- JsBarcode Library for Real Scannable Barcode Generation -->
                <script src="https://cdn.jsdelivr.net/npm/jsbarcode@3.11.6/dist/JsBarcode.all.min.js"><\\/script>
                <style>
                    * { box-sizing: border-box; margin: 0; padding: 0; }
                    body { font-family: sans-serif; background: #333; color: #000; padding: 10px 0; }
                    .print-toolbar { max-width: 100mm; margin: 0 auto 15px auto; display: flex; gap: 10px; justify-content: space-between; align-items: center; background: #fff; padding: 10px 15px; border-radius: 8px; }
                    .print-btn { background: #EE4D2D; color: #fff; border: none; padding: 8px 18px; font-weight: bold; font-size: 14px; border-radius: 6px; cursor: pointer; }
                    .close-btn { background: #e2e8f0; color: #1e293b; border: none; padding: 8px 14px; font-weight: bold; font-size: 14px; border-radius: 6px; cursor: pointer; }
                    
                    /* 4x6 inch / 100x150mm Label Page */
                    .label-page { width: 100mm; height: 146mm; margin: 0 auto 15mm auto; padding: 4.5mm; background: #fff; border: 2px solid #000; display: flex; flex-direction: column; justify-content: space-between; page-break-after: always; position: relative; }
                    .label-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #000; padding-bottom: 3px; }
                    .carrier-name { font-size: 17px; font-weight: 900; }
                    .header-right { text-align: right; }
                    .delivery-type { background: #000; color: #fff; padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: 900; }
                    .cod-tag { font-size: 10px; font-weight: bold; color: #047857; margin-top: 1px; }
                    
                    /* Barcode & QR Code Row */
                    .barcode-qr-row { display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #000; padding: 4px 0; gap: 4px; }
                    .barcode-col { flex-grow: 1; text-align: center; }
                    .barcode-svg { max-width: 100%; height: auto; display: block; margin: 0 auto; }
                    .order-ref-text { font-size: 8.5px; color: #444; font-family: sans-serif; margin-top: 1px; }
                    .qr-col { width: 75px; text-align: center; border-left: 1.5px dashed #000; padding-left: 4px; flex-shrink: 0; }
                    .qr-img { width: 68px; height: 68px; object-contain; display: block; margin: 0 auto; }
                    .qr-subtext { font-size: 7.5px; font-weight: 900; font-family: sans-serif; letter-spacing: 0.5px; }

                    /* Addresses */
                    .address-section { border-bottom: 1.5px solid #000; padding: 4px 0; font-size: 10.5px; line-height: 1.3; }
                    .receiver-section { background: #fafafa; padding: 4px; position: relative; }
                    .to-header { display: flex; align-items: baseline; gap: 5px; }
                    .to-label { font-weight: 900; font-size: 11.5px; }
                    .to-name { font-size: 12.5px; font-weight: 900; }
                    .to-phone { font-size: 12.5px; font-weight: 900; margin: 1px 0; }
                    .to-address { font-size: 10px; padding-right: 55px; line-height: 1.25; }
                    .postal-box { position: absolute; right: 4px; top: 8px; border: 2px solid #000; padding: 2px 5px; font-size: 14px; font-weight: 900; font-family: monospace; background: #fff; }
                    .sender-section { font-size: 9px; color: #333; }
                    .from-label { font-weight: bold; color: #000; }

                    /* Packing List */
                    .packing-list-section { flex-grow: 1; padding-top: 3px; }
                    .packing-title { font-size: 9px; font-weight: 800; margin-bottom: 2px; }
                    .packing-table { width: 100%; border-collapse: collapse; font-size: 9px; }
                    
                    /* Footer */
                    .label-footer { border-top: 1.5px solid #000; padding-top: 2.5px; display: flex; justify-content: space-between; font-size: 8px; }

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
                    <span style="font-size: 13px; font-weight: bold;">🖨️ ใบปะหน้าพร้อมบาร์โค้ด & QR สแกนได้ (${targetOrders.length} รายการ)</span>
                    <div style="display: flex; gap: 8px;">
                        <button onclick="window.print()" class="print-btn">สั่งพิมพ์ทันที (Print)</button>
                        <button onclick="window.close()" class="close-btn">ปิด</button>
                    </div>
                </div>
                ${labelsHtml}
                <script>
                    window.onload = function() {
                        // Render all Real Barcodes (Code 128)
                        if (window.JsBarcode) {
                            JsBarcode(".barcode-svg").init();
                        }
                        setTimeout(() => window.print(), 600);
                    };
                <\\/script>
            </body>
            </html>`;

            const win = window.open("", "_blank");
            if (win) {
                win.document.open();
                win.document.write(printHtml);
                win.document.close();
            }
        }
"""

if old_print_function_start in admin_content:
    parts = admin_content.split(old_print_function_start)
    prefix = parts[0]
    suffix_parts = parts[1].split(old_print_function_end)
    suffix = "        window.onload = init;" + suffix_parts[1]
    admin_content = prefix + new_print_function + "\n" + suffix

with open("/working_dir/slingshot-shop/admin.html", "w", encoding="utf-8") as f:
    f.write(admin_content)

print("admin.html updated with real scannable Barcode & QR Code!")
