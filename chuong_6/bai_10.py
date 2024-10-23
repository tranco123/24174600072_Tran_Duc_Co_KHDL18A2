import math 
a = float(input("NHẬP GIA TỐC CỦA XE LÀ: "))
t = float(input("THỜI GIAN XE CHẠY LÀ: "))
v = - t * math.log(5) / math.log(4) * a ** 4
print(f"Vận chuyển động là: {v:.2f}")