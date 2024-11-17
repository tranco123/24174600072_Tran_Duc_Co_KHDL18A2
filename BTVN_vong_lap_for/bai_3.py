#In n các số Fibonacci 
a = 0
b = 1
n = int(input("Nhap vao so nguyen duong n: "))
for i in range(n):
    print(a)
    sum_a_b = a + b
    a = b
    b = sum_a_b
