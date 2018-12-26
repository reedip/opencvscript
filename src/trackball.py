import numpy
import cv2

IMAGE_SOURCE = '../Pictures/sample2.jpeg'


class Image:

    def __init__(self, src):
        self.img = cv2.imread(src)

    def nothing(self, callback_val):
        # The callback_val is the default value
        # which is the CURRENT TRACKBAR POSITION
        pass

    def show_image(self):
        cv2.namedWindow('image')
        cv2.createTrackbar('R', 'image', 0, 255, self.nothing)
        cv2.createTrackbar('G', 'image', 0, 255, self.nothing)
        cv2.createTrackbar('B', 'image', 0, 255, self.nothing)
        # Trackbar has 5 arguments: Name, Destination Window, Min Val, Max Val
        # and Callback function which will be executed if the TrackBar changes
        # Below is a Button based out of trackbar
        cv2.createTrackbar('On/Off', 'image', 0, 1, self.nothing)
        print(self.img.shape)
        while(1):
            cv2.imshow('image', self.img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            r = cv2.getTrackbarPos('R', 'image')
            g = cv2.getTrackbarPos('G', 'image')
            b = cv2.getTrackbarPos('B', 'image')
            s = cv2.getTrackbarPos('On/Off', 'image')

            if s:
                self.img[:] = 0
            elif b:
                self.img[:,:,0] = b
            elif g:
                self.img[:,:,1] = g
            elif r:
                self.img[:,:,2] = r
                 #Format of Colors in OpenCV

    def close(self): 
        cv2.destroyAllWindows()

img = Image(IMAGE_SOURCE)
img.show_image()
img.close()
