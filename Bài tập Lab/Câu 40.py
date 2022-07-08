n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

total = []
for v in lst:
    if v%2!=0:
        total.append(v)
print(total)        

