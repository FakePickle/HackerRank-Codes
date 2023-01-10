n = int(input())
temp = n
sum = 0
while (n):
    k = n%10
    sum += k
    n //=10
if (temp % sum==0):
    print("True")
else:
    print("False")