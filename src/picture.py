import numpy as np
import cv2
import copy

try:
    # To read an image. The second argument if 0 makes the image Grayscale,
    # not passing anything keeps it colored
    img = cv2.imread('../Pictures/sample1.jpeg')
    # This creates a window where the image is later on displayed
    cv2.namedWindow('imagedisplay', cv2.WINDOW_NORMAL)
    cv2.imshow('imagedisplay', img)
    #Wait for a Key Stroke before moving forward
    cv2.waitKey(0)
    #Destroy existing display windows
    cv2.destroyAllWindows()
    # Save the image to a new file
    cv2.imwrite('../Pictures/sample1.png', img)
    # Show Image properties
    # a) Image Size
    print("Image size is : " + str(img.size))
    # b) Image shape (Row, Col, Col/Gray)
    print("Image shape is :" + str(img.shape))
    # c) Image Data Type
    print("Image is encoded in:" + str(img.dtype))

    # Modify a part of the pic
    # NOTE: the first part is the Rows(Y-Axis)
    # Second is the Column (X-Axis)
    test = img[70:132, 90:160]
    cv2.imwrite('../Pictures/sample1b.png', test)

    # NOTE: BELOW CODE DOESNT WORK WITH GRAYSCALE
    # Split image to 3 primary colors
    blue_img = img[:,:,0]
    green_img = img[:,:,1]
    red_img = img[:,:,2]
    #Saving Blue + Green part of the Image. Note, copy is required
    # to deepcopy the data, else img1 = img will just work as a reference
    img1 = copy.deepcopy(img)
    img1[:,:,2] = 0
    #You can also use b,g,r = cv2.split(img)
    #Split breaks the Array into each row with one color value and then 
    # you can use cv2.merge((b,g,r)) . But the above syntax is easier
    # operation wise and supported by Numpy :)
    cv2.imwrite('../Pictures/sample1c.png', img1)

    #Performing Arithmetic operations on images
    # This works because the shape and depth of both the images
    # is same.For addition, you can use cv2.add(). This function gives
    # better results sometimes when compared to img + img1
    cv2.imwrite('../Pictures/sample1d.png', img - img1)

    # Blending 2 images together
    img2 = cv2.imread('../Pictures/sample1d.png')
    cv2.imwrite('../Pictures/sample1e.png', cv2.addWeighted(img, 0.5,img2, 0.5, 0))
    #addWeighted adds 2 images in the following way:
    # result = x*img1 + (1-x)*img2 + c, where x is the weight of each image and c
    # is the constant( 0 above )

except Exception as e:
    print("Oops something went wrong: " + str(e))


