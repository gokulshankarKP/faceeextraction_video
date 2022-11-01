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
