games = []

while True:
    user_games = input("Enter a game (q to quit):")

    if user_games.lower() =="q":
        break

    games.append(user_games)

def find_longest_game(games):
    longest_game=""

    for game in games:
        if len(game)>len(longest_game):
            longest_game = game
    return longest_game

print(f"Total Games: {len(games)}")
print()
print(f"First game: {games[0]}")
print(f"Last game: {games[-1]}")
print(f"Longest Game: {find_longest_game(games)}")