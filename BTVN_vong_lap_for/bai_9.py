#Viết chương trình nhập vào n, tìm tất cả các số chính phương nhỏ hơn n
n = int(input("Nhập vào một số n: "))
print(f"Các số chính phương nhỏ hơn {n} là:", end=' ')

i = 1
while i * i < n:
    print(i * i, end=' ') 
    i += 1
print() 
