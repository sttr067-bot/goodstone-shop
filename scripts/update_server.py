import re

with open("/working_dir/slingshot-shop/server.py", "r", encoding="utf-8") as f:
    code = f.read()

# Update route serving in server.py
old_route = """        if path in ["/", "/index.html", "/admin", "/track"]:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            html_path = os.path.join(BASE_DIR, "index.html")
            with open(html_path, "rb") as f:
                self.wfile.write(f.read())
            return"""

new_route = """        if path in ["/admin", "/admin.html"]:
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
            return"""

if old_route in code:
    code = code.replace(old_route, new_route)

with open("/working_dir/slingshot-shop/server.py", "w", encoding="utf-8") as f:
    f.write(code)

print("server.py updated to handle /admin separately!")
