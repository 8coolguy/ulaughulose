#purpose of this program is to return the emotion of the person if the person is recognised by the camera 
from emotion_test import returnEmotion
from facial_feature import drawPoints
import cv2
import face_recognition
import numpy as np

#when using video 
path=r'test_images/testlaugh.mp4'
cap =cv2.VideoCapture(-1)

while cap.isOpened():
    success, frame =cap.read()
    if not success:
        print("Ignoring Empty Frames")
        continue
    frame.flags.writeable =False

    
    drawPoints(frame)
    cv2.imshow('Emotion Detector', frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()




