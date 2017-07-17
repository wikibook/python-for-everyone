base = [1, 2, 3]
result = [ (x, y) for x in base for y in base if x != y ]
print(result)


