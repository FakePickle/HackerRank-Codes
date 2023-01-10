x =  int(input())
y = list(map(int, input().split()))
j = int(input())
if j in y:
    if y[-1]==j or y[0]==j:
        print("NO")
    elif (y[y.index(j)+1]+y[y.index(j)-1])%2==0:
        print("NO")
    else:
        print("YES")