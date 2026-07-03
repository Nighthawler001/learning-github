# class Car():
#     def __init__(self,brand,speed):
#         self.brand = brand
#         self.speed = speed

# car1 = Car("Toyota", 120)
# car2 = Car("BMW", 180)
# car3 = Car("Tesla", 200)
# print(car1.brand,car1.speed)
# print(car2.brand,car2.speed)
# print(car3.brand,car3.speed)

# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
# student = Student("Night", 22)

# print(f"{student.name}\n{student.age}")

# class Book():
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

# book1 = Book("Atomic Habits","James Clear","320")
# book2 = Book("Clean Code","Robert C. Martin","464")

# print(f"{book1.title} — {book1.author} — {book1.pages}")
# print(f"{book2.title} — {book2.author} — {book2.pages}")

# class Student():
#     def __init__(self,name):
#         self.name = name 
    
#     def study(self):
#         return f"{self.name} is studying"

# student = Student("Night")

# print(student.study())

# class Game( ):
#     def __init__(self,name,hours):
#         self.name = name
#         self.hours = hours
    
#     def play(self):
#         return f"Playing {self.name} for {self.hours} hours"

# game1 = Game("Ark",220)
# game2 = Game("Minecraft",120)

# print(game1.play())
# print(game2.play())
# O/P
# Playing Ark for 220 hours
# Playing Minecraft for 120 hours

# class Counter():
#     def __init__(self):
#         self.count = 0
    
#     def increase(self):
#         self.count += 1
#     # Just for experiment
#     def decrease(self):
#         self.count -= 1

# counter = Counter() 
# counter.increase()
# counter.increase()
# counter.increase()
# print(counter.count)
# counter.decrease()
# counter.decrease()

# print(counter.count)

# class Game():
#     def __init__(self,name,hours):
#         self.name = name
#         self.hours = hours
    
#     def play(self,played_hours):
#         self.hours += played_hours
#         return self.hours

# game = Game("Ark",220)

# game.play(5)
# print(game.hours)
# game.play(10)
# print(game.hours)

# class Engine():
#     def __init__(self,horsepower):
#         self.horsepower = horsepower
    
#     def start(self):
#         print("Engine started!")
    
# class Car():
#     def __init__(self,brand):
#         self.brand = brand
#         self.engine = Engine(150)

# car = Car("Toyota")

# car.engine.start()


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"'{item}' added to the inventory.")

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()

player = Player("Night")
player.inventory.add_item("Sword")
player.inventory.add_item("Potion")