import time

import cv2
# from cv2 import face
from recogniser import speak


def reco():
    yon = 0
    ctime = time.time()
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
    recognizer.read(r'../face_recognition/trainer/trainer.yml')  # load trained model
    cascadePath = r'../face_recognition/haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascadePath)  # initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type

    id = 4  # number of persons you want to Recognize

    names = ['', 'Narendra', 'Narendra', 'Narendra', 'Narendra', 'Narendra', ' ', '', '', '', '',
             '']  # names, leave first empty bcz counter starts from 0
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to remove warning
    cam.set(3, 640)  # set video FrameWidht
    cam.set(4, 480)  # set video FrameHeight

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    # flag = True

    while True:

        ret, img = cam.read()  # read the frames using the above created object

        converted_image = cv2.cvtColor(img,
                                       cv2.COLOR_BGR2GRAY)  # The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale(
            converted_image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # used to draw a rectangle on any image

            id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])  # to predict on every single image
            print(recognizer.predict(converted_image[y:y + h, x:x + w]))
            # Check if accuracy is less them 100 ==> "0" is perfect match
            if (accuracy > 50):
                id = names[id]
                speak("face detected")
                speak(f"welcome sir")
                yon = 1
                accuracy = "  {0}%".format(round(100 - accuracy))
            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
            cv2.putText(img, 'boss', (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('Face recognition', img)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            cam.release()
            cv2.destroyAllWindows()
            return False

        if time.time() - ctime > 35:
            print("time out")
            cam.release()
            cv2.destroyAllWindows()
            return False
        if yon == 1:
            time.sleep(3)
            cam.release()
            cv2.destroyAllWindows()
            return True

    # Do a bit of cleanup
    print("Thanks for using this program, have a good day.")


if __name__ == "__main__":
    print(reco())
