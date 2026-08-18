import json

with open("/working_dir/slingshot-shop/admin.html", "r", encoding="utf-8") as f:
    admin_content = f.read()

# Let's inspect the printLabels function in admin.html
print("Has printLabels:", "function printLabels" in admin_content)
