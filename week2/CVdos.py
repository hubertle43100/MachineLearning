import cv2
import numpy as np

#resize/crop image---------------------------------------------------------------------------------
cimg = cv2.imread("tesla.jpg")
print(cimg.shape)

resize_img = cv2.resize(cimg, (300, 200))   #almost minimize the image to a smaller one
print(resize_img.shape)

crop_img = cimg[0:450, 450:750] #location of cuts(boundaries)

cv2.imshow("tesla.jpg", cimg)
cv2.imshow("Resize - tesla.jpg", resize_img)
cv2.imshow("Cropped - tesla.jpg", crop_img)

cv2.waitKey(0)

#shapes and texts----------------------------------------------------------------------------------
img = np.zeros((512, 512, 3), np.uint8)
#print(img)
#img[:] = 255, 0, 0 #(:) means to color the entire image

cv2.line(img, (0,0),(img.shape[1],img.shape[0]),(0,255,0), 3) #1.starting point 2.ending 3.color 4.thickness
cv2.rectangle(img, (0,0),(250,350),(0,0,255),2,cv2.FILLED)
cv2.circle(img, (400, 50), 30, (255,255,0), 5)
cv2.putText(img, "--OpenCV--",(200, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 1)

cv2.imshow("Blank", img)

cv2.waitKey(0)

#warp perspective----------------------------------------------------------------------------------
j_img = cv2.imread("cards.jpg")

width, height = 250, 350
pts1 = np.float32([[725,160],[440,430],[685,645],[950, 330]])
print(pts1)
pts2 = np.float32([[0,0], [0,height],[width, height],[width,0]])

for x in range (0,4):
    cv2.circle(j_img, (pts1[x][0],pts1[x][1]), 5, (255,0,0),cv2.FILLED)
cv2.imshow("cards.jpg", j_img)

matrix =cv2.getPerspectiveTransform(pts1, pts2)
img_out = cv2.warpPerspective(j_img, matrix,(width,height))

cv2.imshow("Warp - cards.jpg", img_out)

cv2.waitKey(0)
