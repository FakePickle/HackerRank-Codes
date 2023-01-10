n = int(input())
order = []
for i in range(n):
    a = int(input())
    order.append(a)
cost = 0

for i in range(len(order)):
    if order[i]<6 and order[i]>0:
        cost += 5
    elif order[i]>5 and order[i]<13:
        cost += 10
    elif order[i]>12:
        cost += 20
print(cost)