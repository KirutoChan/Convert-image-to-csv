from PIL import Image
import csv

im = Image.open("scan41.png")
im = im.crop((420, 512, 1615, 1019))  			# to see only the spectrum
im = im.transpose(Image.FLIP_TOP_BOTTOM)		# flipped verticaly because x=0 is in the top, not bottom
im.save("scan41_croped.png")					# saves the croppped image

im.show()
w = im.size[0]
h = im.size[1]
pix = im.load()

with open("xy.csv", 'w', newline = '') as f:	# opens the empty csv file where we will put the spectrum values

	for i in range(6, w-1):
		for j in range(0, h-5):
			if pix[i, j][0] == 255:				# pix[i, j] gives RGBA values, and we need to check only the first one
				writer = csv.writer(f)
				writer.writerows([[i, j]])

f.close()
