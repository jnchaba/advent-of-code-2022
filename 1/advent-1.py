class Elf: 
	def __init__(self, number):
		self.number = number
		self.calories = []

	def appendCalories(self, kcal):
		self.calories.append(kcal)
	
	def getTotalCalories(self):
		return sum(self.calories)
	
	def getElfName(self):
		return "Elf " + str(self.number)

elfDictionary = dict()
elfNumber = 1
elf = Elf(elfNumber)
with open("input.txt", 'r') as file:
	lines = file.readlines()

	for line in lines:
		if line.strip():
			elf.appendCalories(int(line))
		else:
			elfDictionary[elf.getElfName()] = elf.getTotalCalories()
			elfNumber = elfNumber + 1
			elf = Elf(elfNumber)

elfPreppersTotalCalories = 0

for i in range(3):
	fatElf = max(elfDictionary, key=elfDictionary.get)	
	print("Fattest Elf: " + str(fatElf) + " with " + str(elfDictionary[fatElf]) + " kcal")
	elfPreppersTotalCalories = elfPreppersTotalCalories + elfDictionary[fatElf]
	del elfDictionary[fatElf]

print("Calories carried by top 3 elves: " + str(elfPreppersTotalCalories))