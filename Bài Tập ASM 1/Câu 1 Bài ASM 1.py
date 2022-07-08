# Xét xem A, B, C có đủ điều kiện tạo thành tam giác ABC hay không
print('Chương trình giải tam giác')
input_tamgiac = input("Nhập tọa độ dạng list như sau [Ax, Ay, Bx, By, Cx, Cy] = ")
# Lọc ra các số thực từ str "dauvao1"
input_tamgiac_output1=input_tamgiac.strip("][ ")
input_tamgiac_output2=input_tamgiac_output1.replace(" ", "")
input_tamgiac_output=input_tamgiac_output2.split(",")
Ax = float(input_tamgiac_output[0])
Ay = float(input_tamgiac_output[1])
Bx = float(input_tamgiac_output[2])
By = float(input_tamgiac_output[3])
Cx = float(input_tamgiac_output[4])
Cy = float(input_tamgiac_output[5])
# cách kiểm tra tam giác như sau:
vectoAB = float(Bx-Ax)/float(Cx-Bx)
vectoBC = float(By-Ay)/float(Cy-By)
if vectoAB==vectoBC:
    print('Đây không phải là tam giác')
else:
    print('Đây là tam giác')