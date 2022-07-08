# Bài 10.1
class Student ():
    def __init__(self,ten,diem):
        self.ten = ten
        self.diem = diem
    def print_diemtk(self):
        tong = 0
        for element in self.diem :
            tong = tong + element
            diemtk = round(tong/ len(self.diem),2)
        self.diemtk = diemtk
        print("The average mark of {} is {}".format(self.ten,self.diemtk))

#Bài 10.2
class Nhanvien():
    def __init__(self,ten,thang,luongcoban,songay,heso):
        self.ten = ten
        self.thang = thang
        self.luongcoban = luongcoban
        self.songay = songay
        self.heso = heso
    def tinh_luong(self):
        luong_tong= self.luongcoban * self.songay * self.heso - 1000000
        if luong_tong > 9000000 :
            luong_thuc_nhan = int(luong_tong*0.9)
        else :
            luong_thuc_nhan = int(luong_tong)
        self.luong_thuc_nhan = luong_thuc_nhan
    def hien_thi_luong(self):
        print("Luong cua nhan vien {} nhan duoc trong thang {} la: {} VND".format(self.ten,self.thang,self.luong_thuc_nhan)) 


#Bài 10.3
class QuanLy(Nhanvien):
    def tinh_luong_thuong(self):
        luong_tong_chua_thuong = self.luongcoban * self.songay * self.heso - 1000000
        if luong_tong_chua_thuong > 9000000 :
            luong_nhan_chua_thuong = int(luong_tong_chua_thuong*0.9)
        else :
            luong_nhan_chua_thuong = int(luong_tong_chua_thuong)
        if self.heso < 1 :
            luong_thuc_nhan =  int(luong_tong_chua_thuong*self.heso)
        else :
            luong_thuong =  luong_nhan_chua_thuong *(self.heso - 1 )*0.85
            luong_thuc_nhan = int(luong_nhan_chua_thuong + luong_thuong)
        self.luong_thuc_nhan = luong_thuc_nhan


#Hàm main()
def main():
    diem2 = Student("Tên",[6,7,8])
    diem2.print_diemtk()
    print(" ")
    nhanvien = Nhanvien("Tên",2,8000000,24,2)
    nhanvien.tinh_luong()
    nhanvien.hien_thi_luong()
    print(" ")
    quanly2 = QuanLy("Tên",2,100000,15,0.8)
    quanly2.tinh_luong_thuong()
    quanly2.hien_thi_luong()

main()