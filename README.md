# 🎯 GOODSTONE Slingshot Shop (Tactical E-Commerce Web Application)

ระบบเว็บแอปพลิเคชันร้านค้าออนไลน์ (E-Commerce Storefront + Admin Management) สำหรับ **GOODSTONE Slingshot Shop** พัฒนาขึ้นในรูปแบบ Standalone / Static-First รองรับการใช้งานผ่านเบราว์เซอร์ และ backend server น้ำหนักเบาด้วย Python

---

## 🌟 ฟีเจอร์หลัก (Features)

### 🛒 หน้าร้านค้า (Storefront - `index.html`)
- **UI/UX ดีไซน์สวยงาม**: รองรับทั้งโหมดมืด (Dark Mode) และโหมดสว่าง (Light Mode)
- **ระบบตะกร้าสินค้า & สั่งซื้อด่วน**: เลือกสินค้า, คำนวณราคา, ค่าจัดส่งอัตโนมัติ
- **การชำระเงินหลากหลาย**: รองรับ PromptPay (พร้อมเพย์), เก็บเงินปลายทาง (COD +3%), และ Wallet
- **SEO & Social Share**: ตั้งค่า Open Graph, Meta Tags, `sitemap.xml` และ `robots.txt` พร้อมรองรับ Search Engine

### 📦 ระบบหลังบ้าน (Admin Panel - `admin.html`)
- **การจัดการคำสั่งซื้อ (Order Management)**: ตรวจสอบรายการสั่งซื้อ, อัปเดตสถานะ (PAID / SHIPPED / PENDING)
- **การจัดการสต็อก & สินค้า (Inventory Management)**: เพิ่ม/แก้ไข/ลบสินค้า, ราคา variants, รูปภาพสินค้าหลายมุมมอง
- **ระบบขนส่ง (Logistics Gateway)**: รองรับการออกเลขพัสดุและเชื่อมต่อ Goship API (SPX Express & ไปรษณีย์ไทย EMS)
- **พิมพ์ใบปะหน้าพัสดุ**: สร้างใบปะหน้ามาตรฐาน 4x6 พร้อมบาร์โค้ดสำหรับจัดส่ง
- **มอนิเตอร์รายได้ & เพดานภาษี (VAT Monitor)**: สรุปยอดขายสะสมเทียบกับเพดานภาษีมูลค่าเพิ่ม 1.8 ล้านบาท/ปี

### 🚚 ระบบติดตามพัสดุ (Parcel Tracking - `track.html`)
- ตรวจสอบสถานะคำสั่งซื้อด้วย **รหัสคำสั่งซื้อ (Order ID)** หรือ **เบอร์โทรศัพท์**
- แสดงรายละเอียดการจัดส่งและเลข Tracking Number ของขนส่ง

---

## 📁 โครงสร้างโปรเจกต์ (Project Structure)

```text
slingshot_shop_project/
├── index.html        # หน้าร้านค้าสำหรับลูกค้า (Storefront UI)
├── admin.html        # ระบบบริหารจัดการหลังบ้าน (Admin Dashboard)
├── track.html        # หน้าตรวจสอบสถานะพัสดุ (Order & Parcel Tracking)
├── server.py         # Python HTTP & REST API Server (Backend)
├── data.json         # ฐานข้อมูลสินค้า ร้านค้า และรายการสั่งซื้อ (JSON Data Store)
├── robots.txt        # ไฟล์กำหนดสิทธิ์ Search Engine Crawler
├── sitemap.xml       # ผังเว็บไซต์สำหรับ SEO Search Engines
├── images/           # โฟลเดอร์เก็บรูปภาพสินค้าและสื่อต่างๆ
├── scripts/          # สคริปต์เสริมสำหรับสร้าง/อัปเดตระบบ (Build & Migration Scripts)
├── .gitignore        # ไฟล์ยกเว้นการ Commit ขึ้น Git
└── README.md         # เอกสารอธิบายโปรเจกต์
```

---

## 🚀 วิธีการติดตั้งและรันใช้งาน (Getting Started)

### 1. การรันเซิร์ฟเวอร์ท้องถิ่น (Local Development)

คุณสามารถรันระบบ Backend REST API และ Serve หน้าเว็บได้ง่ายๆ ด้วย **Python 3** (ไม่ต้องติดตั้ง Node.js):

```bash
python server.py
```

เมื่อรันสำเร็จ สามารถเปิดเบราว์เซอร์เข้าใช้งานได้ที่:
- **หน้าร้านค้า**: `http://localhost:8000/` หรือ `http://localhost:8000/index.html`
- **ระบบหลังบ้าน**: `http://localhost:8000/admin` หรือ `http://localhost:8000/admin.html`
- **ติดตามพัสดุ**: `http://localhost:8000/track` หรือ `http://localhost:8000/track.html`

---

## 📄 ใบอนุญาตและการใช้งาน (License)

สิทธิ์การใช้งานและการพัฒนาเป็นของร้าน GOODSTONE Slingshot Shop
