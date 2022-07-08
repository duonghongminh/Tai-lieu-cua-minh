#ten_mon = ["Toan", "Ly", "Hoa", "Sinh", "Van", "Anh", "Su", "Dia"]
class BANGDIEM():
    def __init__(self):
        self.data = ""
        self.thongtin = {}

    def load_dulieu(self, file):
        lst = [] # Danh sách bao gồm MS_HS và list điểm thành phần các môn học
        with open(file,'r') as f:
        
        # Tạo danh sách bảng điểm cho các học sinh theo thứ tự từ 1 đến 6 và theo môn học
         for line in f:
             if line.startswith("Ma HS"):
                continue
             else:
                line_split = line.strip().split(";")
                lst.append(line_split)
        self.lst = lst
    def print(self) :
        print(self.lst)

    def tinhdiem_trungbinh(self):
        Ma_HS = ['1','2','3','4','5','6']
        Ten_mon_hoc = ["Toan","Ly","Hoa","Sinh","Van","Anh","Su","Dia"]
        bangdiem_tongquat = []
        for hoc_sinh in self.lst:  # Vòng lặp cho từng học sinh từ 1 đến 6
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
        dtb = dict()
        for i in range(len(Ma_HS)):
            dtb[Ma_HS[i]] = bangdiem_tongquat[i]
        self.thongtin = dtb
        return dtb

        

    def luudiem_trungbinh(self, file):
        with open(file, "w") as f:
            f.write("Ma HS, Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia\n")
            for student_id in self.thongtin:
                f.write(student_id+"; ")
                diemtb = self.thongtin[student_id]
                for tenmon in diemtb:
                    f.write(str(diemtb[tenmon]) + "; ") # dadssdads
                f.write("\n")


class DANHGIA(BANGDIEM):
    def __init__(self):
        super().__init__()
        self.xeploai = {}
        self.xeploai_khoi = {}
    def kiemtradiem(self,diems, threshold):
        for diem in diems:
            if diem < threshold:
                return False
        return True
    def sosanhdiem(self,diem, diems):
        if diem >= 9 and self.kiemtradiem(diems,8):
            return "Xuat Sac"
        elif diem >= 8 and self.kiemtradiem(diems,6.5):
            return "Gioi"
        elif diem >= 6.5 and self.kiemtradiem(diems,5):
            return "Kha"
        elif diem >= 6 and self.kiemtradiem(diems,4.5):
            return "TB Kha"
        else:
            return "TB"
    def xeploai_hocsinh(self):
        for student_id in self.thongtin:
            diemtb = self.thongtin[student_id]
            dtb_chuan = (diemtb["Toan"] + diemtb["Van"] + diemtb["Anh"]) * 2.0
            dtb_chuan += diemtb["Ly"] + diemtb["Hoa"] + diemtb["Sinh"] + diemtb["Su"] + diemtb["Dia"]
            dtb_chuan /= 11
            self.xeploai[student_id] = self.sosanhdiem(dtb_chuan, diemtb.values())
        return self.xeploai
    def xeploai_khoi(self,mon1,mon2,mon3,heso, threshold1,threshold2,threshold3):
        diemtong =  mon1 * heso + mon2 + mon3
        if diemtong >= threshold1:
            return "1"
        elif diemtong >= threshold2:
            return "2"
        elif diemtong >= threshold3:
            return "3"
        else:
            return "4"
    def xeploai_thidaihoc_hocsinh(self):
        for student_id in self.thongtin:
            diemtb = self.thongtin[student_id]
            diemkhoiA = diemtb["Toan"]*1 + diemtb["Ly"] + diemtb["Hoa"]
            if diemkhoiA >= 24:
                khoiA =  1
            elif diemkhoiA >= 18:
                khoiA = 2
            elif diemkhoiA >= 12:
                khoiA =  3
            else:
                khoiA = 4
            #24,18,12)
            diemkhoiA1 = diemtb["Toan"]*1 +  diemtb["Ly"] + diemtb["Anh"]
            if diemkhoiA1 >= 24:
                khoiA1 =  1
            elif diemkhoiA1 >= 18:
                khoiA1 = 2
            elif diemkhoiA1 >= 12:
                khoiA1 = 3
            else:
                khoiA1 = 4
            #24,18,12)
            diemkhoiB = diemtb["Toan"]*1 + diemtb["Hoa"] + diemtb["Sinh"]
            if diemkhoiB >= 24:
                khoiB = 1
            elif diemkhoiB >= 18:
                khoiB = 2
            elif diemkhoiB >= 12:
                khoiB = 3
            else:
                khoiB = 4
            #24,18,12
            diemkhoiC = diemtb["Van"]*1 + diemtb["Su"] + diemtb["Dia"]
            if diemkhoiC >= 21:
                khoiC = 1
            elif diemkhoiC >= 15:
                khoiC = 2
            elif diemkhoiC >= 12:
                khoiC =  3
            else:
                khoiC =  4
            #21,15,12
            diemkhoiD = diemtb["Anh"]*2 + diemtb["Toan"] + diemtb["Van"]
            if diemkhoiD >= 32:
                khoiD =  1
            elif diemkhoiD >= 24:
                khoiD = 2
            elif diemkhoiD >= 20:
                khoiD =  3
            else:
                khoiD = 4
            #32,24,20
            self.xeploai_khoi[student_id] = [khoiA,khoiA1,khoiB,khoiC,khoiD]
        return self.xeploai_khoi

