from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Progress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.value = 0
        self.width = 200
        self.bar_width = 15
        self.bar_rounded_cap = True
        self.max_value = 100
        self.counter = 0  # Счётчик плавного перехода

        # Вспомогательные переменные
        self.centerPoint = QPoint(self.width // 2, self.width // 2)
        self.textBorders = QRect(0, 0, self.width, self.width)
        self.pieBorders = QRect(self.bar_width * 2, self.bar_width * 2,
                                self.width - self.bar_width * 4, self.width - self.bar_width * 4)

        self.resize(self.width, self.width)

    def set_value(self, value):
        self.value = value
        self.repaint()

    def paintEvent(self, event):
        width = self.width - self.bar_width
        height = self.width - self.bar_width
        margin = self.bar_width // 2
        value = self.value * 360 // self.max_value

        # Painter
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)

        # Параметры кисти
        pen = QPen()
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        pen.setColor(0xf8f9fa)
        pen.setWidth(self.bar_width)
        paint.setPen(pen)

        paint.drawArc(margin, margin, width, height, 90 * 16, -value * 16)

        # Progress bar
        pen.setColor(0x42aaff)
        pen.setWidth(self.bar_width - 5)
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, 90 * 16, -value * 16)

        # Отрисовка фона для текста
        pen.setWidth(2)
        paint.setPen(pen)
        brush = QBrush(0xf8f9fa)
        paint.setBrush(brush)

        if self.value < 100:
            paint.drawPie(self.pieBorders, 90 * 16, -value * 16)
            if self.value < 10:
                width = 20
            else:
                width = 26
            paint.drawEllipse(self.centerPoint, width, width)
            if value > 1:
                pen.setWidth(3)
                pen.setColor(0xf8f9fa)
                paint.setPen(pen)

                circlePosition = self.width // 2 - width
                paint.drawArc(QRect(circlePosition, circlePosition, width * 2, width * 2),
                              (90 - 5) * 16, -(value - 10) * 16)

                pen.setWidth(2)
                pen.setColor(0x42aaff)
                paint.setPen(pen)
            paint.setFont(QFont('Segoe Ui', 12))
        else:
            paint.drawEllipse(self.pieBorders)
            paint.drawRoundedRect(QRect((self.width - 65) // 2 - 5, (self.width - 12) // 2 - 5, 65 + 10, 25), 5.0, 5.0)
            font = QFont('Segoe Ui', 14)
            paint.setFont(font)

        # Отрисовка текста
        pen.setColor(0x42aaff)
        paint.setPen(pen)
        if self.value == 100:
            text = 'Готово!'
        else:
            text = f'{self.value}%'
        paint.drawText(self.textBorders, Qt.AlignCenter, text)

        paint.end()


class Bar(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(500, 500)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Создание основных объектов
        self.container = QFrame()
        self.container.setStyleSheet('background-color: transparent')
        self.layout = QVBoxLayout()

        self.progress = Progress()
        self.progress.setMinimumSize(self.progress.width, self.progress.width)

        # Установка виджетов
        self.layout.addWidget(self.progress, Qt.AlignCenter, Qt.AlignCenter)
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.show()

    def clock(self, window, n, c):
        self.progress.counter = n
        self.timer = QTimer()
        self.timer.start(15)
        self.timer.timeout.connect(lambda: self.smooth_transition(window, c))

    def smooth_transition(self, window, c):
        if self.progress.counter != 0:
            self.progress.set_value(self.progress.value + 1)
            self.progress.counter -= 1
        else:
            self.timer.stop()
            if c == 0:
                window.receiveData()
            elif c == 1:
                window.setData()
            elif c == 2:
                QThread.sleep(1)
                self.close()
                window.show()
                window.resizeTables(0)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    bar = Bar()
    sys.exit(app.exec())
