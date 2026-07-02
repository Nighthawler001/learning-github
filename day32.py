# numbers = [100, 200]

# a, b = numbers

# print(a)
# print(b)
# numbers = [1, 2, 3, 4]

# first, *rest = numbers

# print(first)
# print(rest)
# games = [
#     "Ark",
#     "Minecraft",
#     "Valorant",
#     "GTA V"
# ]

# first, *middle, last = games

# print(first)
# print(middle)
# print(last)
# numbers = [1, 2, 3]

# *start, end = numbers

# print(start)
# print(end)
# numbers = [10, 20]

# first, *rest = numbers

# print(first)
# print(rest)
# numbers = [10]

# *start, end = numbers

# print(start)
# print(end)
# numbers = [10]

# first, *middle = numbers

# print(first)
# print(middle)
# numbers = [1, 2]

# first, *middle, last = numbers

# print(first)
# print(middle)
# print(last)
# numbers = [1, 2, 3, 4, 5]

# *start, second_last, last = numbers

# print(start)
# print(second_last)
# print(last)
# pair = ("Night", 95)

# name, score = pair

# print(name)
# print(score)
# games = [
#     ("Ark", 220),
#     ("Minecraft", 120)
# ]

# for game, hours in games:
#     print(f"{game} - {hours}")
# a = 5
# b = 10

# a, b = b, a

# print(a)
# print(b)
# player = ("Night", 22, "India")

# name, age, country = player

# print(age)
# numbers = [1, 2, 3, 4]

# first, *middle, last = numbers
# print(*middle)

# print(len(middle))
# numbers = [2, 3]

# new_list = [1, *numbers, 4]

# print(new_list)
games1 = ["Ark"]
games2 = ["Minecraft", "Valorant"]

games = [*games1, *games2]

print(games)