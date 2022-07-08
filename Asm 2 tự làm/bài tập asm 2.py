# ham tinh diem trung binh
def tinhdiem_trungbinh(fname):
    fname = input("Enter file name: ")
    bigdict = dict()  # output diem trung binh all SV
    with open(fname, 'r') as fh:
        MH = fh.readline().rstrip().split(', ')[1:]  # lay list ten cac mon hoc
        # print(MH)
        for line in fh.readlines():
            SV = line.split(':')[0]  # lay ten HS
            diemtungmon = line.rstrip().split(':')[1].split(';')
            mini = dict()  # output diem trung binh tung SV
            for x in MH:
                i = MH.index(x)
                diemmonX = diemtungmon[i].split(',')
                if i < 4:
                    tb = 0.05 * float(diemmonX[0]) + 0.1 * float(diemmonX[1]) + 0.15 * float(diemmonX[2]) + 0.7 * float(
                        diemmonX[3])
                else:
                    tb = 0.05 * float(diemmonX[0]) + 0.1 * float(diemmonX[1]) + 0.1 * float(diemmonX[2]) + 0.15 * float(
                        diemmonX[3]) + 0.6 * float(diemmonX[4])
                mini.update({x: round(tb, 2)})
            bigdict.update({SV: mini})
        return bigdict
    # print(tinhdiem_trungbinh())


# b/ ham luu diem trung binh
def luudiem_trungbinh(fname2, fname):
    diem = tinhdiem_trungbinh(fname)
    #     diemTBmon = []
    #     print(k,': ',v)
    # fname2 = input("nhap duong dan diem_trungbinh: ")
    with open(fname2, 'a') as f:
        f.write('Ma HS, Toan, Ly, Hoa, Sinh, Van, Anh, Su, Dia\n')
        for k, v in diem.items():  # k = Ten SV, v = diem TB chi tiet tung mon vs tieu de mon hoc
            print(k)
            f.write(k + ": ")
            tbmonhoc = ""
            for diemtb in v.values():
                tbmonhoc += ";" + str(diemtb)
                print(diemtb)
            print(tbmonhoc)
            f.write(tbmonhoc[1:] + '\n')


# print(luudiem_trungbinh())
# c/ ham main()
def main():
    file1 = input("duong dan diem_chitiet.txt: ")  # duong dan input file
    file2 = input("duong dan diem trung binh: ")  # duong dan output diem trung binh
    tinhdiem_trungbinh(file1)
    luudiem_trungbinh(file2, file1)


if __name__ == '__main__':
    main()

    # with open(input("nhap duong dan"), 'w') as f:
    #     print(diem, file=f)
# luudiem_trungbinh()
# print(luudiem_trungbinh())


# for line in handle:
#     if line.startswith('From '):
#         word = line.split()[1]
#         senders[word] =senders.get(word,0) + 1
# print(senders)
# maxsender = None
# maxcount = None
# for k,v in senders.items():
#     if maxcount is None or v > maxcount:
#         maxcount = v
#         maxsender = k
# print(maxsender,maxcount)


# print(line, end='')