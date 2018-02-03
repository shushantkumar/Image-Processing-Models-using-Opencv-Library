import numpy as np
import cv2

img = cv2.imread('p7.jpg',cv2.IMREAD_COLOR)			#reading image
cv2.line(img,(0,0),(200,300),(255,255,255),50)		#drawing a line
cv2.rectangle(img,(500,250),(1000,500),(0,0,255),15)	#drawing a rectangle
cv2.circle(img,(447,63), 63, (0,255,0), -1)				#drawing a circle
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)			#drawing random shapes with straight lines using predefined points 
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Rocks!',(10,500), font, 6, (200,255,155), 13, cv2.LINE_AA)	#writing on images
cv2.imshow('image',img)									#displaying images
cv2.waitKey(0)
cv2.destroyAllWindows()