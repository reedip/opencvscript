import numpy as np
import cv2

try:
    # To read an image
    img = cv2.imread('../Pictures/sample1.jpeg', 0)
    # This creates a window where the image is later on displayed
    cv2.namedWindow('imagedisplay', cv2.WINDOW_NORMAL)
    cv2.imshow('imagedisplay', img)
    #Wait for a Key Stroke before moving forward
    cv2.waitKey(0)
    #Destroy existing display windows
    cv2.destroyAllWindows()
    # Save the image to a new file
    cv2.imwrite('../Pictures/sample1.png', img)
except Exception:
    print("Oops something went wrong")
