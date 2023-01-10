T = int(input("Enter the number of test cases"))

count = 0
for i in range(T):
    n = int(input("Enter number"))
    for j in range(n):
        if j%3==0 or j%5==0:
            count+=j

    print(count)