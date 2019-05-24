from netpbmfile import imread

nt = 0
nl = 0
nc = 0

imgQtd = 0

imgNames = []

with open("config.txt") as file:
	i = 0
	for line in file:
		print (line)
		if i == 0:
			nt = int(line.split(" ")[0])
			nl = int(line.split(" ")[1])
			nc = int(line.split(" ")[2])
		elif i == 1:
			imgQtd = int(line)
		elif i > 1:
			imgNames.append(line.split("\n")[0])
		i += 1

baseImg = imread(imgNames[0])

#print (baseImg)
#print ((baseImg[1][2]))
#print ((baseImg[1][1]))
#print ((baseImg[1][0]))
#print ((baseImg[0][0]))

for x in range(0,nl-1):
	for y in range(0,nc-1):
		print (baseImg[x][y])