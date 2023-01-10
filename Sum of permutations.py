T = int(input())

for i in range(T):
    n = int(input())
    N = list(map(int,input().split()))

    def factorial(n):
        f = 1
        if(n==0 or n==1):
            return 1
        for i in range(2,n+1):
            f = f*i
        return f
    
    def getsum(x,y):
        fact = factorial(n)
        digitsum = 0
        for i in range(y):
            digitsum+=x[i]
        digitsum *= fact//y
        sum = 0
        a = 1
        b = 1
        while a<=y:
            sum += (b*digitsum)
            b = b*10
            a+=1
        print(sum)


    getsum(N,n)
