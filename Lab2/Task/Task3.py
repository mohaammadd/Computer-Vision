import cv2
import numpy as np

I = cv2.imread('damavand.jpg') 
I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
I_gray_3ch = cv2.cvtColor(I_gray, cv2.COLOR_GRAY2BGR)

num_frames = 500

cv2.namedWindow("Grayscale to Color", cv2.WINDOW_NORMAL)

for i in range(num_frames + 1):
    alpha = 1 - (i / num_frames)
    beta = 1 - alpha  
    K = cv2.addWeighted(I_gray_3ch, alpha, I, beta, 0)

    cv2.imshow("Grayscale to Color", K)

    cv2.waitKey(50)

cv2.waitKey(2000)
cv2.destroyAllWindows()
