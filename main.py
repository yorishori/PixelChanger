from PIL import Image

white = 240
delta = 5

def neighborIsSame(i:int, j:int, img:Image, size:int=1) -> bool:
	width, height = img.size
	wmin = i-size if (i-size)>=0 else 0
	wmax = i+size if (i+size)<=width else width
	hmin = j-size if (j-size)>=0 else 0
	hmax = j+size if (j+size)<=height else height

	for w in range(wmin, wmax):
		for h in range(hmin,hmax):
			r,g,b,a = img.getpixel((w,h))
			if(r<white and g<white and b<white):
				return False
	return True
	 



img = Image.open("interlude_15.png")
imgc = img.copy()

pixel_map = imgc.load()

width, height = imgc.size

for i in range(width):
	for j in range(height):
		r,g,b,a = img.getpixel((i,j))
		if(r>=white and g>=white and b>=white and neighborIsSame(i,j,img,delta)):
			pixel_map[i,j] = (64, 43, 69)
		
imgc.save("dark.png", format="png")

imgc = Image.open("dark.png")
imgc.show()