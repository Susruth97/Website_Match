from PIL import Image
import cv2
import numpy as np
import math
from PIL import ImageChops

def rmsdiff(im1, im2):
    "Calculate the root-mean-square difference between two images"
    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()
    sq = (value * ((idx % 256) ** 2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares / float(im1.size[0] * im1.size[1]))
    return rms


img1 = Image.open("src1/img_1.png")
img2 = Image.open("src2/img_1.png")

percentage = rmsdiff(img1, img2)
print (percentage)
