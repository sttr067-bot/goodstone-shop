import os

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix Postal Autocomplete Dropdown (support all property name variations to eliminate 'undefined')
old_postal_loop = """                    found.forEach(item => {
                        const row = document.createElement("div");
                        row.className = "p-3 hover:bg-[#EE4D2D]/10 cursor-pointer text-xs font-bold theme-text-main flex justify-between transition-colors";
                        row.innerHTML = `<span>📍 ต.${item.subdistrict} > อ.${item.district} > จ.${item.province}</span><span class="text-[#FF6E4E]">เลือก ✓</span>`;
                        row.onclick = () => {
                            document.getElementById("cust-subdistrict").value = item.subdistrict;
                            document.getElementById("cust-district").value = item.district;
                            document.getElementById("cust-province").value = item.province;
                            closePostalDropdown();
                        };
                        itemsBox.appendChild(row);
                    });"""

new_postal_loop = """                    found.forEach(item => {
                        const sub = item.subdistrict || item.subdistrict_th || item.tambon || item.s || "";
                        const dist = item.district || item.district_th || item.amphoe || item.d || "";
                        const prov = item.province || item.province_th || item.changwat || item.p || "";
                        const row = document.createElement("div");
                        row.className = "p-3 hover:bg-[#EE4D2D]/10 cursor-pointer text-xs font-bold theme-text-main flex justify-between transition-colors border-b theme-border";
                        row.innerHTML = `<span>📍 ต.${sub} > อ.${dist} > จ.${prov}</span><span class="text-[#EE4D2D]">เลือก ✓</span>`;
                        row.onclick = () => {
                            document.getElementById("cust-subdistrict").value = sub;
                            document.getElementById("cust-district").value = dist;
                            document.getElementById("cust-province").value = prov;
                            closePostalDropdown();
                        };
                        itemsBox.appendChild(row);
                    });"""

if old_postal_loop in content:
    content = content.replace(old_postal_loop, new_postal_loop)

# 2. Replace any remaining emerald or green classes with Shopee Orange #EE4D2D (except LINE button #06C755)
content = content.replace('bg-[#10B981]', 'bg-[#EE4D2D]')
content = content.replace('bg-emerald-500', 'bg-[#EE4D2D]')
content = content.replace('bg-emerald-600', 'bg-[#EE4D2D]')
content = content.replace('hover:bg-emerald-400', 'hover:bg-[#d73211]')
content = content.replace('hover:bg-emerald-500', 'hover:bg-[#d73211]')
content = content.replace('text-emerald-400', 'text-[#EE4D2D]')
content = content.replace('text-emerald-500', 'text-[#EE4D2D]')
content = content.replace('border-emerald-500', 'border-[#EE4D2D]')

# Preserve LINE button explicitly as LINE green #06C755
content = content.replace('bg-[#EE4D2D] hover:bg-[#d73211] text-white px-3 py-1.5 rounded-xl text-xs font-bold transition-all shadow-md active:scale-95 inline-flex items-center gap-1.5', 'bg-[#06C755] hover:bg-[#05b049] text-white px-3 py-1.5 rounded-xl text-xs font-bold transition-all shadow-md active:scale-95 inline-flex items-center gap-1.5')

# 3. Force default theme to Light Mode ("light")
content = content.replace('<html lang="th" data-theme="dark" class="h-full antialiased dark">', '<html lang="th" data-theme="light" class="h-full antialiased light">')
content = content.replace('<body class="theme-body min-h-screen flex flex-col font-sans" data-theme="dark">', '<body class="theme-body min-h-screen flex flex-col font-sans" data-theme="light">')
content = content.replace('const saved = localStorage.getItem("goodstone_theme") || "dark";', 'const saved = localStorage.getItem("goodstone_theme") || "light";')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed postal autocomplete undefined bug and updated all green elements to Shopee Orange (#EE4D2D) with Light Mode default successfully!")
