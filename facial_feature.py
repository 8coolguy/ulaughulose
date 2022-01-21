# puts the dots on thecd
from PIL import Image, ImageDraw
from emotion_detector import showPicture
import face_recognition
import sys
import cv2

def drawPoints(image):
    # Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(image)
    #print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))



    for face_landmarks in face_landmarks_list:

        # Print the location of each facial feature in this image
        for facial_feature in face_landmarks.keys():
            #print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))
            for point in face_landmarks[facial_feature]:
                image =cv2.circle(image, point, 1, (0,255,0),thickness=2)
    return image, len(face_landmarks_list) >0
if __name__ =="__main__":
    #Load the jpg file into a numpy array
    image_path="test_images/test_picture7.jpg"
    if len(sys.argv)>1:
        image_path=str(sys.argv[1])
    print(f'Opening {image_path}')
    image = face_recognition.load_image_file(image_path)

    drawPoints(image)
    # Show the picture
    showPicture(image)

