import cv2
import numpy as np
import matplotlib.pyplot as plt

I = cv2.imread("pasargadae.jpg", cv2.IMREAD_GRAYSCALE)

levels = 256

# Calculating histogram
def calc_hist(I, levels):
    hist = np.zeros(levels)
    for pixel_value in I.ravel():
        hist[pixel_value] += 1
    return hist

# Calculating CDF
def calc_cdf(hist, levels):
    cdf = np.zeros_like(hist)
    cdf[0] = hist[0]
    for i in range(1, levels):
        cdf[i] = cdf[i - 1] + hist[i]
    return cdf

hist = calc_hist(I, levels)
cdf = calc_cdf(hist, levels)

# Normalize CDF
cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
cdf_normalized = cdf_normalized.astype(np.uint8)

# Mapping old intensity values to new ones
mapping = cdf_normalized

# Replace intensity values based on the mapping
equalized_image = mapping[I]

equalized_image_hist = calc_hist(equalized_image, levels)
equalized_image_cdf = calc_cdf(equalized_image_hist, levels)

# Image Classification Function
def classify_image(I, hist):
    mean_intensity = np.mean(I)
    std_dev = np.std(I)
    dark_pixels = np.sum(hist[:50]) / I.size
    bright_pixels = np.sum(hist[200:]) / I.size
    
    category = ""
    if mean_intensity < 50 and dark_pixels > 0.5:
        category = "Underexposed"
    elif mean_intensity > 200 and bright_pixels > 0.5:
        category = "Overexposed"
    elif std_dev < 40:
        category = "Low Contrast"
    else:
        category = "Well-Balanced"
    
    return category

# Classify the image
image_category = classify_image(I, hist)
print(f"Image Category: {image_category}")

fig = plt.figure(figsize=(16, 8))
fig.add_subplot(2, 3, 1)
plt.imshow(I, cmap='gray')
plt.title(f'Original Image: Pasargadae ({image_category})')
plt.axis('off')

fig.add_subplot(2, 3, 2)
plt.plot(hist, color='black')
plt.title('Source Histogram')

fig.add_subplot(2, 3, 3)
plt.plot(cdf, color='blue')
plt.title('Source CDF')

fig.add_subplot(2, 3, 4)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

fig.add_subplot(2, 3, 5)
plt.plot(equalized_image_hist, color='red')
plt.title('Equalized Histogram')

fig.add_subplot(2, 3, 6)
plt.plot(equalized_image_cdf, color='green')
plt.title('Equalized CDF')

plt.show()
