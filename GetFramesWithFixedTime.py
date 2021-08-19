import os
import time
import cv2 as cv

# Opens the built-in camera of laptop to capture video.
cap = cv.VideoCapture(0)
path = '/Users/admin/Documents/GitHub/Extracting-and-Saving-Video-Frames/Output2'
count = 0

while cap.isOpened():
    ret, frame = cap.read()

    # This condition prevents from infinite looping
    # In case video capture ends
    if not ret:
        break

    # Save Frame by Frame into disk using iwrite method
    cv.imwrite(os.path.join(path, 'frame%d.png' % count), frame)
    count += 1
    time.sleep(.5)  # Delay for periodic time

cap.release()
cv.destroyAllWindows()