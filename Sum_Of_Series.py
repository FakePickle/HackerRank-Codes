n = int(input())
x = float(input())
sum = 0
for i in range(2,n+1):
    sum += (x**i)/i
print(sum+1)