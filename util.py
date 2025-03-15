import numpy as np
import cv2

def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Adjusted to better capture the yellow color
    if hue >= 15 and hue <= 35:  # Yellow hue range
        lowerLimit = np.array([20, 100, 100], dtype=np.uint8)  # Lower bound for yellow
        upperLimit = np.array([40, 255, 255], dtype=np.uint8)  # Upper bound for yellow
    else:
        lowerLimit = np.array([0, 0, 0], dtype=np.uint8)  # Default fallback
        upperLimit = np.array([0, 0, 0], dtype=np.uint8)

    return lowerLimit, upperLimit
