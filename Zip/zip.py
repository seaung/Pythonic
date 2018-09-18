name = ["json", "lxml", "parse"]
age = [1, 2, 3]

max_letters = 0

for name, count in zip(name, age):
    if count > max_letters:
        longest_name = name
        max_letters = count
