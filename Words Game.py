x = int(input())
a = ['','one','two','three','four','five','six','seven','eight','nine']
b = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

if x%10==0:
    print(b[x//10])
else:
    print(b[x//10]+'-'+a[x%10])