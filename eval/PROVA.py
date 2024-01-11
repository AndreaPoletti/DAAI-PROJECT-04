from PIL import Image
import numpy as np


im = Image.open("..\Testing_Images/RoadAnomaly/labels_masks/0.png")

print(im.format)
print(im.size)
print(im.mode)

im_arr = (np.asarray(im))

inDom = np.count_nonzero(im_arr == 0)
ooDom = np.count_nonzero(im_arr == 1)

print("OOD pixels / Total Pixels = " + str(ooDom/(ooDom+inDom)))

im_arr = im_arr*100
Image.fromarray(im_arr).show()
