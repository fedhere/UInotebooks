from __future__ import print_function
__author__ = 'fbb 2017'
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
import sys

''' pass it an image and on click it returns the pixel location and flux values in all image channels at that location '''

if not len(sys.argv) == 2:
    print ('''use as 
python onclick.py <image file name>''')
    sys.exit()
    
img = nd.imread(sys.argv[1])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(img)

ix, iy = 0, 0
def onclick(event):
    ix, iy = event.xdata, event.ydata
    print ('x = %d, y = %d'%(ix, iy))
    print ("flux:", img[int(iy),int(ix),:])


for i in xrange(0,1):
    cid = fig.canvas.mpl_connect('button_press_event', onclick)


plt.show()
