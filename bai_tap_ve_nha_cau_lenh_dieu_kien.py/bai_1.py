# 1. Tính năm nhuận. Năm thứ n là nhuận nếu nó chia hết cho 4, nhưng không chia hết cho 100 hoặc chia hết 400. 
n = int(input("Bạn hãy nhập năm mà bạn muốn kiểm tra: "))
if n > 0: 
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0): 
        print(f"Năm {n} là năm nhuận.")
    else:
        print(f"Năm {n} không phải là năm nhuận.")
else:
    print("Bạn đã nhập sai, hãy nhập lại đi.")

