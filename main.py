import cv2

# This is the distance from camera to face oject
KNOWN_DISTANCE = 30  # centimeter
# width of the object face
KNOWN_WIDTH = 14.3  # centimeter
# Definition of the RGB Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
# calling the haarcascade_frontalface_default.xml module for face detection.
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def face_data(image):

    face_width = 0
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)
    for (x, y, h, w) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), WHITE, 1)
        face_width = w

    return face_width
#We use 0 in the VideoCapture function since thats the default camera
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    face_width_in_frame = face_data(frame)
    cv2.imshow("frame", frame)
    #The string 'q' is will be used for quiting
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()