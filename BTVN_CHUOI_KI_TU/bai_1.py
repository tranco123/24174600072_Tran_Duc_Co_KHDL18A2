# Bài 1: Viết chương trình nhập vào chuỗi ký tự, trả về số các từ trong chuỗi ký tự vừa nhập
# Ví dụ: Nhập vào: “Hom nay    troi   mua   ”          Trả về: 4
nhap_chuoi = input("Bạn hãy nhập chuỗi của bạn vào đây :")
ket_qua = len(nhap_chuoi.split())
print(f"Kết quả của bạn là :{ket_qua}")
