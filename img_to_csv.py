from PIL import Image
import csv

file_name = 'met 2 scan 45 wf'
im = Image.open(file_name + '.png')
im = im.crop((420, 512, 1615, 1019))  			# to see only the spectrum
im = im.transpose(Image.FLIP_TOP_BOTTOM)		# flipped verticaly because x=0 is in the top, not bottom
#im.save(file_name + '_cropped' + '.png')		# saves the cropped image

im.show()
w = im.size[0]
h = im.size[1]
pix = im.load()

with open(file_name + ".csv", 'w', newline = '') as f:	# opens the empty csv file where we will put the spectrum values
# check all pixels in image and if it is on our spectrum, we write x, y of that point to csv.
	for i in range(6, w-1):						# from 6 because we need to exclude some points that we don't need
		for j in range(0, h-5):					
			if pix[i, j][0] == 255:				# pix[i, j] gives RGBA values, and we need to check only the first one
				writer = csv.writer(f)
				writer.writerows([[i, j]])

f.close()
