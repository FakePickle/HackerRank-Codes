n = int(input())
l = []
for i in range(1,n+1):
    l.append(i)
l.reverse()
for i in range(len(l)):
    print(str(i+1)*l[i])