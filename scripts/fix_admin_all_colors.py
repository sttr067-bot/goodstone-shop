import os

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\admin.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix renderOrdersView
old_render_orders = """            list.forEach(o => {
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
                        <span class="text-[10px] font-bold px-2.5 py-1 rounded-full ${o.status === 'SHIPPED' ? 'bg-emerald-50 text-emerald-700 border border-emerald-300' : o.payment_method === 'COD' || o.status === 'COD_PENDING' ? 'bg-amber-50 text-amber-800 border border-amber-300' : 'bg-orange-50 text-[#EE4D2D] border border-orange-200'}">
                            ${o.status === 'SHIPPED' ? '✓ จัดส่งแล้ว' : o.payment_method === 'COD' || o.status === 'COD_PENDING' ? '💵 COD รอส่ง' : 'ชำระแล้ว (รอแพ็ก)'}
                        </span>
                    </div>

                    <div class="text-xs app-text-main space-y-1">
                        <p><strong>ผู้รับ:</strong> ${o.customer_name} (${o.phone})</p>
                        <p class="app-text-muted text-[11px] line-clamp-1"><strong>ที่อยู่:</strong> ${o.address}</p>
                        <div class="py-1 border-t app-border-subtle">${itemsHtml}</div>
                    </div>

                    <div class="app-card-subtle p-2.5 rounded-2xl border app-border-subtle flex items-center justify-between text-xs">
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
            });"""

new_render_orders = """            list.forEach(o => {
                const isEMS = o.carrier_type === "THAILAND_POST_EMS" || (o.shipping_provider && o.shipping_provider.includes("ไปรษณีย์"));
                const itemsHtml = o.items.map(i => `<div class="text-xs app-text-main">• ${i.name} <span class="text-[#EE4D2D] font-bold">x${i.quantity}</span></div>`).join("");

                const card = document.createElement("div");
                card.className = "app-card p-4 sm:p-5 rounded-3xl border-2 app-border shadow-sm space-y-3";
                card.innerHTML = `
                    <div class="flex justify-between items-center pb-2 border-b app-border-subtle">
                        <div class="flex items-center gap-2">
                            <input type="checkbox" ${selectedOrderIds.includes(o.id) ? "checked" : ""} onchange="toggleSelectOrder('${o.id}', this)" class="rounded border-slate-300 w-4 h-4">
                            <div>
                                <span class="font-black text-sm app-text-main block">${o.id}</span>
                                <span class="text-[10px] app-text-muted">${o.created_at}</span>
                            </div>
                        </div>
                        <span class="text-[10px] font-bold px-2.5 py-1 rounded-full ${o.status === 'SHIPPED' ? 'bg-emerald-50 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-400 border border-emerald-300 dark:border-emerald-800' : o.payment_method === 'COD' || o.status === 'COD_PENDING' ? 'bg-amber-50 dark:bg-amber-950 text-amber-800 dark:text-amber-400 border border-amber-300 dark:border-amber-800' : 'bg-orange-50 dark:bg-orange-950 text-[#EE4D2D] dark:text-[#FF6E4E] border border-orange-200 dark:border-orange-900'}">
                            ${o.status === 'SHIPPED' ? '✓ จัดส่งแล้ว' : o.payment_method === 'COD' || o.status === 'COD_PENDING' ? '💵 COD รอส่ง' : 'ชำระแล้ว (รอแพ็ก)'}
                        </span>
                    </div>

                    <div class="text-xs app-text-main space-y-1">
                        <p><strong>ผู้รับ:</strong> ${o.customer_name} (${o.phone})</p>
                        <p class="app-text-muted text-[11px] line-clamp-1"><strong>ที่อยู่:</strong> ${o.address}</p>
                        <div class="py-1 border-t app-border-subtle">${itemsHtml}</div>
                    </div>

                    <div class="app-card-subtle p-2.5 rounded-2xl border app-border-subtle flex items-center justify-between text-xs">
                        <div>
                            <span class="text-[10px] px-2 py-0.5 rounded font-bold ${isEMS ? 'bg-red-50 dark:bg-red-950 text-red-600 dark:text-red-400 border border-red-200 dark:border-red-800' : 'bg-orange-50 dark:bg-orange-950 text-[#EE4D2D] dark:text-[#FF6E4E] border border-orange-200 dark:border-orange-900'}">
                                ${o.shipping_provider}
                            </span>
                            <span class="font-mono font-bold app-text-muted block text-[11px] mt-1">${o.tracking_number || '(ยังไม่ออกเลข)'}</span>
                        </div>
                        <div class="text-right">
                            <span class="text-[10px] app-text-muted block">ยอดชำระสุทธิ</span>
                            <span class="text-sm font-black text-[#EE4D2D] dark:text-[#FF6E4E]">฿${Number(o.total_amount).toLocaleString(undefined, {minimumFractionDigits: 2})}</span>
                        </div>
                    </div>

                    <div class="flex gap-2 pt-1">
                        ${o.slip_image ? `<button onclick="viewSlip('${o.id}')" class="flex-1 bg-emerald-50 dark:bg-emerald-950 hover:bg-emerald-100 dark:hover:bg-emerald-900 border border-emerald-300 dark:border-emerald-800 text-emerald-700 dark:text-emerald-400 py-1.5 rounded-xl text-xs font-bold transition-all">🧾 ดูสลิป</button>` : `<span class="flex-1 text-center text-[10px] app-text-muted py-1.5">Credit Wallet</span>`}
                        <button onclick="printSingleLabel('${o.id}')" class="flex-1 bg-[#EE4D2D] hover:bg-[#d73211] text-white py-1.5 rounded-xl text-xs font-bold shadow-sm transition-all">🖨️ พิมพ์ใบปะหน้า</button>
                    </div>
                `;
                container.appendChild(card);
            });"""

