import cv2
import os

# USE GAUSSIAN NOISE IN MY DATA SET 
dirPath = "notRyan"
cascPath = "/Users/samwilliams/Desktop/Novaksky?/face_finder/FaceDetect/haarcascade_frontalface_default.xml"

for file in os.listdir(dirPath):
    print(file)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    image = cv2.imread("notRyan/" + file)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_color = image[y:y + h, x:x + w] 
        print("[INFO] Object found. Saving locally.") 
        cv2.imwrite(str(w) + str(h) + 'faces.jpg', roi_color)

