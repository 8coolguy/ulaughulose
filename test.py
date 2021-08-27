import cv2
import mediapipe as mp
import sys
import time
from os import system


#dispaly sizes
X=800
Y=600





mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh


# For webcam input:
#be able to recognise 2 faces
video ="test_images/testlaugh.mp4"

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=0)
#ser to video to -1 to get screen capture 
cap = cv2.VideoCapture(video)




#webCam.start()

#frame =webCam.get_image()
with mp_face_mesh.FaceMesh(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5, 
    max_num_faces=2)  as face_mesh:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = face_mesh.process(image)

    # Draw the face mesh annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    face_points=results.multi_face_landmarks
    if face_points:
      for face_landmarks in face_points:
        mp_drawing.draw_landmarks(
            image=image,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACE_CONNECTIONS,
            landmark_drawing_spec=drawing_spec,
            connection_drawing_spec=drawing_spec)
    cv2.imshow('MediaPipe FaceMesh', image)

    if cv2.waitKey(5) & 0xFF == 27:
      break

      #frame =webCam.get_image()

      
cap.release()



