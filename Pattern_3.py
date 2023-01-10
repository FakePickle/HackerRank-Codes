n = int(input())
for i in range(1,n+1):
    print(' '*(n-i),end='')
    if i%3==1:
        print('*  '*(2*(i//3)+1))
    elif i%3==2:
        print('*  '*(i//3)+'* *'+'  *'*(i//3))
    else:
        print('*  '*(i//3-1)+'*   *'+'  *'*(i//3-1))