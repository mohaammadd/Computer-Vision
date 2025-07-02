import cv2
import numpy as np

I = cv2.imread('damavand.jpg')
J = cv2.imread('eram.jpg')

num_frames = 500

cv2.namedWindow("Transition", cv2.WINDOW_NORMAL)

for i in range(num_frames + 1):
    alpha = 1 - (i / num_frames)  
    beta = 1 - alpha  

    K = cv2.addWeighted(I, alpha, J, beta, 0)
    cv2.imshow("Transition", K)
    cv2.waitKey(50) 
cv2.waitKey(2000)  
cv2.destroyAllWindows()
