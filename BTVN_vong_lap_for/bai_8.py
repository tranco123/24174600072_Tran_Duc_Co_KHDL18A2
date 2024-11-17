#Viết chương trình nhập vào n, tìm tất cả các số hoàn hảo nhỏ hơn n
n = int(input("Nhập vào một số n: "))
print(f"Các số hoàn hảo nhỏ hơn {n} là:", end=' ')

for i in range(1, n):
    tong_i = 0 
    for k in range(1, i):
        if i % k == 0:
            tong_i += k 
    if tong_i == i: 
        print(i, end=' ')

print() 

