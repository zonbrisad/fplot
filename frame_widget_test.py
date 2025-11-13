import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setFixedHeight(40)
        self.setStyleSheet("background: #2c2c2c; color: white;")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 0, 0)

        # App title
        self.title = QLabel("My App")
        self.title.setStyleSheet("font-weight: bold;")
        layout.addWidget(self.title)

        # Spacer to push controls to the right
        layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Custom widgets in title bar
        self.btn_refresh = QPushButton("Refresh")
        self.btn_refresh.setFixedSize(70, 28)
        layout.addWidget(self.btn_refresh)

        self.btn_settings = QPushButton("Settings")
        self.btn_settings.setFixedSize(70, 28)
        layout.addWidget(self.btn_settings)

        # Window control buttons (minimize, maximize, close)
        self.btn_minimize = QPushButton("🗕")
        self.btn_minimize.setFixedSize(30, 30)
        self.btn_minimize.clicked.connect(parent.showMinimized)

        self.btn_maximize = QPushButton("🗖")
        self.btn_maximize.setFixedSize(30, 30)
        self.btn_maximize.clicked.connect(self.toggle_maximize)

        self.btn_close = QPushButton("🗙")
        self.btn_close.setFixedSize(30, 30)
        self.btn_close.clicked.connect(parent.close)

        for btn in (self.btn_minimize, self.btn_maximize, self.btn_close):
            #btn.setStyleSheet(" QPushButton:hover { background: #555; }")
            btn.setStyleSheet("QPushButton { border: none; } QPushButton:hover { background: #555; }")
            layout.addWidget(btn)

    def toggle_maximize(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
            self.btn_maximize.setText("🗖")
        else:
            self.parent.showMaximized()
            self.btn_maximize.setText("🗗")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Title Bar Example")
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove native title bar
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(800, 600)

        # Main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Add custom title bar
        self.title_bar = CustomTitleBar(self)
        main_layout.addWidget(self.title_bar)
        

        # Content area
        content = QLabel("Your app content goes here.\n\nDrag the title bar to move the window.")
        content.setAlignment(Qt.AlignCenter)
        content.setStyleSheet("background: #f0f0f0; padding: 20px;")
        main_layout.addWidget(content)

        # Enable dragging
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.title_bar.underMouse():
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.old_pos is not None:
            delta = event.globalPos() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.old_pos = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())