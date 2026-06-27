def find_most_played(games):
    if not games:
        return "No games in library"
    
    most_played = games[0]
    for game in games:
        if game["hours"] > most_played["hours"]:
            most_played = game
            
    return most_played["name"]


def total_hours(games):
    total = 0
    for game in games:
        total += game["hours"]
    return total

games = []

while True:
    game_name = input("Enter game name (q to quit): ").strip()
    
    if game_name.lower() == 'q':
        break
        
    if not game_name:
        print("Game name cannot be empty!")
        continue

    already_exists = False
    for game in games:
        if game["name"].lower() == game_name.lower():
            already_exists = True
            break
            
    if already_exists:
        print("Game already exists.")
        continue

    while True:
        try:
            hours_input = input(f"Enter hours played for {game_name}: ")
            hours = int(hours_input)
            if hours < 0:
                print("Hours played cannot be negative. Please try again.")
                continue
            break  
        except ValueError:
            print("Please enter a valid number.")

    
    games.append({"name": game_name, "hours": hours})
    print(f"Added {game_name} ({hours} hours) to your library!\n")

print("\n" + "="*30)
print("       SUMMARY REPORT       ")
print("="*30)

total_games_count = len(games)

if total_games_count > 0:
    print(f"Total Games: {total_games_count}")
    print(f"Total Hours: {total_hours(games)}")
    print(f"Most Played Game: {find_most_played(games)}")
    
    print("\nGame Library:")
    index = 1
    for game in games:
        print(f"{index}. {game['name']} - {game['hours']} hours")
        index += 1
else:
    print("Your game library is empty!")

print("="*30)