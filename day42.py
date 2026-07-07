# try:
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("Age must be an integer")
# else:
#     print("Age accepted")
# O/p 
# Enter your age: 25
# Age accepted
# (.venv) PS C:\Users\admin\Desktop\Python practice> & "c:\Users\admin\Desktop\Python practice\.venv\Scripts\python.exe" "c:/Users/admin/Desktop/Python practice/learning-github/day42.py"
# Enter your age: two five
# Age must be an integer
# (.venv) PS C:\Users\admin\Desktop\Python practice> 

class Student():
    def __init__(self,name,grade):
        if grade < 0:
            raise ValueError("Grade cannot be negative.")
        self.name = name
        self.grade = grade


try:
    # student = Student("Night", 90)
    student = Student("Night", -5)
    print(f"Student name: {student.name} - Grade: {student.grade}")
except ValueError as e:
    print(f"Error creating student: {e}")