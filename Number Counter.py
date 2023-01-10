n = int(input())
y = list(map(int,input().split()))

e = 0
o = 0

for i in range(len(y)):
    if y[i]<=0:
        continue
    elif y[i]%2==0:
        e+=1
    else:
        o+=1
print(e)
print(o)