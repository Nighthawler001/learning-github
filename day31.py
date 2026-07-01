# numbers = [1, 3, 5, 8]

# print(any(n % 2 == 0 for n in numbers))
# numbers = [2, 4, 6, 8]

# print(all(n % 2 == 0 for n in numbers))
# games = [
#     "Ark",
#     "Minecraft",
#     "Valorant"
# ]

# result = any(
#     len(game) > 8
#     for game in games
# )

# print(result)
# numbers = [10, 20, 3, 40]

# print(all(n > 5 for n in numbers))
words = [
    "Ark",
    "Minecraft",
    "GTA"
]

print(any(len(word) > 20 for word in words))