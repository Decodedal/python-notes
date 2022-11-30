# Lambda Functions: another way to form functions shorter
#             the two args : what to do with them 
area = lambda length, width: length * width

print(area(3,3))

print("hi")

greeting = lambda name : print(f"Greetings {name}")

greeting("Dallas")

map(lambda state :state.capitalize(),["washingto","newYourk"])

# List Comprehensions:

#var_name = [expression for in loop]

squares = [num * num for num in range(1,11)]

print(squares)


#Set Comprehension:
                # you can tack if statment on at the end.
                # add all numbers to set if they are not divisable by 2
division = {num for num in range(10) if num % 2 != 0}

print (division)

#Dictionary Comprehension:
        #  key and value
doubled = {num - 1: num * 2 for num in range(10) if num > 5}

print(doubled)


class Car:
        def __init__(self, make, model):
                self.make = make 
                self.model = model

        def __str__(self):
                return f"make: {self.make}, model: {self.model}"   

        def __repr__(self):
                return f"make: {self.make}, model: {self.model}"     

        def __ne__(self, other):
                if self == other:
                        return False
                else:
                        return True                        

Dallas_car = Car("Lincon", "TownCar")
Lynn_car = Car("Toyota", "Camery")                

print(Dallas_car, Lynn_car)

print(Dallas_car != Lynn_car)


print(type(1.0) == float )