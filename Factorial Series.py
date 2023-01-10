import math
x = int(input())
n = int(input())
for i in range(1,n+1):
    a = math.factorial(i)
    sum = 1
    sum += (x**i)/a
print(sum)