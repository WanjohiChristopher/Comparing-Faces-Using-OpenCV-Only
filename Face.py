import face_recognition
import os
import cv2
 #directories
known_faces='Known_faces'
uknown_faces='UnKnown_faces'
TOLERANCE=0.4
FRAME_THICKNESS=3
FONT_THICKNESS=2
MODEL='hog'

invisibles = [".DS_Store", ".Trashes"]
print('loading known_faces')

Known_face=[]
Known_names=[]

for i in os.listdir(known_faces):  # Loop over the folder to list individual files
    image = known_faces + i
    image = face_recognition.load_image_file(image)  # Run your load command
    image_encoding = face_recognition.face_encodings(image)
    