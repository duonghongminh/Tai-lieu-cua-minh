"""
Assignment 2: Đánh giá điểm tổng kết

PhuongNguyen
"""

'''
Bài 2
'''    

'''
a. Hàm xeploai_hocsinh:

Xếp loại học lực chuẩn của học sinh dựa vào điểm tổng kết trung bình chuẩn.
'''
def xeploai_hocsinh(file):
    with open(file,"r") as f:

    # Tạo danh sách bảng điểm trung bình cho các học sinh theo thứ tự từ 1 đến 6 và theo môn học
     xep_loai = {}
  
     for line in f:
        if line.startswith("Ma HS"):
            continue
        else:
            line_split = line.strip().split(";")
            Ma_HS = line_split[0]
            # Chuyển điểm TB của từng môn học từ dạng str sang float
            bangdiem = [float(i) for i in line_split[1:9]]
            
            # Tính điểm TB chuẩn và xếp hạng các môn của từng học sinh
            dtb_chuan = round((sum(bangdiem)+bangdiem[0]+bangdiem[4]+bangdiem[5])/11,2)
            if all(i >= 8.0 for i in bangdiem) and dtb_chuan > 9.0:
                xep_loai[Ma_HS] = "Xuat sac"
            elif all(i >= 6.5 for i in bangdiem) and dtb_chuan > 8.0:
                xep_loai[Ma_HS]= "Gioi"
            elif all(i >= 5.0 for i in bangdiem) and dtb_chuan > 6.5:
                xep_loai[Ma_HS] = "Kha"
            elif all(i >= 4.5 for i in bangdiem) and dtb_chuan > 6.0:
                xep_loai[Ma_HS] = "TB Kha"
            else:
                xep_loai[Ma_HS] = "TB"
                
    return xep_loai
print(xeploai_hocsinh('diem_trungbinh.txt'))

'''
b. Hàm xeploai_thidaihoc_hocsinh:

Phân loại năng lực các học sinh theo khối thi đại học dựa vào điểm tổng kết trung bình.
'''
def xeploai_thidaihoc_hocsinh(file):
    with open(file,'r') as f:
        xeploai_thidaihoc = {}  # Dictionary Output
        
        for line in f:
            if line.startswith("Ma HS"):
                continue
            else:
                line_split = line.strip().split(";")
                Ma_HS = line_split[0]
                bangdiem = [float(i) for i in line_split[1::]]  #Bảng điểm TB các môn học
                
                khoiA = round(sum(bangdiem[0:3]),2)  # Tổng điểm Toán, Lí, Hóa
                khoiA1 = round(bangdiem[0]+bangdiem[1]+bangdiem[5],2)  #Tổng điểm Toán, Lí, Anh         
                khoiB = round(bangdiem[0]+bangdiem[2]+bangdiem[3],2)  # Tổng điểm Toán, Hóa, Sinh
                khoiC = round(bangdiem[4]+bangdiem[6]+bangdiem[7],2)  # Tổng điểm Văn, Sử, Địa               
                khoiD = round(bangdiem[0]+bangdiem[4]+(bangdiem[5]*2),2) #Tổng điểm Toán, Văn, Anh
            
            # Phân loại năng lực học sinh theo khối A
            if khoiA >= 24:
                Xeploai_khoi_A = 1
            elif khoiA >= 18 and khoiA < 24:
                Xeploai_khoi_A = 2
            elif khoiA >= 12 and khoiA < 18:
                Xeploai_khoi_A = 3
            else:
                Xeploai_khoi_A = 4
            
            # Phân loại năng lực học sinh theo khối A1
            if khoiA1 >= 24:
                Xeploai_khoi_A1 = 1
            elif khoiA1 >= 18 and khoiA1 < 24:
                Xeploai_khoi_A1 = 2
            elif khoiA1 >= 12 and khoiA1 < 18:
                Xeploai_khoi_A1 = 3
            else:
                Xeploai_khoi_A1 = 4
            
            # Phân loại năng lực học sinh theo khối B
            if khoiB >= 24:
                Xeploai_khoi_B = 1
            elif khoiB >= 18 and khoiB < 24:
                Xeploai_khoi_B = 2
            elif khoiB >= 12 and khoiB < 18:
                Xeploai_khoi_B = 3
            else:
                Xeploai_khoi_B = 4
           
            # Phân loại năng lực học sinh theo khối C
            if khoiC >= 21:
                Xeploai_khoi_C = 1
            elif khoiC >= 15 and khoiC < 21:
                Xeploai_khoi_C = 2
            elif khoiC >= 12 and khoiC < 15:
                Xeploai_khoi_C = 3
            else:
                Xeploai_khoi_C = 4
            
            # Phân loại năng lực học sinh theo khối D
            if khoiD >= 32:
                Xeploai_khoi_D = 1
            elif khoiD >= 24 and khoiD < 32:
                Xeploai_khoi_D = 2
            elif khoiD >= 20 and khoiD < 24:
                Xeploai_khoi_D = 3
            else:
                Xeploai_khoi_D = 4
            
            # Xếp loại năng lực của từng học sinh theo các khối
            xep_loai = [Xeploai_khoi_A,Xeploai_khoi_A1,Xeploai_khoi_B,
                    Xeploai_khoi_C,Xeploai_khoi_D]
            xeploai_thidaihoc[Ma_HS] = xep_loai
        return xeploai_thidaihoc
    
print(xeploai_thidaihoc_hocsinh('diem_trungbinh.txt'))

'''
c. Hàm main:
'''
def main():
    input_file = "diem_trungbinh.txt"    # Đường dẫn Input cho file
    output_file = "danhgia_hocsinh.txt"  # Đường dẫn Output cho file
    
    # Chạy hàm xeploai_hocsinh(file)
    xeploai = xeploai_hocsinh(input_file) 
    print(xeploai)
    
    # Chạy hàm xeploai_thidaihoc_hocsinh(file)
    xeploai_thidaihoc = xeploai_thidaihoc_hocsinh(input_file)
    print(xeploai_thidaihoc)
    
    with open (output_file,'w') as file:
        # Dòng đầu tiên của file:
        file.write('Ma HS, xeploai_TB chuan, xeploai_A, xeploai_A1, xeploai_B, xeploai_C , xeploai_D'+'\n')
        # Viết mã số HS và xếp loại trung bình chuẩn
        for ma_hs, xeploai_tb_chuan in xeploai.items():
            file.write(str(ma_hs) + '; ' + str(xeploai_tb_chuan))
            # Viết xếp loại thi đại học theo từng môn học
            for ma_hs2, xeploai_daihoc in xeploai_thidaihoc.items():
                if ma_hs2 == ma_hs: # Nếu mã HS của xeploai_thidaihoc trùng với mã HS của xếp loại TB chuẩn thì mới viết
                   for i in xeploai_daihoc: 
                       file.write(' ; ' + str(i))
               
            file.write('\n')
        
main()