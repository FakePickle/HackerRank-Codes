x = int(input())
i = 1
count = 0
while count!=x:
    a = 2*i+3
    if a%5!=0:
        print(a,end=' ')
        count+=1
    i+=1