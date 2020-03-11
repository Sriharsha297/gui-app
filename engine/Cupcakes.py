import cv2
import numpy as np
from tkinter import *
import operator
import time
import os
import sys

argv = sys.argv


def findTime(pc):
    if(pc >= 90 and pc < 100 ):
        print('Green Light for 90 Seconds')
    elif(pc >= 85 and pc < 90 ):
        print('Green Light for 60 Seconds')

    elif(pc >= 79 and pc < 85 ):
        print('Green Light for 40 Seconds')
    elif(pc >= 55 and pc < 79 ):
        print('Green Light for 20 Seconds')
    else:
        print('No Green Light')

# refernce image



reference = cv2.resize(cv2.imread((argv[1])),(512,512))
gray_refernce = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
ref = cv2.Canny(gray_refernce,200,200)


img_1 = cv2.resize(cv2.imread(argv[2]), (512, 512))
img_2 = cv2.resize(cv2.imread(argv[3]), (512, 512))
img_3 = cv2.resize(cv2.imread(argv[4]), (512, 512))
img_4 = cv2.resize(cv2.imread(argv[5]), (512, 512))


# RGB to Gray Conversion
gray_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
gray_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
gray_3 = cv2.cvtColor(img_3, cv2.COLOR_BGR2GRAY)
gray_4 = cv2.cvtColor(img_4, cv2.COLOR_BGR2GRAY)



# Finding Edges with Canny Edge Detector
lane_1 = cv2.Canny(gray_1,200,200)
lane_2 = cv2.Canny(gray_2,200,200)
lane_3 = cv2.Canny(gray_3,200,200)
lane_4 = cv2.Canny(gray_4,200,200)


sift = cv2.xfeatures2d.SIFT_create()
kp, desc = sift.detectAndCompute(ref, None)
kp_1, desc_1 = sift.detectAndCompute(lane_1, None)
kp_2, desc_2 = sift.detectAndCompute(lane_2, None)
kp_3, desc_3 = sift.detectAndCompute(lane_3, None)
kp_4, desc_4 = sift.detectAndCompute(lane_4, None)



L = {}

L['Lane 1'] = len(kp_1)
L['Lane 2'] = len(kp_2)
L['Lane 3'] = len(kp_3)
L['Lane 4'] = len(kp_4)

L = sorted(L.items(), key=operator.itemgetter(1),reverse=True)


order = ""
i=True
for key, value in L:
    if i:
        order = key
    else:
        order = order +" -> "+key
    i = FALSE

print(order)

print("Finding Time Allocation for each Lane")




pcLane1 = int( ( ( len(kp_1) - len(kp) ) / len(kp_1) )*100)

pcLane2 = int( ( ( len(kp_2) - len(kp) ) / len(kp_2) ) * 100)

pcLane3 = int( ( ( len(kp_3) - len(kp) ) / len(kp_3) ) * 100)

pcLane4 = int( ( ( len(kp_4) - len(kp) ) / len(kp_4) ) * 100)



print("Lane 1")
findTime(pcLane1)
print("Lane 2")
findTime(pcLane2)
print("Lane 3")
findTime(pcLane3)
print("Lane 4")
findTime(pcLane4)


sys.stdout.flush()