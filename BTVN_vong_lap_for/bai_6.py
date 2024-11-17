# Viết chương trình nhập vào một số kiểm tra xem số đó có phải số chính phương hay không?
import math 
n = int(input("Nhập số mà bạn muốn kiểm tra là : "))
tinh_can = math.sqrt(n)
if (tinh_can * tinh_can == n ):
    print(f"Số {n} là số chính phương")
else :
    print(f"Số {n} khong phai là số chính phương")
    import math

# Nhập số cần kiểm tra
n = int(input("Nhập một số để kiểm tra xem có phải số chính phương không: "))

# Kiểm tra số chính phương
if n >= 0:
    i = 0
    while i * i < n:
        i += 1
    if i * i == n:
        print(n, "là số chính phương.")
    else:
        print(n, "không phải là số chính phương.")
else:
    print(n, "không phải là số chính phương.")
