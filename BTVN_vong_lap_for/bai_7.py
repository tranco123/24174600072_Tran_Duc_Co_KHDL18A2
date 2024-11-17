# Nhập số n từ người dùng
n = int(input("Nhập vào một số n: "))

# In ra các số nguyên tố nhỏ hơn n
print(f"Các số nguyên tố nhỏ hơn {n} là:", end=' ')

for num in range(2, n):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')  # In ngay số nguyên tố

print()  # In dòng mới sau khi in hết các số

