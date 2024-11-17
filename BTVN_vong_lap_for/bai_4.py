# số nguyên tố là số nguyên dương Lớn hơn 1 và chỉ chia hết cho 1 và chính nó
n = int(input ("Nhập n để kiểm tra xe phải số nguyên tố không : "))
if n <= 1:
    print( "Số này không phải là số nguyên tố ")
else:
    k = n
    for i in range(n) :
        if n % k == 0 and k != n and k != 1:
            print("Đây không phải là số nguyên tố")
            break
            k = k - 1 
    else:
        print("Số này là số nguyên tố ")