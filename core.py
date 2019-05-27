import numpy as np
import matplotlib.pyplot as plt
nt = 0
nl = 0
nc = 0

imgQtd = 0
baseImgFlag = False 
icons = []
fotoMosaico = []

def readpgm (name):
    f = open(name,"r")

    assert f.readline() == 'P2\n'
    line = f.readline()
    while (line[0] == '#'):
           line = f.readline()
    (width, height) = [int(i) for i in line.split()]
    print (width, height)
    depth = int(f.readline())
    assert depth <= 255
    print (depth)
    
    img = []
    row = []
    j = 0
    for line in f:
       values = line.split()
       for val in values:
           row.append (int (val))
           j = j + 1
           if j >= width:
              img.append (row)
              j=0
              row = []

    f.close()
    return img

def imgalloc (nl, nc):
    img = []
    for i in range(nl):
        lin = []
        for j in range(nc):
            lin.append(0)
        img.append(lin)
    return img

def convertToIcon(img):
    finalImg = []
    for x in range(0,nl):
        line = []
        for y in range(0,nc):
            #
            count = 0
            summ = 0
            for i in range(0,9):
                for j in range(0,9):
                    summ += img[(x*10)+i][(y*10)+j]
                    count += 1
            summ /= count
            line.append(int(summ))
        finalImg.append(line)
    return finalImg

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
            icons.append(convertToIcon(readpgm(line.split("\n")[0])))
        i += 1



baseImg = icons[0]
#
print (np.asarray (baseImg))
print ((baseImg[1][2]))
print ((baseImg[1][1]))
print ((baseImg[1][0]))
print ((baseImg[0][0]))

#plt.imshow(baseImg, cmap='gray')
#plt.show()
#
##im1 = numpy.array([[0, 1], [65534, 65535]], dtype='uint16')
##imsave('_tmp.pgm', im1)

#while (x+1) < (nl):
#    line = []
#    y = 1
#    while (y+1) < (nc):
#
#        count = 9
#        summ = 0
#        summ += baseImg[int(x-1)][int(y-1)]
#        summ += baseImg[int(x-1)][int(y)]
#        summ += baseImg[int(x-1)][int(y+1)]
#        summ += baseImg[int(x)][int(y-1)]
#        summ += baseImg[int(x)][int(y)]
#        summ += baseImg[int(x)][int(y+1)]
#        summ += baseImg[int(x+1)][int(y-1)]
#        summ += baseImg[int(x+1)][int(y)]
#        summ += baseImg[int(x+1)][int(y+1)]
#
#        summ /= count
#        print (int(y))
#        #anything
#        line.append(int(summ))
#        y += 1
#    fotoMosaico.append(line)
#    x += 1

plt.imshow(baseImg, cmap='gray')
plt.show()
##print (len(fotoMosaico))
#
#fotoMosaicoPbm = numpy.array(fotoMosaico, dtype='uint16')
#print (fotoMosaicoPbm.shape)
#imsave('fotoMosaico.pgm', fotoMosaicoPbm)