def kiem_tra_so_hoan_hao(n):
    tong=0 
    if n > 0 :
        for i in range(1,n):
            if n % i == 0 :
                tong += i 
        return tong == n
    return False
def kiem_tra_so_hoan_nn(x):
    bien_luu = None
    for i in x :
        if kiem_tra_so_hoan_hao(i):
            if bien_luu is None or i < bien_luu:
                bien_luu = i
    return bien_luu
x = [10,6,28,20,12]
ket_qua = kiem_tra_so_hoan_nn(x)
if ket_qua is None :
    print("Day nay ko phai la day hoan hao")
else :
    print(f"So hoan hao nho nhat trong day nay la : {ket_qua}")
            