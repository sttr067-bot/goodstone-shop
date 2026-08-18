import json
import base64
import os
import zipfile

PROJECT_DIR = "/working_dir/slingshot-shop"

# SVGs
svgs = {
    "tactical": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="400" height="300">
  <defs>
    <linearGradient id="metal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="400" height="300" fill="#0f172a"/>
  <circle cx="200" cy="150" r="110" fill="#1e293b" opacity="0.6"/>
  <path d="M120 70 Q140 160 180 180 L180 270 Q200 285 220 270 L220 180 Q260 160 280 70 L250 65 Q235 130 200 145 Q165 130 150 65 Z" fill="url(#metal)" stroke="#f59e0b" stroke-width="3"/>
  <rect x="185" y="180" width="30" height="85" rx="5" fill="#334155" stroke="#475569" stroke-width="2"/>
  <line x1="185" y1="200" x2="215" y2="200" stroke="#0f172a" stroke-width="2"/>
  <line x1="185" y1="220" x2="215" y2="220" stroke="#0f172a" stroke-width="2"/>
  <line x1="185" y1="240" x2="215" y2="240" stroke="#0f172a" stroke-width="2"/>
  <rect x="110" y="55" width="35" height="20" rx="3" fill="#f59e0b"/>
  <rect x="255" y="55" width="35" height="20" rx="3" fill="#f59e0b"/>
  <circle cx="127" cy="65" r="4" fill="#10b981"/>
  <circle cx="272" cy="65" r="4" fill="#10b981"/>
  <rect x="100" y="78" width="18" height="30" rx="4" fill="#ef4444"/>
  <circle cx="109" cy="93" r="3" fill="#fecaca"/>
  <line x1="109" y1="93" x2="30" y2="93" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4"/>
  <path d="M125 55 Q160 20 200 25 Q240 20 275 55" fill="none" stroke="#fbbf24" stroke-width="6" stroke-linecap="round"/>
  <rect x="185" y="18" width="30" height="14" rx="3" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
  <text x="200" y="28" font-size="8" fill="#fff" text-anchor="middle" font-family="sans-serif">TACTICAL</text>
  <text x="200" y="285" font-size="13" fill="#fbbf24" text-anchor="middle" font-weight="bold" font-family="sans-serif">หนังสติ๊กอัลลอยด์ยุทธวิธี เลเซอร์ช่วยเล็ง</text>
</svg>""",
    "wood": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="400" height="300">
  <defs>
    <linearGradient id="steel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc"/>
      <stop offset="50%" stop-color="#94a3b8"/>
      <stop offset="100%" stop-color="#475569"/>
    </linearGradient>
    <linearGradient id="wood" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#b45309"/>
      <stop offset="50%" stop-color="#78350f"/>
      <stop offset="100%" stop-color="#451a03"/>
    </linearGradient>
  </defs>
  <rect width="400" height="300" fill="#1e293b"/>
  <circle cx="200" cy="150" r="110" fill="#334155" opacity="0.4"/>
  <path d="M125 70 Q145 155 180 175 L180 270 Q200 282 220 270 L220 175 Q255 155 275 70 L245 65 Q230 130 200 145 Q170 130 155 65 Z" fill="url(#steel)" stroke="#e2e8f0" stroke-width="3"/>
  <path d="M183 175 L217 175 L217 265 Q200 275 183 265 Z" fill="url(#wood)"/>
  <circle cx="200" cy="195" r="3" fill="#f59e0b"/>
  <circle cx="200" cy="225" r="3" fill="#f59e0b"/>
  <circle cx="200" cy="250" r="3" fill="#f59e0b"/>
  <rect x="115" y="55" width="35" height="18" rx="2" fill="url(#steel)" stroke="#cbd5e1"/>
  <rect x="250" y="55" width="35" height="18" rx="2" fill="url(#steel)" stroke="#cbd5e1"/>
  <path d="M130 55 Q165 20 200 25 Q235 20 270 55" fill="none" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>
  <text x="200" y="285" font-size="13" fill="#cbd5e1" text-anchor="middle" font-weight="bold" font-family="sans-serif">หนังสติ๊กสแตนเลส CNC ด้ามไม้ประกบ</text>
</svg>""",
    "rubber_075": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="400" height="300">
  <rect width="400" height="300" fill="#0f172a"/>
  <g transform="translate(60, 35)">
    <path d="M20 30 L220 50 L220 70 L20 45 Z" fill="#fbbf24" stroke="#d97706" stroke-width="2"/>
    <path d="M20 75 L220 95 L220 115 L20 90 Z" fill="#fbbf24" stroke="#d97706" stroke-width="2"/>
    <path d="M20 120 L220 140 L220 160 L20 135 Z" fill="#fbbf24" stroke="#d97706" stroke-width="2"/>
    <path d="M20 165 L220 185 L220 205 L20 180 Z" fill="#fbbf24" stroke="#d97706" stroke-width="2"/>
    <rect x="220" y="45" width="45" height="165" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="242" cy="70" r="4" fill="#f59e0b"/>
    <circle cx="242" cy="120" r="4" fill="#f59e0b"/>
    <circle cx="242" cy="170" r="4" fill="#f59e0b"/>
    <text x="242" y="135" font-size="9" fill="#fff" text-anchor="middle" font-family="sans-serif">0.75mm</text>
  </g>
  <text x="200" y="280" font-size="13" fill="#fbbf24" text-anchor="middle" font-weight="bold" font-family="sans-serif">ยางหนังสติ๊กแบน 0.75mm ไล่สโลป (5 เส้น)</text>
</svg>""",
    "rubber_10": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="400" height="300">
  <rect width="400" height="300" fill="#0f172a"/>
  <g transform="translate(60, 35)">
    <path d="M20 30 L220 50 L220 72 L20 48 Z" fill="#10b981" stroke="#047857" stroke-width="2"/>
    <path d="M20 75 L220 95 L220 117 L20 93 Z" fill="#10b981" stroke="#047857" stroke-width="2"/>
    <path d="M20 120 L220 140 L220 162 L20 138 Z" fill="#10b981" stroke="#047857" stroke-width="2"/>
    <path d="M20 165 L220 185 L220 207 L20 183 Z" fill="#10b981" stroke="#047857" stroke-width="2"/>
    <rect x="220" y="45" width="45" height="165" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
    <circle cx="242" cy="70" r="4" fill="#34d399"/>
    <circle cx="242" cy="120" r="4" fill="#34d399"/>
    <circle cx="242" cy="170" r="4" fill="#34d399"/>
    <text x="242" y="135" font-size="9" fill="#fff" text-anchor="middle" font-family="sans-serif">1.0mm</text>
  </g>
  <text x="200" y="280" font-size="13" fill="#34d399" text-anchor="middle" font-weight="bold" font-family="sans-serif">ยางหนังสติ๊กแบน 1.0mm แรงดึงสูง (5 เส้น)</text>
</svg>""",
    "ammo_steel": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="400" height="300">
  <defs>
    <radialGradient id="sphere" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#e2e8f0"/>
      <stop offset="70%" stop-color="#64748b"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </radialGradient>
  </defs>
  <rect width="400" height="300" fill="#0f172a"/>
  <circle cx="120" cy="140" r="35" fill="url(#sphere)" stroke="#94a3b8" stroke-width="1"/>
  <circle cx="180" cy="110" r="35" fill="url(#sphere)" stroke="#94a3b8" stroke-width="1"/>
  <circle cx="240" cy="150" r="35" fill="url(#sphere)" stroke="#94a3b8" stroke-width="1"/>
  <circle cx="170" cy="180" r="35" fill="url(#sphere)" stroke="#94a3b8" stroke-width="1"/>
  <circle cx="280" cy="110" r="30" fill="url(#sphere)" stroke="#94a3b8" stroke-width="1"/>
  <circle cx="90" cy="190" r="25" fill="url(#sphere)" stroke="#94a3b8" stroke-width="1"/>
  <text x="200" y="50" font-size="16" fill="#f8fafc" text-anchor="middle" font-weight="bold" font-family="sans-serif">8 mm STEEL AMMO (500 นัด)</text>
  <text x="200" y="280" font-size="13" fill="#cbd5e1" text-anchor="middle" font-weight="bold" font-family="sans-serif">ลูกเหล็กกลมขัดเงา 8 มม. (500 นัด)</text>
</svg>""",
    "ammo_clay": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="400" height="300">
  <defs>
    <radialGradient id="clay" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#fed7aa"/>
      <stop offset="40%" stop-color="#ea580c"/>
      <stop offset="80%" stop-color="#9a3412"/>
      <stop offset="100%" stop-color="#431407"/>
    </radialGradient>
  </defs>
  <rect width="400" height="300" fill="#1e293b"/>
  <circle cx="130" cy="130" r="32" fill="url(#clay)"/>
  <circle cx="190" cy="100" r="32" fill="url(#clay)"/>
  <circle cx="250" cy="140" r="32" fill="url(#clay)"/>
  <circle cx="180" cy="170" r="32" fill="url(#clay)"/>
  <circle cx="280" cy="100" r="28" fill="url(#clay)"/>
  <circle cx="100" cy="180" r="24" fill="url(#clay)"/>
  <text x="200" y="50" font-size="16" fill="#fed7aa" text-anchor="middle" font-weight="bold" font-family="sans-serif">9 mm CLAY AMMO (1,000 นัด)</text>
  <text x="200" y="280" font-size="13" fill="#fdba74" text-anchor="middle" font-weight="bold" font-family="sans-serif">ลูกกระสุนดินเผารักษ์โลก 9 มม. (1,000 นัด)</text>
</svg>""",
    "laser": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="400" height="300">
  <rect width="400" height="300" fill="#0f172a"/>
  <g transform="translate(100, 50)">
    <rect x="40" y="40" width="120" height="60" rx="8" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
    <circle cx="55" cy="70" r="8" fill="#ef4444"/>
    <circle cx="55" cy="70" r="3" fill="#fff"/>
    <line x1="55" y1="70" x2="-60" y2="70" stroke="#ef4444" stroke-width="2" stroke-dasharray="6,4"/>
    <rect x="130" y="30" width="15" height="15" rx="3" fill="#10b981"/>
    <circle cx="137" cy="37" r="3" fill="#a7f3d0"/>
    <circle cx="137" cy="37" r="1.5" fill="#065f46"/>
    <rect x="70" y="100" width="60" height="40" fill="#334155" stroke="#475569" stroke-width="2"/>
    <circle cx="100" cy="120" r="8" fill="#f59e0b"/>
  </g>
  <text x="200" y="280" font-size="13" fill="#fca5a5" text-anchor="middle" font-weight="bold" font-family="sans-serif">ศูนย์เล็งไฟเบอร์ออปติก + เลเซอร์แดง</text>
</svg>""",
    "bag": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="400" height="300">
  <rect width="400" height="300" fill="#1e293b"/>
  <g transform="translate(100, 35)">
    <path d="M20 40 Q20 20 40 20 L160 20 Q180 20 180 40 L180 180 Q180 200 160 200 L40 200 Q20 200 20 180 Z" fill="#334155" stroke="#f59e0b" stroke-width="2"/>
    <path d="M30 40 L170 40 L160 110 L40 110 Z" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
    <circle cx="100" cy="90" r="8" fill="#f59e0b"/>
    <rect x="50" y="130" width="100" height="50" rx="5" fill="#0f172a" stroke="#64748b"/>
    <text x="100" y="160" font-size="10" fill="#f59e0b" text-anchor="middle" font-family="sans-serif">ช่องแม่เหล็กดูดลูกเหล็ก</text>
  </g>
  <text x="200" y="280" font-size="13" fill="#fcd34d" text-anchor="middle" font-weight="bold" font-family="sans-serif">กระเป๋าคาดเอวใส่หนังสติ๊กและลูกเหล็ก</text>
</svg>"""
}

