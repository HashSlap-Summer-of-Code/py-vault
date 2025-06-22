#!/usr/bin/env python3



import cv2
import sys
import os

def detect_faces(image_path):
    if not os.path.exists(image_path):
        print(f"[!] File not found: {image_path}")
        return

    # Load pre-trained Haar cascade for frontal face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Read image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    print(f"[i] Detected {len(faces)} face(s).")

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the image
    cv2.imshow("Face Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    if len(sys.argv) != 2:
        print("Usage: python face-detection.py <image_path>")
        return

    detect_faces(sys.argv[1])

if __name__ == "__main__":
    main()
