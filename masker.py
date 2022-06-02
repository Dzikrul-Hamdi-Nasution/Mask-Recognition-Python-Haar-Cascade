import numpy as np 
import cv2 
from playsound import playsound
import serial
import time
#arduino = serial.Serial('COM35', 9600)

# Load the cascade
face_cascade = cv2.CascadeClassifier("cascade.xml")
mulut = cv2.CascadeClassifier("mulut.xml")
hidung = cv2.CascadeClassifier("hidung.xml")
# To capture video from webcam.
cap = cv2.VideoCapture(0)
cv2.resolution = (1024, 640)

status=0
status_2=0
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_SIMPLEX 
	# time when we finish processing for this frame 

	 

    faces = face_cascade.detectMultiScale(gray, 5, 15)
    hasil_mulut = mulut.detectMultiScale(gray, 1.3, 11)
    hasil_hidung = hidung.detectMultiScale(gray, 1.1, 11)

    # Draw the rectangle around each face
    status=0
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        status=2
       
        
      
  
         
 
        
    # Display
    cv2.imshow("img", img)
    
    

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
# Release the VideoCapture object
cap.release()
