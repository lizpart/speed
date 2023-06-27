# speed
Estimation of distance of bodies in motion and finding their relative speed

Ensure before running the `speed.py` file, it is in the same directory as `haarcascade_frontalface_default.xml`


Importing the necessary libraries: The code starts by importing the required libraries, including OpenCV (cv2) and time.

Variable initialization: Several variables are initialized to store values related to time, distance, and speed.

Lists for storing distance and speed: Two lists, listDistance and listSpeed, are created to store the calculated distance and speed values.

Camera setup: The code creates a VideoCapture object to access the camera and sets the video properties. It also creates a VideoWriter object to save the output video.

Focal length and distance estimation functions: Two functions, FocalLength and Distance_finder, are defined to calculate the focal length and estimate the distance based on the known distance, width, and the detected face width in the frame.

Face detection function: The face_data function is responsible for detecting faces in the input image using a pre-trained Haar cascade classifier. It returns the width of the detected face.

Speed calculation functions: The speedFinder function calculates the speed based on the covered distance and time taken. The averageFinder function finds the average value from a given list of numbers.

Reference image processing: A reference image is read from the directory, and the face_data function is called to obtain the face width in the reference image. The focal length is then calculated using the FocalLength function.

Main loop: The main loop captures frames from the camera feed and performs the following steps:

a. Calls the face_data function to detect the face width in the current frame.

b. If a face is detected, the distance is estimated using the Distance_finder function. The calculated distance is appended to listDistance, and the average distance is calculated using averageFinder.

c. The distance is converted from centimeters to meters.

d. If it's not the first frame, the change in distance and time is calculated. The speed is then calculated using the speedFinder function. The calculated speed is appended to listSpeed, and the average speed is calculated using averageFinder. The average speed is displayed on the frame.

e. The progressive line and speed-dependent line are drawn on the frame based on the average speed.

f. The current distance is displayed on the frame.

g. The frame is recorded using the VideoWriter object.

Exiting the program: The program exits when the "q" key is pressed. The camera, video recorder, and OpenCV windows are released and closed.

Note: The code assumes that you have the "haarcascade_frontalface_default.xml" file and a reference image named "Ref_image.png" in the same directory as the Python script. The face cascade classifier file can be downloaded from the OpenCV repository or other sources.
