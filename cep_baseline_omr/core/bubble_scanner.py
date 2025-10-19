import cv2
import numpy as np # noqa

def detect_bubbles(img, min_radius=5, max_radius=25):
    """
    Detects filled bubbles in the OMR sheet using contour analysis.
    Returns a list of bubble centers and bounding boxes.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bubbles = []

    for cnt in contours:
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        if min_radius < radius < max_radius:
            bubbles.append({
                "center": (int(x), int(y)),
                "radius": int(radius),
                "bbox": cv2.boundingRect(cnt)
            })

    print(f"🟢 Detected {len(bubbles)} bubbles")
    return bubbles
