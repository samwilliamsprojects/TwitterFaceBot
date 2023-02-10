import joblib
from keras.applications.vgg16 import preprocess_input
import numpy as np
import cv2
import urllib.request
import face_recognition
import random

# using the same package as we did for setting up the train and testing directories
cascPath = "/Users/samwilliams/Desktop/Novaksky?/face_finder/FaceDetect/haarcascade_frontalface_default.xml"

# Tweet bot responses
options = [
    "lmao ryan looks so dumb here",
    "ouija board says ryan is with us here",
    "ryan is dumb and also in this image",
    "wow ryan looks awful here lmao",
    "ryan looks big dumb in this pic",
    "i see ryan",
    "Ryan Novak is in this picture",
    "Young Novy is here",
    "whoa, thats ryan novak from tiktok :0",
    "This is Ryan Novak",
    "Ryan in pic",
    "its novak",
    "that boy really needs his teeth fixed",
]

def is_ryan(picture):
    """Takes a url picture as an input and searches for Ryan in it"""
    model = joblib.load("model_2_9.pkl")
    tweet_pic = urllib.request.urlopen(picture)
    url_pic = np.asarray(bytearray(tweet_pic.read()), dtype="uint8")
    url_pic = cv2.imdecode(url_pic, cv2.IMREAD_COLOR)
    faceCascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    gray_image = cv2.cvtColor(url_pic, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE,
    )

    resp = "no faces detected"
    for x, y, w, h in faces:
        cv2.rectangle(url_pic, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_color = url_pic[y : y + h, x : x + w]
        # model requires 224x224 dim
        the_image = cv2.resize(roi_color, dsize=(224, 224))

        # face_locations looks for faces in an image, since the face detector identifies non-faces as faces
        face_locations = face_recognition.face_landmarks(the_image)
        if len(face_locations) == 0:
            resp = "hm, ryans not in this... and neither is anybody else"
        else:
            # reshapes the face image to fit the models input requirements
            the_image = the_image.reshape(
                (1, the_image.shape[0], the_image.shape[1], the_image.shape[2])
            )
            pred = model.predict(the_image)
            for i, p in pred:
                # if i is greater than p then it is ryan
                if i > p:
                    # randomly chooses a response from the options
                    ran = random.randint(0, 12)
                    resp = options[ran]
                    break
                else:
                    resp = "This is not Ryan Novak"

    return resp
