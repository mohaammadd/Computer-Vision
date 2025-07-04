import cv2
import numpy as np
from matplotlib import pyplot as plt

fname = 'office.jpg'
#fname = 'crayfish.jpg'

I = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
print('shape(I) = ', I.shape)
print('shape(I.ravel) = ', I.ravel().shape)

f, axes = plt.subplots(2, 3, figsize=(10, 7))

# ---------------------------- Visualize Image I and its Histogram ------------------------------
axes[0, 0].imshow(I, 'gray', vmin=0, vmax=255)
axes[0, 0].axis('off')
axes[1, 0].hist(I.ravel(), 256, [0, 256], color='black')

# -------------------------------- Automatically Obtaining a and b  --------------------------------

def find_ab(image, percent=2):
    """
    Automatically determines values for `a` and `b` for histogram expansion.
    :param image: Grayscale input image.
    :param percent: Threshold percentage for defining `a` and `b`.
    :return: a, b - computed intensity values.
    """
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    max_index = np.where(hist == np.max(hist))[0][0]
    print(max_index)
    print(np.max(hist))

    for i in range(max_index):
        if hist[max_index - i] <= ((np.max(hist) * percent) / 100):
            a = max_index - i
            print('a =', a)
            break
    for i in range(max_index):
        if hist[max_index + i] <= ((np.max(hist) * percent) / 100):
            b = max_index + i
            print('b =', b)
            break
    return a, b

# Obtain values for `a` and `b`
a, b = find_ab(I)

# ------------------------------------ Constructing Image J --------------------------------------

J = (I - a) * 255.0 / (b - a)
J[J < 0] = 0
J[J > 255] = 255
J = J.astype(np.uint8)
print('shape(J) = ', J.shape)
print('shape(J.ravel) = ', J.ravel().shape)

# ---------------------------- Visualize Image J and its Histogram ------------------------------
axes[0, 1].imshow(J, 'gray', vmin=0, vmax=255)
axes[0, 1].axis('off')
axes[1, 1].hist(J.ravel(), 256, [0, 256], color='blue')

# --------------------------- Constructing Histogram Equalization of I -------------------------
K = cv2.equalizeHist(I)

# ---------------------------- Visualize Histogram Equalization of I  -------------------------
axes[0, 2].imshow(K, 'gray', vmin=0, vmax=255)
axes[0, 2].axis('off')
axes[1, 2].hist(K.ravel(), 256, [0, 256], color='red')

plt.show()