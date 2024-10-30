# 10. Viết chương trình nhập lương nhân viên, tính thuế thu nhập và lương ròng (số tiền
# lương thực sự mà nhân viên đó nhận được).
# Với các thông số giả sử như sau
# • 30% thuế thu nhập nếu lương là 15 triệu.
# • 20% thuế thu nhập nếu lương từ 7 đến 15 triệu.
# • 10% thuế thu nhập nếu lương dưới 7 triệu.
luong = float(input("Lương hàng tháng bạn nhận được là (Triệu đồng): "))
if luong > 0:
    if luong >= 15:
        thue = 0.3 * luong
    elif luong >= 7:
        thue = 0.2 * luong
    else:
        thue = 0.1 * luong
    luong_rong = luong - thue
    print(f"Số tiền hiện tại của bạn là: {luong_rong:.2f} triệu đồng")
else:
    print("Bạn đã nhập nhầm lương của mình")
