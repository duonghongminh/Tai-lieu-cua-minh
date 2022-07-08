str = str(input())

def minmin(str):
    arr=[]
    lst = str.split(" ")
    for i in range (len(lst)):
        if len(lst[i])>3:
            arr.append(lst[i])
    return arr
print(minmin(str))