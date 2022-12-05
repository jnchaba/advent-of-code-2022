IDX_MAP = {
	1 : 0, 5 : 1, 9 : 2, 13 : 3, 17 : 4, 21 : 5, 25 : 6, 29 : 7, 33 : 8
}

def processStackLine(line, stacks):
	for idx, char in enumerate(line):
		if char != " " and char != "]" and char != "[" :
			indexToPushTo = IDX_MAP[int(idx)]
			stacks[indexToPushTo].append(char)
	return stacks

def readStacks():
	stacks = [[],[],[],[],[],[],[],[],[]]
	with open("input.txt", 'r') as file:
		containerLines = file.readlines()[0:8]
		for line in containerLines:
			strippedLine = line.strip()
			stacks = processStackLine(strippedLine, stacks)
	for stack in stacks:
		stack = stack.reverse()
	return stacks

def processMove(num, source, destination, stacks, part1):
	source = source - 1
	destination = destination - 1
	if (part1):
		for i in range(num):
			container = stacks[source].pop()
			stacks[destination].append(container)
	else:
		containers = []
		for i in range(num):
			containers.append(stacks[source].pop())
		for container in reversed(containers):
			stacks[destination].append(container)
	return stacks

def topOfStacks(stacks):
	return "" + stacks[0][-1] + stacks[1][-1] + stacks[2][-1] + stacks[3][-1] + stacks[4][-1] + stacks[5][-1] + stacks[6][-1] + stacks[7][-1] + stacks[8][-1]

with open("input.txt", 'r') as file:
	stacks = readStacks()
	lines = file.readlines()[10:]
	part1 = 0
	part2 = 0
	for line in lines:
		instruction = line.strip().split()
		num = int(instruction[1])
		source = int(instruction[3])
		dest = int(instruction[5])
		stacks = processMove(num, source, dest, stacks, True)
	print("result:", topOfStacks(stacks))