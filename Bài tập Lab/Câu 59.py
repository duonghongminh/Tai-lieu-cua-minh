n = int(input())


def is_abundant(n):
    lst=[]
    for i in range (1,n):
        if n%i==0:
            lst.append(i)
    sum = 0
    for j in lst:
        sum+=j
        if sum>n:
            print('True')
        else:
            print('False')
is_abundant(n)