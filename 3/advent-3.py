ITEM_VALUES = {
	'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 
	'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 
	'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 
	'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 
	'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 
	'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48,
	'W': 49, 'X': 50, 'Y': 51, 'Z': 52 }

def sumPriorities(line):
	comp1 = set(sorted(line.strip()[:len(line)//2]))
	comp2 = set(sorted(line.strip()[len(line)//2:len(line)]))
	found = (comp1 & comp2).pop()
	return ITEM_VALUES[found]

def sumGroups(lines):
	line1 = set(sorted(lines[0].strip()))
	line2 = set(sorted(lines[1].strip()))
	line3 = set(sorted(lines[2].strip()))
	badge = (line1 & line2 & line3).pop()
	return ITEM_VALUES[badge]

with open("input.txt", 'r') as file:
	lines = file.readlines()
	part1 = 0
	part2 = 0
	groups = []
	currentGroup = []
	groupCount = 0
	for line in lines:
		part1 = part1 + sumPriorities(line)
		if groupCount < 3:
			currentGroup.append(line.strip())
		groupCount = groupCount + 1
		if groupCount == 3:
			groups.append(currentGroup)
			currentGroup = []
			groupCount = 0
	for group in groups:
		part2 = part2 + sumGroups(group)
	
	print("Part 1:", part1)
	print("Part 2:", part2)
