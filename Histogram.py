# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:07:03 2021

@author: Dipti
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def count_elements(seq):
    hist = np.zeros((256))
    for i in seq:
        hist[i] = hist[i] + 1
    return hist

image = Image.open("pic.jpg")
print(image.format)
print(image.size)
print(image.mode)

np_img = np.array(image)
print(np_img.shape)
result = np_img.flatten()
print(result)
print(result.shape)

counted = count_elements(result)
plt.plot(counted)