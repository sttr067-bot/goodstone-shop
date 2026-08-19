import os

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

floating_js = """
        function updateFloatingCTA() {
            const cta = document.getElementById('floating-cta');
            const catalogVisible = document.getElementById('view-catalog') && !document.getElementById('view-catalog').classList.contains('hidden');
            if (cta) {
                if (catalogVisible && window.scrollY > 200) {
                    cta.classList.remove('hidden');
                } else {
                    cta.classList.add('hidden');
                }
            }
        }
        window.addEventListener('scroll', updateFloatingCTA);
"""

if "function updateFloatingCTA()" not in content:
    content = content.replace("window.onload = init;", floating_js + "\n        window.onload = init;")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Added updateFloatingCTA scroll logic successfully!")
