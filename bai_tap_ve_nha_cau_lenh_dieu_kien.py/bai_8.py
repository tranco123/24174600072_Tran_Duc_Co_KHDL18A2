# 8. Viết chương trình phân loại sinh viên dựa vào kết quả điểm học tập. 
# Nếu điểm A thì phân loại là sinh viên xuất sắc, 
# điểm A =  print("A là sinh viên xuất sắc") 
# điểm B là sinh viên loại giỏi,
# điểm C là sinh viên loại khá, 
# điểm D là sinh viên loại trung bình, 
# điểm E là sinh viên loại yếu, 
# điểm F là sinh viên xếp loại kém.
Diem = input("Nhập mức điểm của bạn:")
if Diem == 'A' :
    print("BẠN LÀ SINH VIÊN XUẤT SẮC")
elif Diem == 'B' :
    print("BẠN LÀ SINH VIÊN LOẠI GIỎI ")
elif Diem == 'C' :
    print("BẠN LÀ SINH VIÊN LOẠI KHÁ")
elif Diem == 'D' :
    print("BẠN LÀ SINH VIÊN LOẠI TRUNG BÌNH ")
elif Diem == 'E':
    print("BẠN LÀ SINH VIÊN LOẠI YẾU ")
elif Diem == 'F' :
    print("BẠN LÀ SINH VIÊN LOẠI KÉM")
else :
    print("Bạn nhập mức điểm ko phù hợp , hãy nhập lại ")