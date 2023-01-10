p = int(input("Enter the principle"))
r = int(input("Enter rate"))
t1 = 2
t2 = 2

#compound interest for the first 2 years
ci =  p * ((1+r/100)**t1) 
print(ci)

p = ci
total = (p*r*t2)/100



