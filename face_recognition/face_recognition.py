import cv2
import dlib

#read the image
img = cv2.imread("photo-1-1618127005328991106558-161822213965230372779.webp")

#convert img to graycale: 3D (RGB) -> 2D (BW)
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

#dlib: Load face recognition detector
face_detector = dlib.get_frontal_face_detector()

#use detector to find facw landmarks
faces = face_detector(gray)

for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()

    #draw a rectangle
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0,255,0), thickness=3)

#show the image
cv2.imshow(winname="Face Recognition App", mat=img)

#wait for a key press to exit
cv2.waitKey(delay=0) #user ấn 1 phím bất kì để exit img

#Close all windows
cv2.destroyAllWindows()
