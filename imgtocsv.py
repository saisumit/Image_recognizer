from PIL import Image
import numpy as np
import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot
import matplotlib.animation

import matplotlib.pyplot as plt
import matplotlib.cm as cm


im = Image.open('../AI-project/two.jpg')
#pixels = list(im.getdata())
# width, height = im.size 
# pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
pixels = np.asarray(im)
pixels = pixels.ravel()
pixels = pixels.transpose() 
pixels = np.multiply(pixels, 1 / 255 )
pixels = pixels.astype(np.int)
np.savetxt("pixel_data_two.csv", pixels, delimiter=",") 
