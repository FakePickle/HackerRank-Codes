l = list(map(int,input().split()))
a = len(l)

for j in range(1,a+1):
    for i in range(1,j+1):
          print(l[j-1]*i,end=' ')
    
    print()