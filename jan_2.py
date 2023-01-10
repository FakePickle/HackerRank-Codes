#q1 check if a string is a heterogram
def check_het():
    s=input()
    x=set(s)
    print(x)
    if len(x)==len(s):
        print("heterogram")
    else:
        print("not a heterogram")
# check_het()
        
# find multiples of 15 using sets of multiples of 3 and 5
def mult_15():
    n=int(input())
    set3=set()
    set5=set()
    for i in range(1,n+1):
        if i%3==0:
            set3.add(i)
        if i%5==0:
            set5.add(i)
    print("Set 3 elemets => ",set3)
    print("Set 5 elemets = > ",set5)
    
    #finding the intersection of the two sets
    set15=set3.intersection(set5)
    print("Set 15 elemets => ",set15)
    # set15.symmetric_difference_update(set3)
# mult_15()

def tuple_demo():
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(int(input()))
    
    my_tuple = tuple(lst)
    my_new_tuple = my_tuple[:4] + my_tuple[5:]
    singleton_tuple = (my_tuple[4],)
    my_newer_tuple = my_new_tuple + singleton_tuple
    print(my_newer_tuple)
# tuple_demo()

def func():
    my_str = input()
    my_str = my_str.lower()
    my_dict = {}
    
    is_heterogram = 1
    
    for i in my_str:
        
        if i not in my_dict.keys():
            my_dict[i] = 1
        else:
            is_heterogram = 0
            my_dict[i] += 1
        print(my_dict)
    
    # print(len(my_dict)==len(my_str))
    if is_heterogram == 1:
        print("Yes, it is a heterogram")
    else:
        print("Not a heterogram")
    
    for key,value in my_dict.items():
        print(key, value)
# func()

def dict_func():
    population = {'Ram': 20, 
                'Shyam': 80,
                'Mohan': 45,
                'Rahul': 16,
                'Heena': 17,
                'Neha': 15,
                'Salman': 18}

    population['Neha'] =17 
    voters = {}
    for key in population.keys():
        print(key,population[key])
        if population[key] >= 18:
            voters[key] = population[key]
    
    print(voters) 


