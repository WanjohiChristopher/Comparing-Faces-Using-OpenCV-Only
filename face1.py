import cv2
import face_recognition
from PIL import Image
import sys
#img=cv2.imread('./Known_faces/*.jpg')
img=cv2.imread('857_63bd106e.jpg')
#conversion to RGB from BGR
Cvt=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
encoding=face_recognition.face_encodings(Cvt)[0]

img1=cv2.imread('3we.jpg')
#conversion to RGB from BGR
Cvt1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
try:
    encoding1=face_recognition.face_encodings(Cvt1)[0]
except IndexError as e:
    print(e)
    sys.exit(1)
#comparing faces
output=face_recognition.compare_faces([encoding],encoding1)

print('The results are:',output)

''' #displaying the images
cv2.imshow('img',Cvt)
cv2.imshow('img1',Cvt1)
cv2.waitKey(0)
cv2.destroyAllWindows()'''