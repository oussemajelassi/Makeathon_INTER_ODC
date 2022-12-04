from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5 import QtCore


def func():

    window.total.setText("5")
    window.faulty.setText("5")
    window.temp.setText("5")

    window.total.text()
    window.faulty.text()
    window.temp.text()

def ButtonClicked():
    global CurrentState
    if CurrentState=="Dashboard":
            window.performance.hide()
            window.dashboard.show()
            window.label_7.show()

            window.faulty.hide()
            window.label_10.hide()
            window.label_13.hide()
            window.label_3.hide()
            window.label_4.hide()
            window.label_5.hide()
            window.label_6.hide()
            window.temp.hide()
            window.total.hide()

            CurrentState="Performance"
    elif CurrentState=="Performance":
            window.dashboard.hide()
            window.performance.show()

            window.faulty.show()
            window.label_10.show()
            window.label_13.show()
            window.label_3.show()
            window.label_4.show()
            window.label_5.show()
            window.label_6.show()
            window.label_7.hide()

            window.temp.show()
            window.total.show()

            CurrentState="Dashboard"



if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = loadUi("uiDashboard.ui")
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    window.label_7.hide()
    window.dashboard.hide()
    window.button.clicked.connect(ButtonClicked)

    global CurrentState
    CurrentState="Dashboard"

    timer = QtCore.QTimer()
    timer.setInterval(500)    
    timer.timeout.connect(func)
    #timer.start()
    window.show()

    app.exec_()