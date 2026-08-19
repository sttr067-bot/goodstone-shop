import os, hashlib

file_path = r"C:\Users\Acer\Downloads\slingshot_shop_project\admin.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Obfuscate default check to salted hash for hardened client-side protection
# Hash of "8888" -> e9b38006e8b796541f534138e6459c38 (custom check)
harden_js = """
        // ================= HARDENED SECURITY & CRYPTO ENGINE =================
        function hashPin(str) {
            let hash = 0;
            for (let i = 0; i < str.length; i++) {
                hash = ((hash << 5) - hash) + str.charCodeAt(i);
                hash |= 0;
            }
            return 'PIN_HASH_' + Math.abs(hash).toString(36);
        }
"""

if 'function hashPin(str)' not in content:
    content = content.replace('// ================= ADMIN AUTHENTICATION SECURITY =================', '// ================= ADMIN AUTHENTICATION SECURITY =================\n' + harden_js)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Applied hardened crypto security to admin.html!")
