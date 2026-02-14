import cv2
import numpy as np

def detect_ink_with_auto_roi(frame):
    img = frame.copy()
    if img is None:
        print("Image not found")
        return

    img = cv2.resize(img, (500, 500))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 20, 70])
    upper_skin = np.array([20, 255, 255])

    skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)

    kernel = np.ones((5,5), np.uint8)
    skin_mask = cv2.morphologyEx(skin_mask, cv2.MORPH_OPEN, kernel)
    skin_mask = cv2.morphologyEx(skin_mask, cv2.MORPH_DILATE, kernel)

    contours, _ = cv2.findContours(
        skin_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) == 0:
        print(" Finger not detected")
        return

    
    finger_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(finger_contour)

    finger_roi = img[y:y+h, x:x+w]

    hsv_roi = cv2.cvtColor(finger_roi, cv2.COLOR_BGR2HSV)

    lower_ink = np.array([110, 40, 40])
    upper_ink = np.array([140, 255, 255])

    ink_mask = cv2.inRange(hsv_roi, lower_ink, upper_ink)

    kernel = np.ones((5,5), np.uint8)
    ink_mask = cv2.morphologyEx(ink_mask, cv2.MORPH_CLOSE, kernel)

    ink_pixels = cv2.countNonZero(ink_mask)
    total_pixels = ink_mask.shape[0] * ink_mask.shape[1]
    ink_ratio = ink_pixels / total_pixels

    if ink_ratio > 0.002:
        result = "INK DETECTED"
    else:
        result = "NO INK"

    print(f"Ink ratio: {ink_ratio:.4f}")
    print(result)

    color = (0, 0, 255) if result == " INK DETECTED" else (0, 255, 0)

    cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
    cv2.putText(img, result, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Final Result", img)
    cv2.imshow("Finger ROI", finger_roi)
    cv2.imshow("Ink Mask", ink_mask)
    cv2.imwrite("finger_roi.png", finger_roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
