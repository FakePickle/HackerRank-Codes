p = int(input("Enter the principle amount : "))
r = int(input("Enter the rate of interest : "))
t = int(input("Enter the time in the years: "))

ci =  p * ((1+r/100)**t) 

print(ci)