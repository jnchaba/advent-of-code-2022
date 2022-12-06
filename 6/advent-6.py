from collections import Counter

with open("input.txt", 'r') as file:
	lines = file.readlines()
	detectedPacket = False
	detectedMessage = False
	for line in lines:
		length = len(line)
		for i in range(length):
			if (i < length - 4):
				packetWindow = line[i:i+4]
				messageWindow = line[i:i+14]
				packetFreq = Counter(packetWindow)
				messageFreq = Counter(messageWindow)
				if (len(packetFreq) == 4 and not detectedPacket):
					print("Part 1: ", i + 4)
					detectedPacket = True
				if (len(messageFreq) == 14 and not detectedMessage):
					print("Part 2: ", i + 14)
					detectedMessage = True
