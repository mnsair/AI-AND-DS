import cv2 as cv
import numpy as np

# read webcam using opencv in grayscale
cap = cv.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False
while ret:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2HLS)
    cv.imshow('webcam', gray)
    if cv.waitKey(25) & 0xFF == ord('q'):
        break
        
cap.release()
cv.destroyAllWindows()