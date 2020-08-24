import cv2
import numpy as np

#simple image display------------------------------------------------------------------------------
img = cv2.imread('rock.jpg')
cv2.imshow("Rock.jpg", img)
cv2.waitKey(0)

#video display
cap = cv2.VideoCapture("Lego.mp4")

while True:
    success, img_v = cap.read()
    cv2.imshow("Video", img_v)
    if(cv2.waitKey(50) & 0xFF == ord('q')): #error if 'q' is not pressed
        break
cv2.destroyAllWindows()

#webcam display(don't have)------------------------------------------------------------------------
#cap = cv2.VideoCapture(0)   #change 0 --> 1 if there is more than one webcam
#cap.set(3, 640)
#cap.set(4, 480)
#cap.set(10, 100)    #change brightness

#while True:
    #success, img_w = cap.read()
    #cv2.imshow("Video", img_w)
    #if(cv2.waitKey(1) == ord('q')):
        #break

#many image(rock)----------------------------------------------------------------------------------
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(7, 7), 0) #odd nums only (7,7) <-- blur intensity
img_canny = cv2.Canny(img, 600, 700)    #increasing (600, 700) will get a clearer image

kernel = np.ones((5,5), np.uint8)   #create 5 x 5 matrix (color range 0 - 255)
img_dialation = cv2.dilate(img_canny, kernel, iterations = 1)   #iteration == thickness in line
img_eroded =cv2.erode(img_dialation, kernel, iterations = 1)

cv2.imshow("Gray - Rock.jpg", img_gray)
cv2.imshow("Blur - Rock.jpg", img_blur)
cv2.imshow("Canny - Rock.jpg", img_canny)
cv2.imshow("Dialation - Rock.jpg", img_dialation)
cv2.imshow("Eroded - Rock.jpg", img_eroded)
cv2.waitKey(0)
