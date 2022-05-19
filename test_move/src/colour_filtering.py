import rospy
import numpy as np
import cv2
import imutils

#To add in more pictures of garbage:
imageCopyPath = "/home/westonrobot/catkin_ws/src/test_move/src/images/copy/"
imagePath = "/home/westonrobot/catkin_ws/src/test_move/src/images/"
imageName = "plastic_bottle"

#Read image file:
img = cv2.imread(imagePath + imageName + ".jpg", cv2.IMREAD_COLOR)

#Create window for an image:
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.moveWindow("Image", 0, 0)

#Convert to hsv format:
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Find upper/lower bounds of blue colour (plastic bottle):
blueLower = (90, 80, 10)
blueUpper = (110, 255, 255)

#Define mask
mask = cv2.inRange(hsv, blueLower, blueUpper)

cv2.imshow("mask image", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()