base64_images = {}
for k, v in svgs.items():
    b64 = base64.b64encode(v.encode("utf-8")).decode("ascii")
    base64_images[k] = f"data:image/svg+xml;base64,{b64}"

products_data = [
    {
        "id": "PROD-001",
        "name": "หนังสติ๊กอัลลอยด์ยุทธวิธี พร้อมเลเซอร์ช่วยเล็งและระดับน้ำ",
        "category": "slingshot",
        "price": 390.0,
        "stock": 35,
        "image_file": "images/slingshots/prod-001.jpg",
        "fallback_image": base64_images["tactical"],
        "description": "ด้ามจับอัลลอยด์ แข็งแรงทนทาน น้ำหนักกระชับมือ พร้อมศูนย์เล็งเลเซอร์และระดับน้ำ ช่วยจับเป้าแม่นยำ"
    },
    {
        "id": "PROD-002",
        "name": "หนังสติ๊กสแตนเลส CNC ด้ามไม้ประกบเกรดพรีเมียม",
        "category": "slingshot",
        "price": 550.0,
        "stock": 20,
        "image_file": "images/slingshots/prod-002.jpg",
        "fallback_image": base64_images["wood"],
        "description": "สแตนเลส 304 กลึง CNC สวยงาม ไร้สนิม ประกบไม้แท้เนื้อแข็ง จับถนัดมือ ยิงนิ่ง แม่นยำสูง"
    },
    {
        "id": "PROD-003",
        "name": "ยางหนังสติ๊กแบบแบน ไล่สโลป หนา 0.75mm (แพ็ก 5 เส้น)",
        "category": "rubber",
        "price": 120.0,
        "stock": 100,
        "image_file": "images/rubber-bands/prod-003.jpg",
        "fallback_image": base64_images["rubber_075"],
        "description": "ยางนำเข้า ยืดหยุ่นสูง แรงดีดสม่ำเสมอ ตัดสโลปมาตรฐาน หนังรองกระสุนไมโครไฟเบอร์ทนทาน"
    },
    {
        "id": "PROD-004",
        "name": "ยางหนังสติ๊กแบบแบน หนา 1.0mm แรงดึงสูงพิเศษ (แพ็ก 5 เส้น)",
        "category": "rubber",
        "price": 140.0,
        "stock": 80,
        "image_file": "images/rubber-bands/prod-004.jpg",
        "fallback_image": base64_images["rubber_10"],
        "description": "ยางหนา 1.0 มม. เหมาะสำหรับลูกเหล็ก 8-9 มม. แรงถีบแรง สะใจ ทนทานไม่ขาดง่าย"
    },
    {
        "id": "PROD-005",
        "name": "ลูกเหล็กกลมขัดเงา ขนาด 8 มม. (กล่องละ 500 นัด)",
        "category": "ammo",
        "price": 150.0,
        "stock": 150,
        "image_file": "images/ammo/prod-005.jpg",
        "fallback_image": base64_images["ammo_steel"],
        "description": "ลูกเหล็กคาร์บอนเกรดมาตรฐาน กลมเกลี้ยง ผิวเรียบเงา ไม่สะดุดลำกล้องหรือหนังรอง น้ำหนักแม่นยำ"
    },
    {
        "id": "PROD-006",
        "name": "ลูกกระสุนดินเผาผสมสมุนไพร ขนาด 9 มม. รักษ์โลก (1,000 นัด)",
        "category": "ammo",
        "price": 99.0,
        "stock": 200,
        "image_file": "images/ammo/prod-006.jpg",
        "fallback_image": base64_images["ammo_clay"],
        "description": "กระสุนดินอัดแข็ง โดนเป้าแล้วแตก ย่อยสลายได้ตามธรรมชาติ ไม่เป็นอันตรายต่อสิ่งแวดล้อม"
    },
    {
        "id": "PROD-007",
        "name": "ศูนย์เล็งไฟเบอร์ออปติก + เลเซอร์แดง พร้อมถ่านกระดุม",
        "category": "accessories",
        "price": 190.0,
        "stock": 45,
        "image_file": "images/accessories/prod-007.jpg",
        "fallback_image": base64_images["laser"],
        "description": "อุปกรณ์ช่วยเล็งแบบสองระบบ ไฟเบอร์เรืองแสงกลางวัน และเลเซอร์มองเห็นชัดเจนในที่แสงน้อย"
    },
    {
        "id": "PROD-008",
        "name": "กระเป๋าคาดเอวเก็บหนังสติ๊กและลูกเหล็ก พร้อมแม่เหล็กดูดลูก",
        "category": "accessories",
        "price": 220.0,
        "stock": 60,
        "image_file": "images/accessories/prod-008.jpg",
        "fallback_image": base64_images["bag"],
        "description": "กระเป๋าผ้าแคนวาสทหาร มีช่องใส่หนังสติ๊กและช่องใส่ลูกเหล็กพร้อมแถบแม่เหล็กแรงสูง หยิบลูกยิงได้รวดเร็ว"
    }
]

