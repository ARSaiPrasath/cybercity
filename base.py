import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create two instances of the main window
        self.screen1 = QMainWindow()
        self.screen2 = QMainWindow()

        # Set the initial content for each screen
        self.set_content()

    def set_content(self):
        count = 5  # Replace with your count variable

        # Check if the count is even or odd
        if count % 2 == 0:
            # Set image on screen 1 and content on screen 2
            self.screen1.setCentralWidget(QLabel("Image"))
            self.screen2.setCentralWidget(QLabel("Content"))
        else:
            # Set content on screen 1 and image on screen 2
            self.screen1.setCentralWidget(QLabel("Content"))
            self.screen2.setCentralWidget(QLabel("Image"))


app = QApplication(sys.argv)
game = MainWindow()
game.show()