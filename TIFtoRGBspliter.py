# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
from astropy.io import fits
#Set up matplotlib and use a nicer set of plot parameters
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
#Load and display the original 3-color jpeg image:
name = input("<Enter filename> ")
image = Image.open(name)
xsize, ysize = image.size
print("Image size: {} x {}".format(xsize, ysize))
plt.imshow(image)
#Split the three channels (RGB) and get the data as Numpy arrays. The arrays are flattened, so they are 1-dimensional
r, g, b = image.split()
r_data = np.array(r.getdata()) # data is now an array of length ysize*xsize
g_data = np.array(g.getdata())
b_data = np.array(b.getdata())
print(r_data.shape)
#Reshape the image arrays to be 2-dimensional
r_data = r_data.reshape(ysize, xsize)
g_data = g_data.reshape(ysize, xsize)
b_data = b_data.reshape(ysize, xsize)
#Write out the channels as separate FITS images
red = fits.PrimaryHDU(data=r_data)
# add spurious header info
Dec = input("<Enter Declination> ")
Ra = input("<Enter Right ascension> ")
red.header['LATOBS'] = Dec
red.header['LONGOBS'] = Ra
red.writeto(name + '_red.fits')
green = fits.PrimaryHDU(data=g_data)
green.header['LATOBS'] = Dec
green.header['LONGOBS'] = Ra
green.writeto(name + '_green.fits')
blue = fits.PrimaryHDU(data=b_data)
blue.header['LATOBS'] = Dec
blue.header['LONGOBS'] = Ra
blue.writeto(name + '_blue.fits')