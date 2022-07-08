# [-2,6,-2,9,9,8]
# [Ax, Ay, Bx, By, Cx, Cy]
import numpy as np
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
x_trongtam = round((Ax+Bx+Cx)/3,2)
y_trongtam = round((Ay+By+Cy)/3,2)
print("Toa do trong tam: [{} , {}]".format(x_trongtam,y_trongtam))
AB = (Bx-Ax,By-Ay)
AC = (Cx-Ax,Cy-Ay)
BC = (Cx-Bx,Cy-By)
a = float((-1)*(BC[0]*(-1)*Ax+BC[1]*(-1)*Ay))
b = float((-1)*(AC[0]*(-1)*Bx+AC[1]*(-1)*By))
aa= [[BC[0],BC[1]],[AC[0],AC[1]]]
bb= [a,b]
truc_tam = np.linalg.solve(aa,bb)
x_tructam = np.round(truc_tam[0],2)
y_tructam = np.round(truc_tam[1],2)
print("Toa do truc tam: [{} , {}]".format(x_tructam,y_tructam))
