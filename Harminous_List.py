n = int(input())
l = []
for i in range(n):
    a = int(input())
    l.append(a)
max = l[0]
for i in l:
    if i>max:
        max = i
min = l[0]
for i in l:
    if i<min:
        min = i
if (max-min == 1):
    print("True")
else:
    print("False")