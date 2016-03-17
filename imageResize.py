#python function for resizeing any image

def imageResize(input,size,output):
	import Image
	im = Image.open(input)
	im.thumbnail(size,Image.ANTIALIAS)
	im.save(output,"JPEG")

