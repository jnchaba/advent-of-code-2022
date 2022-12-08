class File:
	def __init__(self, name, size, parent):
		self.name = name
		self.size = int(size)
		self.parent = parent
		self.parent.updateSize(int(size))

class Directory:
	def __init__(self, name, parent=None):
		self.name = name
		if (parent and type(parent) == Directory):
			self.parent = parent
		else:
			self.parent = None
		self.folders = []
		self.files = []
		self.size = 0
	
	def appendFolder(self, folder):
		if (type(folder) == Directory):
			self.folders.append(folder)
	
	def appendFile(self, file):
		if (type(file) == File):
			self.files.append(file)
	
	def updateSize(self, size):
		self.size += int(size)
		if self.parent:
			self.parent.updateSize(int(size))

currentDirectory = None
root = None

def changeCurrentDirectory(directory):
	global currentDirectory
	global root
	if currentDirectory == None:
		root = directory
	currentDirectory = directory

def processResult(line):
	global currentDirectory
	result = line.split()
	if (not result[0].isnumeric()):
		newFolder = Directory(result[1], currentDirectory)
		currentDirectory.appendFolder(newFolder)
	else:
		newFile = File(result[1], result[0], currentDirectory)
		currentDirectory.appendFile(newFile)	

def processCommand(line):
	global currentDirectory
	command = line.split()
	if (command[1] == "cd"):
		if currentDirectory == None:
			changeCurrentDirectory(Directory('/'))
		for folder in currentDirectory.folders:
			if folder.name == command[2]:
				changeCurrentDirectory(folder)
				break
		if (command[2] == '..'):
			changeCurrentDirectory(currentDirectory.parent)

def processLine(line):
	if (line[0] == '$'):
		processCommand(line)
	else:
		processResult(line)

def partOne(directory, maxsize, results):
	if (directory.size <= maxsize):
		results.append(directory)
	for folder in directory.folders:
		results = partOne(folder, maxsize, results)
	return results

def partTwo(directory, minsize, results):
	if (directory.size >= minsize):
		results.append(directory)
	for folder in directory.folders:
		results = partTwo(folder, minsize, results)
	return results

with open("input.txt", 'r') as file:
	lines = file.readlines()
	for line in lines:
		processLine(line.strip())
	totalSize = 0
	for directory in partOne(root, 100000, []):
		totalSize += directory.size
	print("part one:", totalSize)
	diskSpace = 70000000
	neededSpace = 30000000
	freeSpace = diskSpace - root.size
	smallestDeletableDirectory = 0
	for directory in partTwo(root, (neededSpace - freeSpace), []):
		if smallestDeletableDirectory == 0 or directory.size < smallestDeletableDirectory.size:
			smallestDeletableDirectory = directory
	print("part two:", smallestDeletableDirectory.size)