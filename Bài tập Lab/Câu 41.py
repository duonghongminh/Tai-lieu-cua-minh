n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
abc = []
for v in lst:
    if v % 5==0:
        abc.append(v)
if len(abc)==0:
    abc = [0]   
print(abc)        