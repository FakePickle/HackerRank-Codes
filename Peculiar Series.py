n = int(input())
t = int(input())


for i in range(t-1):
    if n%2==0:
        n-=n//2
    elif n%2!=0:
        n=n*3+1

print(n)