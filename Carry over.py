for i in range(int(input())):
    a,b = map(int,input().split())
    carry = 0
    count = 0
    while a>0 or b>0:
        r=a%10
        s= b%10
        carry = (r+s+carry)//10
        if carry>0:
            count+=1
        a//=10
        b//=10
    print(count)
