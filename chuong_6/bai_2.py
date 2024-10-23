import math 

x = float(input("Nhập giá trị x là: "))
F = (-x + math.sqrt(x ** 2 + 4 )) / (x ** 4 + 1) ** (1/7)
print(f"Giá trị của f là: {F:.2f}")
