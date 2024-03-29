from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt-helloworld")

        label = QLabel("Hello World")

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
