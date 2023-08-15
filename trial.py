# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication,  QLabel
# from PyQt5.QtGui import QPixmap

# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.button = QtWidgets.QPushButton('Switch to Image Window', self)
#         self.button.clicked.connect(self.on_click)
#         self.second_window = SecondWindow(self)

#     def on_click(self):
#         self.second_window.show()  # show the second window

# class SecondWindow(QtWidgets.QMainWindow):
#     def __init__(self, parent = None):
#         super(SecondWindow, self).__init__(parent)
#         self.title = 'Image Window'
#         self.left = 0
#         self.top = 0
#         self.width = 1000
#         self.height = 1000
#         self.label = QLabel(self)
#         self.label.setPixmap(QPixmap('./img/13 reason y'))
#         self.setGeometry(self.left, self.top, self.width, self.height)
#         self.button = QtWidgets.QPushButton('Switch to First Window', self)
#         self.button.clicked.connect(self.on_click)
#         # self.first_window = MainWindow()

#     def on_click(self):
#         self.parent.show()  # show the second window
# def main():
#     app = QApplication([])
#     app.setStyle('Fusion')
#     mainWindow = MainWindow()
#     mainWindow.show()
#     app.exec_()

# if __name__ == '__main__':
#     main()





# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QStyle, QSizePolicy
# from PyQt5.QtCore import QSize

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.title = "App"
#         self.top = 100
#         self.left = 100
#         self.width = 680
#         self.height = 500
#         self.InitUI()

#     def InitUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.top, self.left, self.width, self.height)

#         buttonWindow1 = QPushButton('Window1', self)
#         buttonWindow1.move(100, 100)
#         buttonWindow1.clicked.connect(self.buttonWindow1_onClick)
#         self.lineEdit1 = QLineEdit("Type here what you want to transfer for [Window1].", self)
#         self.lineEdit1.setGeometry(250, 100, 400, 30)

#         buttonWindow2 = QPushButton('Window2', self)
#         buttonWindow2.move(100, 200)
#         buttonWindow2.clicked.connect(self.buttonWindow2_onClick)        
#         self.lineEdit2 = QLineEdit("Type here what you want to transfer for [Window2].", self)
#         self.lineEdit2.setGeometry(250, 200, 400, 30)
#         self.show()

#     def buttonWindow1_onClick(self):
#         self.statusBar().showMessage("Switched to window 1")
#         self.window1 = Window1(self.lineEdit1.text(), self)
#         self.window1.show()
#         self.hide()

#     def buttonWindow2_onClick(self):
#         self.statusBar().showMessage("Switched to window 2")
#         self.window2 = Window2(self.lineEdit2.text(), self)
#         self.window2.show()
#         self.hide()
        
        
# class Window1(QDialog):
#     def __init__(self, value, parent=None):
#         super(Window1, self).__init__(parent)
#         self.setWindowTitle('Window1')
#         self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

#         label1 = QLabel(value)
#         self.button = QPushButton()
#         self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
#         self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
#         self.button.setIconSize(QSize(200, 200))
        
#         layoutV = QVBoxLayout()
#         self.pushButton = QPushButton(self)
#         self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
#         self.pushButton.setText('Click me!')
#         self.pushButton.clicked.connect(self.goMainWindow)
#         layoutV.addWidget(self.pushButton)
        
#         layoutH = QHBoxLayout()
#         layoutH.addWidget(label1)
#         layoutH.addWidget(self.button)
#         layoutV.addLayout(layoutH)
#         self.setLayout(layoutV)

#     def goMainWindow(self):
#         self.parent().show()
#         self.close() 
        
    
# class Window2(QDialog):
#     def __init__(self, value, parent=None):
#         super(Window2, self).__init__(parent)
#         self.setWindowTitle('Window2')
#         self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))

#         label1 = QLabel(value)
#         self.button = QPushButton()
#         self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
#         self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
#         self.button.setIconSize(QSize(200, 200))
        
