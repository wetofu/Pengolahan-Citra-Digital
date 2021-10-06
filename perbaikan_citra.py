from PIL import Image


# nama_file = "paru.jpeg"
nama_file = "einstein.jpg"
# nama_file = "sinichi.jpg"
ein = Image.open(nama_file)
ein = ein.convert('L')
d_ein = ein.load()

size = width, height = ein.size


def low_pass():
	gb = Image.new('L',(width,height))
	dgb = gb.load()
	for x in range(1,width-1):
		for y in range(1,height-1):
			r = d_ein[x-1,y-1] \
				+ d_ein[x,y-1] \
				+ d_ein[x+1,y-1] \
				+ d_ein[x-1,y] \
				+ d_ein[x,y] \
				+ d_ein[x+1,y] \
				+ d_ein[x-1,y+1] \
				+ d_ein[x,y+1] \
				+ d_ein[x+1,y+1]
			r = int(r/9)
			dgb[x,y] = r
	gb.show()
	# gb.save("einstein_low_pass.jpg")

def median():
	gb = Image.new('L',(width,height))
	dgb = gb.load()
	for x in range(1,width-1):
		for y in range(1,height-1):
			r = []
			r.append(d_ein[x-1,y-1])
			r.append(d_ein[x,y-1])
			r.append(d_ein[x+1,y-1])
			r.append(d_ein[x-1,y])
			r.append(d_ein[x,y])
			r.append(d_ein[x+1,y])
			r.append(d_ein[x-1,y+1])
			r.append(d_ein[x,y+1])
			r.append(d_ein[x+1,y+1])
			r.sort()
			dgb[x,y] = r[4]
	gb.show()
	# gb.save("einstein_median.jpg")

# make_rgb()
low_pass()
# median()


