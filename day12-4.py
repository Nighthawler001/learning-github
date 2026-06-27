player = {
    "name": "Night",
    "age": 22
}

player["game"] = input("What's your favorite game? ")

for key,value in player.items():
    print(f"{key}: {value}")