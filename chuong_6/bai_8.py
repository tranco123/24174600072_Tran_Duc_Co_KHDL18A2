import math 
x = float(input("Nhập giá trị x: "))
G = math.log(4) / math.log(x) + math.log(2) / math.log(x)
print(f"Giá trị của G là: {G:4.2f}")