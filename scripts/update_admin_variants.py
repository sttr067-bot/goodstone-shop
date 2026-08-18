import json

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))
products_json = json.dumps(data["products"], ensure_ascii=False)
orders_json = json.dumps(data["orders"], ensure_ascii=False)

with open("/working_dir/slingshot-shop/admin.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update DEFAULT_PRODUCTS in admin.html
start_m = "const DEFAULT_PRODUCTS = "
end_m = ";\n        const DEFAULT_ORDERS ="
s_idx = html.find(start_m)
e_idx = html.find(end_m)
if s_idx != -1 and e_idx != -1:
    html = html[:s_idx + len(start_m)] + products_json + html[e_idx:]

# Replace the modal content with the interactive variant table
old_modal_body = """                <div>
                    <label class="block text-xs font-semibold text-slate-300 mb-1">
                        ตัวเลือก / สเปกสินค้า (คั่นแต่ละตัวเลือกด้วยเครื่องหมายจุลภาค ,)
                    </label>
                    <textarea id="edit-prod-variants" rows="3" placeholder="เช่น หนา 0.65mm, หนา 0.75mm, หนา 0.80mm" class="w-full bg-slate-800 border border-slate-600 rounded-xl px-3 py-2 text-xs text-white focus:ring-2 focus:ring-amber-500"></textarea>
                    <span class="text-[10px] text-slate-400">ระบุราคาเสริมในวงเล็บได้ เช่น: ครบชุดพร้อมเลเซอร์ (฿550), เฉพาะด้าม (฿390)</span>
                </div>"""

new_modal_body = """                <!-- Interactive Variant Rows System -->
                <div class="space-y-2 pt-2 border-t border-slate-700">
                    <div class="flex items-center justify-between">
                        <div>
                            <label class="block text-xs font-bold text-amber-400">ตัวเลือกสเปกสินค้า & ตั้งราคาแยกตามตัวเลือก</label>
                            <span class="text-[10px] text-slate-400">เพิ่ม/ลดแถวตัวเลือก และกำหนดราคา + สต็อกของแต่ละตัวเลือกได้อิสระ</span>
                        </div>
                        <button type="button" onclick="addVariantRow()" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs px-2.5 py-1.5 rounded-lg flex items-center gap-1 shadow-sm active:scale-95">
                            <i data-lucide="plus" class="w-3.5 h-3.5"></i> เพิ่มตัวเลือก
                        </button>
                    </div>

                    <!-- Variant Table Header -->
                    <div class="grid grid-cols-12 gap-2 text-[11px] font-bold text-slate-400 px-2 py-1 bg-slate-950 rounded-lg">
                        <div class="col-span-6">ชื่อตัวเลือก / สเปก</div>
                        <div class="col-span-3">ราคา (บาท)</div>
                        <div class="col-span-2">สต็อก (ชิ้น)</div>
                        <div class="col-span-1 text-center">ลบ</div>
                    </div>

                    <!-- Dynamic Variant Rows Container -->
                    <div id="variant-rows-container" class="space-y-2 max-h-48 overflow-y-auto pr-1">
                        <!-- Populated by JS -->
                    </div>
                </div>"""

if old_modal_body in html:
    html = html.replace(old_modal_body, new_modal_body)

# Replace JS logic for modal
old_js_modal_funcs = """        function openProductModal() {
            document.getElementById('edit-prod-id').value = "";
            document.getElementById('product-modal-title').innerText = "+ เพิ่มสินค้าใหม่ในร้าน";
            document.getElementById('edit-prod-name').value = "";
            document.getElementById('edit-prod-cat').value = "slingshot";
            document.getElementById('edit-prod-price').value = "100";
            document.getElementById('edit-prod-stock').value = "50";
            document.getElementById('edit-prod-variants').value = "รุ่นมาตรฐาน, รุ่นโปรโมชัน";
            document.getElementById('edit-prod-desc').value = "";
            document.getElementById('product-modal').classList.remove('hidden');
        }

        function editProductModal(productId) {
            const prod = products.find(p => p.id === productId);
            if (!prod) return;

            document.getElementById('edit-prod-id').value = prod.id;
            document.getElementById('product-modal-title').innerText = `✏️ แก้ไขสินค้า: ${prod.name}`;
            document.getElementById('edit-prod-name').value = prod.name;
            document.getElementById('edit-prod-cat').value = prod.category || "slingshot";
            document.getElementById('edit-prod-price').value = prod.price;
            document.getElementById('edit-prod-stock').value = prod.stock;
            document.getElementById('edit-prod-variants').value = (prod.variants || []).join(", ");
            document.getElementById('edit-prod-desc').value = prod.description || "";
            document.getElementById('product-modal').classList.remove('hidden');
        }

        function closeProductModal() {
            document.getElementById('product-modal').classList.add('hidden');
        }

        function saveProductModal() {
            const id = document.getElementById('edit-prod-id').value;
            const name = document.getElementById('edit-prod-name').value.trim();
            const cat = document.getElementById('edit-prod-cat').value;
            const price = parseFloat(document.getElementById('edit-prod-price').value) || 0;
            const stock = parseInt(document.getElementById('edit-prod-stock').value) || 0;
            const variantsStr = document.getElementById('edit-prod-variants').value;
            const desc = document.getElementById('edit-prod-desc').value.trim();

            if (!name || price <= 0) {
                alert('กรุณากรอกชื่อสินค้าและราคาให้ถูกต้องครับ');
                return;
            }

            const variantsList = variantsStr.split(",").map(s => s.trim()).filter(s => s.length > 0);

            if (id) {
                const prod = products.find(p => p.id === id);
                if (prod) {
                    prod.name = name;
                    prod.category = cat;
                    prod.price = price;
                    prod.stock = stock;
                    prod.variants = variantsList;
                    prod.description = desc;
                }
            } else {
                const newId = `PROD-${String(products.length + 1).padStart(3, '0')}`;
                products.push({
                    id: newId,
                    name: name,
                    category: cat,
                    price: price,
                    stock: stock,
                    variants: variantsList,
                    description: desc,
                    fallback_image: DEFAULT_PRODUCTS[0].fallback_image
                });
            }

            localStorage.setItem('goodstone_products', JSON.stringify(products));
            alert('💾 บันทึกข้อมูลสินค้าและสต็อกเรียบร้อยแล้วครับ!');
            closeProductModal();
            renderAdminProducts();
            updateInventoryStats();
        }"""

new_js_modal_funcs = """        // ================= DYNAMIC VARIANT ROW SYSTEM =================
        function addVariantRow(name = "", price = 100, stock = 20) {
            const container = document.getElementById("variant-rows-container");
            const div = document.createElement("div");
            div.className = "variant-row grid grid-cols-12 gap-2 items-center bg-slate-950 p-2 rounded-xl border border-slate-700";
            div.innerHTML = `
                <div class="col-span-6">
                    <input type="text" value="${name}" placeholder="เช่น หนา 0.75mm" class="v-name w-full bg-slate-800 border border-slate-600 rounded-lg px-2.5 py-1.5 text-xs text-white focus:ring-1 focus:ring-amber-500">
                </div>
                <div class="col-span-3">
                    <input type="number" value="${price}" step="1" placeholder="ราคา" oninput="recalcModalSummary()" class="v-price w-full bg-slate-800 border border-slate-600 rounded-lg px-2.5 py-1.5 text-xs text-amber-400 font-bold focus:ring-1 focus:ring-amber-500">
                </div>
                <div class="col-span-2">
                    <input type="number" value="${stock}" min="0" placeholder="สต็อก" oninput="recalcModalSummary()" class="v-stock w-full bg-slate-800 border border-slate-600 rounded-lg px-2 py-1.5 text-xs text-white font-bold focus:ring-1 focus:ring-amber-500">
                </div>
                <div class="col-span-1 text-center">
                    <button type="button" onclick="removeVariantRow(this)" class="text-red-400 hover:text-red-300 p-1 rounded transition-colors" title="ลบตัวเลือกนี้">
                        <i data-lucide="trash-2" class="w-4 h-4"></i>
                    </button>
                </div>
            `;
            container.appendChild(div);
            lucide.createIcons();
            recalcModalSummary();
        }

        function removeVariantRow(btn) {
            const row = btn.closest(".variant-row");
            if (row) {
                row.remove();
                recalcModalSummary();
            }
        }

        function recalcModalSummary() {
            const rows = document.querySelectorAll(".variant-row");
            if (rows.length === 0) return;

            let totalStock = 0;
            let minPrice = Infinity;

            rows.forEach(r => {
                const p = parseFloat(r.querySelector(".v-price")?.value) || 0;
                const s = parseInt(r.querySelector(".v-stock")?.value) || 0;
                totalStock += s;
                if (p > 0 && p < minPrice) minPrice = p;
            });

            if (minPrice !== Infinity) {
                document.getElementById("edit-prod-price").value = minPrice;
            }
            document.getElementById("edit-prod-stock").value = totalStock;
        }

        function openProductModal() {
            document.getElementById('edit-prod-id').value = "";
            document.getElementById('product-modal-title').innerText = "+ เพิ่มสินค้าใหม่ในร้าน";
            document.getElementById('edit-prod-name').value = "";
            document.getElementById('edit-prod-cat').value = "slingshot";
            document.getElementById('edit-prod-price').value = "100";
            document.getElementById('edit-prod-stock').value = "30";
            document.getElementById('edit-prod-desc').value = "";
            
            const container = document.getElementById("variant-rows-container");
            container.innerHTML = "";
            addVariantRow("รุ่นมาตรฐาน", 100, 20);
            addVariantRow("รุ่นโปรโมชัน", 150, 10);
            
            document.getElementById('product-modal').classList.remove('hidden');
        }

        function editProductModal(productId) {
            const prod = products.find(p => p.id === productId);
            if (!prod) return;

            document.getElementById('edit-prod-id').value = prod.id;
            document.getElementById('product-modal-title').innerText = `✏️ แก้ไขสินค้า: ${prod.name}`;
            document.getElementById('edit-prod-name').value = prod.name;
            document.getElementById('edit-prod-cat').value = prod.category || "slingshot";
            document.getElementById('edit-prod-price').value = prod.price;
            document.getElementById('edit-prod-stock').value = prod.stock;
            document.getElementById('edit-prod-desc').value = prod.description || "";

            const container = document.getElementById("variant-rows-container");
            container.innerHTML = "";

            if (prod.variants && prod.variants.length > 0) {
                prod.variants.forEach(v => {
                    const vName = typeof v === "object" ? v.name : v;
                    const vPrice = typeof v === "object" ? v.price : prod.price;
                    const vStock = typeof v === "object" ? v.stock : Math.floor(prod.stock / prod.variants.length);
                    addVariantRow(vName, vPrice, vStock);
                });
            } else {
                addVariantRow("รุ่นมาตรฐาน", prod.price, prod.stock);
            }

            document.getElementById('product-modal').classList.remove('hidden');
        }

        function closeProductModal() {
            document.getElementById('product-modal').classList.add('hidden');
        }

        function saveProductModal() {
            const id = document.getElementById('edit-prod-id').value;
            const name = document.getElementById('edit-prod-name').value.trim();
            const cat = document.getElementById('edit-prod-cat').value;
            const desc = document.getElementById('edit-prod-desc').value.trim();

            const rows = document.querySelectorAll(".variant-row");
            const variants = [];
            let totalStock = 0;
            let minPrice = Infinity;

            rows.forEach(r => {
                const vName = r.querySelector(".v-name")?.value.trim();
                const vPrice = parseFloat(r.querySelector(".v-price")?.value) || 0;
                const vStock = parseInt(r.querySelector(".v-stock")?.value) || 0;

                if (vName && vPrice > 0) {
                    variants.push({
                        name: vName,
                        price: vPrice,
                        stock: vStock
                    });
                    totalStock += vStock;
                    if (vPrice < minPrice) minPrice = vPrice;
                }
            });

            if (!name || variants.length === 0) {
                alert('กรุณากรอกชื่อสินค้า และระบุตัวเลือกสินค้าอย่างน้อย 1 รายการพร้อมราคาครับ');
                return;
            }

            const basePrice = minPrice === Infinity ? parseFloat(document.getElementById('edit-prod-price').value) : minPrice;

            if (id) {
                const prod = products.find(p => p.id === id);
                if (prod) {
                    prod.name = name;
                    prod.category = cat;
                    prod.price = basePrice;
                    prod.stock = totalStock;
                    prod.variants = variants;
                    prod.description = desc;
                }
            } else {
                const newId = `PROD-${String(products.length + 1).padStart(3, '0')}`;
                products.push({
                    id: newId,
                    name: name,
                    category: cat,
                    price: basePrice,
                    stock: totalStock,
                    variants: variants,
                    description: desc,
                    fallback_image: DEFAULT_PRODUCTS[0].fallback_image
                });
            }

            localStorage.setItem('goodstone_products', JSON.stringify(products));
            alert('💾 บันทึกข้อมูลตัวเลือก ราคา และสต็อกเรียบร้อยแล้วครับ!');
            closeProductModal();
            renderAdminProducts();
            updateInventoryStats();
        }"""

if old_js_modal_funcs in html:
    html = html.replace(old_js_modal_funcs, new_js_modal_funcs)

# Update inventory table variant rendering
old_var_render = """                const variantsTags = (p.variants && p.variants.length > 0)
                    ? p.variants.map(v => `<span class="inline-block bg-slate-900 border border-slate-700 px-2 py-0.5 rounded text-[11px] text-slate-300 mr-1 mb-1">${v}</span>`).join('')
                    : `<span class="text-xs text-slate-500">รุ่นมาตรฐาน</span>`;"""

new_var_render = """                const variantsTags = (p.variants && p.variants.length > 0)
                    ? p.variants.map(v => {
                        const vName = typeof v === "object" ? v.name : v;
                        const vPrice = typeof v === "object" ? v.price : p.price;
                        const vStock = typeof v === "object" ? v.stock : "";
                        return `<span class="inline-block bg-slate-950 border border-slate-700 px-2 py-1 rounded-lg text-xs text-slate-200 mr-1 mb-1 shadow-sm">
                            <strong>${vName}</strong> <span class="text-amber-400 font-bold">(฿${vPrice})</span> <span class="text-[10px] text-slate-400 font-mono">[${vStock}ชิ้น]</span>
                        </span>`;
                    }).join('')
                    : `<span class="text-xs text-slate-500">รุ่นมาตรฐาน (฿${p.price})</span>`;"""

if old_var_render in html:
    html = html.replace(old_var_render, new_var_render)

with open("/working_dir/slingshot-shop/admin.html", "w", encoding="utf-8") as f:
    f.write(html)

print("admin.html updated with interactive Variant Table rows and per-variant pricing!")
