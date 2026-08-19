import os

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Comprehensive Google SEO Meta Tags & Schema Markup
seo_head_tags = """
    <!-- GOOGLE SEO & SEARCH ENGINE OPTIMIZATION META TAGS -->
    <title>หนังสติ๊ก ยางหนังสติ๊ก ลูกยิงหนังสติ๊ก ของแท้ 100% — GOODSTONE</title>
    <meta name="description" content="ศูนย์รวม หนังสติ๊ก ยางหนังสติ๊ก ยางแบน ลูกยิงหนังสติ๊ก ลูกเหล็กยุทธวิธี ด้ามอัลลอยด์ CNC พร้อมเลเซอร์ช่วยเล็ง ของแท้ 100% จัดส่งด่วน SPX/EMS 24 ชม. มีบริการเก็บเงินปลายทาง (COD)">
    <meta name="keywords" content="หนังสติ๊ก, ยางหนังสติ๊ก, ลูกยิงหนังสติ๊ก, หนังสติ๊กยุทธวิธี, ยางแบนหนังสติ๊ก, ลูกเหล็กหนังสติ๊ก, หนังสติ๊กเลเซอร์, หนังสติ๊กสแตนเลส, GOODSTONE">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://goodstone-shop.vercel.app">

    <!-- OPEN GRAPH / SOCIAL MEDIA SEO -->
    <meta property="og:title" content="หนังสติ๊ก ยางหนังสติ๊ก ลูกยิงหนังสติ๊ก ของแท้ 100% — GOODSTONE">
    <meta property="og:description" content="ศูนย์รวม หนังสติ๊ก ยางหนังสติ๊ก ยางแบน ลูกยิงหนังสติ๊ก ลูกเหล็กยุทธวิธี ของแท้ 100% ส่งด่วน 24 ชม.">
    <meta property="og:url" content="https://goodstone-shop.vercel.app">
    <meta property="og:site_name" content="GOODSTONE">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://lh3.googleusercontent.com/d/1u5fhZmlGqWrCY7CJpGSe5xHQqbt6ArDa">

    <!-- GOOGLE STRUCTURED DATA SCHEMA (JSON-LD RICH SNIPPETS) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "OnlineStore",
      "name": "GOODSTONE - ร้านหนังสติ๊ก ยางหนังสติ๊ก ลูกยิงหนังสติ๊ก",
      "url": "https://goodstone-shop.vercel.app",
      "logo": "https://lh3.googleusercontent.com/d/1u5fhZmlGqWrCY7CJpGSe5xHQqbt6ArDa",
      "description": "ร้านจำหน่าย หนังสติ๊ก ยางหนังสติ๊ก ยางแบน ลูกยิงหนังสติ๊ก ลูกเหล็กยุทธวิธี ของแท้ 100%",
      "telephone": "0615372239",
      "priceRange": "฿290 - ฿650",
      "knowsAbout": ["หนังสติ๊ก", "ยางหนังสติ๊ก", "ลูกยิงหนังสติ๊ก", "หนังสติ๊กยุทธวิธี", "ยางแบน", "ลูกเหล็ก"]
    }
    </script>
"""

# Replace old title and add SEO tags
if "<title>" in content:
    old_title_start = content.find("<title>")
    old_title_end = content.find("</title>") + 8
    content = content[:old_title_start] + seo_head_tags + content[old_title_end:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Added Google SEO Meta Tags successfully!")
