import os, json

index_html_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\index.html"
admin_html_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\admin.html"

with open(index_html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update fetchProducts in index.html to read from localStorage first (syncing real-time with admin changes)
old_fetch_js = """        function fetchProducts() {
            fetch("data.json")
                .then(res => res.json())
                .then(data => {
                    if (data && data.products && data.products.length > 0) {
                        products = data.products;
                    }
                    renderCatalogGrid();
                })
                .catch(() => renderCatalogGrid());
        }"""

new_fetch_js = """        function fetchProducts() {
            const saved = localStorage.getItem("goodstone_products");
            if (saved) {
                try {
                    const parsed = JSON.parse(saved);
                    if (parsed && parsed.length > 0) {
                        products = parsed;
                        renderCatalogGrid();
                        return;
                    }
                } catch(e) {}
            }
            fetch("data.json")
                .then(res => res.json())
                .then(data => {
                    if (data && data.products && data.products.length > 0) {
                        products = data.products;
                        localStorage.setItem("goodstone_products", JSON.stringify(products));
                    }
                    renderCatalogGrid();
                })
                .catch(() => renderCatalogGrid());
        }"""

if old_fetch_js in content:
    content = content.replace(old_fetch_js, new_fetch_js)

# 2. Update renderProductCheckoutDetail to render gallery thumbnail buttons and switch images on click
old_render_detail_js = """        function renderProductCheckoutDetail() {
            if (!selectedProduct) return;
            const p = selectedProduct;
            const mainImg = p.image_file || p.fallback_image;
            document.getElementById("checkout-main-img").src = mainImg;
            document.getElementById("checkout-prod-category").innerText = p.category;
            document.getElementById("checkout-prod-title").innerText = p.name;
            document.getElementById("checkout-prod-desc").innerText = p.description || "หนังสติ๊กยุทธวิธีเกรดพรีเมียม";

            // Render Variants
            const variantsContainer = document.getElementById("checkout-variants-container");
            variantsContainer.innerHTML = "";
            const vars = (p.variants && p.variants.length > 0) ? p.variants : [{ name: "รุ่นมาตรฐาน", price: p.price }];

            vars.forEach((v, idx) => {
                const pill = document.createElement("button");
                pill.type = "button";
                pill.className = `px-3.5 py-2 rounded-xl text-xs font-bold border-2 transition-all cursor-pointer ${idx === selectedVariantIdx ? 'border-[#EE4D2D] bg-[#EE4D2D]/10 text-[#EE4D2D]' : 'theme-border theme-card-subtle theme-text-main'}`;
                pill.innerHTML = `${v.name} (฿${Number(v.price).toLocaleString()})`;
                pill.onclick = () => {
                    selectedVariantIdx = idx;
                    renderProductCheckoutDetail();
                    updateCalculations();
                };
                variantsContainer.appendChild(pill);
            });

            document.getElementById("checkout-quantity-display").innerText = quantity;
        }"""

new_render_detail_js = """        function renderProductCheckoutDetail() {
            if (!selectedProduct) return;
            const p = selectedProduct;
            
            // Image Gallery Array
            const imgs = (p.images && p.images.length > 0)
                ? p.images
                : [{ file: p.image_file || p.fallback_image, name: p.name }];

            if (currentGalleryIdx >= imgs.length) currentGalleryIdx = 0;
            const activeImg = imgs[currentGalleryIdx]?.file || p.image_file || p.fallback_image;

            document.getElementById("checkout-main-img").src = activeImg;
            document.getElementById("checkout-prod-category").innerText = p.category;
            document.getElementById("checkout-prod-title").innerText = p.name;
            document.getElementById("checkout-prod-desc").innerText = p.description || "หนังสติ๊กยุทธวิธีเกรดพรีเมียม";

            // Render Gallery Thumbnails (Clickable Image Selector)
            const thumbsBox = document.getElementById("checkout-gallery-thumbs");
            if (thumbsBox) {
                thumbsBox.innerHTML = "";
                imgs.forEach((imgObj, idx) => {
                    const imgUrl = imgObj.file || imgObj;
                    const thumb = document.createElement("button");
                    thumb.type = "button";
                    thumb.className = `relative aspect-square overflow-hidden rounded-xl border-2 transition-all p-1 bg-white cursor-pointer ${idx === currentGalleryIdx ? 'border-[#EE4D2D] ring-2 ring-[#EE4D2D]/30' : 'border-slate-200 opacity-70 hover:opacity-100'}`;
                    thumb.innerHTML = `<img src="${imgUrl}" onerror="this.onerror=null; this.src='${p.fallback_image}';" class="w-full h-full object-contain">`;
                    thumb.onclick = () => {
                        currentGalleryIdx = idx;
                        renderProductCheckoutDetail();
                    };
                    thumbsBox.appendChild(thumb);
                });
            }

            // Render Variants
            const variantsContainer = document.getElementById("checkout-variants-container");
            variantsContainer.innerHTML = "";
            const vars = (p.variants && p.variants.length > 0) ? p.variants : [{ name: "รุ่นมาตรฐาน", price: p.price }];

            vars.forEach((v, idx) => {
                const pill = document.createElement("button");
                pill.type = "button";
                pill.className = `px-3.5 py-2 rounded-xl text-xs font-bold border-2 transition-all cursor-pointer ${idx === selectedVariantIdx ? 'border-[#EE4D2D] bg-[#EE4D2D]/10 text-[#EE4D2D]' : 'theme-border theme-card-subtle theme-text-main'}`;
                pill.innerHTML = `${v.name} (฿${Number(v.price).toLocaleString()})`;
                pill.onclick = () => {
                    selectedVariantIdx = idx;
                    renderProductCheckoutDetail();
                    updateCalculations();
                };
                variantsContainer.appendChild(pill);
            });

            document.getElementById("checkout-quantity-display").innerText = quantity;
        }"""

if old_render_detail_js in content:
    content = content.replace(old_render_detail_js, new_render_detail_js)

# Also update openProductDirectCheckout to reset currentGalleryIdx = 0
content = content.replace(
    'selectedVariantIdx = 0;\n                quantity = 1;',
    'selectedVariantIdx = 0;\n                currentGalleryIdx = 0;\n                quantity = 1;'
)

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated gallery thumbnails & synced products with localStorage successfully!")
