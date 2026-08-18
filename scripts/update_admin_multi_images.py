import json

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))
products_json = json.dumps(data["products"], ensure_ascii=False)
orders_json = json.dumps(data["orders"], ensure_ascii=False)

with open("/working_dir/slingshot-shop/admin.html", "r", encoding="utf-8") as f:
    admin_content = f.read()

# Replace the single image uploader with the Multi-Image Gallery Manager
old_img_section = """                <!-- Product Image Uploader -->
                <div class="bg-slate-950 p-3 rounded-xl border border-slate-700 space-y-2">
                    <label class="block text-xs font-bold text-amber-400">🖼️ อัปโหลดรูปภาพสินค้าจากเครื่อง:</label>
                    <div class="flex items-center gap-3">
                        <div class="w-14 h-14 bg-slate-900 rounded-lg border border-slate-700 p-0.5 flex items-center justify-center overflow-hidden flex-shrink-0">
                            <img id="edit-prod-img-preview" src="" class="w-full h-full object-contain">
                        </div>
                        <div class="space-y-1">
                            <input type="file" id="edit-prod-img-file" accept="image/*" onchange="handleProductImageUpload(this)" class="text-xs text-slate-300 file:mr-2 file:py-1 file:px-2.5 file:rounded-lg file:border-0 file:text-xs file:font-bold file:bg-amber-500 file:text-slate-950 hover:file:bg-amber-400 cursor-pointer">
                            <div class="text-[10px] text-slate-400">เลือกรูปจากคอม/แท็บเล็ตได้ทันที ระบบจะนำไปโชว์ที่หน้าร้านทันที</div>
                        </div>
                    </div>
                </div>"""

new_img_section = """                <!-- Multi-Image Gallery Manager (อัปโหลดได้หลายรูป ไม่จำกัด) -->
                <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-700 space-y-2.5">
                    <div class="flex items-center justify-between">
                        <div>
                            <label class="block text-xs font-bold text-amber-400">🖼️ รูปภาพสินค้า (เพิ่มได้หลายรูป ไม่จำกัด):</label>
                            <span class="text-[10px] text-slate-400">รูปแรกคือรูปหน้าปก แตะเครื่องหมาย ✕ เพื่อลบรูป หรือกดเพิ่มรูปใหม่</span>
                        </div>
                        <button type="button" onclick="document.getElementById('edit-prod-imgs-file').click()" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs px-3 py-1.5 rounded-lg flex items-center gap-1.5 shadow-sm active:scale-95 cursor-pointer">
                            <i data-lucide="plus-circle" class="w-3.5 h-3.5"></i> + เพิ่มรูปภาพ
                        </button>
                        <input type="file" id="edit-prod-imgs-file" multiple accept="image/*" class="hidden" onchange="handleMultiImageUpload(this)">
                    </div>

                    <!-- Images Grid -->
                    <div id="edit-prod-imgs-grid" class="grid grid-cols-4 sm:grid-cols-5 gap-2 max-h-44 overflow-y-auto p-1 bg-slate-900 rounded-xl border border-slate-800">
                        <!-- Populated dynamically -->
                    </div>
                    <div id="edit-prod-imgs-count" class="text-[11px] text-amber-400 font-medium text-right">0 รูปภาพ</div>
                </div>"""

if old_img_section in admin_content:
    admin_content = admin_content.replace(old_img_section, new_img_section)

# Replace the single image JS functions with Multi-Image JS functions
old_img_js = """        let currentEditingImageBase64 = null;

        function handleProductImageUpload(input) {
            const file = input.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = function(e) {
                currentEditingImageBase64 = e.target.result;
                document.getElementById('edit-prod-img-preview').src = currentEditingImageBase64;
            };
            reader.readAsDataURL(file);
        }

        function openProductModal() {
            currentEditingImageBase64 = null;
            document.getElementById('edit-prod-id').value = "";
            document.getElementById('edit-prod-img-preview').src = DEFAULT_PRODUCTS[0].fallback_image;
            document.getElementById('edit-prod-img-file').value = "";"""

