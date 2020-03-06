def solid_rectangle(rows):
	for i in range(1, rows):
		for j in range(1, rows + 1):
			print('*', end = '')
		print()


def printPattern(rows):
	print('solid_rectangle:')
	solid_rectangle(rows)


rows = 90
printPattern(rows)
