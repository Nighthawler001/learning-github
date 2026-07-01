numbers = [8,9,10,11,12,13,15,14,16]
# result = list(
#     filter(lambda n: n < 5, numbers)
# )
# print(result)


# result = []

# for n in numbers:
#     if n<5:
#         result.append(n)

# print(result)

# games = [
#     "Ark",
#     "Minecraft",
#     "GTA",
#     "Valorant"
# ]

# result = list(
#     filter(lambda game: len(game) > 3, games)
# )
# print(result)
# def is_long(word):
#     return len(word) > 4

# words = [
#     "Ark",
#     "Minecraft",
#     "GTA",
#     "Valorant"
# ]

# result = list(
#     filter(is_long, words)
# )
# result = list(
#     filter(lambda n: n > 10, numbers)
# )
# print(result)
result = [n for n in numbers if n>10]
print(result)