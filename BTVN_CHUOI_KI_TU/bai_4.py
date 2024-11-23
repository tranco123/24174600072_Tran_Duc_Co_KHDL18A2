# Bài 4: Viết chương trình nhập vào chuỗi ký tự, trả về kết quả đếm số ký tự là chữ, số ký tự là số và số ký tự là ký tự 
# đặc biệt (Không là số, không là chữ) trong chuỗi
#isalpha(): kiểm tra chữ cái
# isdigit(): kiểm tra số
chuoi = input("Nhập chuôix của bạn vào đây :")
ki_tu_chu = 0 
ki_tu_so = 0 
ki_tu_dac_biet = 0 
for chu in chuoi :
    if chu.isalpha() == True :
        ki_tu_chu = ki_tu_chu + 1 
    else :
        if chu.isdigit() == True :
            ki_tu_so = ki_tu_so + 1 
        else :
            ki_tu_dac_biet = ki_tu_dac_biet + 1 
print(f"Số kí tự chữ là :{ki_tu_chu}")
print(f"Số kí tự số là :{ki_tu_so}")
print(f"Số kí tự đặc biệt là :{ki_tu_dac_biet}")