from emotion_test import returnEmotion
import face_recognition
import numpy as np
import cv2

def showPicture(picture):
    cv2.imshow("Face Spotted:",picture)
    #waits for user to press any key 
    #(this is necessary to avoid Python kernel form crashing)
    while True:
        if cv2.waitKey(5) & 0xFF == 27:
            break
    #closing all open windows 
    cv2.destroyAllWindows() 
def scanEmotion(image):
    face_locations =face_recognition.face_locations(image)
   
    start_point=end_point=(0,0)
    #print(f'Face Locations{face_locations}')
    if len(face_locations) > 0:
        print("Face Found")
        start_point=tuple(face_locations[0][0:2])
        end_point =tuple(face_locations[0][2:4])
    else:
        return

    
    #image = cv2.rectangle(image, start_point, end_point, color, thick)
    #print(f'{start_point}----{end_point}')
    
    image = image[start_point[0]:end_point[0], end_point[-1]:start_point[-1]]
    image =cv2.resize(image, (48,48))    

    #showPicture(image)
    emotion =returnEmotion(image)
    #if emotion != "Surprise":
    print(emotion)

if __name__ =="__main__":
    color =(0,255,0)
    thick =2
    path =r'test_images/test_picture2.jpg'
    image = face_recognition.load_image_file(path)
    scanEmotion(image)
    showPicture(image)
    
    




