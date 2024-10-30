# 9. Tính cước tacxi: 
# Viết chương trình tính cước taxi theo biểu phí cơ bản như sau:
# -	Loại xe 4 chỗ
#   Giá mở cửa			11.000 đồng/0.8km
#   Trong phạm vi 20km 	12.100đ/km
#   Từ km thứ 21 trở đi 		10.000 đồng/km
# -	Loại  xe 7 chỗ
#   Giá mở cửa			13.000 đồng/0.8km
#   Trong phạm vi 30km 	14.100đ/km
#   Từ km thứ 31 trở đi 		12.000 đồng/km
# Tiền chờ: 05 phút đầu được miễn phí, từ phút thứ sáu trở đi là 800đ/phút.
# Loại xe chỉ nhập 4 hoặc 7.

# Nhập loại xe và số km di chuyển
loai_xe = int(input("Nhập loại xe (4 hoặc 7 chỗ): "))
so_km = float(input("Nhập số km di chuyển: "))
thoi_gian_cho = int(input("Nhập số phút chờ: "))

# Khởi tạo biến tính cước
cuoc_taxi = 0

# Tính cước theo loại xe
if loai_xe == 4:
    # Giá mở cửa xe 4 chỗ cho 0.8 km đầu tiên
    if so_km <= 0.8:
        cuoc_taxi = 11000
    elif so_km <= 20:
        cuoc_taxi = 11000 + (so_km - 0.8) * 12100
    else:
        cuoc_taxi = 11000 + (20 - 0.8) * 12100 + (so_km - 20) * 10000
elif loai_xe == 7:
    # Giá mở cửa xe 7 chỗ cho 0.8 km đầu tiên
    if so_km <= 0.8:
        cuoc_taxi = 13000
    elif so_km <= 30:
        cuoc_taxi = 13000 + (so_km - 0.8) * 14100
    else:
        cuoc_taxi = 13000 + (30 - 0.8) * 14100 + (so_km - 30) * 12000
else:
    print("Loại xe không hợp lệ. Vui lòng nhập 4 hoặc 7.")
    exit()

# Tính tiền chờ nếu thời gian chờ nhiều hơn 5 phút
if thoi_gian_cho > 5:
    cuoc_taxi += (thoi_gian_cho - 5) * 800

# In kết quả
print(f"Tổng cước taxi là: {cuoc_taxi} đồng")
