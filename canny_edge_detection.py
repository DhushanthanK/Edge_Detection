import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Function to display and save images in one frame
def show_and_save_images(images, titles, save_path):
    plt.figure(figsize=(18, 12))
    
    for i in range(len(images)):
        plt.subplot(2, 3, i + 1)
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB) if len(images[i].shape) == 3 else images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()

# Read the image
image = cv2.imread("data/image.jpg")
print("Original Image Shape:", image.shape)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("Grayscale Image Shape:", gray.shape)

# Apply Bilateral Filtering to reduce noise while preserving edges
diameter = 10
sigma_color = 75
sigma_space = 75
blur_gray = cv2.bilateralFilter(gray, diameter, sigma_color, sigma_space)
print("Bilateral Filter Applied.")

# Apply Adaptive Thresholding to handle uneven lighting conditions
max_output_value = 255
block_size = 11
C = 2
adaptive_thresh = cv2.adaptiveThreshold(blur_gray, max_output_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, C)
print("Adaptive Thresholding Applied.")

# Apply Canny Edge Detection
low_threshold = 20
high_threshold = 60
edges = cv2.Canny(adaptive_thresh, low_threshold, high_threshold)
print("Canny Edge Detection Applied.")

# Perform dilation to connect broken edges (useful for noisy edges)
kernel = np.ones((5, 5), np.uint8)
dilated_edges = cv2.dilate(edges, kernel, iterations=1)
print("Dilation Applied.")

# Create output directory if not exists
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Titles for each image
titles = ["Original Image", "Grayscale Image", "Bilateral Filter", "Adaptive Threshold", "Canny Edges", "Dilated Edges"]

# List of images
images = [image, gray, blur_gray, adaptive_thresh, edges, dilated_edges]

# Path to save the output image
save_path = os.path.join(output_dir, "Canny_results.jpg")

# Show and save all images
show_and_save_images(images, titles, save_path)
print(f"Result saved to {save_path}")