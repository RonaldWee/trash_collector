import numpy as np
import cv2

print("Import successful")

imageCopyPath = "/home/westonrobot/catkin_ws/src/test_move/src/images/copy/"
imagePath = "/home/westonrobot/catkin_ws/src/test_move/src/images/"
imageName = "plastic_bottle"

#Read image file
img = cv2.imread(imagePath + imageName + ".jpg", cv2.IMREAD_COLOR)

#Create window for an image
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.moveWindow("Image", 0, 0)

#Draw a rectangle on the image:
img1 = cv2.rectangle(img, (10,50), (325,350), (0,0,0),10)
#Show/Display image on the window
cv2.imshow("Image", img1)

#Numpy array type
print(type(img))
print(img.size)

#Height (row), Width (columns), Channels (3 -- 1 for red, 1 for green, 1 for blue if using RGB format, have grayscale/HSV as well)
print(img.shape) 

#######------Image Encoding------------############

#Splitting image into blue, green and red parts:
blue, green, red = cv2.split(img)
#Show the 3 parts individually
cv2.namedWindow("Blue", cv2.WINDOW_NORMAL)
cv2.imshow("Blue", blue)
cv2.namedWindow("Green", cv2.WINDOW_NORMAL)
cv2.imshow("Green", green)
cv2.namedWindow("Red", cv2.WINDOW_NORMAL)
cv2.imshow("Red", red)

#Convert to hsv format:
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

#(Optional) Fit all the images on 1 window by concatenating them tgt
hsv_image = np.concatenate((h, s, v), axis=1)
cv2.namedWindow("HSV Image", cv2.WINDOW_NORMAL)
cv2.imshow("HSV Image", hsv_image)

#Convert to grayscale format:
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Gray Image", cv2.WINDOW_NORMAL)
cv2.imshow("Gray Image", gray_img)

#Displays window for a given amt of time (0 means until user input)
cv2.waitKey(0)

#Copy image to another folder:
cv2.imwrite(imageCopyPath + imageName + ".jpg", img)

cv2.destroyAllWindows()