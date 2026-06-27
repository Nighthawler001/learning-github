games =set()

while True:
    user_games = input("Enter the game (q to quit): ")

    if user_games.lower() == "q":
        break

    games.add(user_games)

print(games)
print(f"Total Unique Games: {len(games)}")