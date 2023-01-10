def ispoweroftwo(x):
    return x and (not(x & (x-1)))

def differ(a,b):
    return ispoweroftwo(a^b)

a = int(input())
b = int(input())
if differ(a,b):
    print("0")
else:
    print("1")
