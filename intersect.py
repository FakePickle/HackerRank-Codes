l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
s1 = set(l1)
s2 = set(l2)
a = s1.intersection(s2)
l3 = list(a)
print(sorted(l3))