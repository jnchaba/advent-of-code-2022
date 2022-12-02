values = dict()
# Rock = A == X
values["Rock"] = 1
# Paper = B == Y
values["Paper"] = 2
# Scissors = C == Z
values["Scissors"] = 3
# Paper beats Rock. 2 - 1 = 1 == WIN. Rock loses to Paper. 1 - 2 = -1 == LOSS.
# Rock beats Scissors. 1 - 3 = -2 == WIN. Scissors loses to Rock. 3 - 1 = 2 == LOSS.
# Scissors beats Papaer. 3- 2 = 1 == WIN. Paper loses to Scissors. 2 - 3 = -1 == LOSS.

label = dict()
label["A"] = "Rock"
label["X"] = "Rock"
label["B"] = "Paper"
label["Y"] = "Paper"
label["C"] = "Scissors"
label["Z"] = "Scissors"

bigBrain = dict()
bigBrain[1] = "X"
bigBrain[2] = "Y"
bigBrain[3] = "Z"

# X == need to lose. Y == need to draw. Z == need to win.

def calculateMove(opponent, me):
	oppMove = label[opponent]
	oppValue = values[oppMove]
	returnValue = ""
	if me == "X":
		if oppValue > 1:
			returnValue = bigBrain[oppValue - 1]
		else:
			returnValue = "Z"
	elif me == "Y":
		returnValue = bigBrain[oppValue]
	elif me == "Z":
		if oppValue < 3:
			returnValue = bigBrain[oppValue + 1]
		else:
			returnValue = "X"
	return returnValue


def calculateWinner(opponent, me):
	asciiOpp = ord(opponent)
	asciiMe = ord(me) - 23
	winner = asciiMe - asciiOpp
	if winner == 1 or winner == -2:
		return 6
	elif winner == 0:
		return 3
	elif winner == -1 or winner == 2:
		return 0

def processLine(line, part2):
	turns = line.split()
	opponent = turns[0]
	me = turns[1]
	if (part2):
		me = calculateMove(opponent, me)
	pointsFromWinning = values[label[me]] + calculateWinner(opponent, me)
	return pointsFromWinning


with open("input.txt", 'r') as file:
	lines = file.readlines()
	totalScore = 0
	lineCount = 0
	for line in lines:
		lineCount = lineCount + 1
		totalScore = totalScore + processLine(line, True)
	print("total score: " + str(totalScore))
