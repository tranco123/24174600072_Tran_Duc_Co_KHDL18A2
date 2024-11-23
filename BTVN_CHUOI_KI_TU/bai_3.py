# Bài 3: Viết chương trình nhập vào họ tên đầy đủ, trả về tên và họ riêng
# Ví dụ: Nhập vào: “Vo Van Nam”
#              Trả về: “Ho: Vo, Ten: Nam”
ho_ten = input("Họ và tên của bạn là :")
ket_qua = ho_ten.split()
ho = ket_qua[0]
ten = ket_qua[-1]
print(f"Họ của bạn là :{ho}")
print(f"Tên của bạn là :{ten}")
