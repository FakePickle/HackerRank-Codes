def reverse_digit(n):
    a=0
    n=str(n)
    r=n[::-1]
    for i in r:
        if i=="0":
            a+=1
        else:
            break
    if a:
        x=r[a:]
        return int(x)
    return int(r)
n = int(input())
print(reverse_digit(n))