if old_render_orders in content:
    content = content.replace(old_render_orders, new_render_orders)

# Fix quickRefill buttons in renderInventoryView
content = content.replace(
    '<button onclick="quickRefill(\'${p.id}\', 10)" class="bg-[#F2EDE4] hover:bg-emerald-600 hover:text-white text-slate-700 px-2.5 py-1 rounded-lg font-bold text-xs">+10</button>',
    '<button onclick="quickRefill(\'${p.id}\', 10)" class="app-tab-inactive hover:bg-emerald-600 hover:text-white app-text-main px-2.5 py-1 rounded-lg font-bold text-xs transition-all">+10</button>'
)
content = content.replace(
    '<button onclick="quickRefill(\'${p.id}\', 50)" class="bg-[#F2EDE4] hover:bg-emerald-600 hover:text-white text-slate-700 px-2.5 py-1 rounded-lg font-bold text-xs">+50</button>',
    '<button onclick="quickRefill(\'${p.id}\', 50)" class="app-tab-inactive hover:bg-emerald-600 hover:text-white app-text-main px-2.5 py-1 rounded-lg font-bold text-xs transition-all">+50</button>'
)
content = content.replace(
    '<button onclick="quickRefill(\'${p.id}\', 100)" class="bg-[#F2EDE4] hover:bg-emerald-600 hover:text-white text-slate-700 px-2.5 py-1 rounded-lg font-bold text-xs">+100</button>',
    '<button onclick="quickRefill(\'${p.id}\', 100)" class="app-tab-inactive hover:bg-emerald-600 hover:text-white app-text-main px-2.5 py-1 rounded-lg font-bold text-xs transition-all">+100</button>'
)

# Fix Shopee box in renderInventoryView
content = content.replace(
    '<div class="bg-[#FFF5F2] p-2 rounded-xl border border-[#FFD5CC] flex items-center justify-between text-xs">',
    '<div class="app-card-subtle p-2 rounded-xl border app-border-subtle flex items-center justify-between text-xs">'
)
content = content.replace(
    '<span class="text-[10px] text-slate-600 truncate mr-2">',
    '<span class="text-[10px] app-text-muted truncate mr-2">'
)
content = content.replace(
    '<button onclick="openEditModal(\'${p.id}\')" class="w-full bg-[#2C241E] hover:bg-[#EE4D2D] text-white py-2 rounded-xl font-bold text-xs transition-all shadow-sm flex items-center justify-center gap-1 active:scale-95">',
    '<button onclick="openEditModal(\'${p.id}\')" class="w-full bg-[#EE4D2D] hover:bg-[#d73211] text-white py-2 rounded-xl font-bold text-xs transition-all shadow-sm flex items-center justify-center gap-1 active:scale-95">'
)

# Fix Slip Modal
content = content.replace(
    '<div class="bg-white rounded-3xl border-2 border-[#EBE3D5] max-w-sm w-full p-4 space-y-3 shadow-2xl">',
    '<div class="app-card rounded-3xl border-2 app-border max-w-sm w-full p-4 space-y-3 shadow-2xl">'
)
content = content.replace(
    '<h4 id="slip-modal-title" class="text-xs sm:text-sm font-bold text-[#2C241E]">สลิปโอนเงิน</h4>',
    '<h4 id="slip-modal-title" class="text-xs sm:text-sm font-bold app-text-main">สลิปโอนเงิน</h4>'
)
content = content.replace(
    '<div class="max-h-[55vh] overflow-y-auto flex items-center justify-center bg-[#FAF7F2] rounded-2xl p-2 border border-[#EBE3D5]">',
    '<div class="max-h-[55vh] overflow-y-auto flex items-center justify-center app-card-subtle rounded-2xl p-2 border app-border-subtle">'
)
content = content.replace(
    '<div id="slip-modal-info" class="text-xs text-slate-700 space-y-1 bg-[#FFF5F2] p-2.5 rounded-2xl border border-[#FFD5CC]"></div>',
    '<div id="slip-modal-info" class="text-xs app-text-main space-y-1 app-card-subtle p-2.5 rounded-2xl border app-border-subtle"></div>'
)

# Remove duplicate printSingleLabel function if exists
if "function printSingleLabel(id) {\n            const o = orders.find(x => x.id === id);\n            if (o) printLabels([o]);\n        }\n\n        function printSingleLabel(id) {" in content:
    content = content.replace(
        "function printSingleLabel(id) {\n            const o = orders.find(x => x.id === id);\n            if (o) printLabels([o]);\n        }\n\n        function printSingleLabel(id) {\n            const o = orders.find(x => x.id === id);\n            if (o) printLabels([o]);\n        }",
        "function printSingleLabel(id) {\n            const o = orders.find(x => x.id === id);\n            if (o) printLabels([o]);\n        }"
    )

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated renderOrdersView and all sub-card colors successfully!")
