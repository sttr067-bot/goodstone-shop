import json

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))
orders_json = json.dumps(data["orders"], ensure_ascii=False)

track_html = """<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ตรวจสอบสถานะพัสดุ - GOODSTONE</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>body { font-family: "Prompt", sans-serif; background-color: #F9F6F0; color: #2C241E; }</style>
</head>
<body class="bg-[#F9F6F0] text-[#2C241E] min-h-screen py-10 px-4 font-sans">
    <div class="max-w-2xl mx-auto space-y-6">
        <div class="text-center space-y-2">
            <div class="w-14 h-14 bg-[#FFF2EE] text-[#EE4D2D] rounded-3xl flex items-center justify-center mx-auto text-2xl shadow-inner border border-[#FFD5CC]">
                🚚
            </div>
            <h1 class="text-2xl sm:text-3xl font-black text-[#2C241E]">ตรวจสอบสถานะพัสดุ</h1>
            <p class="text-xs sm:text-sm text-slate-500">กรอกเพียงเบอร์โทรศัพท์ที่ใช้สั่งซื้อ หรือรหัสคำสั่งซื้อ</p>
        </div>

        <div class="bg-white p-5 rounded-3xl border-2 border-[#EBE3D5] shadow-sm space-y-3">
            <div class="flex gap-2">
                <input type="text" id="track-q" placeholder="ระบุเบอร์โทรศัพท์ (เช่น 0819998877) หรือ ORD-..." class="flex-grow px-4 py-3 bg-[#FAF7F2] border border-[#EBE3D5] rounded-2xl text-sm focus:ring-2 focus:ring-[#EE4D2D] focus:bg-white text-[#2C241E]">
                <button onclick="doTrack()" class="bg-[#EE4D2D] hover:bg-[#d73211] text-white font-bold px-6 py-3 rounded-2xl text-sm transition-all shadow-md active:scale-95">
                    ค้นหา
                </button>
            </div>
        </div>

        <div id="track-results-container" class="space-y-4"></div>

        <div class="text-center pt-4">
            <a href="index.html" class="text-xs font-bold text-[#EE4D2D] hover:underline">← กลับไปหน้าร้านค้าสั่งซื้อสินค้า</a>
        </div>
    </div>

    <script>
        const DEFAULT_ORDERS = """ + orders_json + """;
        function doTrack() {
            const q = document.getElementById('track-q').value.trim().replace(/[^0-9a-zA-Z-]/g, '').toLowerCase();
            const container = document.getElementById('track-results-container');
            if (!q) { alert('กรุณาระบุเบอร์โทรศัพท์ครับ'); return; }

            let orders = DEFAULT_ORDERS;
            const saved = localStorage.getItem('goodstone_orders');
            if (saved) { try { orders = JSON.parse(saved); } catch(e) {} }

            const matches = orders.filter(o => {
                const oId = (o.id || '').replace(/-/g, '').toLowerCase();
                const oPhone = (o.phone || '').replace(/-/g, '').toLowerCase();
                return oId.includes(q.replace(/-/g, '')) || oPhone.includes(q.replace(/-/g, ''));
            });

            if (matches.length === 0) {
                container.innerHTML = `<div class="bg-white p-8 rounded-3xl border-2 border-[#EBE3D5] text-center space-y-2"><span class="text-3xl">🔍</span><h3 class="font-bold text-[#2C241E]">ไม่พบคำสั่งซื้อ</h3><p class="text-xs text-slate-500">โปรดตรวจสอบเบอร์โทรศัพท์อีกครั้งครับ</p></div>`;
                return;
            }

            container.innerHTML = '';
            matches.forEach(o => {
                const isEMS = o.carrier_type === 'THAILAND_POST_EMS' || (o.shipping_provider && o.shipping_provider.includes('ไปรษณีย์'));
                const div = document.createElement('div');
                div.className = 'bg-white p-6 rounded-3xl border-2 border-[#EBE3D5] shadow-sm space-y-4';
                div.innerHTML = `
                    <div class="flex justify-between items-center pb-3 border-b border-slate-100">
                        <div>
                            <span class="text-[11px] text-slate-400">รหัสคำสั่งซื้อ</span>
                            <h3 class="text-base font-black text-[#2C241E]">${o.id}</h3>
                        </div>
                        <span class="px-3 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-300">
                            ${o.status === 'SHIPPED' ? '✓ จัดส่งแล้ว' : 'ชำระแล้ว (รอแพ็ก)'}
                        </span>
                    </div>

                    ${o.tracking_number ? `
                        <div class="bg-[#FAF7F2] border-2 border-[#EBE3D5] text-[#2C241E] p-4 rounded-2xl flex justify-between items-center">
                            <div>
                                <span class="text-xs text-slate-500">ขนส่ง: ${o.shipping_provider}</span>
                                <p class="text-lg font-mono font-black text-[#EE4D2D]">${o.tracking_number}</p>
                            </div>
                            <span class="bg-[#EE4D2D] text-white text-xs px-3 py-1.5 rounded-xl font-bold">
                                ${isEMS ? 'ไปรษณีย์ไทย EMS' : 'SPX Express'}
                            </span>
                        </div>
                    ` : `
                        <div class="bg-[#FFF5F2] text-[#2C241E] p-3.5 rounded-2xl text-xs font-medium border border-[#FFD5CC]">
                            ⏳ ร้านค้าได้รับยอดเงินเรียบร้อยแล้ว อยู่ระหว่างจัดเตรียมสินค้าและออกเลขพัสดุ
                        </div>
                    `}

                    <div class="text-xs text-slate-600 space-y-1">
                        <p><strong>ผู้รับ:</strong> ${o.customer_name} (${o.phone})</p>
                        <p><strong>ที่อยู่จัดส่ง:</strong> ${o.address}</p>
                        <div class="pt-2 border-t border-slate-100">
                            <strong>รายการสินค้า:</strong>
                            <ul class="list-disc pl-5 pt-1">
                                ${o.items.map(i => `<li>${i.name} x${i.quantity} (฿${i.price})</li>`).join('')}
                            </ul>
                        </div>
                        <div class="pt-2 flex justify-between items-center text-sm font-black text-[#2C241E] border-t border-slate-100">
                            <span>ยอดชำระสุทธิ:</span>
                            <span class="text-[#EE4D2D] text-base">฿${Number(o.total_amount).toLocaleString(undefined, {minimumFractionDigits: 2})}</span>
                        </div>
                    </div>
                `;
                container.appendChild(div);
            });
        }
    </script>
</body>
</html>"""

with open("/working_dir/slingshot-shop/track.html", "w", encoding="utf-8") as f:
    f.write(track_html)

print("slingshot-shop/track.html updated with cream theme!")
