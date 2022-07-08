'''
 Assignment 2: Tính toán điểm tổng kết

 PhuongNguyen
'''

'''
Bài 1
'''

'''
a. Tính toán hàm tinhdiem_trungbinh

Tính toán toàn bộ điểm trung bình của sinh viên theo từng môn học.
'''
def tinhdiem_trungbinh(bang_diem):
    Ma_HS = ['1','2','3','4','5','6']
    Ten_mon_hoc = ["Toan","Ly","Hoa","Sinh","Van","Anh","Su","Dia"]
    lst = [] # Danh sách bao gồm MS_HS và list điểm thành phần các môn học
    bangdiem_tongquat = []
    
    with open(bang_diem,'r') as f:
        
        # Tạo danh sách bảng điểm cho các học sinh theo thứ tự từ 1 đến 6 và theo môn học
         for line in f:
             if line.startswith("Ma HS"):
                continue
             else:
                line_split = line.strip().split(";")
                lst.append(line_split)
         for hoc_sinh in lst:  # Vòng lặp cho từng học sinh từ 1 đến 6
             Mon_hoc = hoc_sinh[1:9]   # Danh sách điểm cho các môn học
             Diem_monhoc = []
             bangdiem_TB = []
             for diem_so in Mon_hoc:
                 # Phân tách điểm của các môn học và chuyển điểm thành phần sang dạng int
                 diem = diem_so.strip().split(",")
                 Diem_monhoc.append([int(j) for j in diem]) 
                 # Xét điểm từng môn học theo các môn tự nhiên và môn xã hội
                 for i in range(len(Diem_monhoc)):
                     mon_hoc = Diem_monhoc[i]
                     # Điểm trung bình của môn học tự nhiên (có 4 điểm thành phần)
                     if len(mon_hoc) == 4: 
                        diemTB = round(mon_hoc[0]*0.05 + mon_hoc[1]*0.1 + 
                                        mon_hoc[2]*0.15 + mon_hoc[3]*0.7,2)
                     # Điểm trung bình của môn học xã hội (có 5 điểm thành phần)   
                     if len(mon_hoc) == 5:
                        diemTB = round(mon_hoc[0]*0.05 + mon_hoc[1]*0.1 +
                                        mon_hoc[2]*0.10 + mon_hoc[3]*0.15 + 
                                        mon_hoc[4]*0.6,2)
                 # List bảng điểm trung bình các môn của từng học sinh       
                 bangdiem_TB.append(diemTB)
                 
             # Tạo dictionary nhỏ cho từng học sinh: {'Môn học': Điểm TB}    
                 dict_bangdiem = dict()
             for i in range(len(Ten_mon_hoc)):
                 dict_bangdiem[Ten_mon_hoc[i]] = bangdiem_TB[i]
             bangdiem_tongquat.append(dict_bangdiem)
         
         # Tạo dictionary tổng quát cho Output của hàm:{'Ma_HS':{'Môn học':Điểm TB}}      
         tinhdiem_trungbinh = dict()
         for i in range(len(Ma_HS)):
             tinhdiem_trungbinh[Ma_HS[i]] = bangdiem_tongquat[i]
                    
    return tinhdiem_trungbinh

print(tinhdiem_trungbinh('diem_chitiet.txt'))

'''
b. Hàm luudiem_trungbinh: 

Lưu điểm trung bình ra 1 file có tên là “diem_trungbinh.txt” theo đường dẫn có sẵn.

Input: 

- Output dictionary của hàm tinhdiem_trungbinh (bangdiem)

- Đường dẫn thư mục của bảng điểm trung bình (folder)
''' 

def bangdiem_trungbinh(bangdiem,folder):
    with open(folder,"w") as file:
        file.write("Ma HS,Toan,Ly,Hoa,Sinh,Van,Anh,Su,Dia"+"\n") 
# Tạo danh sách các keys là mã học sinh:
        for ma_hs,diem in bangdiem.items():
            file.write(ma_hs)
            for mon,diem_tb in diem.items():
                file.write(";" + str(diem_tb))
            file.write("\n")
            
bangdiem = tinhdiem_trungbinh('diem_chitiet.txt')
bangdiem_trungbinh(bangdiem,"diem_trungbinh.txt")  

  
        
'''    
c. Hàm main():    
'''         
def main():
    input_file = "diem_chitiet.txt"
    output_file = "diem_trungbinh.txt"
    
    diem_TB = tinhdiem_trungbinh(input_file)  #Output hàm tinhdiem_trungbinh
    
    bangdiem_trungbinh(diem_TB,output_file)   #Lưu bảng điểm trung bình diem_trungbinh.txt

main()




            
            
            
        
    
            
        
          
                
                      
                
            
            
            
            
             
                

              
         