from PyQt6 import QtCore, QtGui
import cv2
import numpy as np
from PyQt6.QtCore import *

frame = None

class ThreadOpenCV(QThread):
    changePixmap = pyqtSignal(QtGui.QImage)

    def __init__(self):
        super().__init__()

    #.start
    def run(self):
        global frame
        #Capture images from any available camera
        cap = cv2.VideoCapture(-1)
        cap.set(cv2.CAP_PROP_FPS, 24)

        while True:
            #Reading the image from the camera
            ret, frame = cap.read()
            #If the image exists
            if ret:
                #BGR --> RGB
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                #rgbImage --> QImage
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QtGui.QImage(
                    rgbImage.data, w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                self.changePixmap.emit(p)

                if cv2.waitKey(1) == ord('q'):
                    break

            cv2.destroyAllWindows()

#A class for taking photos from a camera
class Photo():

    #taking photos
    def TakePhoto(self, obj):
        global frame
        try:
            #Сохранение фото в файл
            img_name = "photo.jpg"
            cv2.imwrite(img_name, frame)
        except Exception as E:
            print(E)
            pass
        #Installing a photo in the pyqt window
        self.SetPhoto(frame,obj)

    #Installing a photo in the pyqt window
    def SetPhoto(self,img,obj):
        try:
            #Image transformations for embedding in qt
            self.img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.img_expanded = np.expand_dims(self.img_rgb, axis=0)
            self.rgbImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.h, self.w, self.ch = self.rgbImage.shape
            self.bytesPerLine = self.ch * self.w
            self.convertToQtFormat = QtGui.QImage(
                self.rgbImage.data, self.w, self.h, self.bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            self.p = self.convertToQtFormat.scaled(640, 480, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            pix = QtGui.QPixmap(self.p)
            obj.setPixmap(pix)
        except Exception as E:
            print(E)


