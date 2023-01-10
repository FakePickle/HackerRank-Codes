T = int(input())
x = 0
for i in range(T):
    a = int(input())
    b = int(input())
    N = int(input())
    x += a
    for j in range(N):
        x += (2**j)*b
        print(x,end=" ")