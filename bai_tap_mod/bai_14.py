#Viết hàm trả về giá trị trung bình của một dãy số nguyên tố bất kì
import modun_4
def tinh_gia_tri_trung_binh(tham_so):
    tong = 0 
    dem = 0
    for i in tham_so:
        if modun_4.kiem_tra_so_nguyen_to(i):
            tong += i 
            dem +=1 
    if dem == 0 :
        return "Không có số nguyên tố nào"
    return tong / dem 
tham_so = [4,6,8]
ket_qua = tinh_gia_tri_trung_binh(tham_so)
print(ket_qua)