import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen


draw_circles = []


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 650, 550)
        self.clicked = QPushButton("Нажать", self)
        self.clicked.move(275, 450)
        self.clicked.resize(150, 100)
        self.clicked.clicked.connect(self.add_circle)

    def add_circle(self):
        radius = random.randint(10, 150)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        x = random.randint(radius, self.width() - radius)
        y = random.randint(radius, self.height() - radius)
        draw_circles.append((x, y, radius, (red, green, blue)))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in draw_circles:
            x, y, radius, color = circle
            brush = QBrush(QColor(*color))
            painter.setBrush(brush)
            painter.drawEllipse(x - radius, y - radius, 2 * radius, 2 * radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())