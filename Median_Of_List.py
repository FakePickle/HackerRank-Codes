n = int(input())
l1 = []
for i in range(n):
    a = int(input())
    l1.append(a)
m = int(input())
for i in range(m):
    b = int(input())
    l1.append(b)
l1.sort()
mid = len(l1)//2
res = (l1[mid]+l1[~mid])/2
print(res)