import math

# Nhập bán kính và chiều cao từ 
r = float(input("Nhập bán kính của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))
pi = 3.14
if r > 0 and h > 0 :

    dien_tich_xung_quanh = 2 * pi * r * h
    dien_tich_toan_phan = dien_tich_xung_quanh + 2 * pi * r**2
    the_tich = pi * r**2 * h
    print(f"Diện tích xung quanh của khối trụlà: {dien_tich_xung_quanh}")
    print(f"Diện tích toàn phần của khối trụ là: {dien_tich_toan_phan}")
    print(f"Thể tích của khối trụ là: {the_tich}")
else :
    print(f"BAN DA NHAP SAI BIEN r VA h ")