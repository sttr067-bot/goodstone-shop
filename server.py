#!/usr/bin/env python3
import http.server
import socketserver
import json
import os
import urllib.parse
import datetime
import random

PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

DEFAULT_DATA = {
    "store_info": {
        "name": "GOODSTONE TACTICAL SLINGSHOT (ร้านหนังสติ๊กยุทธวิธี)",
        "phone": "089-123-4567",
        "address": "123/45 ถนนพระราม 2 แขวงท่าข้าม เขตบางขุนเทียน กรุงเทพฯ 10150",
        "promptpay_number": "0891234567"
    },
    "products": [
        {
            "id": "PROD-001",
            "name": "หนังสติ๊กอัลลอยด์ยุทธวิธี พร้อมเลเซอร์ช่วยเล็งและระดับน้ำ",
            "category": "slingshot",
            "price": 390.0,
            "stock": 35,
            "image": "https://images.unsplash.com/photo-1595590424283-b8f17842773f?auto=format&fit=crop&w=600&q=80",
            "description": "ด้ามจับอัลลอยด์ แข็งแรงทนทาน น้ำหนักกระชับมือ พร้อมศูนย์เล็งเลเซอร์และระดับน้ำ ช่วยจับเป้าแม่นยำ"
        },
        {
            "id": "PROD-002",
            "name": "หนังสติ๊กสแตนเลส CNC ด้ามไม้ประกบเกรดพรีเมียม",
            "category": "slingshot",
            "price": 550.0,
            "stock": 20,
            "image": "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=600&q=80",
            "description": "สแตนเลส 304 กลึง CNC สวยงาม ไร้สนิม ประกบไม้แท้เนื้อแข็ง จับถนัดมือ ยิงนิ่ง แม่นยำสูง"
        },
        {
            "id": "PROD-003",
            "name": "ยางหนังสติ๊กแบบแบน ไล่สโลป หนา 0.75mm (แพ็ก 5 เส้น)",
            "category": "rubber",
            "price": 120.0,
            "stock": 100,
            "image": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=600&q=80",
            "description": "ยางนำเข้า ยืดหยุ่นสูง แรงดีดสม่ำเสมอ ตัดสโลปมาตรฐาน หนังรองกระสุนไมโครไฟเบอร์ทนทาน"
        },
        {
            "id": "PROD-004",
            "name": "ยางหนังสติ๊กแบบแบน หนา 1.0mm แรงดึงสูงพิเศษ (แพ็ก 5 เส้น)",
            "category": "rubber",
            "price": 140.0,
            "stock": 80,
            "image": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=600&q=80",
            "description": "ยางหนา 1.0 มม. เหมาะสำหรับลูกเหล็ก 8-9 มม. แรงถีบแรง สะใจ ทนทานไม่ขาดง่าย"
        },
        {
            "id": "PROD-005",
            "name": "ลูกเหล็กกลมขัดเงา ขนาด 8 มม. (กล่องละ 500 นัด)",
            "category": "ammo",
            "price": 150.0,
            "stock": 150,
            "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=600&q=80",
            "description": "ลูกเหล็กคาร์บอนเกรดมาตรฐาน กลมเกลี้ยง ผิวเรียบเงา ไม่สะดุดลำกล้องหรือหนังรอง น้ำหนักแม่นยำ"
        },
        {
            "id": "PROD-006",
            "name": "ลูกกระสุนดินเผาผสมสมุนไพร ขนาด 9 มม. รักษ์โลก (1,000 นัด)",
            "category": "ammo",
            "price": 99.0,
            "stock": 200,
            "image": "https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?auto=format&fit=crop&w=600&q=80",
            "description": "กระสุนดินอัดแข็ง โดนเป้าแล้วแตก ย่อยสลายได้ตามธรรมชาติ ไม่เป็นอันตรายต่อสิ่งแวดล้อม"
        },
        {
            "id": "PROD-007",
            "name": "ศูนย์เล็งไฟเบอร์ออปติก + เลเซอร์แดง พร้อมถ่านกระดุม",
            "category": "accessories",
            "price": 190.0,
            "stock": 45,
            "image": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80",
            "description": "อุปกรณ์ช่วยเล็งแบบสองระบบ ไฟเบอร์เรืองแสงกลางวัน และเลเซอร์มองเห็นชัดเจนในที่แสงน้อย"
        },
        {
            "id": "PROD-008",
            "name": "กระเป๋าคาดเอวเก็บหนังสติ๊กและลูกเหล็ก พร้อมแม่เหล็กดูดลูก",
            "category": "accessories",
            "price": 220.0,
            "stock": 60,
            "image": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=600&q=80",
            "description": "กระเป๋าผ้าแคนวาสทหาร มีช่องใส่หนังสติ๊กและช่องใส่ลูกเหล็กพร้อมแถบแม่เหล็กแรงสูง หยิบลูกยิงได้รวดเร็ว"
        }
    ],
    "orders": [
        {
            "id": "ORD-20260817-001",
            "customer_name": "สมชาย ใจดี",
            "phone": "081-999-8877",
            "address": "45/2 หมู่ 3 ต.บางกระดี่ อ.เมือง จ.สมุทรปราการ 10270",
            "shipping_provider": "Flash Express",
            "shipping_cost": 45.0,
            "total_amount": 540.0,
            "status": "PAID",
            "tracking_number": "",
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
            "tracking_number": "",
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
            "tracking_number": "",
            "items": [
                {"product_id": "PROD-003", "name": "ยางหนังสติ๊กแบน 0.75mm (5 เส้น)", "price": 120.0, "quantity": 2},
                {"product_id": "PROD-004", "name": "ยางหนังสติ๊กแบน 1.0mm (5 เส้น)", "price": 140.0, "quantity": 1}
            ],
            "created_at": "2026-08-17 11:55:00"
        }
    ]
}

