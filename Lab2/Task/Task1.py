import cv2
import numpy as np

I = cv2.imread('Lake.jpg') 

B = np.zeros_like(I)  
G = np.zeros_like(I)
R = np.zeros_like(I)

B[:, :, 0] = I[:, :, 0]  
G[:, :, 1] = I[:, :, 1]  
R[:, :, 2] = I[:, :, 2]  

cv2.namedWindow('RGB Lake', cv2.WINDOW_NORMAL)
cv2.imshow('RGB Lake', I)

while True:
    k = cv2.waitKey(0) 

    if k == ord('o'):  
        cv2.imshow('RGB Lake', I)
    elif k == ord('b'):  
        cv2.imshow('RGB Lake', B)
    elif k == ord('g'):  
        cv2.imshow('RGB Lake', G)
    elif k == ord('r'):  
        cv2.imshow('RGB Lake', R)
    elif k == ord('q'):  
        cv2.destroyAllWindows()
        break
