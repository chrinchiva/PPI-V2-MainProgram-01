import cv2
import os

print("Loading file")
# Load the pre-trained Haar Cascade model for face detection
base_dir = os.path.dirname(cv2.__file__)
xml_path = os.path.join(base_dir, 'data', 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(xml_path)

# Load the image where you want to detect faces
image = cv2.imread('images/image1.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Save or display the result
cv2.imwrite('faces_detected.jpg', image)
# If you want to display the result using OpenCV's GUI window uncomment the lines below
cv2.imshow('Faces Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
