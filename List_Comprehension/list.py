a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = [x**2 for x in a]

print(squares)

squares1 = map(lambda s: s**2, a)

print(squares1)

even_sqjares = [x**2 for x in a if x % 2 == 0]

print(even_sqjares)

lat = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))

chile_ranks = {"ghost": 1, "habanero": 2, "cayenne": 3}

rank_dict = {rank: name for name, rank in chile_ranks.items()}

chile_le_set = {len(name) for name in rank_dict.values()}

print(rank_dict)

print(chile_le_set)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [x for row in matrix for x in row]

print(flat)

squaraed = [[x**2 for x in row] for row in matrix]

print(squaraed)

value = [len(x) for x in open('/temp/file.txt')]

print(value)

it = (len(x) for x in open('/temp/file.txt'))

print(next(it))
print(next(it))