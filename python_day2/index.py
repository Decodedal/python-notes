def greeting(first_name, mid_name, last_name):
    first = first_name
    mid =mid_name
    last =last_name
    return first , mid , last

#can call these anything not qute the same as destructuring 
one, two, three = greeting("Dallas", "Andrew","Palumbo")

#print(three)

#nested functions
def inner_funcs(int_param):
    def minus_five(inner_param):
        return inner_param - 5
#inner function call
    new_val = minus_five(int_param)
    
    return(new_val)

#print(inner_funcs(10))   

#Default args
#the = 0 after num_two means that it will defalt to zero if their is no input
def default_add(num_one, num_two = 0):
    total = num_one + num_two
    return total

sum_one = default_add(6,4)
sum_two = default_add(6)

#print(sum_two)

#Arbitrary Arguments (*args)
def print_all(*args):
    print(args)

#print_all(1,5,"Dallas","Poo")    


#Recursive function 

#factorial 4! = 4 *3 *2 *1 

def find_factorial(num):
    #Base case
    if num == 1:
        print(num)
        return 1
    #Recursive case
    else:
        print(num)
        return(num * find_factorial(num -1) )

#print(find_factorial(4))

# **kwargs keyword arguments ** is the important part "kwarg could be anything"

def print_contacts(**kwargs):
    for name, phone in kwargs.items():
        print(f"{name.title()}, {phone}")


print_contacts(Dallas = "718-290-3752", lynn = "555-555-5555")  


x = "dallas"

print(x.replace('a', 'b'))