import random

def random_cacti(row, column):
	return [
		[random.randint(0, 9) for _ in range(row)]
		for _ in range(column)
	]

def print_cacti(cactus):
	for row in cactus:
		print(" ".join(f"{c}" for c in row))

print_cacti(random_cacti(4, 4))
