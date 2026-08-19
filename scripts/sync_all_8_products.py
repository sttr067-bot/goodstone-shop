import os, json

data_json_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\data.json"
index_html_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\index.html"

with open(data_json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

products_list = data["products"]
products_json_str = json.dumps(products_list, ensure_ascii=False)

with open(index_html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace DEFAULT_PRODUCTS in index.html with full 8 products array
marker_start = "const DEFAULT_PRODUCTS = "
marker_end = "];"

pos_start = content.find(marker_start)
if pos_start != -1:
    pos_end = content.find(marker_end, pos_start) + len(marker_end)
    new_default_js = f"const DEFAULT_PRODUCTS = {products_json_str};"
    content = content[:pos_start] + new_default_js + content[pos_end:]

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Synced all {len(products_list)} products into DEFAULT_PRODUCTS in index.html successfully!")
