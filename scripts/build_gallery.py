import json

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))

# Add multi-image gallery for each product
for p in data["products"]:
    cat_folder = "slingshots" if p["category"] == "slingshot" else ("rubber-bands" if p["category"] == "rubber" else ("ammo" if p["category"] == "ammo" else "accessories"))
    base_id = p["id"].lower()
    
    # 3-4 images per product with folder names
    p["images"] = [
        {
            "file": f"images/{cat_folder}/{base_id}_main.jpg",
            "name": f"{base_id}_main.jpg (ภาพรวมสินค้ามุมตรง)",
            "fallback": p.get("fallback_image", "")
        },
        {
            "file": f"images/{cat_folder}/{base_id}_detail1.jpg",
            "name": f"{base_id}_detail1.jpg (ซูมรายละเอียดวัสดุ/สเปก)",
            "fallback": p.get("fallback_image", "")
        },
        {
            "file": f"images/{cat_folder}/{base_id}_detail2.jpg",
            "name": f"{base_id}_detail2.jpg (มุมมองด้านข้างและอุปกรณ์แถม)",
            "fallback": p.get("fallback_image", "")
        },
        {
            "file": f"images/{cat_folder}/{base_id}_package.jpg",
            "name": f"{base_id}_package.jpg (อุปกรณ์ในกล่องพัสดุพร้อมส่ง)",
            "fallback": p.get("fallback_image", "")
        }
    ]

with open("/working_dir/slingshot-shop/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("data.json updated with multi-image gallery support!")
