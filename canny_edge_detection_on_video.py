import cv2
import numpy as np

cap = cv2.VideoCapture('data/video.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    width, height = frame.shape[1], frame.shape[0]
    
    # Convert the frame to grayscale for edge detection
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to smooth the image
    kernel_size = 5
    blur = cv2.GaussianBlur(grayscale, (kernel_size, kernel_size), 0)
    
    # Canny edge detection
    low_t = 50
    high_t = 150
    edges = cv2.Canny(blur, low_t, high_t)
    
    # Hough Line Transform for lane detection on the entire frame
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=100, maxLineGap=50)
    
    # Draw the detected lines on the original frame
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    # Display the edges and the frame with lines
    cv2.imshow("Edges", edges)
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()