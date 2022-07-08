#Initial list
res = []

# Input lengths
abc = int(input())

# Add element
for i in range(abc):
    # Input elements
    n = int(input())
    res.append(n)
def a(res):
    a = ""
    for i in res:
        a+=str(i)
    return a
print(a(res))