class TUNHIEN(DANHGIA):
    def __init__(self):
        super().__init__()
        self.tunhien = {}      
    def xeploai_thidaihoc_tunhien(self):
        for student_id in self.thongtin:
            diemtb = self.thongtin[student_id]
            diemkhoiA = diemtb["Toan"]*1 + diemtb["Ly"] + diemtb["Hoa"]
            if diemkhoiA >= 24:
                khoiA =  1
            elif diemkhoiA >= 18:
                khoiA = 2
            elif diemkhoiA >= 12:
                khoiA =  3
            else:
                khoiA = 4
            #24,18,12)
            diemkhoiA1 = diemtb["Toan"]*1 +  diemtb["Ly"] + diemtb["Anh"]
            if diemkhoiA1 >= 24:
                khoiA1 =  1
            elif diemkhoiA1 >= 18:
                khoiA1 = 2
            elif diemkhoiA1 >= 12:
                khoiA1 = 3
            else:
                khoiA1 = 4
            #24,18,12)
            diemkhoiB = diemtb["Toan"]*1 + diemtb["Hoa"] + diemtb["Sinh"]
            if diemkhoiB >= 24:
                khoiB = 1
            elif diemkhoiB >= 18:
                khoiB = 2
            elif diemkhoiB >= 12:
                khoiB = 3
            else:
                khoiB = 4
            self.tunhien[student_id] = [khoiA,khoiA1,khoiB]
        return self.tunhien

class XAHOI(DANHGIA):        
    def __init__(self):
        super().__init__()
        self.xahoi = {}
    def xeploai_thidaihoc_xahoi(self):
        for student_id in self.thongtin:
            diemtb = self.thongtin[student_id]
            diemkhoiC = diemtb["Van"]*1 + diemtb["Su"] + diemtb["Dia"]
            if diemkhoiC >= 21:
                khoiC = 1
            elif diemkhoiC >= 15:
                khoiC = 2
            elif diemkhoiC >= 12:
                khoiC =  3
            else:
                khoiC =  4
            self.xahoi[student_id] = khoiC
        return self.xahoi

class COBAN(DANHGIA) :
    def __init__(self):
        super().__init__()
        self.coban = {}
    def xeploai_thidaihoc_coban(self):
        for student_id in self.thongtin:
            diemtb = self.thongtin[student_id]
            diemkhoiD = diemtb["Anh"]*2 + diemtb["Toan"] + diemtb["Van"]
            if diemkhoiD >= 32:
                khoiD =  1
            elif diemkhoiD >= 24:
                khoiD = 2
            elif diemkhoiD >= 20:
                khoiD =  3
            else:
                khoiD = 4
            #32,24,20
            self.coban[student_id] = khoiD
        return self.coban




def main():

    bangdiem = DANHGIA()
    bangdiem.load_dulieu("C:/Users/ACER/Desktop/Tài liệu của Minh/ASM 3/diem_chitiet.txt")
    a = bangdiem.tinhdiem_trungbinh()   
    print("Điểm trung bình từng học sinh : ", a)
    bangdiem.luudiem_trungbinh("C:/Users/ACER/Desktop/Tài liệu của Minh/ASM 3/output.txt")
    print("Xếp loại từng học sinh : ",bangdiem.xeploai_hocsinh())
    print("Xếp loại thi đại học : ",bangdiem.xeploai_thidaihoc_hocsinh())
    print(" ")

    tunhien2 = TUNHIEN()
    tunhien2.load_dulieu("C:/Users/ACER/Desktop/Tài liệu của Minh/ASM 3/diem_chitiet.txt")
    b = tunhien2.tinhdiem_trungbinh()
    #print("Điểm trung bình tự nhiên: ", b)
    print("Xếp loại tự nhiên : ",tunhien2.xeploai_thidaihoc_tunhien())
    print(" ")
    
    xahoi2 = XAHOI()
    xahoi2.load_dulieu("C:/Users/ACER/Desktop/Tài liệu của Minh/ASM 3/diem_chitiet.txt")
    c = xahoi2.tinhdiem_trungbinh()
    #print("Điểm trung bình xã hội: ", c)
    print("Xếp loại xã hội : ",xahoi2.xeploai_thidaihoc_xahoi())
    print(" ")

    coban2 = COBAN()
    coban2.load_dulieu("C:/Users/ACER/Desktop/Tài liệu của Minh/ASM 3/diem_chitiet.txt")
    d = coban2.tinhdiem_trungbinh()
    #print("Điểm trung bình cơ bản: ", d)
    print("Xếp loại cơ bản : ",coban2.xeploai_thidaihoc_coban())
    print(" ")


try :
    if __name__ == "__main__":
        main()