n =  int(input())
for i in range(1,n+1):
    p = i
    for j in range(1,i+1):
        print(p,end=' ')
        p+=n-j
    print()