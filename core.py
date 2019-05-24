from netpbmfile import imread, imsave
import numpy
nt = 0
nl = 0
nc = 0

imgQtd = 0

imgArr = []
fotoMosaico = []

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
			imgArr.append(imread(line.split("\n")[0]))
		i += 1

nl = nl *10
nc = nc *10
baseImg = imgArr[0]

#print (baseImg)
#print ((baseImg[1][2]))
#print ((baseImg[1][1]))
#print ((baseImg[1][0]))
#print ((baseImg[0][0]))

#im1 = numpy.array([[0, 1], [65534, 65535]], dtype='uint16')
#imsave('_tmp.pgm', im1)
for x in range(0,nl*nl):
	line = []
	for y in range(0,nc*nc):
		line.append(baseImg[int(x/nl)][int(y/nc)])
	fotoMosaico.append(line)
#print (len(fotoMosaico))
fotoMosaicoPbm = numpy.array(fotoMosaico, dtype='uint16')
imsave('fotoMosaico.pgm', fotoMosaicoPbm)