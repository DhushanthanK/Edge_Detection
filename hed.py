import cv2
from matplotlib import pyplot as plt
import numpy as np
from skimage import measure
import pandas as pd

# Class definition remains unchanged
class CropLayer(object):
    def __init__(self, params, blobs):
        self.startX = 0
        self.startY = 0
        self.endX = 0
        self.endY = 0

    def getMemoryShapes(self, inputs):
        (inputShape, targetShape) = (inputs[0], inputs[1])
        (batchSize, numChannels) = (inputShape[0], inputShape[1])
        (H, W) = (targetShape[2], targetShape[3])
        self.startX = int((inputShape[3] - targetShape[3]) / 2)
        self.startY = int((inputShape[2] - targetShape[2]) / 2)
        self.endX = self.startX + W
        self.endY = self.startY + H
        return [[batchSize, numChannels, H, W]]

    def forward(self, inputs):
        return [inputs[0][:, :, self.startY:self.endY, self.startX:self.endX]]


# Load model
protoPath = "HED/HED_models/deploy.prototxt"
modelPath = "HED/HED_models/hed_pretrained_bsds.caffemodel"
net = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

# Register the crop layer with the model
cv2.dnn_registerLayer("Crop", CropLayer)

# Load the input image
img = cv2.imread("data/image.jpg")
(H, W) = img.shape[:2]

# Create a blob from the image
blob = cv2.dnn.blobFromImage(img, scalefactor=0.7, size=(W, H),
                             mean=(105, 117, 123), swapRB=False, crop=False)

# Perform a forward pass to compute the edges
net.setInput(blob)
hed = net.forward()
hed = hed[0, 0, :, :]
hed = (255 * hed).astype("uint8")

# Connected component-based labeling
blur = cv2.GaussianBlur(hed, (3, 3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
n_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh, connectivity=4)

# Create a false color image with connected components
colors = np.random.randint(0, 255, size=(n_labels, 3), dtype=np.uint8)
colors[0] = [0, 0, 0]  # black background
false_colors = colors[labels]

# Filter out small objects
MIN_AREA = 50
false_colors_area_filtered = false_colors.copy()
for i, centroid in enumerate(centroids[1:], start=1):
    area = stats[i, 4]
    if area > MIN_AREA:
        cv2.drawMarker(false_colors_area_filtered, (int(centroid[0]), int(centroid[1])),
                       color=(255, 255, 255), markerType=cv2.MARKER_CROSS)

# Create a grid to display and save all images
fig, axs = plt.subplots(2, 2, figsize=(12, 12))

# Plot original image
axs[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title("Original Image")
axs[0, 0].axis('off')

# Plot HED edge detection result
axs[0, 1].imshow(hed, cmap='gray')
axs[0, 1].set_title("HED Edge Detection")
axs[0, 1].axis('off')

# Plot thresholded image (binary)
axs[1, 0].imshow(thresh, cmap='gray')
axs[1, 0].set_title("Threshold Image")
axs[1, 0].axis('off')

# Plot false-colored connected components
axs[1, 1].imshow(false_colors_area_filtered)
axs[1, 1].set_title("Connected Components (Filtered)")
axs[1, 1].axis('off')

# Adjust layout to avoid overlap and show the figure
plt.tight_layout()

# Save the final collage image
plt.savefig("output/HED_results.jpg")

# Show the image
plt.show()