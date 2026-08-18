import re

with open("/working_dir/slingshot-shop/index.html", "r", encoding="utf-8") as f:
    code = f.read()

old_submit_start = """            const activeV = selectedProduct.variants[selectedVariantIdx] || { name: "รุ่นมาตรฐาน", price: selectedProduct.price };
            const subtotal = activeV.price * quantity;
            const isFreeShipping = (subtotal >= 200);
            const shippingCost = isFreeShipping ? 0 : 25;
            const baseTotal = subtotal + shippingCost;
            const codFee = (paymentMethod === "COD") ? Number((baseTotal * 0.03).toFixed(2)) : 0;
            const total = Number((baseTotal + codFee).toFixed(2));"""

new_submit_start = """            const p = selectedProduct || products[0] || DEFAULT_PRODUCTS[0];
            const variants = (p.variants && Array.isArray(p.variants) && p.variants.length > 0) ? p.variants : [{ name: "รุ่นมาตรฐาน", price: Number(p.price) || 390, stock: Number(p.stock) || 20 }];
            if (selectedVariantIdx < 0 || selectedVariantIdx >= variants.length) selectedVariantIdx = 0;
            const activeV = variants[selectedVariantIdx] || variants[0];

            const unitPrice = Number(activeV.price) || Number(p.price) || 390;
            const qty = Math.max(1, Number(quantity) || 1);
            const subtotal = unitPrice * qty;
            const isFreeShipping = (subtotal >= 200);
            const shippingCost = isFreeShipping ? 0 : 25;
            const baseTotal = subtotal + shippingCost;
            const codFee = (paymentMethod === "COD") ? Number((baseTotal * 0.03).toFixed(2)) : 0;
            const total = Number((baseTotal + codFee).toFixed(2));"""

if old_submit_start in code:
    code = code.replace(old_submit_start, new_submit_start)
    print("Fixed submitDirectOrder calculations!")

with open("/working_dir/slingshot-shop/index.html", "w", encoding="utf-8") as f:
    f.write(code)
