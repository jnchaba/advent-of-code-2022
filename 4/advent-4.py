def partOneProcessLine(line):
	pairs = line.split(',')
	one = pairs[0]
	two = pairs[1]
	rangeOne = one.split('-')
	rangeTwo = two.split('-')
	rangeOneWithinRangeTwo = (int(rangeOne[0]) >= int(rangeTwo[0])) and (int(rangeOne[1]) <= int(rangeTwo[1]))
	rangeTwoWithinRangeOne = (int(rangeTwo[0]) >= int(rangeOne[0])) and (int(rangeTwo[1]) <= int(rangeOne[1]))

	if rangeOneWithinRangeTwo or rangeTwoWithinRangeOne:
		return True
	else:
		return False

def partTwoProcessLine(line):
	pairs = line.split(',')
	one = pairs[0]
	two = pairs[1]
	rangeOne = one.split('-')
	rangeTwo = two.split('-')
	rangeOneWithinRangeTwo = ((int(rangeOne[0]) >= int(rangeTwo[0])) and (int(rangeOne[0]) <= int(rangeTwo[1]))) or ((int(rangeOne[1]) <= int(rangeTwo[1])) and (int(rangeOne[1]) >= int(rangeTwo[0])))
	rangeTwoWithinRangeOne = ((int(rangeTwo[0]) >= int(rangeOne[0])) and (int(rangeTwo[0]) <= int(rangeOne[1]))) or ((int(rangeTwo[1]) <= int(rangeOne[1])) and (int(rangeTwo[1]) >= int(rangeOne[0])))

	if rangeOneWithinRangeTwo or rangeTwoWithinRangeOne:
		return True
	else:
		return False

with open("input.txt", 'r') as file:
	lines = file.readlines()
	part1 = 0
	part2 = 0
	for line in lines:
		strippedLine = line.strip()
		elvesAreCompletelyWastngTime = partOneProcessLine(strippedLine)
		elvesArePartiallyWastingTime = partTwoProcessLine(strippedLine)
		if elvesAreCompletelyWastngTime:
			part1 = part1 + 1
		if elvesArePartiallyWastingTime:
			part2 = part2 + 1
	print("part1: ", part1)
	print("part2: ", part2)
