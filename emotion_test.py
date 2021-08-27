from keras.models import load_model
#from emotion_detector import showPicture
import numpy as np
import face_recognition
import cv2

model =load_model(r'/home/arnav/ulaughulose/face_and_emotion_detection/emotion_detector_models/model_v6_23.hdf5')
emotion_dict= {'Angry': 0, 'Sad': 5, 'Neutral': 4, 'Disgust': 1, 'Surprise': 6, 'Fear': 2, 'Happy': 3}
def returnEmotion(picture):
    picture=cv2.resize(picture,(48,48))
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)
    #if __name__ == "__main__":
    #    showPicture(picture)


    picture = np.reshape(picture, [1, picture.shape[0], picture.shape[1], 1])



    predicted_class=np.argmax(model.predict(picture))
    label_map = dict((v,k) for k,v in emotion_dict.items()) 
    predicted_label = label_map[predicted_class]

    return predicted_label

if __name__ == "__main__":
    path =r'test_images/test_picture8.jpg'

    image = face_recognition.load_image_file(path)
    picture =cv2.imread(path)
    print(returnEmotion(picture))



