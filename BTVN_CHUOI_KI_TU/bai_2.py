#Viết chương trình nhập vào chuỗi ký tự, trả về chuỗi ký tự sau khi loại bỏ tất cả các dấu cách thừa
# Ví dụ: Nhập vào: “Hom nay    troi   mua   ”
#              Trả về: “Hom nay troi mua”
nhap_chuoi = input("Nhập chuỗi của bạn vào :")
chuoi_ki_tu = " ".join(nhap_chuoi.split())
print(f"Trả về kết quả là : {chuoi_ki_tu}")