default_orders = [
    {
        "id": "ORD-20260817-001",
        "customer_name": "สมชาย ใจดี",
        "phone": "081-999-8877",
        "address": "45/2 หมู่ 3 ต.บางกระดี่ อ.เมือง จ.สมุทรปราการ 10270",
        "shipping_provider": "Flash Express",
        "shipping_cost": 45.0,
        "total_amount": 540.0,
        "status": "PAID",
        "tracking_number": "TH1027088921A",
        "items": [
            {"product_id": "PROD-001", "name": "หนังสติ๊กอัลลอยด์ยุทธวิธี พร้อมเลเซอร์ช่วยเล็ง", "price": 390.0, "quantity": 1},
            {"product_id": "PROD-005", "name": "ลูกเหล็กกลมขัดเงา 8 มม.", "price": 150.0, "quantity": 1}
        ],
        "created_at": "2026-08-17 10:15:00"
    },
    {
        "id": "ORD-20260817-002",
        "customer_name": "กิตติพงษ์ ยอดเยี่ยม",
        "phone": "082-345-6789",
        "address": "99 อาคารสุขใจ ชั้น 4 ถ.พหลโยธิน แขวงสามเสนใน เขตพญาไท กทม. 10400",
        "shipping_provider": "J&T Express",
        "shipping_cost": 45.0,
        "total_amount": 690.0,
        "status": "PAID",
        "tracking_number": "820399482910",
        "items": [
            {"product_id": "PROD-002", "name": "หนังสติ๊กสแตนเลส CNC ด้ามไม้ประกบ", "price": 550.0, "quantity": 1},
            {"product_id": "PROD-004", "name": "ยางหนังสติ๊กแบน 1.0mm (5 เส้น)", "price": 140.0, "quantity": 1}
        ],
        "created_at": "2026-08-17 11:30:20"
    },
    {
        "id": "ORD-20260817-003",
        "customer_name": "วิชัย มุ่งมั่น",
        "phone": "086-777-1234",
        "address": "12/8 ต.ในเมือง อ.เมือง จ.นครราชสีมา 30000",
        "shipping_provider": "Flash Express",
        "shipping_cost": 40.0,
        "total_amount": 380.0,
        "status": "PAID",
        "tracking_number": "TH3000055219B",
        "items": [
            {"product_id": "PROD-003", "name": "ยางหนังสติ๊กแบน 0.75mm (5 เส้น)", "price": 120.0, "quantity": 2},
            {"product_id": "PROD-004", "name": "ยางหนังสติ๊กแบน 1.0mm (5 เส้น)", "price": 140.0, "quantity": 1}
        ],
        "created_at": "2026-08-17 11:55:00"
    }
]

# Write data.json
data = {
    "store_info": {
        "name": "GOODSTONE TACTICAL SLINGSHOT (ร้านหนังสติ๊กยุทธวิธี)",
        "owner_name": "สุเมธา แท่นธรรมโรจน์",
        "phone": "061-537-2239",
        "address": "123/45 ถนนพระราม 2 แขวงท่าข้าม เขตบางขุนเทียน กรุงเทพฯ 10150",
        "promptpay_phone": "0615372239",
        "promptpay_id_card": "1100400828330"
    },
    "products": products_data,
    "orders": default_orders
}

with open(os.path.join(PROJECT_DIR, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Data saved!")
