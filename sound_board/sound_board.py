import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QImage
from playsound import playsound

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Austin Oliver')
        self.backgound = QImage("pix.jpg")
#____________________________________________________________________________________
        vbox_1 = QVBoxLayout()

        count = 0
        btn_ls_1 = []

        lbl_1 = self.lbl = QLabel('Instraments')
        vbox_1.addWidget(lbl_1)

        while (count < 5):
            add_btn = QPushButton(str(count), self)
            add_btn.setStyleSheet("background-color: brown")
            btn_ls_1.append(add_btn)
            vbox_1.addWidget(btn_ls_1[count])

            count = count + 1
#____________________________________________________________________________________
        vbox_2 = QVBoxLayout()

        count = 0
        btn_ls_2 = []

        lbl_2 = self.lbl = QLabel('Everyday')
        vbox_2.addWidget(lbl_2)

        while (count < 5):
            add_btn = QPushButton(str(count), self)
            add_btn.setStyleSheet("background-color: green")
            btn_ls_2.append(add_btn)
            vbox_2.addWidget(btn_ls_2[count])

            count = count + 1
#____________________________________________________________________________________
        vbox_3 = QVBoxLayout()

        count = 0
        btn_ls_3 = []

        lbl_3 = QLabel('Video Games')
        vbox_3.addWidget(lbl_3)

        while (count < 5):
            add_btn = QPushButton(str(count), self)
            add_btn.setStyleSheet("background-color: gold")
            btn_ls_3.append(add_btn)
            vbox_3.addWidget(btn_ls_3[count])

            count = count + 1

#____________________________________________________________________________________
        vbox_4 = QVBoxLayout()

        count = 0
        btn_ls_4 = []
        #lbl_ls_4 = []
        lbl_4 = self.lbl = QLabel('   Funny')
        vbox_4.addWidget(lbl_4)

        while (count < 5):
            add_btn = QPushButton(str(count), self)
            add_btn.setStyleSheet("background-color: blue")
            btn_ls_4.append(add_btn)
            vbox_4.addWidget(btn_ls_4[count])

            count = count + 1

#____________________________________________________________________________________
        btn_ls_1[0].clicked.connect(self.on_cl_v1_1)
        btn_ls_1[1].clicked.connect(self.on_cl_v1_2)
        btn_ls_1[2].clicked.connect(self.on_cl_v1_3)
        btn_ls_1[3].clicked.connect(self.on_cl_v1_4)
        btn_ls_1[4].clicked.connect(self.on_cl_v1_5)

        btn_ls_2[0].clicked.connect(self.on_cl_v2_1)
        btn_ls_2[1].clicked.connect(self.on_cl_v2_2)
        btn_ls_2[2].clicked.connect(self.on_cl_v2_3)
        btn_ls_2[3].clicked.connect(self.on_cl_v2_4)
        btn_ls_2[4].clicked.connect(self.on_cl_v2_5)

        btn_ls_3[0].clicked.connect(self.on_cl_v3_1)
        btn_ls_3[1].clicked.connect(self.on_cl_v3_2)
        btn_ls_3[2].clicked.connect(self.on_cl_v3_3)
        btn_ls_3[3].clicked.connect(self.on_cl_v3_4)
        btn_ls_3[4].clicked.connect(self.on_cl_v3_5)

        btn_ls_4[0].clicked.connect(self.on_cl_v4_1)
        btn_ls_4[1].clicked.connect(self.on_cl_v4_2)
        btn_ls_4[2].clicked.connect(self.on_cl_v4_3)
        btn_ls_4[3].clicked.connect(self.on_cl_v4_4)
        btn_ls_4[4].clicked.connect(self.on_cl_v4_5)
#____________________________________________________________________________________
        hbox = QHBoxLayout()

        hbox.addLayout(vbox_1)
        hbox.addLayout(vbox_2)
        hbox.addLayout(vbox_3)
        hbox.addLayout(vbox_4)

        self.setLayout(hbox)
        self.show()
#____________________________________________________________________________________

    #V_box_1
    @pyqtSlot()
    def on_cl_v1_1(self):
        playsound('sounds/instraments/banjo.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v1_2(self):
        playsound('sounds/instraments/brass.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v1_3(self):
        playsound('sounds/instraments/cymbal.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v1_4(self):
        playsound('sounds/instraments/guitar.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v1_5(self):
        playsound('sounds/instraments/piano.wav')
        # self.lbl_name.setText('Button clicked')

    #V_box_2
    @pyqtSlot()
    def on_cl_v2_1(self):
        playsound('sounds/everyday/mail.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v2_2(self):
        playsound('sounds/everyday/glass.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v2_3(self):
        playsound('sounds/everyday/modem.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v2_4(self):
        playsound('sounds/everyday/paper.mp3')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v2_5(self):
        playsound('sounds/everyday/phone.mp3')
        # self.lbl_name.setText('Button clicked')

    #V_box_3
    @pyqtSlot()
    def on_cl_v3_1(self):
        playsound('sounds/games/clean-up.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v3_2(self):
        playsound('sounds/games/Jump.mp3')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v3_3(self):
        playsound('sounds/games/pac_dies.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v3_4(self):
        playsound('sounds/games/pac_intro.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v3_5(self):
        playsound('sounds/games/ufo_lowpitch.wav')
        # self.lbl_name.setText('Button clicked')

    #V_box_4
    @pyqtSlot()
    def on_cl_v4_1(self):
        playsound('sounds/funny/cork_pop_x.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v4_2(self):
        playsound('sounds/funny/deadcat.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v4_3(self):
        playsound('sounds/funny/floop2_x.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v4_4(self):
        playsound('sounds/funny/Game-Show-Buzzer.wav')
        # self.lbl_name.setText('Button clicked')
    def on_cl_v4_5(self):
        playsound('sounds/funny/hit_with_frying_pan_y.wav')
        # self.lbl_name.setText('Button clicked')

#____________________________________________________________________________________

class Pic_sound(QWidget):
    def __init__(self):
        super().__init__()

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("404.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)

        self.setLayout(hbox)
        self.show()
