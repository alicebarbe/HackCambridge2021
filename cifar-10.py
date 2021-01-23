
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
#from keras.datasets import cifar10
import argparse
import cvlib as cv
from cvlib.object_detection import draw_bbox
import os

def saving_image(image, output, image_name):
    #save your image to output path using opencv
    path = output
    im_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(os.path.join(path, image_name), im_bgr)
    cv2.waitKey(0)

# Read, Detect, Write and Repeat
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help = 'Use -i flag with path to image as argument')
ap.add_argument('-s', '--save', required=True, help = 'Use -s flag with path to output as argument')
args = vars(ap.parse_args())

# Loading an image from Cambridge, with wildlife
image = cv2.imread(args["image"]) #B G R
output = args["save"]
cv2.imshow('Input Image', image)

#you must press to continue
cv2.waitKey(0)

# manipulate the image
bbox, label, conf = cv.detect_common_objects(image) 
output_image = draw_bbox(image, bbox, label, conf)

# saving_image(output_image, output, "detection.jpg")
plt.imshow(np.flip(output_image, axis=2))
plt.show()

