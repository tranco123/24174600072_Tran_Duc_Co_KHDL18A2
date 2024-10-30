# Viết chương trình tìm số lớn nhất trong 3 số 
print("Cậu hãy nhập dãy số ccủa mình :")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if a >= b and a >= c :
    print(f"Số lớn nhất trong ba số là : {a}")
elif b >= a and b >= c :
    print(f"Số lớn nhất trong ba số là : {b}")
else :
    print(f"Số lớn nhất trong ba số là : {c}")