print("Chào mừng đến với rạp chiếu phim ABC! của Cơ ")
print("Vui lòng chọn thể loại phim bạn muốn xem nhất:")
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim khoa học viễn tưởng")
so_thu_tu = input("Nhập số tương ứng với thể loại bạn muốn xem: ")
if so_thu_tu == "1":
    print("Bạn đã chọn thể loại Phim tình cảm.")
elif so_thu_tu == "2":
    print("Bạn đã chọn thể loại Phim kinh dị.")
elif so_thu_tu == "3":
    print("Bạn đã chọn thể loại Phim hoạt hình.")
elif so_thu_tu == "4":
    print("Bạn đã chọn thể loại Phim khoa học viễn tưởng.")
else:
    print("Lựa chọn của bạn không hợp lệ. Vui lòng xemm lại menu và nhập lại.")
