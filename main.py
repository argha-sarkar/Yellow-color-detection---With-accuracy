import cv2
from PIL import Image
from util import get_limits

yellow = [0, 255, 255]  # yellow in BGR colorspace
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Convert the frame to HSV color space
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get HSV limits for yellow color
    lowerLimit, upperLimit = get_limits(color=yellow)

    # Create a mask for yellow color
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # If contour area is too small, ignore it
        if cv2.contourArea(contour) > 500:  # Threshold to avoid noise
            # Get bounding box around contour
            x, y, w, h = cv2.boundingRect(contour)
            
            # Calculate the area of the bounding box and the contour
            bbox_area = w * h
            contour_area = cv2.contourArea(contour)

            # Calculate accuracy as the ratio of contour area to bounding box area
            accuracy = (contour_area / bbox_area) * 100

            # Draw the bounding box on the frame
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)

            # Add accuracy percentage on the bounding box
            accuracy_text = f"{accuracy:.2f}%"
            cv2.putText(frame, accuracy_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('frame', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
