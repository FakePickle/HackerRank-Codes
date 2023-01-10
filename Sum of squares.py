T = int(input("Enter number of test cases"))

c1 = 0
c2 = 0

for i in range(T):
    n = int(input("Enter the number"))
    for j in range(1,n+1):
        c1 += j*j
        c2 += j
        c3 = c2*c2
print(c3 - c1)