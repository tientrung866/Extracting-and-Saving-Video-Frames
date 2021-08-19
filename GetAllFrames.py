import cv2 as cv
import os

# Opens the built-in camera of laptop to capture video.
cap = cv.VideoCapture(0)
path = '/Users/admin/Documents/GitHub/Extracting-and-Saving-Video-Frames/Output'
i = 0

while cap.isOpened():
    ret, frame = cap.read()

    # This condition prevents from infinite looping
    # In case video capture ends :
    if not ret:
        break

    # Save Frame by Frame into disk using iwrite method
    cv.imwrite(os.path.join(path, 'frame%d.png' % i), frame)
    i += 1

cap.release()
cv.destroyAllWindows()