ln = int(input("Enter length"))
bd = int(input("Enter breadth"))
ht = int(input("Enter height"))
cost = int(input("Cost"))

area = 2*((ln*bd)+(ln*ht)+(bd*ht))

tcost = area*cost

print(tcost)
