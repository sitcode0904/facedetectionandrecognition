import os

import cv2
import numpy as np
from cv2 import face
from PIL import Image

recognizer=cv2.face.LBPHFaceRecognizer_create()
path='C:/Users/KIIT/Desktop/facerecognition/dataset'
def getimgwithid(path):
    images_path=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    ids=[]
    for singleimgpath in images_path:
        faceImg=Image.open(singleimgpath).convert('L')
        faceNp=np.array(faceImg,np.uint8)
        id=int(os.path.split(singleimgpath)[-1].split(".")[1])
        print(id)
        faces.append(faceNp)
        ids.append(id)
        cv2.imshow("Training",faceNp)
        cv2.waitKey(10)
    return np.array(ids),faces
ids,faces=getimgwithid(path)
recognizer.train(faces,ids)
recognizer.save('recognizer/trainingdata.yml')
cv2.destroyAllWindows