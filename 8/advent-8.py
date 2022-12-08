grid = []

VISIBLE = 0

with open("input.txt", 'r') as file:
	
	lines = file.readlines()
	for line in lines:
		grid.append(list(line.strip()))
	for i in range(1, len(grid) - 1):
		for j in range(1, len(grid[0]) - 1):
			tree = grid[i][j]
			if (max(grid[i][:j]) < tree or 
				max(grid[i][j+1:]) < tree or
				max([grid[row][j] for row in range(i)]) < tree or
				max([grid[row][j] for row in range(i + 1, len(grid))]) < tree):
				VISIBLE += 1
	VISIBLE += (len(grid) * 2 + (len(grid) - 2) * 2)



	print('visible', VISIBLE)