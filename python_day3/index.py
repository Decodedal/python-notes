#OOP
#function declared in a class is called a method

class Car:
    def start(self):
        return("vroom!")

    def talk(self, driver):
        return(f"Greetings, {driver}.")     

my_car = Car()   
dallas_car =Car()

print(dallas_car.talk("Dallas"))
print(my_car.talk("kent"))

#init will give absic data to each class much like this in javascript

class Person:
    arms = 4
    senses = 5
    def __init__(self,name):
        # print('Hello!')
        self.name = name
     

    def talk(self, country):
        return(f"hello, {country}, I am {self.name} i have {self.senses}")    

dallas = Person('Dallas')
cody = Person('Cody')
lynn = Person('Lynn')

print(dallas.talk("america"), lynn.talk("cambodia"))

#print(dallas.name, cody.name, lynn.name)

#class inheritence accepts arent class as argument inherits parents methods

class Robot_person(Person):
    def __init__(self, name, type):
        super().__init__(name)

        self.type = type
        

    def who_am(self):
        return (f"My name is {self.name} i am a {self.type} murderbot from the future i have {self.arms} arms to stab you with. and {self.senses} senses to hunt you with!")   


ti88 = Robot_person("murder_bot", "sentient")
#inherited method from parent class "Person"
print(ti88.talk('john conner'))
print(ti88.who_am())



def is_consonant(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(letter not in vowels): 
        return True
    else: 
      return False
   
letter_list = ['k', 'o', 'a', 'l', 'a']

filter(is_consonant, letter_list)

print(letter_list)
