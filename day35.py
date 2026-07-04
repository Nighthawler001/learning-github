# class Animal():
#     def eat(self):
#         print("Animal eats.")

# class Cat(Animal):
#     def eat(self):
#         print("Cat eats fish.")

# class Dog(Animal):
#     def eat(self):
#         print("Dog eats dog food.")

# animals = [Cat(),Dog()]

# for animal in animals:
#     animal.eat()
# O/p 
# Cat eats fish.
# Dog eats dog food.

# class Weapon():
#     def attack(self):
#         print("𓆩☠︎︎𓆪 Weapon attacks 𓆩☠︎︎𓆪")

# class Sword(Weapon):
#     def attack(self):
#         print("⚔️ Sword slashes! ⚔️")

# class Bow(Weapon):
#     def attack(self):
#         print("🏹 Bow shoots an arrow! 🏹")

# class Staff(Weapon):
#     def attack(self):
#         print("🪄 Staff casts a spell! 🪄")

# weapons = [Sword(),Bow(),Staff()]

# for weapon in weapons:
#     weapon.attack()

# O/P 
# ⚔️ Sword slashes! ⚔️
# 🏹 Bow shoots an arrow! 🏹
# 🪄 Staff casts a spell! 🪄

# class Player():
#     def __init__(self):
#         self.__health = 100
#     def take_damage(self,amount):
#         self.__health -= amount
#     def show_health(self):
#         print(self.__health)

# player = Player()

# player.take_damage(30)
# player.show_health()
# O/P 
# 70

# class BankAccount():
#     def __init__(self):
#         self.__balance = 0
    
#     def deposit(self,amount):
#         if amount >0:
#             self.__balance += amount
#         print(f"${amount} deposited to your account.")
    
#     def withdraw(self,amount):
#         if amount > self.__balance:
#             print("Insufficient balance.")
#         else:
#             self.__balance -= amount
#             print(f"${amount} withdraw from your account.")
    
#     def show_balance(self):
#         print("-"*30)
#         print(f"Current Balance: ${self.__balance}")

# account = BankAccount()

# account.deposit(1000)

# account.withdraw(300)

# account.show_balance()
# O/P 
# $1000 deposited to your account.
# $300 withdraw from your account.
# ------------------------------
# Current Balance: $700

# Abstraction

# from abc import ABC, abstractmethod

# class Shape(ABC):
    
#     @abstractmethod
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self,side):
#         self.side = side
    
#     def area(self):
#         print(self.side * self.side)

# square = Square(5)

# square.area()
# O/P 
# 25

from abc import ABC,abstractmethod

class Weapon(ABC):
    
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Sword slashes!")

class Bow(Weapon):
    def attack(self):
        print("Bow shoots an arrow!")
    
weapons = [Sword(),Bow()]

for weapon in weapons:
    weapon.attack()