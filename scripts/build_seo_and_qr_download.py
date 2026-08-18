import json

# 1. Update index.html
with open("/working_dir/slingshot-shop/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add SEO Meta Tags in <head>
old_head = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>GOODSTONE - ร้านหนังสติ๊กยุทธวิธีและอุปกรณ์ครบวงจร</title>"""

new_seo_head = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    
    <!-- ================= SEO PRIMARY META TAGS ================= -->
    <title>GOODSTONE หนังสติ๊กยุทธวิธี หนังสติ๊กเลเซอร์ ยางหนังสติ๊ก ลูกเหล็ก ลูกดินเผา กระสุนหนังสติ๊ก</title>
    <meta name="title" content="GOODSTONE หนังสติ๊กยุทธวิธี หนังสติ๊กเลเซอร์ ยางหนังสติ๊ก ลูกเหล็ก ลูกดินเผา กระสุนหนังสติ๊ก">
    <meta name="description" content="ร้านขายหนังสติ๊กยุทธวิธี หนังสติ๊กเลเซอร์ ยางหนังสติ๊กแบนเกรดพรีเมียม ลูกเหล็กกลมขัดเงา ลูกดินเผา กระสุนหนังสติ๊ก อุปกรณ์ครบชุด ส่งฟรีเมื่อครบ 200 บาท จัดส่งด่วน SPX / EMS ทั่วไทย">
    <meta name="keywords" content="หนังสติ๊ก, หนังสติ๊กเลเซอร์, ลูกเหล็ก, ยางหนังสติ๊ก, ลูกดินเผา, กระสุนหนังสติ๊ก, หนังสติ๊กยุทธวิธี, หนังสติ๊กสแตนเลส, ยางแบนหนังสติ๊ก, ลูกกระสุนดินเผา, slingshot thailand, goodstone">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="author" content="GOODSTONE SHOP">
    <link rel="canonical" href="https://goodstone-slingshot.com/">

    <!-- ================= OPEN GRAPH / FACEBOOK / LINE ================= -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://goodstone-slingshot.com/">
    <meta property="og:title" content="GOODSTONE หนังสติ๊กยุทธวิธี หนังสติ๊กเลเซอร์ ยางหนังสติ๊ก ลูกเหล็ก ลูกดินเผา">
    <meta property="og:description" content="ร้านจำหน่ายหนังสติ๊กยุทธวิธีเกรดพรีเมียม เลเซอร์ช่วยเล็ง ยางหนังสติ๊ก ลูกเหล็ก ลูกดินเผา ส่งฟรีเมื่อครบ 200 บ. ชำระพร้อมเพย์หรือเก็บเงินปลายทาง COD">
    <meta property="og:image" content="https://lh3.googleusercontent.com/d/14_-w1jmY24fFWj2Am7Zm8cbBuXlgxsaj">
    <meta property="og:locale" content="th_TH">
    <meta property="og:site_name" content="GOODSTONE SHOP">

    <!-- ================= TWITTER CARDS ================= -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="GOODSTONE หนังสติ๊กยุทธวิธี & อุปกรณ์ครบวงจร">
    <meta name="twitter:description" content="หนังสติ๊กเลเซอร์ ยางหนังสติ๊ก ลูกเหล็ก ลูกดินเผา ส่งฟรีทั่วไทย">
    <meta name="twitter:image" content="https://lh3.googleusercontent.com/d/14_-w1jmY24fFWj2Am7Zm8cbBuXlgxsaj">

    <!-- ================= JSON-LD STRUCTURED DATA (SCHEMA.ORG) ================= -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Store",
          "@id": "https://goodstone-slingshot.com/#store",
          "name": "GOODSTONE SHOP ร้านหนังสติ๊กยุทธวิธีและอุปกรณ์",
          "url": "https://goodstone-slingshot.com/",
          "description": "ร้านขายหนังสติ๊กยุทธวิธี หนังสติ๊กเลเซอร์ ยางหนังสติ๊ก ลูกเหล็ก ลูกดินเผา กระสุนหนังสติ๊ก",
          "telephone": "061-537-2239",
          "priceRange": "฿35 - ฿490",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "123/45 ถนนพระราม 2 แขวงท่าข้าม",
            "addressLocality": "บางขุนเทียน",
            "addressRegion": "กรุงเทพมหานคร",
            "postalCode": "10150",
            "addressCountry": "TH"
          }
        },
        {
          "@type": "ItemList",
          "name": "สินค้าแนะนำ หนังสติ๊กยุทธวิธีและกระสุน",
          "itemListElement": [
            {
              "@type": "Product",
              "position": 1,
              "name": "หนังสติ๊กอัลลอยด์ยุทธวิธี พร้อมเลเซอร์ช่วยเล็งและระดับน้ำ",
              "description": "หนังสติ๊กเลเซอร์อลูมิเนียมอัลลอยด์ ศูนย์เล็งไฟเบอร์ออปติกและเลเซอร์ความแม่นยำสูง",
              "offers": {
                "@type": "Offer",
                "price": "390",
                "priceCurrency": "THB",
                "availability": "https://schema.org/InStock"
              }
            },
            {
              "@type": "Product",
              "position": 2,
              "name": "ยางหนังสติ๊ก ยางแบนพรีเมียม ความหนา 0.75 มม.",
              "description": "ยางหนังสติ๊ก ยางแบนเกรดแข่งขัน เหนียว ทนทาน แรงดีดสม่ำเสมอ",
              "offers": {
                "@type": "Offer",
                "price": "89",
                "priceCurrency": "THB",
                "availability": "https://schema.org/InStock"
              }
            },
            {
              "@type": "Product",
              "position": 3,
              "name": "ลูกเหล็กกลมขัดเงา 8 มม. (กระสุนหนังสติ๊ก 100 ลูก)",
              "description": "ลูกเหล็กเกรดพรีเมียม ไร้รอยต่อ ศูนย์ถ่วงเสถียร ยิงแม่นยำ",
              "offers": {
                "@type": "Offer",
                "price": "65",
                "priceCurrency": "THB",
                "availability": "https://schema.org/InStock"
              }
            },
            {
              "@type": "Product",
              "position": 4,
              "name": "ลูกดินเผาชีวภาพ ปลอดภัย รักษ์โลก (กระสุนหนังสติ๊ก 500 ลูก)",
              "description": "ลูกดินเผากลมกลึง ย่อยสลายได้ตามธรรมชาติ ไม่เป็นพิษต่อสิ่งแวดล้อม",
              "offers": {
                "@type": "Offer",
                "price": "45",
                "priceCurrency": "THB",
                "availability": "https://schema.org/InStock"
              }
            }
          ]
        }
      ]
    }
    </script>"""

if old_head in html:
    html = html.replace(old_head, new_seo_head)
    print("Replaced head with SEO meta tags & Schema.org JSON-LD!")

# 2. Add Download QR Code Button under PromptPay QR image
old_qr_box = """                            <!-- Dynamic QR Code Container -->
                            <div class="flex justify-center">
                                <div class="bg-white p-3 rounded-2xl border-2 border-[#EBE3D5] shadow-inner inline-block">
                                    <img id="promptpay-qr-img" src="" alt="PromptPay QR Code" class="w-48 h-48 sm:w-56 sm:h-56 mx-auto object-contain">
                                </div>
                            </div>"""

new_qr_box = """                            <!-- Dynamic QR Code Container with Download Button -->
                            <div class="flex flex-col items-center justify-center space-y-2.5">
                                <div class="bg-white p-3 rounded-2xl border-2 border-[#EBE3D5] shadow-inner inline-block">
                                    <img id="promptpay-qr-img" src="" alt="PromptPay QR Code" class="w-48 h-48 sm:w-56 sm:h-56 mx-auto object-contain">
                                </div>

                                <!-- PROMINENT DOWNLOAD QR BUTTON -->
                                <button type="button" onclick="downloadPromptPayQR()" class="bg-[#2C241E] hover:bg-[#EE4D2D] text-white text-xs px-4 py-2.5 rounded-xl font-bold transition-all shadow-md flex items-center justify-center gap-1.5 active:scale-95 cursor-pointer">
                                    <span>📥 บันทึกรูปภาพ QR Code (Save QR)</span>
                                </button>
                            </div>"""

if old_qr_box in html:
    html = html.replace(old_qr_box, new_qr_box)
    print("Added Download QR Code Button in index.html!")

# 3. Add JavaScript downloadPromptPayQR() function
download_qr_js = """
        // ================= DOWNLOAD PROMPTPAY QR CODE =================
        function downloadPromptPayQR() {
            const qrImg = document.getElementById("promptpay-qr-img");
            if (!qrImg || !qrImg.src) {
                alert("ไม่พบรูป QR Code กรุณารอสักครู่ครับ");
                return;
            }

            const total = document.getElementById("summary-total")?.innerText || "0.00";
            const sanitizedTotal = total.replace(/[^0-9.]/g, "");
            const filename = `PromptPay_QR_GOODSTONE_${sanitizedTotal}THB.png`;

            // Convert image to blob via canvas for instant download across all mobile browsers
            const img = new Image();
            img.crossOrigin = "anonymous";
            img.onload = function() {
                const canvas = document.createElement("canvas");
                canvas.width = img.width || 300;
                canvas.height = img.height || 300;
                const ctx = canvas.getContext("2d");
                
                // Draw background white
                ctx.fillStyle = "#ffffff";
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.drawImage(img, 0, 0);

                canvas.toBlob(function(blob) {
                    if (!blob) {
                        window.open(qrImg.src, "_blank");
                        return;
                    }
                    const url = URL.createObjectURL(blob);
                    const link = document.createElement("a");
                    link.href = url;
                    link.download = filename;
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                    setTimeout(() => URL.revokeObjectURL(url), 1000);
                    alert("📥 บันทึกรูปภาพ QR Code เรียบร้อยแล้วครับ! (เปิดแอปธนาคารแล้วเลือกรูปจากคลังภาพเพื่อสแกนจ่ายได้เลย)");
                }, "image/png");
            };
            img.onerror = function() {
                // Fallback: direct download link
                const link = document.createElement("a");
                link.href = qrImg.src;
                link.download = filename;
                link.target = "_blank";
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            };
            img.src = qrImg.src;
        }
"""

if "function downloadPromptPayQR()" not in html:
    html = html.replace("window.onload = init;", download_qr_js + "\n        window.onload = init;")
    print("Added downloadPromptPayQR JS function!")

with open("/working_dir/slingshot-shop/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("slingshot-shop/index.html updated successfully!")
