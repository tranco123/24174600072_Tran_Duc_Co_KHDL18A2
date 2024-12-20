
doi_bong = []

def xem_danh_sach():
    if not doi_bong:
        print("Danh sách cầu thủ đừng để trốngtrống.")
    else:
        for cau_thu in doi_bong:
            print(f"Mã cầu thủ: {cau_thu['ma']}, Tên: {cau_thu['ten']}, Tuổi: {cau_thu['tuoi']}, "
                f"Vị trí: {cau_thu['vi_tri']}, Số huy chương: {cau_thu['so_huy_chuong']}, Thưởng: {cau_thu['thuong']}")

def tinh_thuong(so_huy_chuong):
    if so_huy_chuong > 10:
        return so_huy_chuong * 500000
    elif 5 <= so_huy_chuong < 10:
        return so_huy_chuong * 300000
    elif 1 <= so_huy_chuong < 5:
        return so_huy_chuong * 200000
    return 0

def nhap_thong_tin():
    try:
        ma = input("Nhập mã cầu thủ bạn yêu thíchthích: ")
        ten = input("Nhập tên cầu thủ yêu thích: ")
        tuoi = int(input("Nhập tuổi cầu thủ của bạn: "))
        vi_tri = input("Nhập vị trí cầu thủ đá trên sân: ")
        so_huy_chuong = int(input("Nhập số huy chương: "))
        thuong = tinh_thuong(so_huy_chuong)
        cau_thu = {
            "ma": ma,
            "ten": ten,
            "tuoi": tuoi,
            "vi_tri": vi_tri,
            "so_huy_chuong": so_huy_chuong,
            "thuong": thuong
        }
        doi_bong.append(cau_thu)
        print("Đã thêm cầu thủ thành công , tốt nhé ")
    except ValueError:
        print("Giá trị nhập vào không hợp lệ. Vui lòng thử lại.")

def tim_kiem_xoa():
    try:
        ma = input("Nhập mã cầu thủ để tìm và xóa: ")
        cau_thu_ton_tai = False
        for cau_thu in doi_bong:
            if cau_thu["ma"] == ma:
                doi_bong.remove(cau_thu)
                cau_thu_ton_tai = True
                print("Đã xóa cầu thủ thành công!")
                break
        if not cau_thu_ton_tai:
            print("Không tìm thấy cầu thủ với mã này.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

while True:
    print("\nChọn chức năng:")
    print("1. Xem danh sách cầu thủ")
    print("2. Nhập thông tin cầu thủ mới")
    print("3. Tìm kiếm và xóa cầu thủ")
    print("4. Thoát")

    lua_chon = input("Nhập lựa chọn của bạn: ")
    
    if lua_chon == "1":
        xem_danh_sach()
    elif lua_chon == "2":
        nhap_thong_tin()
    elif lua_chon == "3":
        tim_kiem_xoa()
    elif lua_chon == "4":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng thử lại.")
