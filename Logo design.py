ih = int(input())
iw = int(input())
tw = int(input())
th = int(input())
bw = int(input())
bh = int(input())

for i in range(ih):
    print("*"*iw)
print()
for j in range(th):
    print("*"*tw)
for k in range(bh):
    gh=tw//2
    gh1=bw//2
    print(" "*(gh-gh1),end='')
    print("*"*bw)