players = [
    {"name": "Night", "age": 22},
    {"name": "Alex", "age": 25},
    {"name": "John", "age": 20}
]

oldest_age =0
oldest_player =""

for player in players:
    if player["age"] >oldest_age:
        oldest_age = player["age"]
        oldest_player = player["name"]
        
    
print(f"Oldest player is {oldest_player} and his age is {oldest_age}")