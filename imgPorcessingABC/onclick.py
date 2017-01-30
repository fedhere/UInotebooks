import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd


img = nd.imread("sol_2.png")
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(img)

coords = [0,0]

def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print 'x = %d, y = %d'%(
        ix, iy)


    coords = [ix, iy]
    print (ix,iy)
    print ("flux:", img[int(iy),int(ix),:])
    return coords


for i in xrange(0,1):

    cid = fig.canvas.mpl_connect('button_press_event', onclick)


plt.show()
