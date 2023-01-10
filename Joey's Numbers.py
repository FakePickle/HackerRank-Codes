x = int(input())

a = 0

l = [int(i) for i in str(x)]
for i in range(len(l)):
    a += l[i]

if x%a==0:
    print("True")
else:
    print(False)
