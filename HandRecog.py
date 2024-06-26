# import the opencv library 
import cv2 
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap=cv2.VideoCapture(1)
hands=mp_hands.Hands()
while True:
    data,image=cap.read()
    #Flip Camera
    image=cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB)
    #Result Database
    results=hands.process(image)
    image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,mp_hands.HAND_CONNECTIONS)
    cv2.imshow('Handtracker', image)
    cv2.waitKey(1)
    if cv2.waitKey(20) & 0xFF  == ord("q"):
        break 