#         layoutV = QVBoxLayout()
#         self.pushButton = QPushButton(self)
#         self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
#         self.pushButton.setText('Click me!')
#         self.pushButton.clicked.connect(self.goMainWindow)
#         layoutV.addWidget(self.pushButton)
        
#         layoutH = QHBoxLayout()
#         layoutH.addWidget(label1)
#         layoutH.addWidget(self.button)
#         layoutV.addLayout(layoutH)
#         self.setLayout(layoutV)

#     def goMainWindow(self):
#         self.parent().show()
#         self.close()    
        

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MainWindow()
#     sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
class MainWindow(QMainWindow):
    def __init__(self, x, y, grid, title):
        super().__init__()
        self.setGeometry(x, y, 960, 540)
        self.setWindowTitle(title)
        self.grid = grid

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawGrid(event, qp)
        qp.end()

    def drawGrid(self, event, qp):
        size = self.size()
        w = size.width()
        h = size.height()
        for i in range(0, w, w // self.grid):
            qp.setPen(QColor(0, 0, 0))
            qp.drawLine(i, 0, i, h)

        for i in range(0, h, h // self.grid):
            qp.setPen(QColor(0, 0, 0))
            qp.drawLine(0, i, w, i)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    num_rows = 10
    num_cols = 10
    game1 = MainWindow(50, 50, num_rows, "Game 1")
    game1.show()
    game2 = MainWindow(700, 50, num_cols, "Game 2")
    game2.show()
    sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt5.QtGui import QPainter, QColor

# class MainWindow(QMainWindow):
#     def __init__(self, x, y, grid, title, other_window_title):
#         super().__init__()
#         self.setGeometry(x, y, 960, 540)
#         self.setWindowTitle(title)
#         self.grid = grid
#         self.other_window_title = other_window_title
#         self.active = True

#         # Create a button to switch to the other window
#         self.switch_button = QPushButton('Switch to ' + self.other_window_title, self)
#         self.switch_button.setGeometry(10, 10, 150, 30)
#         self.switch_button.clicked.connect(self.switch_to_other_window)

#     def paintEvent(self, event):
#         qp = QPainter()
#         qp.begin(self)
#         self.drawGrid(event, qp)
#         qp.end()

#     def drawGrid(self, event, qp):
#         size = self.size()
#         w = size.width()
#         h = size.height()
#         if self.active:
#             qp.setBrush(QColor(255, 255, 255))  # Set background color to white if active
#         else:
#             qp.setBrush(QColor(200, 200, 200))  # Set background color to gray if passive
#         qp.drawRect(0, 0, w, h)

#         for i in range(0, w, w // self.grid):
#             qp.setPen(QColor(0, 0, 0))
#             qp.drawLine(i, 0, i, h)

#         for i in range(0, h, h // self.grid):
#             qp.setPen(QColor(0, 0, 0))
#             qp.drawLine(0, i, w, i)
#     def update(self):
#         size = self.size()
#         qp = QPainter()
#         qp.begin(self)
#         # self.drawGrid(event, qp)
#         # qp.end()
#         w = size.width()
#         h = size.height()
#         if self.active:
#             qp.setBrush(QColor(255, 255, 255))  # Set background color to white if active
#         else:
#             qp.setBrush(QColor(200, 200, 200))  # Set background color to gray if passive
#         qp.drawRect(0, 0, w, h)
#         qp.end()
#     def switch_to_other_window(self):
#         self.active = not self.active  # Toggle the active state
#         self.update()  # Redraw the window to reflect the new background color
#         # self.hide()
#         self.active = not self.active
#         self.other_window.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     num_rows = 10
#     num_cols = 10

#     game1 = MainWindow(50, 50, num_rows, "Game 1", "Game 2")
#     game2 = MainWindow(700, 50, num_cols, "Game 2", "Game 1")

#     # Set the other_window attribute for each window
#     game1.other_window = game2
#     game2.other_window = game1

#     game1.show()
#     sys.exit(app.exec_())