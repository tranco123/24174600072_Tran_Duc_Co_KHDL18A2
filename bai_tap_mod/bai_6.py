# Viết hàm kiểm tra một số có phải số hoàn hảo hay không
import modun_6

n = input("Nhập số của bạn muốn kiểm tra là :")
if modun_6.kiem_tra_so_hoan_hao(n):
    print("Đây là số hoàn hảo ")
else :
    print("Đây không phải là số hoàn hảo")