new_img_js = """        let editingProductImages = [];

        function renderEditingImagesGrid() {
            const grid = document.getElementById("edit-prod-imgs-grid");
            grid.innerHTML = "";

            if (editingProductImages.length === 0) {
                grid.innerHTML = `<div class="col-span-full py-6 text-center text-slate-500 text-xs">ยังไม่มีรูปภาพ กดปุ่ม "+ เพิ่มรูปภาพ" เพื่ออัปโหลด</div>`;
                document.getElementById("edit-prod-imgs-count").innerText = "0 รูปภาพ";
                return;
            }

            document.getElementById("edit-prod-imgs-count").innerText = `${editingProductImages.length} รูปภาพ (รูปที่ 1 คือรูปหน้าปก)`;

            editingProductImages.forEach((img, idx) => {
                const div = document.createElement("div");
                const isCover = (idx === 0);
                div.className = `relative group h-20 bg-slate-950 rounded-lg border-2 p-1 flex items-center justify-center overflow-hidden ${isCover ? 'border-amber-400 ring-2 ring-amber-400/30' : 'border-slate-700'}`;
                
                div.innerHTML = `
                    <img src="${img.file || img.fallback}" onerror="this.onerror=null; this.src='${img.fallback || DEFAULT_PRODUCTS[0].fallback_image}';" class="w-full h-full object-contain">
                    ${isCover ? '<span class="absolute bottom-1 left-1 bg-amber-500 text-slate-950 text-[9px] px-1 rounded font-black">หน้าปก</span>' : ''}
                    <button type="button" onclick="removeEditingImage(${idx})" class="absolute top-1 right-1 bg-red-600 hover:bg-red-500 text-white rounded-full p-0.5 shadow-md transition-all active:scale-90" title="ลบรูปนี้">
                        <i data-lucide="x" class="w-3 h-3"></i>
                    </button>
                `;
                grid.appendChild(div);
            });
            lucide.createIcons();
        }

        function handleMultiImageUpload(input) {
            const files = Array.from(input.files);
            if (files.length === 0) return;

            let loadedCount = 0;
            files.forEach(file => {
                const reader = new FileReader();
                reader.onload = function(e) {
                    editingProductImages.push({
                        file: e.target.result,
                        name: file.name,
                        fallback: e.target.result
                    });
                    loadedCount++;
                    if (loadedCount === files.length) {
                        renderEditingImagesGrid();
                    }
                };
                reader.readAsDataURL(file);
            });
            input.value = "";
        }

        function removeEditingImage(idx) {
            editingProductImages.splice(idx, 1);
            renderEditingImagesGrid();
        }

        function openProductModal() {
            editingProductImages = [{
                file: DEFAULT_PRODUCTS[0].fallback_image,
                name: "รูปตัวอย่าง",
                fallback: DEFAULT_PRODUCTS[0].fallback_image
            }];
            renderEditingImagesGrid();
            document.getElementById('edit-prod-id').value = "";"""

if old_img_js in admin_content:
    admin_content = admin_content.replace(old_img_js, new_img_js)

old_edit_populate_js2 = """            currentEditingImageBase64 = null;
            document.getElementById('edit-prod-id').value = prod.id;
            document.getElementById('product-modal-title').innerText = `✏️ แก้ไขสินค้า: ${prod.name}`;
            document.getElementById('edit-prod-img-preview').src = prod.image_file || prod.fallback_image;
            document.getElementById('edit-prod-img-file').value = "";"""

new_edit_populate_js2 = """            document.getElementById('edit-prod-id').value = prod.id;
            document.getElementById('product-modal-title').innerText = `✏️ แก้ไขสินค้า: ${prod.name}`;

            if (prod.images && prod.images.length > 0) {
                editingProductImages = JSON.parse(JSON.stringify(prod.images));
            } else {
                editingProductImages = [{
                    file: prod.image_file || prod.fallback_image,
                    name: `${prod.id}_main.jpg`,
                    fallback: prod.fallback_image
                }];
            }
            renderEditingImagesGrid();"""

if old_edit_populate_js2 in admin_content:
    admin_content = admin_content.replace(old_edit_populate_js2, new_edit_populate_js2)

# Update saveProductModal
old_save_multi_img_js = """                    if (currentEditingImageBase64) {
                        prod.image_file = currentEditingImageBase64;
                        prod.fallback_image = currentEditingImageBase64;
                        if (!prod.images) prod.images = [];
                        prod.images.unshift({
                            file: currentEditingImageBase64,
                            name: `${prod.id}_custom.jpg (ภาพที่อัปโหลด)`,
                            fallback: currentEditingImageBase64
                        });
                    }"""

new_save_multi_img_js = """                    prod.images = editingProductImages.length > 0 ? editingProductImages : [{
                        file: prod.fallback_image,
                        name: "รูปหลัก",
                        fallback: prod.fallback_image
                    }];
                    prod.image_file = prod.images[0].file;
                    prod.fallback_image = prod.images[0].fallback || prod.images[0].file;"""

if old_save_multi_img_js in admin_content:
    admin_content = admin_content.replace(old_save_multi_img_js, new_save_multi_img_js)

old_new_prod_save = """                products.push({
                    id: newId,
                    name: name,
                    category: cat,
                    price: basePrice,
                    stock: totalStock,
                    variants: variants,
                    description: desc,
                    fallback_image: DEFAULT_PRODUCTS[0].fallback_image
                });"""

new_new_prod_save = """                const imgsToSave = editingProductImages.length > 0 ? editingProductImages : [{
                    file: DEFAULT_PRODUCTS[0].fallback_image,
                    name: "รูปหลัก",
                    fallback: DEFAULT_PRODUCTS[0].fallback_image
                }];
                products.push({
                    id: newId,
                    name: name,
                    category: cat,
                    price: basePrice,
                    stock: totalStock,
                    variants: variants,
                    description: desc,
                    image_file: imgsToSave[0].file,
                    fallback_image: imgsToSave[0].fallback || imgsToSave[0].file,
                    images: imgsToSave
                });"""

if old_new_prod_save in admin_content:
    admin_content = admin_content.replace(old_new_prod_save, new_new_prod_save)

with open("/working_dir/slingshot-shop/admin.html", "w", encoding="utf-8") as f:
    f.write(admin_content)

print("admin.html updated with Multi-Image Gallery Uploader!")
