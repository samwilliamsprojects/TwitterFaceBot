import face_recognition
import os
import glob
import shutil

os.chdir("facedetection")
# Determines if a pic in your directory is a face, since face_detection.py identifies a lot of objects as faces
for image2 in glob.glob("*.jpg"):
    image = face_recognition.load_image_file(image2)
    face_locations = face_recognition.face_landmarks(image)
    if len(face_locations) == 0:
        os.remove(image2)

def move_faces():
    """Moves faces to the directory specified in the shutil function"""
    for image3 in glob.glob("*.jpg"):
        shutil.move(image3, "../train/notRyan")

move_faces()
