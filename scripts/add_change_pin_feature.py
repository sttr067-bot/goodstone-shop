import os

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\admin.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add Change Admin PIN box in Tab 3 (Goship & Settings)
change_pin_html = """
                <!-- Change Admin PIN Box -->
                <div class="app-card-subtle p-4 sm:p-5 rounded-2xl border app-border-subtle space-y-3">
                    <h3 class="text-xs sm:text-sm font-black app-text-main flex items-center gap-2">
                        <span>🔑</span> ตั้งรหัสผ่านแอดมินด้วยตนเอง (Change Admin Password / PIN):
                    </h3>
                    <div class="flex flex-col sm:flex-row gap-3 items-stretch sm:items-center">
                        <input type="password" id="new-admin-pin" placeholder="ใส่รหัสผ่านใหม่ที่คุณต้องการ (เช่น 1234 หรือ 9999)" class="flex-grow app-input border app-border rounded-xl px-3 py-2 text-xs font-mono app-text-main focus:ring-2 focus:ring-[#EE4D2D]">
                        <button type="button" onclick="updateAdminPin()" class="bg-[#EE4D2D] hover:bg-[#d73211] text-white font-bold text-xs px-4 py-2 rounded-xl transition-all shadow-sm active:scale-95">
                            💾 บันทึกรหัสผ่านใหม่
                        </button>
                    </div>
                    <span class="text-[10px] app-text-muted block">* รหัสผ่านใหม่จะถูกบันทึกไว้ในเครื่องของคุณทันที</span>
                </div>
"""

target_marker = '<!-- Action Buttons -->'
if target_marker in content and 'id="new-admin-pin"' not in content:
    content = content.replace(target_marker, change_pin_html + "\n                " + target_marker)

# Add updateAdminPin JS function
update_pin_js = """
        function updateAdminPin() {
            const input = document.getElementById("new-admin-pin");
            const val = (input ? input.value : "").trim();
            if (!val) {
                alert("กรุณากรอกรหัสผ่านใหม่ก่อนกดบันทึกครับ");
                return;
            }
            ADMIN_PIN = val;
            localStorage.setItem("goodstone_admin_pin", val);
            alert(`✅ บันทึกรหัสผ่านแอดมินใหม่สำเร็จ!\nรหัสผ่านปัจจุบันของคุณคือ: ${val}`);
            if (input) input.value = "";
        }
"""

if 'function updateAdminPin()' not in content:
    content = content.replace('function logoutAdmin() {', update_pin_js + '\n        function logoutAdmin() {')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Added Change Admin PIN feature successfully!")
