# Bài 6:  Viết chương trình nhập vào chuỗi ký tự, kiểm tra xem chuỗi đó có phải là số âm hay không
chuoi = input("Nhập số bạn muốn kiểm tra :")
if  len(chuoi) > 1 and chuoi[0] == "-" and chuoi[1:].isdigit() :                                       
    print("ĐÂY là chuỗi kí tự âm ")
else :
    print("Đây ko phải là chuỗi kí tự âm ")