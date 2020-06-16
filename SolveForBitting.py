import csv

bottomPins = {}
with open('BottomPins.csv') as bottomPinsFile:
	reader = csv.reader(bottomPinsFile, delimiter=',')
	header = next(reader, None)
	bottomPins['k'] = [None] + next(reader, None)
	bottomPins['m'] = [None] + next(reader, None)
	bottomPins['b'] = [None] + next(reader, None)
	bottomPins['d'] = [None] + next(reader, None)
	bottomPins['q'] = [None] + next(reader, None)
	bottomPins['s'] = [None] + next(reader, None)

	for row in bottomPins.keys():
		for col,val in enumerate(bottomPins[row]):
			if (bottomPins[row][col] != None):
				# print(bottomPins[row][col])
				bottomPins[row][col] = int(val)

# print(bottomPins)

# Access bottomPins dict of arrays with the letter and 1-indexed number as follows
# print(bottomPins['s'][5])

masterWafers = []
with open('MasterWafers.csv') as masterWafersFile:
	reader = csv.reader(masterWafersFile, delimiter=',')
	header = next(reader, None)
	masterWafers = next(reader, None)
masterWafers = [None] + masterWafers

# Access masterWafers array with the 1-indexed number as follows
# print(masterWafers[1])

keys = {}
with open('Keys.csv') as keysFile:
	reader = csv.reader(keysFile, delimiter=',')
	header = next(reader, None)
	for row in reader:
		# print(row[0] + ',' + row[7] + ',' + row[8] + ',' + row[9] + ',' + row[10] + ',' + row[11] + ',' + row[12] + ',' + row[13])
		keys[row[0]] = [None] + [row[7],row[8],row[9],row[10],row[11],row[12],row[13]]

# Access array of key bittings as such. 1-indexed, so to get the first pin of MF1 stamp:
# print(keys['MF1'][1])

def pinsAreAvailable(key):
	for pin in key:
		if pin == None or pin == '': continue

		# print(bottomPins[pin[1]][int(pin[0])])
		if bottomPins[pin[1]][int(pin[0])] <= 0:
			return False
	
	# We found a bitting we have pins for, so deduct from the counts
	for pin in key:
		if pin == None or pin == '': continue
		# print(pin[1])
		# print(pin[0])
		if bottomPins[pin[1]][int(pin[0])] != None:
			bottomPins[pin[1]][int(pin[0])] -= 1


	return True

count = 0
for key,bitting in keys.items():
	# print(key)
	# print(bitting)
	if pinsAreAvailable(bitting):
		print("Found pins for: " + key)
		count += 1

print(count)

outputBittings = {}

# for i, value in enumerate(keys):
# 	print(i)
# 	print(value)
# 	print(keys[value])
