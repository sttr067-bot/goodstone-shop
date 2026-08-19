import os

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\admin.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Improved checkAdminAuth and updateAdminPin logic
old_auth_js = """        let ADMIN_PIN = localStorage.getItem("goodstone_admin_pin") || "8888";

        function checkAdminAuth() {
            const inputEl = document.getElementById("admin-pass-input");
            const errEl = document.getElementById("auth-error-msg");
            const overlay = document.getElementById("admin-auth-overlay");
            const val = (inputEl ? inputEl.value : "").trim();

            if (val === ADMIN_PIN || val === "goodstone8888" || val === "1234") {
                sessionStorage.setItem("goodstone_admin_authed", "true");
                if (overlay) overlay.classList.add("hidden");
                if (errEl) errEl.classList.add("hidden");
                if (inputEl) inputEl.value = "";
            } else {
                if (errEl) errEl.classList.remove("hidden");
                if (inputEl) inputEl.value = "";
            }
        }"""

new_auth_js = """        let ADMIN_PIN = localStorage.getItem("goodstone_admin_pin") || "8888";

        function checkAdminAuth() {
            const inputEl = document.getElementById("admin-pass-input");
            const errEl = document.getElementById("auth-error-msg");
            const overlay = document.getElementById("admin-auth-overlay");
            const val = (inputEl ? inputEl.value : "").trim();

            const activePin = localStorage.getItem("goodstone_admin_pin") || ADMIN_PIN || "8888";

            if (val === activePin) {
                sessionStorage.setItem("goodstone_admin_authed", "true");
                if (overlay) overlay.classList.add("hidden");
                if (errEl) errEl.classList.add("hidden");
                if (inputEl) inputEl.value = "";
            } else {
                if (errEl) errEl.classList.remove("hidden");
                if (inputEl) inputEl.value = "";
            }
        }"""

if old_auth_js in content:
    content = content.replace(old_auth_js, new_auth_js)

old_update_pin_js = """        function updateAdminPin() {
            const input = document.getElementById("new-admin-pin");
            const val = (input ? input.value : "").trim();
            if (!val) {
                alert("กรุณากรอกรหัสผ่านใหม่ก่อนกดบันทึกครับ");
                return;
            }
            ADMIN_PIN = val;
            localStorage.setItem("goodstone_admin_pin", val);
            alert(`✅ บันทึกรหัสผ่านแอดมินใหม่สำเร็จ!
รหัสผ่านปัจจุบันของคุณคือ: ${val}`);
            if (input) input.value = "";
        }"""

new_update_pin_js = """        function updateAdminPin() {
            const input = document.getElementById("new-admin-pin");
            const val = (input ? input.value : "").trim();
            if (!val) {
                alert("กรุณากรอกรหัสผ่านใหม่ก่อนกดบันทึกครับ");
                return;
            }
            ADMIN_PIN = val;
            localStorage.setItem("goodstone_admin_pin", val);
            
            const currentPinDisplay = document.getElementById("current-saved-pin-display");
            if (currentPinDisplay) currentPinDisplay.innerText = val;

            alert(`✅ บันทึกรหัสผ่านแอดมินใหม่เรียบร้อยแล้ว!\\n\\nรหัสผ่านแอดมินที่คุณตั้งไว้คือ: ${val}\\n(เมื่อล็อกเอาต์หรือเข้าใหม่ ให้ใช้รหัส ${val} นี้เข้าใช้งานได้ทันทีครับ)`);
            if (input) input.value = "";
        }"""

if old_update_pin_js in content:
    content = content.replace(old_update_pin_js, new_update_pin_js)

# Update HTML in Goship tab to display current active saved PIN
old_pin_box_html = """                <!-- Change Admin PIN Box -->
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
                </div>"""

new_pin_box_html = """                <!-- Change Admin PIN Box -->
                <div class="app-card-subtle p-4 sm:p-5 rounded-2xl border app-border-subtle space-y-3">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                        <h3 class="text-xs sm:text-sm font-black app-text-main flex items-center gap-2">
                            <span>🔑</span> ตั้งรหัสผ่านแอดมินด้วยตนเอง (Change Admin Password / PIN)
                        </h3>
                        <div class="text-xs app-text-muted">
                            รหัสปัจจุบันที่บันทึกไว้: <strong id="current-saved-pin-display" class="text-[#EE4D2D] font-mono text-sm">8888</strong>
                        </div>
                    </div>
                    <div class="flex flex-col sm:flex-row gap-3 items-stretch sm:items-center">
                        <input type="password" id="new-admin-pin" placeholder="ใส่รหัสผ่านใหม่ที่คุณต้องการ (เช่น 1234 หรือ 9999)" class="flex-grow app-input border app-border rounded-xl px-3 py-2 text-xs font-mono app-text-main focus:ring-2 focus:ring-[#EE4D2D]">
                        <button type="button" onclick="updateAdminPin()" class="bg-[#EE4D2D] hover:bg-[#d73211] text-white font-bold text-xs px-4 py-2 rounded-xl transition-all shadow-sm active:scale-95 cursor-pointer">
                            💾 บันทึกรหัสผ่านใหม่
                        </button>
                    </div>
                </div>"""

if old_pin_box_html in content:
    content = content.replace(old_pin_box_html, new_pin_box_html)

# Add loadGoshipConfig call to update current-saved-pin-display text
if 'document.getElementById("goship-auto-tracking").checked = cfg.autoTracking ?? true;' in content:
    content = content.replace(
        'document.getElementById("goship-auto-tracking").checked = cfg.autoTracking ?? true;',
        'document.getElementById("goship-auto-tracking").checked = cfg.autoTracking ?? true;\n                    const activePin = localStorage.getItem("goodstone_admin_pin") || "8888";\n                    const pDisplay = document.getElementById("current-saved-pin-display");\n                    if (pDisplay) pDisplay.innerText = activePin;'
    )

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed admin PIN saving and display logic successfully!")
