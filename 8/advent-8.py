grid = []
totalVisibleTrees = 0
mostScenicTree = 0

def isVisible(left, right, top, bottom):
	global totalVisibleTrees
	if (max(left) < tree or max(right) < tree or max(top) < tree or max(bottom) < tree):
		totalVisibleTrees += 1

def calculateScenery(tree, left, right, top, bottom):
	global mostScenicTree
	leftScore = 0
	rightScore = 0
	topScore = 0
	bottomScore = 0
	for l in range(len(left)):
		if left[l] < tree:
			leftScore += 1
		elif left[l] >= tree:
			leftScore += 1
			break
	for r in range(len(right)):
		if right[r] < tree:
			rightScore += 1
		elif right[r] >= tree:
			rightScore += 1
			break
	for t in range(len(top)):
		if top[t] < tree:
			topScore += 1
		elif top[t] >= tree:
			topScore += 1
			break
	for b in range(len(bottom)):
		if bottom[b] < tree:
			bottomScore += 1
		elif bottom[b] >= tree:
			bottomScore += 1
			break
	if (leftScore * rightScore * topScore * bottomScore) > mostScenicTree: 
		mostScenicTree = (leftScore * rightScore * topScore * bottomScore)

with open("input.txt", 'r') as file:
	lines = file.readlines()
	for line in lines:
		grid.append(list(line.strip()))
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			tree = grid[r][c]
			leftTrees = grid[r][:c]
			rightTrees = grid[r][c+1:]
			topTrees = [grid[row][c] for row in range(r)]
			botTrees = [grid[row][c] for row in range(r + 1, len(grid))]
			if (c > 0 and c < len(grid) - 1 and r > 0 and r < len(grid[0]) - 1):
				isVisible(leftTrees, rightTrees, topTrees, botTrees)
			calculateScenery(tree, leftTrees[::-1], rightTrees, topTrees[::-1], botTrees)
	totalVisibleTrees += (len(grid) * 2 + (len(grid) - 2) * 2)
	print('part 1:', totalVisibleTrees)
	print('part 2:', mostScenicTree)