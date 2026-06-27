try:
    number = int(input("What's the number? "))
    print(10/number)
except ValueError:
    print("Please enter a number")

except ZeroDivisionError:
    print("Cannot divide by zero")