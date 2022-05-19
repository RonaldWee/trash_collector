import rospy
import cv2
import numpy as np
import sys
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()
imageCopyPath = "/home/westonrobot/catkin_ws/src/test_move/src/images/copy/"
imageName = "test_image"

def image_callback(ros_image):
    global bridge
    #Converting ros image into an opencv-compatible image
    try:
        cv_image = bridge.imgmsg_to_cv2(ros_image,"bgr8")
    except CvBridgeError as e:
        print(e)
    #Use image just like in OpenCV -- image is in the form of matrixs
    print(cv_image)

    #Allocates memory and creates the window
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    #Show the image on the created window with name "Image"
    cv2.imshow("Image", cv_image)
    #Wait for user input on keyboard
    cv2.waitKey(0)
    #Write image to specified file location
    cv2.imwrite(imageCopyPath + imageName + ".jpg", cv_image)
    #Deallocate memory and closes the windows
    cv2.destroyAllWindows()


def main(args):
    #Defining the node
    rospy.init_node('image_converter', anonymous=True)
    #Defining the topic
    Image_topic = "/usb_cam/image_raw"
    #Subscribing to the topic
    image_sub = rospy.Subscriber(Image_topic, Image, image_callback)
    #Keeps the main function running
    try:
        rospy.spin()
    except KeyboardInterrupt:
        #Shutting down
        cv2.destroyAllWindows()
if __name__ == '__main__':
    main(sys.argv)
