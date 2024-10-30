# Nhập một ký tự từ bàn phím
char = input("Nhập một ký tự bạn muốn: ").lower()

# Kiểm tra nguyên âm hoặc phụ âm
if char in 'aeiou':
    print(f"{char} là nguyên âm.")
elif char.isalpha():
    print(f"{char} là phụ âm.")
else:
    print("Bạn hãy nhập lại .")
