from PIL import Image
from random import randint
import numpy as np

WIDTH, HEIGHT = 400, 400
n = 0
points = []
nPoints = 50
points = [np.array([randint(0,WIDTH),randint(0,HEIGHT)]) for i in range(nPoints)]

img = Image.new('RGB',(WIDTH,HEIGHT))

pixels = img.load()

for x in range(WIDTH):
	for y in range(HEIGHT):
		d = np.zeros(len(points))
		for i,point in enumerate(points):
			d[i] = ((point[0]-x)**2+(point[1]-y)**2)**0.5
		d.sort()
		c = int(d[n])
		pixels[x,y] = (c,c,c)

img.show()
img.save('Example.jpg','JPEG')