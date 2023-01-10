n = int(input())
r = int(input())
flag = False
for i in range(2,r):
    a = i
    if r%i==0:
        flag=True
        break
if flag:
    pass
else:
    print(a)