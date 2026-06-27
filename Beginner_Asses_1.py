games =[]

while True:
    user_games = input("Enter a game name (q to Quit): ")

    if user_games.lower() == "q":
        break 

    games.append(user_games)

print("--------------------------------------------")
print(f"Total Games: {len(games)}")
print()
print("********************************************")
count = 1

for game in games:
    print(f"Game {count}: {game}")
    count += 1

print("********************************************")