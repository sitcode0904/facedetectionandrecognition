import sqlite3

import cv2
import numpy as np

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)

def create_table(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS Students
                    (Id INTEGER PRIMARY KEY, Name TEXT, age INTEGER)''')
    conn.commit()

def insertorupdate(Id,Name,age):
    conn=sqlite3.connect("C:/Users/KIIT/Desktop/facerecognition/sqlite.db")
    create_table(conn)  # Create the table if it doesn't exist
    cmd="SELECT * FROM Students WHERE Id="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        conn.execute("UPDATE Students SET Name=? WHERE Id=?",(Name,Id,))
        conn.execute("UPDATE Students SET age=? WHERE Id=?", (age, Id,))
    else:
        conn.execute("INSERT INTO Students (Id,Name,age) values(?,?,?)",(Id,Name,age))
    conn.commit()
    conn.close()

Id=input('Enter User Id:')
Name=input('Enter User Name:')
age=input('Enter User Age:')

insertorupdate(Id,Name,age)

sampleNum=0
while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1
        cv2.imwrite("dataset/user."+str(Id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow("Face",img)
    cv2.waitKey(1)
    if(sampleNum>20):
        break

cam.release()
cv2.destroyAllWindows()                   #quit



































