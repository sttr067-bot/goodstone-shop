import json

data = json.load(open("/working_dir/slingshot-shop/data.json", "r", encoding="utf-8"))
print("Products count:", len(data["products"]))
