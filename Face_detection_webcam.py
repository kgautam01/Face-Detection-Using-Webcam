#Importing the libraries
import cv2

#Loading the cascades
face_cascade = cv2.CascadeClassifier('face.xml')
smile_cascade = cv2.CascadeClassifier('smile.xml')
eye_cascade = cv2.CascadeClassifier('eye.xml')

#Defining a function for detecting face, smile and eyes.
#Gray is being used for gray images and frame for actual colored image.
#Image here means the frame captured by the webcam per second.
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            flags = cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        # Extracting just that part of image containing the face
        roi_gray = gray[y:y+h, x:x+w]
        # Extracting just that part of image containing the face
        roi_color = frame[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(
                roi_gray,scaleFactor = 1.65,
                minNeighbors = 23,
                minSize = (10,10),
                flags = cv2.CASCADE_SCALE_IMAGE)
        eyes = eye_cascade.detectMultiScale(
                roi_gray,scaleFactor = 1.08,
                minNeighbors = 15,
                minSize = (10,10),
                flags = cv2.CASCADE_SCALE_IMAGE)
        for (x, y, w, h) in smiles:
            cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255,255,0), 2)
        for (x, y, w, h) in eyes:
            cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255,255,0), 2)    
    return frame


#Doing some Face Detection with the webcam.
#For videos, provide the filename( present in the same directory). Use '0' for 
#webcam.
video_capture = cv2.VideoCapture(0)

while True:
    # Here two values are returned by this function used(video_capture.read()) 
    # below. First one is a boolean value telling whether the reading using 
    # webcam is successful.
    # Second one is the image captured using the webcam.
    _, frame = video_capture.read()
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    #Just type 'x' to stop video capturing.
    if cv2.waitKey(1) == ord('x'):
        break
    

video_capture.release()
cv2.destroyAllWindows()