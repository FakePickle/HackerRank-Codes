l1 = list(map(int,input().split()))
l2 = list(map(str,input().split()))
l4 = []
for i in range(len(l1)):
    l3 = []
    l3.append(l1[i])
    l3.append(l2[i])
    a = tuple(l3)
    l4.append(a)
print(l4)