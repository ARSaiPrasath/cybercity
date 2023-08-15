from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class FirstScreen(QWidget):
    def __init__(self, parent=None):
        super(FirstScreen, self).__init__(parent)
        self.button = QPushButton('Go to Second Screen')
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

class SecondScreen(QWidget):
    def __init__(self, parent=None):
        super(SecondScreen, self).__init__(parent)
        self.button = QPushButton('Go to First Screen')
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

class MainApp(QApplication):
    def __init__(self, args):
        super(MainApp, self).__init__(args)
        self.first_screen = FirstScreen()
        self.second_screen = SecondScreen()
        self.first_screen.button.clicked.connect(self.go_to_second_screen)
        self.second_screen.button.clicked.connect(self.go_to_first_screen)
        self.first_screen.show()

    def go_to_second_screen(self):
        self.first_screen.hide()
        self.second_screen.show()

    def go_to_first_screen(self):
        self.second_screen.hide()
        self.first_screen.show()

if __name__ == '__main__':
    app = MainApp([])
    app.exec_()