def load_data():
    if not os.path.exists(DATA_FILE):
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_DATA

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

class SlingshotHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        if path == "/api/products":
            data = load_data()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(data.get("products", []), ensure_ascii=False).encode("utf-8"))
            return

        elif path == "/api/orders":
            data = load_data()
            status_filter = query.get("status", [None])[0]
            orders = data.get("orders", [])
            if status_filter and status_filter != "ALL":
                orders = [o for o in orders if o.get("status") == status_filter]
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(orders, ensure_ascii=False).encode("utf-8"))
            return

        elif path == "/api/orders/track":
            q = query.get("q", [""])[0].strip()
            data = load_data()
            matched = []
            for o in data.get("orders", []):
                if q and (q.lower() in o.get("id", "").lower() or q.replace("-", "") in o.get("phone", "").replace("-", "")):
                    matched.append(o)
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(matched, ensure_ascii=False).encode("utf-8"))
            return

        elif path == "/api/store-info":
            data = load_data()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(data.get("store_info", {}), ensure_ascii=False).encode("utf-8"))
            return

        elif path == "/api/postal-db":
            postal_path = os.path.join(BASE_DIR, "thai_postal_db.json")
            if os.path.exists(postal_path):
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                with open(postal_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.end_headers()
            return

        if path in ["/admin", "/admin.html"]:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            html_path = os.path.join(BASE_DIR, "admin.html")
            with open(html_path, "rb") as f:
                self.wfile.write(f.read())
            return

        if path in ["/", "/index.html", "/track"]:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            html_path = os.path.join(BASE_DIR, "index.html")
            with open(html_path, "rb") as f:
                self.wfile.write(f.read())
            return

        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")
        payload = json.loads(body) if body else {}

        if path == "/api/orders":
            data = load_data()
            now = datetime.datetime.now()
            date_str = now.strftime("%Y%m%d")
            rand_num = random.randint(100, 999)
            order_id = f"ORD-{date_str}-{rand_num}"
            
            new_order = {
                "id": order_id,
                "customer_name": payload.get("customer_name", ""),
                "phone": payload.get("phone", ""),
                "address": payload.get("address", ""),
                "shipping_provider": payload.get("shipping_provider", "Flash Express"),
                "shipping_cost": float(payload.get("shipping_cost", 45)),
                "total_amount": float(payload.get("total_amount", 0)),
                "status": "PAID" if payload.get("paid_now", True) else "PENDING_PAYMENT",
                "tracking_number": "",
                "items": payload.get("items", []),
                "created_at": now.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            data.setdefault("orders", []).insert(0, new_order)
            save_data(data)

            self.send_response(201)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "order": new_order}, ensure_ascii=False).encode("utf-8"))
            return

        elif path == "/api/orders/bulk-confirm":
            order_ids = payload.get("order_ids", [])
            data = load_data()
            updated_orders = []

            for o in data.get("orders", []):
                if not order_ids or o.get("id") in order_ids:
                    if o.get("status") in ["PAID", "PENDING_PAYMENT"]:
                        o["status"] = "SHIPPED"
                        if not o.get("tracking_number"):
                            prefix = "FLS" if "Flash" in o.get("shipping_provider", "") else "JNT"
                            o["tracking_number"] = f"{prefix}-TH{random.randint(10000000, 99999999)}"
                        updated_orders.append(o)

            save_data(data)
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "count": len(updated_orders), "orders": updated_orders}, ensure_ascii=False).encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()

if __name__ == "__main__":
    os.chdir(BASE_DIR)
    load_data()
    print(f"Slingshot Server initialized successfully on port {PORT}")
    with socketserver.TCPServer(("", PORT), SlingshotHandler) as httpd:
        httpd.serve_forever()
