with open("game.txt", "a") as file:
    while True:
        game = input("Enter a game name (or 'q' to quit): ")
        if game.lower() == "q":
            break
        file.write(game + "\n")

with open("game.txt", "r") as file:
    games = file.readlines()

print(f"\nTotal Games: {len(games)}")
for i, game in enumerate(games, 1):
    print(f"Game {i}: {game.strip()}")