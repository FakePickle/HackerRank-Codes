N = int(input())
a = 0
b = 0
c = 1
if N == 2:
    print('1')
else:
    for i in range(1,N-1):
        s = a+b+c
        a = b
        b = c
        c = s
    print(s)