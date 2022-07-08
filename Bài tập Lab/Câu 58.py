n = int(input())

def sumOfAll(n):
    r = 0
    for i in range (1,n-1):
        if n%i == 0:
            r+=i
    return r

print(sumOfAll(n))