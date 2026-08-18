import json
import base64
import os

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))
products_json = json.dumps(data["products"], ensure_ascii=False)
orders_json = json.dumps(data["orders"], ensure_ascii=False)

# Read Thai address database
addresses_data = [
  {"postal_code": "10150", "subdistrict": "ท่าข้าม", "district": "บางขุนเทียน", "province": "กรุงเทพมหานคร", "is_remote": False},
  {"postal_code": "10150", "subdistrict": "แสมดำ", "district": "บางขุนเทียน", "province": "กรุงเทพมหานคร", "is_remote": False},
  {"postal_code": "10140", "subdistrict": "บางมด", "district": "ทุ่งครุ", "province": "กรุงเทพมหานคร", "is_remote": False},
  {"postal_code": "10400", "subdistrict": "สามเสนใน", "district": "พญาไท", "province": "กรุงเทพมหานคร", "is_remote": False},
  {"postal_code": "10330", "subdistrict": "ปทุมวัน", "district": "ปทุมวัน", "province": "กรุงเทพมหานคร", "is_remote": False},
  {"postal_code": "10110", "subdistrict": "คลองเตย", "district": "คลองเตย", "province": "กรุงเทพมหานคร", "is_remote": False},
  {"postal_code": "10270", "subdistrict": "บางกระดี่", "district": "เมืองสมุทรปราการ", "province": "สมุทรปราการ", "is_remote": False},
  {"postal_code": "11000", "subdistrict": "บางกระสอ", "district": "เมืองนนทบุรี", "province": "นนทบุรี", "is_remote": False},
  {"postal_code": "12000", "subdistrict": "บางปรอก", "district": "เมืองปทุมธานี", "province": "ปทุมธานี", "is_remote": False},
  {"postal_code": "20000", "subdistrict": "บางปลาสร้อย", "district": "เมืองชลบุรี", "province": "ชลบุรี", "is_remote": False},
  {"postal_code": "20150", "subdistrict": "หนองปรือ", "district": "บางละมุง", "province": "ชลบุรี (พัทยา)", "is_remote": False},
  {"postal_code": "30000", "subdistrict": "ในเมือง", "district": "เมืองนครราชสีมา", "province": "นครราชสีมา", "is_remote": False},
  {"postal_code": "40000", "subdistrict": "ในเมือง", "district": "เมืองขอนแก่น", "province": "ขอนแก่น", "is_remote": False},
  {"postal_code": "50000", "subdistrict": "ศรีภูมิ", "district": "เมืองเชียงใหม่", "province": "เชียงใหม่", "is_remote": False},
  {"postal_code": "65000", "subdistrict": "บ้านคลอง", "district": "เมืองพิษณุโลก", "province": "พิษณุโลก", "is_remote": False},
  {"postal_code": "83000", "subdistrict": "ตลาดใหญ่", "district": "เมืองภูเก็ต", "province": "ภูเก็ต", "is_remote": False},
  {"postal_code": "90000", "subdistrict": "บ่อยาง", "district": "เมืองสงขลา", "province": "สงขลา", "is_remote": False},
  {"postal_code": "90110", "subdistrict": "หาดใหญ่", "district": "หาดใหญ่", "province": "สงขลา", "is_remote": False},

  # Remote Areas: Islands & Mountains & 3 Southern Border Provinces
  {"postal_code": "84320", "subdistrict": "บ่อผุด", "district": "เกาะสมุย", "province": "สุราษฎร์ธานี", "is_remote": True},
  {"postal_code": "84320", "subdistrict": "แม่น้ำ", "district": "เกาะสมุย", "province": "สุราษฎร์ธานี", "is_remote": True},
  {"postal_code": "84360", "subdistrict": "เกาะพะงัน", "district": "เกาะพะงัน", "province": "สุราษฎร์ธานี", "is_remote": True},
  {"postal_code": "84360", "subdistrict": "เกาะเต่า", "district": "เกาะพะงัน", "province": "สุราษฎร์ธานี", "is_remote": True},
  {"postal_code": "23170", "subdistrict": "เกาะช้าง", "district": "เกาะช้าง", "province": "ตราด", "is_remote": True},
  {"postal_code": "23120", "subdistrict": "เกาะกูด", "district": "เกาะกูด", "province": "ตราด", "is_remote": True},
  {"postal_code": "81150", "subdistrict": "เกาะลันตา", "district": "เกาะลันตา", "province": "กระบี่", "is_remote": True},
  {"postal_code": "82160", "subdistrict": "เกาะยาว", "district": "เกาะยาว", "province": "พังงา", "is_remote": True},
  {"postal_code": "95000", "subdistrict": "สะเตง", "district": "เมืองยะลา", "province": "ยะลา", "is_remote": True},
  {"postal_code": "95110", "subdistrict": "เบตง", "district": "เบตง", "province": "ยะลา", "is_remote": True},
  {"postal_code": "94000", "subdistrict": "สะบารัง", "district": "เมืองปัตตานี", "province": "ปัตตานี", "is_remote": True},
  {"postal_code": "96000", "subdistrict": "บางนาค", "district": "เมืองนราธิวาส", "province": "นราธิวาส", "is_remote": True},
  {"postal_code": "96110", "subdistrict": "สุไหงโก-ลก", "district": "สุไหงโก-ลก", "province": "นราธิวาส", "is_remote": True},
  {"postal_code": "58000", "subdistrict": "จองคำ", "district": "เมืองแม่ฮ่องสอน", "province": "แม่ฮ่องสอน", "is_remote": True},
  {"postal_code": "58110", "subdistrict": "ปาย", "district": "ปาย", "province": "แม่ฮ่องสอน", "is_remote": True},
  {"postal_code": "63170", "subdistrict": "อุ้มผาง", "district": "อุ้มผาง", "province": "ตาก", "is_remote": True}
]
addresses_json = json.dumps(addresses_data, ensure_ascii=False)

print("Address data prepared. Now assembling index.html and admin.html...")
