numbers= [1,2,3]
# result = list(
#     map(lambda n: n * 3, numbers)
# )
# print(result)
# numbers= [1,2,3]
# result = []

# for n in numbers:
#     result.append(n*3)

# print(result)
names = ["night", "alex", "john"]

# result = list(
#     map(lambda name: name.capitalize(), names)
# )

# print(result)
# words = ["ark", "minecraft", "gta"]

# def make_upper(word):
#     return word.upper()

# result = list(
#     map(make_upper, words)
# )

# print(result)

# result = list(
#     map(lambda n: n * 5, numbers)
# )
# print(result)

result = [n*5 for n in numbers]
print(result)