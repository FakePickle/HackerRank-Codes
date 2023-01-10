N = int(input())
a = 0
b = 1
if N == 1:
    print("0")
else:
    for i in range(N-2):
        c = a+b
        a = b
        b = c
    print(c)