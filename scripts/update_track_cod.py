with open("/working_dir/slingshot-shop/track.html", "r", encoding="utf-8") as f:
    track_code = f.read()

# Check how order details are rendered in track.html
old_track_pay_status = """<span class="text-xs font-bold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-300">✓ ชำระเงินแล้ว</span>"""
new_track_pay_status = """${o.payment_method === 'COD' || o.status === 'COD_PENDING' ? '<span class="text-xs font-bold text-amber-800 bg-amber-50 px-2.5 py-1 rounded-full border border-amber-300">💵 เก็บเงินปลายทาง (COD)</span>' : '<span class="text-xs font-bold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-300">✓ ชำระเงินแล้ว</span>'}"""

if old_track_pay_status in track_code:
    track_code = track_code.replace(old_track_pay_status, new_track_pay_status)

with open("/working_dir/slingshot-shop/track.html", "w", encoding="utf-8") as f:
    f.write(track_code)

print("track.html updated with COD!")
