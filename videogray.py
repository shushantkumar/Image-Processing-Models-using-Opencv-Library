import numpy as np
import cv2

cap = cv2.VideoCapture(0)						#Function to start capturing videos
fourcc = cv2.VideoWriter_fourcc(*'XVID')		
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))	#Storing in external file

while(True):
    ret, frame = cap.read()						#reading videos as frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	#converting each frames to gray
    #out.write(frame)
    cv2.imshow('frame',gray)					#displaying greyscale frames 
    if cv2.waitKey(1) & 0xFF == ord('q'):		#while any break 
        break

cap.release()
out.release()
cv2.destroyAllWindows()