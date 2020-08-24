import cv2
import numpy as np
img = cv2.imread("portrait.jpg")

def rescale(scale, imgA):
    rows = len(imgA)
    cols = len(imgA[0])
    rows_num = isinstance(imgA[0], list)
    width = imgA[0][0].shape[1]
    height = imgA[0][0].shape[0]
    if rows_num:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgA[x][y].shape[:2] == imgA[0][0].shape[:2]:
                    imgA[x][y] = cv2.resize(imgA[x][y], (0, 0), None, scale, scale)
                else:
                    imgA[x][y] = cv2.resize(imgA[x][y], (imgA[0][0].shape[1], imgA[0][0].shape[0]), None, scale, scale)
                if len(imgA[x][y].shape) == 2: imgA[x][y]= cv2.cvtColor( imgA[x][y], cv2.COLOR_GRAY2BGR)
        Blank = np.zeros((height, width, 3), np.uint8)
        hor = [Blank]*rows
        hor_con = [Blank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgA[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgA[x].shape[:2] == imgA[0].shape[:2]:
                imgA[x] = cv2.resize(imgA[x], (0, 0), None, scale, scale)
            else:
                imgA[x] = cv2.resize(imgA[x], (imgA[0].shape[1], imgA[0].shape[0]), None,scale, scale)
            if len(imgA[x].shape) == 2: imgA[x] = cv2.cvtColor(imgA[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgA)
        ver = hor
    return ver

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgStack = rescale(0.5,([img,imgGray,img],[imgGray,img,imgGray]))

hor = np.hstack((img, img))
ver = np.vstack((img, img))

cv2.imshow("Horizontal", hor)
cv2.imshow("Vertical", ver)
cv2.imshow("Stack",imgStack)

cv2.waitKey(0)


#def empty(a):
#    pass

#def stackImages(scale,imgArray):
#    rows = len(imgArray)
#    cols = len(imgArray[0])
#    rowsAvailable = isinstance(imgArray[0], list)
#    width = imgArray[0][0].shape[1]
#    height = imgArray[0][0].shape[0]
#    if rowsAvailable:
#        for x in range ( 0, rows):
#            for y in range(0, cols):
#                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
#                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                else:
#                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
#                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
#        imageBlank = np.zeros((height, width, 3), np.uint8)
#        hor = [imageBlank]*rows
#        hor_con = [imageBlank]*rows
#        for x in range(0, rows):
#            hor[x] = np.hstack(imgArray[x])
#        ver = np.vstack(hor)
#    else:
#        for x in range(0, rows):
#            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#            else:
#                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
    #        if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
    #    hor= np.hstack(imgArray)
#        ver = hor
#    return ver

#cv2.namedWindow("Trackbars")
#cv2.resizeWindow("TrackBars", 640, 240)
#cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
#cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)
#cv2.createTrackbar("Sat Min","TrackBars",110,255,empty)
#cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)
#cv2.createTrackbar("Val Min","TrackBars",153,255,empty)
#cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

#while True:
    #simg = cv2.imread("scar.jpg")
    #simgHSV = cv2.cvtColor(simg,cv2.COLOR_BGR2HSV)
    #h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    #h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    #s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    #s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    #v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    #v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    #lower = np.array([h_min,s_min, v_min])
    #upper = np.array([h_max, s_max, v_max])
    #mask = cv2.inRange(simgHSV, lower, upper)

#cv2.imshow("Basic", simg)
#cv2.imshow("HSV", simg_HSV)
#cv2.imshow("Mask", mask)
#cv2.waitKey(0)
