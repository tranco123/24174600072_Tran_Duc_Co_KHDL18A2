# 2. Viết chương trình kiểm tra xem điểm M(x,y) có nằm trong hình tròn tâm I(a,b) và bán kính 12
# R bằng cách xuất ra giá trị True nếu điểm M nằm trong hoặc trên hình tròn và False nếu nằm ngoài hình tròn, 
# với x, y, a, b, R nhập vào từ bàn phím?
import math 
print("Nhập tọa đọo của điểm M")
x = float(input("x="))
y = float(input("y="))
print("Nhập tọa độ tâm I")
a = float(input("a="))
b = float(input("b="))
R = 12
# gọi d là độ dài của M đến tâm y 
d = math.sqrt((x - a) ** 2 + (y - b) ** 2)
if d > R :
    print("TRUE")
    if d == R :
        print("Điểm M nằm trên hình tròn")
else :
    print ("FALSE")