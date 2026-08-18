import json
import os

data = {"products": [{"id": 1, "name": "หนังสติ๊กสแตนเลส เลเซอร์ช่วยเล็ง", "price": 450, "stock": 50}]}
with open('/working_dir/slingshot-shop/data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open('/working_dir/slingshot-shop/data.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)

print("JSON Storage working:", loaded)
