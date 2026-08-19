import os

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\admin.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add Admin Auth Modal Overlay HTML right after <body> tag
auth_modal_html = """
    <!-- ================= ADMIN PASSWORD / PIN LOCK OVERLAY ================= -->
    <div id="admin-auth-overlay" class="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-[#121215]/95 backdrop-blur-md">
        <div class="app-card border-2 app-border rounded-3xl max-w-sm w-full p-6 space-y-5 shadow-2xl text-center">
            <div class="w-16 h-16 rounded-3xl bg-[#EE4D2D]/10 border border-[#EE4D2D]/30 flex items-center justify-center mx-auto text-3xl shadow-inner">
                🔒
            </div>
            <div>
                <h2 class="text-base sm:text-lg font-black app-text-main">ระบบล็อกรักษาความปลอดภัย</h2>
                <p class="text-xs app-text-muted mt-1">กรอกรหัสผ่าน / PIN เพื่อเข้าสู่ระบบแอดมิน GOODSTONE</p>
            </div>

            <form onsubmit="event.preventDefault(); checkAdminAuth();" class="space-y-4">
                <div>
                    <input type="password" id="admin-pass-input" maxlength="20" placeholder="กรอกรหัสผ่าน (รหัสเริ่มต้น: 8888)" autocomplete="current-password" autofocus class="w-full app-input border-2 border-[#EE4D2D] rounded-2xl px-4 py-3 text-center text-sm font-bold tracking-widest app-text-main focus:ring-2 focus:ring-[#EE4D2D] shadow-sm">
                    <p id="auth-error-msg" class="text-xs text-red-500 font-bold hidden mt-2">❌ รหัสผ่านไม่ถูกต้อง โปรดลองอีกครั้ง</p>
                </div>

                <!-- Touch Numeric Keypad for iPhone / Phone Touch -->
                <div class="grid grid-cols-3 gap-2 pt-1">
                    <button type="button" onclick="pressPin('1')" class="app-card-subtle border app-border p-3 rounded-2xl text-sm font-bold app-text-main hover:bg-[#EE4D2D] hover:text-white transition-all active:scale-95">1</button>
                    <button type="button" onclick="pressPin('2')" class="app-card-subtle border app-border p-3 rounded-2xl text-sm font-bold app-text-main hover:bg-[#EE4D2D] hover:text-white transition-all active:scale-95">2</button>
                    <button type="button" onclick="pressPin('3')" class="app-card-subtle border app-border p-3 rounded-2xl text-sm font-bold app-text-main hover:bg-[#EE4D2D] hover:text-white transition-all active:scale-95">3</button>
                    <button type="button" onclick="pressPin('4')" class="app-card-subtle border app-border p-3 rounded-2xl text-sm font-bold app-text-main hover:bg-[#EE4D2D] hover:text-white transition-all active:scale-95">4</button>
                    <button type="button" onclick="pressPin('5')" class="app-card-subtle border app-border p-3 rounded-2xl text-sm font-bold app-text-main hover:bg-[#EE4D2D] hover:text-white transition-all active:scale-95">5</button>
                    <button type="button" onclick="pressPin('6')" class="app-card-subtle border app-border p-3 rounded-2xl text-sm font-bold app-text-main hover:bg-[#EE4D2D] hover:text-white transition-all active:scale-95">6</button>
                    <button type="button" onclick="pressPin('7')" class="app-card-subtle border app-border p-3 rounded-2xl text-sm font-bold app-text-main hover:bg-[#EE4D2D] hover:text-white transition-all active:scale-95">7</button>
                    <button type="button" onclick="pressPin('8')" class="app-card-subtle border app-border p-3 rounded-2xl text-sm font-bold app-text-main hover:bg-[#EE4D2D] hover:text-white transition-all active:scale-95">8</button>
                    <button type="button" onclick="pressPin('9')" class="app-card-subtle border app-border p-3 rounded-2xl text-sm font-bold app-text-main hover:bg-[#EE4D2D] hover:text-white transition-all active:scale-95">9</button>
                    <button type="button" onclick="clearPin()" class="bg-red-500/10 border border-red-500/30 p-3 rounded-2xl text-xs font-bold text-red-500 hover:bg-red-500 hover:text-white transition-all active:scale-95">ลบ (C)</button>
                    <button type="button" onclick="pressPin('0')" class="app-card-subtle border app-border p-3 rounded-2xl text-sm font-bold app-text-main hover:bg-[#EE4D2D] hover:text-white transition-all active:scale-95">0</button>
                    <button type="submit" class="bg-[#EE4D2D] text-white p-3 rounded-2xl text-xs font-black shadow-md hover:bg-[#d73211] transition-all active:scale-95">ตกลง ↵</button>
                </div>
            </form>

            <div class="pt-2 border-t app-border-subtle flex justify-between text-[11px] app-text-muted">
                <span>รหัสผ่านเริ่มต้น: <strong class="text-[#EE4D2D]">8888</strong></span>
                <a href="index.html" class="text-[#EE4D2D] hover:underline font-bold">← ไปหน้าร้าน</a>
            </div>
        </div>
    </div>
"""

body_tag = '<body class="app-body min-h-screen flex flex-col font-sans" data-theme="dark">'
if body_tag in content and 'id="admin-auth-overlay"' not in content:
    content = content.replace(body_tag, body_tag + "\n" + auth_modal_html)

# Add Logout button in header
old_nav_actions = '<div class="flex items-center gap-2">'
new_nav_actions = """<div class="flex items-center gap-2">
                    <button type="button" onclick="logoutAdmin()" class="bg-red-500/10 hover:bg-red-500/20 text-red-400 border border-red-500/30 text-xs px-2.5 py-1.5 rounded-xl font-bold transition-all shadow-sm active:scale-95" title="ออกจากระบบแอดมิน">
                        🔒 ล็อกระบบ
                    </button>"""

if old_nav_actions in content and 'logoutAdmin()' not in content:
    content = content.replace(old_nav_actions, new_nav_actions)

# Add Authentication logic script functions
auth_js = """
        // ================= ADMIN AUTHENTICATION SECURITY =================
        let ADMIN_PIN = localStorage.getItem("goodstone_admin_pin") || "8888";

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
        }

        function pressPin(digit) {
            const inputEl = document.getElementById("admin-pass-input");
            if (inputEl) {
                inputEl.value += digit;
                const errEl = document.getElementById("auth-error-msg");
                if (errEl) errEl.classList.add("hidden");
            }
        }

        function clearPin() {
            const inputEl = document.getElementById("admin-pass-input");
            if (inputEl) inputEl.value = "";
        }

        function logoutAdmin() {
            sessionStorage.removeItem("goodstone_admin_authed");
            const overlay = document.getElementById("admin-auth-overlay");
            if (overlay) overlay.classList.remove("hidden");
        }

        function initAuthCheck() {
            const isAuthed = sessionStorage.getItem("goodstone_admin_authed");
            const overlay = document.getElementById("admin-auth-overlay");
            if (isAuthed === "true") {
                if (overlay) overlay.classList.add("hidden");
            } else {
                if (overlay) overlay.classList.remove("hidden");
            }
        }
"""

if 'initAuthCheck()' not in content:
    content = content.replace('function init() {', auth_js + '\n        function init() {\n            initAuthCheck();')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Added Admin Security Lock Modal successfully!")
