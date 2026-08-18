with open("/working_dir/slingshot-shop/index.html", "r", encoding="utf-8") as f:
    code = f.read()

print("Has btn-pay-cod:", "btn-pay-cod" in code)
print("Has panel-cod:", "panel-cod" in code)
print("Has COD_PENDING:", "COD_PENDING" in code)
