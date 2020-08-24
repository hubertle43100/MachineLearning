import cv2
import numpy as np
import matplotlib.pyplot as plt

def make_coordinates(img, line_parameters):
    slope, intercept = line_parameters
    y1 = img.shape[0]
    y2 = int(y1 * (3/5))    #cuts line going from the bottom of the image and 3/5 up
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return np.array([x1, y1, x2, y2])

def avg_slope_intercept(img, HoughLinesP):
    left_fit = []   #stores slope & intercept of left line
    right_fit = []  #^similar but right side
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)  #creates a 1 by 2 array containing slope and intercept
        slope = parameters[0]
        intercept = parameters[1]
        if(slope < 0):
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    left_avg = np.average(left_fit, axis = 0)   #sums slope and intercept into one average value
    right_avg = np.average(right_fit, axis = 0)
    left_line = make_coordinates(img, left_avg)
    right_line = make_coordinates(img, right_avg)
    return np.array([left_line, right_line])

def canny(img):
    gray =cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #change copy img into gray scale
    blur = cv2.GaussianBlur(gray, (5, 5), 0)#reduce noise
    canny = cv2.Canny(blur, 50, 150) #trace edge through intensity diff
    return canny

def display_line(img, lines):
    line_img =np.zeros_like(img)
    if lines is not None:
        for x1, y1, x2, y2 in lines:
            cv2.line(line_img, (x1, y1), (x2, y2), (0, 255, 0), 10)
    return line_img

def region(img):    #outline region we want
    hieght = img.shape[0]
    poly = np.array([[(200, hieght), (1100, hieght), (550, 250)]])
    mask = np.zeros_like(img) #create zero outline
    cv2.fillPoly(mask, poly, 255)
    mask_img = cv2.bitwise_and(img, mask)
    return mask_img

#img = cv2.imread('test_image.jpg')  #reads the image pixel by pixel
#lane_img = np.copy(img)
#canny_img = canny(lane_img)
#cropped_img = region(canny_img)
#lines = cv2. HoughLinesP(cropped_img, 2,  np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5)
#avg = average_slope_intercept(lane_img, lines)
#line_img = display_line(lane_img, avg)
#combine_img = cv2.addWeighted(lane_img, 0.8, line_img, 1, 1) #blend line_img with actual img
#cv2.imshow('road.jpg', combine_img)
#cv2.waitKey(0)  #display the image infinitely until button is pressed

cap = cv2.VideoCapture("test2.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    canny_img = canny(frame)
    cropped_img = region(canny_img)
    lines = cv2. HoughLinesP(cropped_img, 2,  np.pi/180, 100, np.array([]), minLineLength = 40, maxLineGap = 5)
    avg = avg_slope_intercept(frame, lines)
    line_img = display_line(frame, avg)
    combine_img = cv2.addWeighted(frame, 0.8, line_img, 1, 1) #blend line_img with actual img
    cv2.imshow('road.jpg', combine_img)
    if (cv2.waitKey(1) == ord('q')):  #display the image infinitely until button is pressed
        break
cap.release()
cv2.destroyAllWindows()
