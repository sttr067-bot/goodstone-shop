import re

# 1. Update index.html
with open("/working_dir/slingshot-shop/index.html", "r", encoding="utf-8") as f:
    code = f.read()

# Update Light Mode Colors in <style>
old_light_style_pattern = r"/\* Light Theme \(Warm Cream\) \*/[\s\S]*?--shopee-btn-hover: #D73211;\s*\}"
new_light_style = """/* Light Theme (Bright Modern Crisp White) */
        [data-theme="light"] {
            --bg-body: #F8FAFC;
            --bg-header: #FFFFFF;
            --bg-card: #FFFFFF;
            --bg-card-subtle: #F1F5F9;
            --bg-input: #FFFFFF;
            --border-main: #E2E8F0;
            --border-subtle: #CBD5E1;
            --text-main: #0F172A;
            --text-muted: #475569;
            --text-sub: #64748B;
            --badge-bg: #FFF1EE;
            --badge-border: #FFDDD6;
            --badge-text: #EE4D2D;
            --hero-from: #FFF5F2;
            --hero-via: #FFFFFF;
            --hero-to: #F8FAFC;
            --tab-inactive-bg: #F1F5F9;
            --tab-inactive-text: #334155;
            --shopee-btn-bg: #EE4D2D;
            --shopee-btn-hover: #D73211;
        }"""

code = re.sub(old_light_style_pattern, new_light_style, code)

# Add Download QR button in PromptPay Panel
old_qr_box = """                        <div class="flex justify-center">
                            <img id="promptpay-qr-img" src="" class="w-44 h-44 rounded-xl border-2 app-border bg-white p-2">
                        </div>"""

new_qr_box = """                        <div class="flex flex-col items-center justify-center gap-2">
                            <img id="promptpay-qr-img" src="" class="w-44 h-44 rounded-xl border-2 app-border bg-white p-2 shadow-sm">
                            <button type="button" onclick="downloadPromptPayQR()" id="btn-download-qr" class="app-card border app-border text-xs font-bold px-3.5 py-1.5 rounded-xl flex items-center gap-1.5 shadow-sm active:scale-95 hover:border-[#EE4D2D] transition-all">
                                <span>📥 บันทึกรูป QR Code</span>
                            </button>
                        </div>"""

if old_qr_box in code:
    code = code.replace(old_qr_box, new_qr_box)
    print("Added Download QR Code button in index.html!")

# Add downloadPromptPayQR function in JavaScript
download_js_func = """
        function downloadPromptPayQR() {
            const qrImg = document.getElementById("promptpay-qr-img");
            if (!qrImg || !qrImg.src) {
                alert("ไม่พบรูปภาพ QR Code กรุณาลองใหม่อีกครั้งครับ");
                return;
            }

            // Create temporary download anchor or fetch blob
            fetch(qrImg.src)
                .then(res => res.blob())
                .then(blob => {
                    const blobUrl = window.URL.createObjectURL(blob);
                    const link = document.createElement("a");
                    link.style.display = "none";
                    link.href = blobUrl;
                    link.download = `PromptPay_QR_GOODSTONE_${Date.now()}.png`;
                    document.body.appendChild(link);
                    link.click();
                    window.URL.revokeObjectURL(blobUrl);
                    document.body.removeChild(link);
                })
                .catch(() => {
                    const fallbackLink = document.createElement("a");
                    fallbackLink.href = qrImg.src;
                    fallbackLink.download = "PromptPay_QR.png";
                    fallbackLink.target = "_blank";
                    fallbackLink.click();
                });
        }
"""

if "function copyPromptPay()" in code:
    code = code.replace("function copyPromptPay()", download_js_func + "\n        function copyPromptPay()")
    print("Added downloadPromptPayQR JS function in index.html!")

with open("/working_dir/slingshot-shop/index.html", "w", encoding="utf-8") as f:
    f.write(code)

# 2. Update admin.html Light Mode Style
with open("/working_dir/slingshot-shop/admin.html", "r", encoding="utf-8") as f:
    adm_code = f.read()

old_adm_light = r"/\* Light Theme \(Warm Cream\) \*/[\s\S]*?--tab-inactive-text: #2C241E;\s*\}"
new_adm_light = """/* Light Theme (Bright Clean White) */
        [data-theme="light"] {
            --bg-body: #F8FAFC;
            --bg-header: #FFFFFF;
            --bg-card: #FFFFFF;
            --bg-card-subtle: #F1F5F9;
            --bg-input: #FFFFFF;
            --border-main: #E2E8F0;
            --border-subtle: #CBD5E1;
            --text-main: #0F172A;
            --text-muted: #475569;
            --text-sub: #64748B;
            --badge-bg: #FFF1EE;
            --badge-border: #FFDDD6;
            --badge-text: #EE4D2D;
            --tab-inactive-bg: #F1F5F9;
            --tab-inactive-text: #334155;
        }"""

adm_code = re.sub(old_adm_light, new_adm_light, adm_code)
with open("/working_dir/slingshot-shop/admin.html", "w", encoding="utf-8") as f:
    f.write(adm_code)

print("Updated index.html and admin.html with Download QR Code button and Bright White Light Theme!")
