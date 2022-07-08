s = str(input())

def format(s):
    if len(s)>=3:
        if s[-3]=="ing":
            return s+"ly"
        else:
            return s+"ing"
        return s
    else:
        return s
print(format(s))
