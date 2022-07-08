# Tính toán độ dài các cạnh và độ lớn các góc của tam giác ABC.
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
# Tính độ dài các cạnh của tam giác
AB = (Bx-Ax)**2+(By-Ay)**2
BC = (Cx-Bx)**2+(Cy-By)**2
AC = (Cx-Ax)**2+(Cy-Ay)**2
print('Do dai canh AB la', AB**(1/2))
print('Do dai canh BC la', BC**(1/2))
print('Do dai canh AC la', AC**(1/2))
# Tính độ lớn các góc của tam giác ABC
# Tọa độ vecto AB là a = (Bx-Ax;By-Ay)
# Độ dài vecto AB là b = ((Bx-Ax)**2+(By-Ay)**2)*0.5

