gia_tien_dien = 7000
t = float(input("thoi gian su dung la: "))
U = 220
I = 2.4
if t > 0 :
    P = U * I
    # Tính năng lượng tiêu thụ (kWh)
    E = (P * t) / (1000 * 3600)
    # Tính tiền điện phải trả
    tien_dien = E * gia_tien_dien
    print(f"TIỀN ĐIỆN CỦA MÀY LÀ: {tien_dien:2f} ")
else :
    print("ỦA THỜI GIAN MÀ ÂM ĐƯỢC À , NHẬP LẠI MAU ")