import os
import face_recognition
from time import time
import cv2
dir='./imgs'
start=time()
for i in os.listdir(dir):
    #img=cv2.imread(dir+'/'+i)
    dir2=os.path.join(dir,i)
    if os.path.isdir(dir2):
        for filename in os.listdir(dir2):
         
          if not filename.startswith('.'): 
            filepath = os.path.join(dir2, filename)
            img= face_recognition.load_image_file(filepath)
            Cvi=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            encoding=face_recognition.face_encodings(Cvi)[0]
        

    for j in os.listdir(dir):
        #img=cv2.imread(dir+'/'+j)
        dir2=os.path.join(dir,j)
        if os.path.isdir(dir2):
            for filenname in os.listdir(dir2):
             
              if not filenname.startswith('.'): 
                filepaths=os.path.join(dir2, filenname)
                imgs=face_recognition.load_image_file(filepaths)
                
                Cvt=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
                encoding1=face_recognition.face_encodings(Cvt)[0]
                result=face_recognition.compare_faces([encoding],encoding1)
                
                if result[0]==True:
                    print(i+' is the same as '+j)
                    break
                else:
                    print(i+' is not the same as '+j)
                    break
print(f'The time taken to run is:{time()-start} seconds')