from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from PyQt5.QtCore import Qt
from motion_capture import *
from PyQt5.QtWidgets import QFileDialog


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("uis/FrontPage.ui", self)
        # click logic for button
        self.Camera_btn.clicked.connect(self.capture_live)
        self.BrouseVideo_btn.clicked.connect(self.Browse_File)
        self.PreviousVideo_btn.clicked.connect(self.show_saved_content)
        self.Setting_btn.clicked.connect(self.clicked)

    def capture_live(self):
        # print("clicked")
        motion_capture()


    def Browse_File(self):
        fname,ftype = QFileDialog.getOpenFileName(self, 'Select a video', './','Video (*.mp4 *.avi)')
        motion_capture_video(fname)
        
    def show_saved_content(self):
        #Dialog()
        files = os.listdir('motion_data')
    
    
        
    def clicked(self):
        print("other one")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())