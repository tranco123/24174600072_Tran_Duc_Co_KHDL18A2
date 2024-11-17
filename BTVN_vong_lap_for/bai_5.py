n = int(input("Nhập một số: "))
s = 0
if n <= 1:
    print("hãy nhập số nguyên dng")
else:
    
    for i in range(1, n):  
        if n % i == 0:
            s += i  
    if s == n:
        print(f"{n} là số hoàn hảo.")
    else:
        print(f"{n} không phải là số hoàn hảo.")