# Resize some photos and save back to camera roll

import photos
import clipboard
import Image
import console

x = 0

# Here is where you set the amount of original size 
# that you'd like the final images to be, e.g. 100
# would be original size (and would break the script)
# and 25 would result in images 1/4 original size.
# Default values turn a screenshot on the stated device
# into an image *** pixels wide. 
riPhonePercent = 40
nriPhonePercent = 60
riPadPercent = 30
nriPadPercent = 50

if riPhonePercent >= 100 or nriPhonePercent >= 100 or riPadPercent >= 100 or nriPadPercent >= 100 :
	print ''

# Be careful if you change these strings, as
# the first 2 characters are used in setting resizeAmount.
riPhone = '{0}% (from  retina iPhone)'.format(riPhonePercent)
nriPhone = '{0}% (from  non-retina iPhone)'.format(nriPhonePercent)
riPad = '{0}% (from retina iPad)'.format(riPadPercent)
nriPad = '{0}% (from non-retina iPad)'.format(nriPadPercent)

# This takes a max of 5 arguments including the title and message, 
# so you can really only put in 2 devices and 'Custom'. Set the two
# you want here.
q1 = riPhone
q2 = nriPad

resizeAmountQ = console.alert('What percent of original size?','',q1,q2,'Custom')
if resizeAmountQ == 1 :
	resizeAmount = float(q1[0:2]) / 100
elif resizeAmountQ == 2 :
	resizeAmount = float(q2[0:2]) / 100 
elif resizeAmountQ == 3 :
	resizeAmount = float(console.input_alert('What percent of original size?','Number only','40')) / 100
else:
	print 'Whups!'
	exit
	
while True:
	img = clipboard.get_image(idx=x)

	if img:
		width, height = img.size

		smaller = img.resize( (int(width * resizeAmount), int(height * resizeAmount) ), Image.ANTIALIAS)
		photos.save_image(smaller)
		
		x += 1
		
	elif x == 0 :
		print 'No images found on the clipboard.'

	else:
		print 'Looks like it worked. The downsampled images should be in your camera roll.'
		break 

