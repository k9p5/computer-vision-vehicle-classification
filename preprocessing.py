#import matplotlib.pyplot as plt
#import numpy as np
#import cv2

#read gray scale image:
#img=cv2.imread("test.png",cv2.IMREAD_GRAYSCALE)
# plot the image and the histogram:
#fig, (ax1, ax2) = plt.subplots(ncols=2)
#ax1.imshow(img, cmap='gray')
#ax1.set_axis_off()
#ax2.hist(img.flatten(), bins=51)
#ax2.set_xlim((0,255))
#ax2.set_xlabel("Grauwert")
#ax2.set_ylabel("Haeufigkeit")
#fig.tight_layout()
#plt.show()
#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

img = plt.imread("flowers.jpg")
plt.imshow(img)

# %%

# %%
