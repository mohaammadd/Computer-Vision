# Task 2
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("masoleh_gray.jpg", cv2.IMREAD_GRAYSCALE)
inverted_image = image[::-1]
new_image = np.vstack((image, inverted_image))

plt.imshow(new_image, cmap='gray')
plt.axis('off')
plt.show()