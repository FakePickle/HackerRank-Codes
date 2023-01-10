x = int(input())
a,b=0,0
while x!=0:
    y = x%10
    a = a+y*pow(2,b)
    x = x//10
    b+=1
print(a)