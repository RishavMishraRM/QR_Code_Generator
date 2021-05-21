#import the module
import pyqrcode

#define the data
data = 'github.com'

#create qrcode
img = pyqrcode.create(data)

#save the qrcode in png format with proper scaling
img.png('blogwebsite.png', scale= 10)