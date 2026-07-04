# class Animal():
#     def __init__(self,name,health):
#         self.name = name 
#         self.health = health
    
#     def sleep(self):
#         print(f"{self.name} is sleeping")
    
#     def eat(self):
#         print(f"{self.name} is eating")

# class Cat(Animal):
#     pass

# class Dog(Animal):
#     pass
# class Bird(Animal):
#     pass

# cat = Cat("Jack",420)

# cat.eat()

# class Animal():
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name} makes a sound")

# class Dog(Animal):
#     pass

# dog = Dog("Buddy")

# dog.speak()

# class Vehicle():
#     def __init__(self,brand):
#         self.brand = brand
    
#     def start(self):
#         print(f"{self.brand} started")

# class Car(Vehicle):
#     def drive(self):
#         print(f"{self.brand} is driving")
    
# car  = Car("Toyota")

# car.start()
# car.drive()

# class Animal():
#     def move(self):
#         print("Animal moves")

# class Bird(Animal):
#     def move(self):
#         print("Bird flies")

# bird = Bird()
# bird.move()

# class Vehicle:
#     def __init__(self,brand):
#         self.brand = brand
    
#     def start(self):
#         print("Vehical started.")

# class Car(Vehicle):
#     def start(self):
#         print(f"{self.brand} car started.")
    
# car = Car("Toyota")

# car.start()
# O/P 
# Toyota car started.

# class Person:
#     def __init__(self,name):
#         self.name = name

# class Student(Person):
#     def __init__(self, name,grade):
#         super().__init__(name)
#         self.grade =grade

# student = Student("Night","A+")

# print(student.name)
# print(student.grade)
# o/p 
# Night
# A+

class Animal():

    def __init__(self,name,health):
        self.name = name 
        self.health = health
class Rex(Animal):
    def __init__(self, name, health,roar_power):
        super().__init__(name, health)
        self.roar_power = roar_power
    
rex = Rex("Rex", 500, 90)

print(rex.name)
print(rex.health)
print(rex.roar_power)
# o/p 
# Rex
# 500
# 90
