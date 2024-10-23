import math 
a = float(input("NHẬP GIA TỐC CỦA XE LÀ: "))
if a > 0 :
    t = -(1 / math.log(5) / math.log(4) * a ** 4)
    print(f"Vận chuyển động là: {t:.2f}")
else :
    print("Bạn đã nhập giá trị gia tốc sai, xin vui lòng nhìn lại đề bài ")
    