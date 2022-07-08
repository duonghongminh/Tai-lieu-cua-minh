#Bạn hãy viết hàm trả về tổng của các phần tử trong list các số nguyên được nhập vào từ bàn phím.
n = int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
total=0
for v in lst:
    total+=v
print(total)  
