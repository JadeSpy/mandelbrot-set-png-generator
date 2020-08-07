from PIL import Image
import math
from random import seed
from random import random
from random import randint
#import matplotlib.pyplot as plt
import colorsys
import matplotlib.colors as mcolors
scale = 2
offsetX = 0
offsetY = 0
size = 305
#img = Image.open("logo.png")
img = Image.new('RGBA', (size,size), (100, 100, 100, 0))
workWithImage = img.load()

def mandelbrot(can1, can2, areax1, areax2, areay1, areay2):
	nans2 = 0
	nans1 = 0
	canvasSize = [can1, can2]
	area = [areax1, areax2, areay1, areay2]
	zVal = 0
	imageColors = ()
	imageColors += (242, 153, 211)
	imageColors += (242, 203, 5)
	imageColors += (242, 120, 12)
	imageColors += (166, 3, 33)
	testoffset = 0
	#for i in range (0, 1000):
		#imageColors += randint(0,255), randint(0,255), randint(0,255)
		#print()
	for x in range (0, canvasSize[0]):
		print((1-(x/canvasSize[0]))*100, "% more to go.")
		xConverted = (x/(canvasSize[0] / (area[1] - area[0]))) + area [0]
		for y in range (0, canvasSize[1]):
			yConverted = (y/(canvasSize[1] / (area[3] - area[2]))) + area [2]
			zInteration = zVal
			for i in range (0, 200):
				zInteration = (zInteration*zInteration)+complex(xConverted, yConverted)
				if(zInteration.real > 2):
					try:
						workWithImage[x+testoffset,y] = 0,i*2,0,
					except:
						pass
					break
				elif (i == 199):
					try:
						workWithImage[x+testoffset,y] = 255, 255, 255
					except:
						pass

mandelbrot(size, size, (0-scale+offsetX), scale+offsetX, (0-scale)+offsetY, scale+offsetY)
img.show()
img.save("mandalbrot.png")