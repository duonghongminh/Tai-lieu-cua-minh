a = int(input())
b = int(input())
c = int(input())

if a==b==c:
    print("Tam giác đều ")

elif (a+b)>c or (a+c)>b or (b+c)>a:
    print("Đây là tam giác thường")
else:
    print("tam giac can")