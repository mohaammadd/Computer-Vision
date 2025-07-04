import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "/home/mohammad/Desktop/CV_Lab3/cv-lab3/inversion.png"  # Replace with your image file path
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


# Invert the image
inverted_image = 255 - original_image

# Display the original and inverted images side by side
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Inverted Image
plt.subplot(1, 2, 2)
plt.imshow(inverted_image, cmap='gray')
plt.title('Inverted Image')
plt.axis('off')

plt.show()