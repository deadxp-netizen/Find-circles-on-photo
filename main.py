
from PyQt6 import QtCore, QtGui, QtWidgets, QtTest
from PyQt6.QtCore import *
import circle_find

# Declare global variables so that I don't pass them to the function every time
minD = None
minR = None
par1 = None
par2 = None
maxR = None
photo = None
photo_text = None

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 694)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.vid_cam_Layout = QtWidgets.QVBoxLayout()
        self.vid_cam_Layout.setObjectName("vid_cam_Layout")
        self.vid_text = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.vid_text.setFont(font)
        self.vid_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.vid_text.setObjectName("vid_text")
        self.vid_cam_Layout.addWidget(self.vid_text)
        self.vid_video = QtWidgets.QLabel(parent=self.centralwidget)
        self.vid_video.setObjectName("vid_video")
        self.vid_cam_Layout.addWidget(self.vid_video)
        self.vid_cam_Layout.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.vid_cam_Layout, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MinR_Layout = QtWidgets.QHBoxLayout()
        self.MinR_Layout.setObjectName("MinR_Layout")
        self.MinR_text = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MinR_text.setFont(font)
        self.MinR_text.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.MinR_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MinR_text.setObjectName("MinR_text")
        self.MinR_Layout.addWidget(self.MinR_text)
        self.MinR_count = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MinR_count.setFont(font)
        self.MinR_count.setObjectName("MinR_count")
        self.MinR_Layout.addWidget(self.MinR_count)
        self.verticalLayout.addLayout(self.MinR_Layout)
        self.MinR_red_Layout = QtWidgets.QHBoxLayout()
        self.MinR_red_Layout.setObjectName("MinR_red_Layout")
        self.MinR_min = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.MinR_min.setFont(font)
        self.MinR_min.setObjectName("MinR_min")
        self.MinR_red_Layout.addWidget(self.MinR_min)
        self.MinR_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.MinR_slider.setMaximum(500)
        self.MinR_slider.setMinimum(1)
        self.MinR_slider.setPageStep(1)
        self.MinR_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.MinR_slider.setObjectName("MinR_slider")
        self.MinR_red_Layout.addWidget(self.MinR_slider)
        self.MinR_max = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.MinR_max.setFont(font)
        self.MinR_max.setObjectName("MinR_max")
        self.MinR_red_Layout.addWidget(self.MinR_max)
        self.verticalLayout.addLayout(self.MinR_red_Layout)
        self.MaxR_Layout = QtWidgets.QHBoxLayout()
        self.MaxR_Layout.setObjectName("MaxR_Layout")
        self.MaxR_text = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MaxR_text.setFont(font)
        self.MaxR_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MaxR_text.setObjectName("MaxR_text")
        self.MaxR_Layout.addWidget(self.MaxR_text)
        self.MaxR_count = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MaxR_count.setFont(font)
        self.MaxR_count.setObjectName("MaxR_count")
        self.MaxR_Layout.addWidget(self.MaxR_count)
        self.verticalLayout.addLayout(self.MaxR_Layout)
        self.MaxR_red_Layout = QtWidgets.QHBoxLayout()
        self.MaxR_red_Layout.setObjectName("MaxR_red_Layout")
        self.MaxR_min = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.MaxR_min.setFont(font)
        self.MaxR_min.setObjectName("MaxR_min")
        self.MaxR_red_Layout.addWidget(self.MaxR_min)
        self.MaxR_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.MaxR_slider.setMaximum(500)
        self.MaxR_slider.setMinimum(1)
        self.MaxR_slider.setPageStep(1)
        self.MaxR_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.MaxR_slider.setObjectName("MaxR_slider")
        self.MaxR_red_Layout.addWidget(self.MaxR_slider)
        self.MaxR_max = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.MaxR_max.setFont(font)
        self.MaxR_max.setObjectName("MaxR_max")
        self.MaxR_red_Layout.addWidget(self.MaxR_max)
        self.verticalLayout.addLayout(self.MaxR_red_Layout)
        self.MinD_Layout = QtWidgets.QHBoxLayout()
        self.MinD_Layout.setObjectName("MinD_Layout")
        self.MinD_text = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MinD_text.setFont(font)
        self.MinD_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.MinD_text.setObjectName("MinD_text")
        self.MinD_Layout.addWidget(self.MinD_text)
        self.MinD_count = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.MinD_count.setFont(font)
        self.MinD_count.setObjectName("MinD_count")
        self.MinD_Layout.addWidget(self.MinD_count)
        self.verticalLayout.addLayout(self.MinD_Layout)
        self.MinD_red_Layout = QtWidgets.QHBoxLayout()
        self.MinD_red_Layout.setObjectName("MinD_red_Layout")
        self.MinD_min = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.MinD_min.setFont(font)
        self.MinD_min.setObjectName("MinD_min")
        self.MinD_red_Layout.addWidget(self.MinD_min)
        self.MinD_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.MinD_slider.setMaximum(500)
        self.MinD_slider.setMinimum(1)
        self.MinD_slider.setPageStep(1)
        self.MinD_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.MinD_slider.setObjectName("MinD_slider")
        self.MinD_red_Layout.addWidget(self.MinD_slider)
        self.MinD_max = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.MinD_max.setFont(font)
        self.MinD_max.setObjectName("MinD_max")
        self.MinD_red_Layout.addWidget(self.MinD_max)
        self.verticalLayout.addLayout(self.MinD_red_Layout)
        self.Par11_Layout = QtWidgets.QHBoxLayout()
        self.Par11_Layout.setObjectName("Par11_Layout")
        self.Par1_text = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Par1_text.setFont(font)
        self.Par1_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Par1_text.setObjectName("Par1_text")
        self.Par11_Layout.addWidget(self.Par1_text)
        self.Par1_count = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Par1_count.setFont(font)
        self.Par1_count.setObjectName("Par1_count")
        self.Par11_Layout.addWidget(self.Par1_count)
        self.verticalLayout.addLayout(self.Par11_Layout)
        self.Par1_red_Layout = QtWidgets.QHBoxLayout()
        self.Par1_red_Layout.setObjectName("Par1_red_Layout")
        self.Par1_min = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Par1_min.setFont(font)
        self.Par1_min.setObjectName("Par1_min")
        self.Par1_red_Layout.addWidget(self.Par1_min)
        self.Par1_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.Par1_slider.setMaximum(29)
        self.Par1_slider.setMinimum(1)
        self.Par1_slider.setPageStep(1)
        self.Par1_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.Par1_slider.setObjectName("Par1_slider")
        self.Par1_red_Layout.addWidget(self.Par1_slider)
        self.Par1_max = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Par1_max.setFont(font)
        self.Par1_max.setObjectName("Par1_max")
        self.Par1_red_Layout.addWidget(self.Par1_max)
        self.verticalLayout.addLayout(self.Par1_red_Layout)
        self.Par2_Layout = QtWidgets.QHBoxLayout()
        self.Par2_Layout.setObjectName("Par2_Layout")
        self.Par2_text = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Par2_text.setFont(font)
        self.Par2_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Par2_text.setObjectName("Par2_text")
        self.Par2_Layout.addWidget(self.Par2_text)
        self.Par2_count = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Par2_count.setFont(font)
        self.Par2_count.setObjectName("Par2_count")
        self.Par2_Layout.addWidget(self.Par2_count)
        self.verticalLayout.addLayout(self.Par2_Layout)
        self.Par2_red_Layout = QtWidgets.QHBoxLayout()
        self.Par2_red_Layout.setObjectName("Par2_red_Layout")
        self.Par2_min = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Par2_min.setFont(font)
        self.Par2_min.setObjectName("Par2_min")
        self.Par2_red_Layout.addWidget(self.Par2_min)
        self.Par2_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.Par2_slider.setMaximum(500)
        self.Par2_slider.setMinimum(1)
        self.Par2_slider.setPageStep(1)
        self.Par2_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.Par2_slider.setObjectName("Par2_slider")
        self.Par2_red_Layout.addWidget(self.Par2_slider)
        self.Par2_max = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Par2_max.setFont(font)
        self.Par2_max.setObjectName("Par2_max")
        self.Par2_red_Layout.addWidget(self.Par2_max)
        self.verticalLayout.addLayout(self.Par2_red_Layout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PhotoButt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.PhotoButt.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.PhotoButt.setFont(font)
        self.PhotoButt.setObjectName("PhotoButt")
        self.horizontalLayout_2.addWidget(self.PhotoButt)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 3, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 0, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.photo_text = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.photo_text.setFont(font)
        self.photo_text.setObjectName("photo_text")
        self.horizontalLayout.addWidget(self.photo_text)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.photo = QtWidgets.QLabel(parent=self.centralwidget)
        self.photo.setObjectName("photo")
        self.verticalLayout_4.addWidget(self.photo)
        self.verticalLayout_4.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 4, 1, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #A function that sets labels on Ui elements
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.vid_text.setText(_translate("MainWindow", "Вид с вебки"))
        self.vid_video.setText(_translate("MainWindow", "TextLabel"))
        self.MinR_text.setAccessibleDescription(_translate("MainWindow", "0"))
        self.MinR_text.setText(_translate("MainWindow", "MinR:"))
        self.MinR_count.setText(_translate("MainWindow", "1"))
        self.MinR_min.setText(_translate("MainWindow", "1"))
        self.MinR_max.setText(_translate("MainWindow", "500"))
        self.MaxR_text.setText(_translate("MainWindow", "MaxR:"))
        self.MaxR_count.setText(_translate("MainWindow", "1"))
        self.MaxR_min.setText(_translate("MainWindow", "1"))
        self.MaxR_max.setText(_translate("MainWindow", "500"))
        self.MinD_text.setText(_translate("MainWindow", "MinD:"))
        self.MinD_count.setText(_translate("MainWindow", "1"))
        self.MinD_min.setText(_translate("MainWindow", "1"))
        self.MinD_max.setText(_translate("MainWindow", "500"))
        self.Par1_text.setText(_translate("MainWindow", "Par1:"))
        self.Par1_count.setText(_translate("MainWindow", "1"))
        self.Par1_min.setText(_translate("MainWindow", "1"))
        self.Par1_max.setText(_translate("MainWindow", "29"))
        self.Par2_text.setText(_translate("MainWindow", "Par2:"))
        self.Par2_count.setText(_translate("MainWindow", "1"))
        self.Par2_min.setText(_translate("MainWindow", "1"))
        self.Par2_max.setText(_translate("MainWindow", "500"))
        self.PhotoButt.setText(_translate("MainWindow", "Фото"))
        self.pushButton.setText(_translate("MainWindow", "Обработка"))
        self.photo_text.setText(_translate("MainWindow", "Обнаруженно предметов:"))
        self.photo.setText(_translate("MainWindow", "TextLabel"))
        # Ф-я привязки к действий к кнопкам и ползункам
        self.con()

    # A function for binding actions to buttons and sliders
    def con(self):

        self.photo_ = circle_find.Photo()

        global photo

        photo = self.photo

        minD = self.MinD_slider.value()
        minR = self.MinR_slider.value()
        par1 = self.Par1_slider.value()
        par2 = self.Par2_slider.value()
        maxR = self.MaxR_slider.value()

        #Linking to function sliders
        self.Par2_slider.valueChanged.connect(lambda: [self.ren(self.Par2_count,self.Par2_slider),self.her()])
        self.Par1_slider.valueChanged.connect(lambda: [self.ren(self.Par1_count,self.Par1_slider),self.her()])
        self.MaxR_slider.valueChanged.connect(lambda: [self.ren(self.MaxR_count,self.MaxR_slider),self.her()])
        self.MinR_slider.valueChanged.connect(lambda: [self.ren(self.MinR_count,self.MinR_slider),self.her()])
        self.MinD_slider.valueChanged.connect(lambda: [self.ren(self.MinD_count,self.MinD_slider),self.her()])

        #Привязка функций к кнопка для снимка
        self.PhotoButt.clicked.connect(lambda: self.photo_.TakePhoto(self.photo))

        #Linking functions to the snapshot button
        self.pushButton.clicked.connect(lambda: self.test(self.MinR_slider,self.MaxR_slider,
            self.Par1_slider,self.Par2_slider,self.MinD_slider))

        #Creating a stream that will take images from the camera and install them in the window
        self.thread = circle_find.ThreadOpenCV()                                      # +++    
        self.thread.changePixmap.connect(self.setImage)                   # +++
        self.thread.start()


    # The function of assigning slider data to variables
    def her(self):
        global minD
        global minR
        global par1
        global par2
        global maxR
        global photo_text

        minD = self.MinD_slider.value()
        minR = self.MinR_slider.value()
        par1 = self.Par1_slider.value()
        par2 = self.Par2_slider.value()
        maxR = self.MaxR_slider.value()
        photo_text = self.photo_text

    #Installing images from the camera
    def setImage(self, image):                                            # +++
        self.vid_video.setPixmap(QtGui.QPixmap.fromImage(image))  

    #The function of setting the slider value as text
    def ren(self,ob,sl):
        _translate = QtCore.QCoreApplication.translate
        ob.setText(_translate("MainWindow", str(sl.value())))

    #Starting photo processing in the stream so that the program does not freeze
    def test(self,minR,maxR,par1,par2,minD):
        self.a = test2(minR,maxR,par1,par2,minD)
        if self.a.isRunning() == False:
            self.a.start()


#A class for processing photos
class test2(QThread):
    
    def __init__(self,minR,maxR,par1,par2,minD):
        super().__init__()
        self.minD = minD
        self.minR =minR
        self.par1 = par1
        self.par2 = par2
        self.maxR = maxR

    #processing photos
    def run(self):
        global minD
        global minR
        global par1
        global par2
        global maxR  
        global photo   
        global photo_text    

        import cv2
        import numpy as np
        while True:
            #Load photos
            img = cv2.imread('photo.jpg')

            try:
                #BGR --> GRAY
                gray_img = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
                img_ = cv2.medianBlur(gray_img.copy(), 5)
                try:
                    #We do a circle search using opencv2
                    circles = cv2.HoughCircles(img_.copy(),cv2.HOUGH_GRADIENT,1,minD,
                        param1=par2,param2=par1,minRadius=minR,maxRadius=maxR)
                    _translate = QtCore.QCoreApplication.translate
                    #Output the number of circles in the image
                    photo_text.setText(_translate("MainWindow", f"Обнаруженно предметов: {len(circles[0,:])}"))
                except Exception as E:
                    circles = None
                #If the circles are found, draw them in the photo
                if circles is not None:
                    circles_ = np.uint16(np.around(circles.copy()))
                    for i in circles_[0,:]:
                        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
                        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
                    #Installing a photo in a window
                    circle_find.Photo().SetPhoto(img,photo)
            except Exception as E:
                print(E)
                pass

#Run program
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
