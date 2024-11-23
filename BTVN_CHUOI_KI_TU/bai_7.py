#Bài 7: Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải số thập phân hay không
#.isdecimal() # số thập phân
chuoi = input("Nhập chuỗi bạn muốn kiểm tra :")
if chuoi.count('.') == 1 and chuoi.replace('.','').isdigit():
    print("Đây là số thập phân ")
else :
    print("Đây ko phải số thập phân ")