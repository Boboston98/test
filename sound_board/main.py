from PIL import Image
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from playsound import playsound
import sound_board as sb

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Austin Oliver')
        self.mainmenu()

    def mainmenu(self):
        self.setWindowTitle('Austin Oliver')
        vbox = QVBoxLayout()

        self.btn_board = QPushButton('Soundboard')
        self.btn_pictures = QPushButton('Pictures to Sound (Not working)')
        #self.btn_credits = QPushButton('Credits')

        vbox.addWidget(self.btn_board)
        vbox.addWidget(self.btn_pictures)
        #vbox.addWidget(self.btn_credits)

        self.setLayout(vbox)
        self.resize(500,200)
        self.show()

        self.btn_board.clicked.connect(self.open_sound)
        self.btn_pictures.clicked.connect(self.open_pic)
        # self.btn_board.clicked.connect(self.open_cred)

    def open_sound(self):
        self.newWindow = sb.Example()

    def open_pic(self):
        self.newWindow = sb.Pic_sound()

    # def open_cred(self):
    #     self.newWindow =

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
