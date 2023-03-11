
import cv2
import os
import numpy as np
import functools

abc = 0
tholdzz = 127

def ROI(path):

    grayy=cv2.imread(path,0)

    ret,thresh = cv2.threshold(grayy,tholdzz,255,0)
    ret,thresh = cv2.threshold(grayy,tholdzz,255,0)
    M = cv2.moments(thresh)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    tempimg = grayy[cX-160:cX+160,cY-160:cY+160]
    return tempimg
