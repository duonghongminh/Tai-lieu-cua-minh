a = int(input())
b = int(input())
tong = 0
while a<=b:
    if a % 2!=0:
        tong=tong+a
    a=a+1
print(tong)