import cv2

# Opens the inbuilt camera of laptop to capture video.
webCam = cv2.VideoCapture(0)
currentframe = 0

while (True):
    success, frame = webCam.read()

    # Save Frame by Frame into disk using imwrite method
    cv2.imshow("Output", frame)
    cv2.imwrite(f"target_folder/frame_{currentframe}.jpg",frame)
    if currentframe<=4:
        currentframe+=1
    else:
        pass

    webCam.release()
    cv2.destroyAllWindows()
    




    

    import cv2
# os and sys for path findings
    import sys,os


    path = "D:/secureus/target_folder"
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    count = 0

    for path in imagePaths:
        print(path)
        image = cv2.imread(path)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray,1.3,5)
        if faces is not ():
            for (x,y,w,h) in faces:
                face = image[y:y+h,x:x+w]
                count += 1
                cv2.imwrite("faces/"+str(count)+".jpg",face)      
    print("done")

import glob 
import cv2
import sys
while 1 :
    filename = input("Enter the file name in which images are present =")
    for img in glob.glob(filename+'/*.*'):
        #try :
            var_img = cv2.imread(img)
            cv2.imshow(str(img) , var_img)

    def detect_face(img):

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

        if (len(faces) == 0):
            return None, None

        (x, y, w, h) = faces[0]
        return gray[y:y+w, x:x+h], faces[0]
    cv2.imshow(str(img) , img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
