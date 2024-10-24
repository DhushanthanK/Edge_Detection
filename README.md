# Edge Detection and Lane Detection Project

This project demonstrates the use of edge detection techniques for edge detection in images and videos. It involves a comparison between Canny Edge Detection and Holistically Nested Edge Detection (HED), testing the performance of Canny Edge Detection on video, and focusing on specific regions using a Region of Interest (ROI) for more targeted edge detection.

## Key Features

1. **Edge Detection Comparison**: A comparative analysis of Canny Edge Detection and Holistically Nested Edge Detection (HED).

2. **Canny Edge Detection on Video**: Testing the performance of Canny Edge Detection for real-time video edge detection.

3. **Region of Interest (ROI)**: Focusing on specific areas of the frame to detect edges relevant to lane detection.

## Project Workflow

1. **Canny vs HED Comparison**:

   - Canny Edge Detection: A classical edge detection method using gradients and thresholds.

   - Holistically Nested Edge Detection (HED): A deep learning-based edge detection method providing more detailed edge maps.

   - The results of both methods are compared visually.

2. **Canny Edge Detection on Video**:

   - The project tests Canny Edge Detection’s ability to handle edge detection in video frames.

   - Results are processed and saved as a video file showing edges in each frame.

3. **Region of Interest (ROI) for Lane Detection**:

   - An ROI is applied to focus on specific parts of the frame for robot navigation.

   - The project uses the ROI to mask unwanted areas and perform Canny Edge Detection only on the relevant region.

   - Hough Line Transform is then used to detect lines in the ROI, which are drawn on the original frame.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/edge-detection.git
   cd edge-detection

2. **Install dependencies:
Ensure Python 3.x and the required libraries are installed:

   ```bash
   pip install opencv-python numpy
    
3. Place your file:
`data` folder contains image and video files.

## Usage

1. Edge Detection Comparison

- To compare Canny Edge Detection with Holistically Nested Edge Detection (HED):

   ```bash
   python canny_edge_detection.py
   python hed.py

2. Canny Edge Detection on Video

- To test Canny Edge Detection on a video and save the processed video:

  ```bash
  python canny_edge_detection_on_video.py

3. Canny Edge Detection with Region of Interest (ROI)

- To detect edges within a specific region of the video and highlight lane lines:

  ```bash
  python canny_edge_detection_on_video_in_the_roi.py

## Processing Pipeline

	1.	Grayscale Conversion: Converts the frame to grayscale for easier edge detection.
	2.	Gaussian Blur: Smooths the image to reduce noise.
	3.	Canny Edge Detection: Detects edges based on gradient changes in the image.
	4.	Region of Interest (ROI): Masks the image to focus only on the relevant region for lane detection.
	5.	Hough Line Transform: Detects straight lane lines in the masked edge-detected image.
	6.	Line Drawing: Draws the detected lines on the original frame and saves the video output.

## License

This project is licensed under the MIT License. See the LICENSE file for details.






  
