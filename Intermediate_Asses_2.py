players = [
    {"name": "Night", "age": 22},
    {"name": "Alex", "age": 25},
    {"name": "John", "age": 20}
]

try:
    user_age = int(input("Enter minimum age: "))

    for player in players:
        if player["age"] >= user_age:
            print(f"{player['name']} - {player['age']}")

except ValueError:
    print("Input should be an integer")