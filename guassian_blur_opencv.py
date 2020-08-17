import cv2
import numpy
# load img
img=cv2.imread('Lenna.png',-1)

# apply gaussian blur on src img
dst=cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)

# display input and output img
cv2.imshow("Gaussian Blurring", numpy.hstack((img,dst)))
cv2.waitKey(0) # wait until a key is pressed
cv2.destroyAllWindows() # destroys the window
        
