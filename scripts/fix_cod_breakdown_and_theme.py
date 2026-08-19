import os

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix updateCalculations to update COD breakdown values dynamically
old_update_calc = """            // QR Code
            const qrImg = document.getElementById("promptpay-qr-img");"""

new_update_calc = """            // Update COD Breakdown Panel
            const codBaseEl = document.getElementById("cod-base-amount");
            if (codBaseEl) codBaseEl.innerText = `฿${baseTotal.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            
            const codFeeAmountEl = document.getElementById("cod-fee-amount");
            if (codFeeAmountEl) codFeeAmountEl.innerText = `+฿${codFee.toLocaleString(undefined, {minimumFractionDigits: 2})}`;
            
            const codTotalAmountEl = document.getElementById("cod-total-amount");
            if (codTotalAmountEl) codTotalAmountEl.innerText = `฿${total.toLocaleString(undefined, {minimumFractionDigits: 2})}`;

            // QR Code
            const qrImg = document.getElementById("promptpay-qr-img");"""

if old_update_calc in content and "codBaseEl" not in content:
    content = content.replace(old_update_calc, new_update_calc)

# Fix HTML initial text for COD breakdown to ฿0.00 instead of $0.00
content = content.replace('$0.00', '฿0.00')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed COD breakdown currency calculation and initial values successfully!")
