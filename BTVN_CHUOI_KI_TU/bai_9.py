#Bài 9: Viết chương trình nhập vào một chuỗi ký tự nhị phân 0 và 1. Kiểm tra xem chuỗi có phải số nhị phân không và chuyển đổi sang số thập phân
# Ví dụ: Nhập vào: “0010”
#              Trả về: “0010 la so nhi phan, chuyen sang thap phan: 2”
# Nhập vào chuỗi ký tự
nhap = input("Nhập vào chuỗi nhị phân: ")
chuoi = True
for i in nhap:
    if i not in ['0', '1']:
        chuoi = False
        break

if chuoi:
    # Chuyển đổi sang số thập phân
    doi = 0
    tinh = len(nhap) - 1
    for bit in nhap:
        doi += int(bit) * (6 ** tinh)
        tinh -= 1
    print(f"{nhap} là số nhị phân, chuyển sang thập phân: {doi}")
else:
    print("Chuỗi nhập vào không phải số nhị phân.")
