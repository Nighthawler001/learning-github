players = [
    {"name": "Night", "age": 22},
    {"name": "Alex", "age": 25},
    {"name": "John", "age": 20}
]

def find_oldest(players):
    oldest_player = ""
    highest_age = 0
    for player in players:
        if player["age"] > highest_age:
            highest_age = player["age"]
            oldest_player = player["name"]

    return oldest_player

print(find_oldest(players))