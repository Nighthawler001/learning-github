numbers = [1, 2, 3, 4]

result = {
    n: "Big" if n > 2 else "Small"
    for n in numbers
}

print(result)