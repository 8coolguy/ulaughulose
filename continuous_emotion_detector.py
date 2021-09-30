#purpose of this program is to return the emotion of the person if the person is recognised by the camera 
from emotion_detector import scanEmotion
from facial_feature import drawPoints
import cv2
import face_recognition

#when using video 
path=r'test_images/testlaugh.mp4'
cap =cv2.VideoCapture(path)

while cap.isOpened():
    success, frame =cap.read()
    if not success:
        print("Ignoring Empty Frames")
        continue

    frame.flags.writeable =True
    frame,face_found=drawPoints(frame)
    cv2.imshow('Emotion Detector', frame)
    if face_found:
        scanEmotion(frame)
    
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()




