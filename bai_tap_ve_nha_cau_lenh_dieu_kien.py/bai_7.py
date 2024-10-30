# 7. Viết chương trình giải hệ phương trình 2 ẩn:
# 	    a_1*x + b_1*y = c_1
#       a_2*x + b_2*y = c_2
# Các hệ số a1, a2, b1, b2, c1, c2 nhập từ bàn phím. Xét tất cả các trường hợp cụ thể
# Công thức Cramer2 dùng tính hệ phương trình 2 ẩn
a_1 = float(input("Nhập hệ số a_1 :"))
b_1 = float(input("Nhập hệ số b_1 :"))
a_2 = float(input("Nhập hệ số a_2 :"))
b_2 = float(input("Nhập hệ số b_2 :"))
c_1 = float(input("Nhập hệ số c_1 :"))
c_2 = float(input("Nhập hệ số c_2 :"))
D = a_1 * b_2 - a_2 * b_1 
D_x = b_1 * c_2 - c_1 * b_2 
D_y = a_1 * c_2 - a_2 * c_1 
if D != 0 :
    x = D_x / D 
    y = D_y / D 
    print(f"Giá trị của x là : {x}")
    print(f"Giá trị của y là : {y}")
elif (D == 0 ) and (D_x == 0) or (D_y == 0) :
    print("Hệ này của bạn có vô số nghiệm")
else :
    print("Hệ này của bạn vô nghiệm ")