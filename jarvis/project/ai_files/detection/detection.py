import os

import cv2
from recogniser import *


# from ai_files.animate import *

def detection():
    vari = 0
    speak("security detection mode activated")
    pathv1 = os.path.join(r'E:\project\ai_files\detection', 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt')
    config_file = pathv1
    pathv2 = os.path.join(r'E:\project\ai_files\detection', 'frozen_inference_graph.pb')
    frozen_model = pathv2
    model = cv2.dnn_DetectionModel(frozen_model, config_file)

    classLabels = []
    filename = r'E:\project\ai_files\detection/labels.txt'
    with open(filename, 'rt') as fpt:
        classLabels = fpt.read().strip('\n').split('\n')  # classLabels.append(fpt.read())

    model.setInputSize(320, 320)
    model.setInputScale(1.0 / 127.5)
    model.setInputMean((127.5, 127.5, 127.5))
    model.setInputSwapRB(True)

    # read an image
    # img= cv2.imread('IMG_20210727_095417.jpg')     #have to give the path for the image
    # plt.imshow(img)
    #
    # ClassIndex, confidence, bbox = model.detect(img,confThreshold=0.5)
    # print(ClassIndex)
    # font_scale = 3
    # font = cv2.FONT_HERSHEY_PLAIN
    # for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
    #     cv2.rectangle(img,boxes,(255,0,0),2)
    #     cv2.putText(img,classLabels[ClassInd-1],(boxes[0]+10,boxes[1]+40),font,fontScale=font_scale,color=(0,255,0),thickness=3)
    # plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)) #to show the image and have to modify the code
    # plt.show()

    # video demo

    cap = cv2.VideoCapture(0)  # have to give the path for the video
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    font_scale = 3
    font = cv2.FONT_HERSHEY_PLAIN
    while True:
        ret, frame = cap.read()
        ClassIndex, confidence, bbox = model.detect(frame, confThreshold=0.55)
        print(ClassIndex)
        if (len(ClassIndex) != 0):
            for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
                if (ClassInd <= 80):
                    if (classLabels[ClassInd - 1] == "person"):
                        cv2.rectangle(frame, boxes, (255, 0, 0), 2)
                        cv2.putText(frame, classLabels[ClassInd - 1], (boxes[0] + 10, boxes[1] + 40), font,
                                    fontScale=font_scale, color=(0, 255, 0), thickness=3)
                        print(classLabels[ClassInd - 1])
                    if (classLabels[ClassInd - 1] == "person"):
                        # print("some one is enterd in to the field ")

                        speak("someone is enterd in to the field ")
                        vari = 1
        cv2.imshow('Detecting the tresspassers', frame)

        if vari == 1:
            break
            return True

        # k = cv2.waitKey(3) & 0xff  # Press 'ESC' for exiting video
        # print(k)
        if cv2.waitKey(33) == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
            return False
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detection()
