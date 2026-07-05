# class Student():
#     def __init__(self,name,grade):
#         self.name = name 
#         self.grade = grade
    
#     @classmethod
#     def create_new_student(cls,name):
#         return cls(name,"Not Assigned")

# student = Student.create_new_student("Night")

# print(student.name)
# print(student.grade)
# O/P 
# Night
# Not Assigned

# class Game():
#     def __init__(self,title,hours,completed):
#         self.title = title
#         self.hours = hours
#         self.completed = completed

#     @classmethod
#     def create_new_game(cls,title):
#         return cls(title,0,False)

# game = Game.create_new_game("Cyberpunk 2077")

# print(f"Game: {game.title}")
# print(f"Played Hours: {game.hours} hrs")
# print(f"Completed? {game.completed}")
# O/P 
# Game: Cyberpunk 2077
# Played Hours: 0 hrs
# Completed? 0