U = 220 
I = 2.7 
gia_tien_dien = 7000
t = float(input("Thời gian sử dụng điện là: "))
P = U * I 
# Lượng điện tiêu thụ là 
W = P * t / 3600 * 1000 #kwh
# Tiền điện phải trả là 
tien_dien = W * gia_tien_dien 
print(f"TIỀN ĐIỆN CỦA MÀY LÀ: {tien_dien:2f} ")