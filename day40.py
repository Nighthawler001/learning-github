# class Student():
#     def __init__(self,name):
#         self.name = name 

#     def __eq__(self, other):
#         return self.name == other.name
    
# student1 = Student("Night")
# student2 = Student("Night")

# print(student1 == student2)
# O/P 
# True

# class Game():
#     def __init__(self,title,hours):
#         self.title =title
#         self.hours = hours

#     def __eq__(self, other):
#         if not isinstance(other,Game):
#             return False
#         return (
#         self.title == other.title
#         and
#         self.hours == other.hours
#         )

# game1 = Game("Ark", 220)
# game2 = Game("Ark", 220)

# print(game1 == game2)

# game3 = Game("Ark", 100)

# print(game1 == game3)
# O/p 
# True
# True

# class Student():
#     def __init__(self,grade):
#         self._grade = grade
    
#     @property
#     def grade(self):
#         return self._grade
    
#     @grade.setter
#     def grade(self,new_grade):
#         if new_grade.strip()=="":
#             print("Invalid grade.")
#             return
    
#         self._grade = new_grade
    
# student = Student("A")

# print(student.grade)

# student.grade = "B"

# print(student.grade)

# student.grade = ""
# O/P 
# A
# B
# Invalid grade.

# class Game():
#     def __init__(self,rating):
#         self._rating = rating
    
#     @property
#     def rating(self):
#         return self._rating

#     @rating.setter
#     def rating(self,new_rating):
#         if 1 <= new_rating <=5:
#             self._rating = new_rating
#         else:
#             print("Invalid rating")

# game = Game(5)

# print(game.rating)

# game.rating = 3

# print(game.rating)

# game.rating = 10
# O/P 
# 5
# 3
# Invalid rating