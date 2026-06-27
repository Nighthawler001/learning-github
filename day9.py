games = []

while True:
    add_games = input("Enter a Game (Q or q to quit): ")

    if add_games.lower() == 'q':
        break

    else:
        games.append(add_games)

total = 0
for game in range(len(games)):
    total +=1
print(f"Total Games: {total}")

print(f"First game: {games[0]}")
print(f"Last game: {games[-1]}")

longest =""

for game in games:
    if len(game) > len(longest):
        longest = game
    
print(f"Longest game: {longest}")