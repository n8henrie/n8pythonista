# Taken from Viticci :: https://github.com/viticci/pythonista-scripts
#covert an image in the clipboard to an rgb icon and store base64 version of it into the clipboard.
#if an image is not in the clipboard the base64 string 'b64str' will be loaded and displayed.
#after running the 1st time replace the contents of b64str with the clipboard.

from PIL import Image
import clipboard
from StringIO import *
import base64
import console

global iconSize
device = console.alert('What device is this for?','','iPhone / iPod Touch','iPad')
retina = console.alert('Retina or non-retina?','','Retina','Non-retina')
if device == 1 and retina == 1:
	iconSize = 114
if device == 1 and retina == 2:
	iconSize = 57
if device == 2 and retina == 1:
	iconSize = 144
if device == 2 and retina == 2:
	iconSize = 72

b64str="""
replace this with contents of clipboard after 1st run.
"""

def main():
	global b64str
	cpimage = clipboard.get_image()
	#if image was in clipboard.
	if cpimage:
		#resize to icon size.
		icon = cpimage.resize((iconSize, iconSize), Image.ANTIALIAS)
		#convert to rgb format.
		icon = icon.convert('RGB')
#		icon.show()	#show resized image.
		#create string buffer to write png file to.
		iconstr = StringIO()
		#write image to string buffer in png format.
		icon.save(iconstr, 'png')
		#convert save buffer to base64.
		b64str = base64.standard_b64encode(iconstr.getvalue())
		#put base64 string in clipboard.
		clipboard.set(b64str)
	
	#now decode to test.	
	mystr = base64.standard_b64decode(b64str)
	#read file from string buffer.
	stb = StringIO(mystr)
	img = Image.open(stb)
	#show the image.
	img.show()
	#print some info.
	print str(img.format)
	print str(img.mode)
	print str(img.size)
	print str(img.info)
	
if __name__ == '__main__':
	main()
