# Face-Detection-Using-Webcam
A computer vision project detecting face, eyes and smile of a person using a webcam and also in a video being imported by the user.

PRE-REQUISITES :

1. OpenCV(3+)

2. Haar cascade files for :
   -Smile
   -Eye
   -Face
(All are included in the repository)

DESCRIPTION :

This computer vision project uses OpenCV for detecting the face, eyes and smile using webcam. It uses Haar cascade
files to understand how to detect certain features as providede in the XML file itself. The person must be
properly at some minimum distance and within the range of the webcam so that his/her face can be properly detected.
For a person, who is far away from the webcam, it might detect the face but probably not eyes and smile. It can also
be used to detect same features in a video being provided by the user but just like for webcam, faces which are far 
away might just get their face detected and not eyes and smile. This project is still under development as I am
working on improvising it even more.
