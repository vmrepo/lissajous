import sys
import os
import PyQt5.QtWidgets as qt
from PyQt5 import uic, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAggBase as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import json

from lissajousgen import LissajousGenerator,  lissajous_figure


class LissajousWindow(qt.QMainWindow):
    def __init__(self):
        super(LissajousWindow, self).__init__()

        # Загружаем интерфейс из файла
        uic.loadUi("main_window.ui", self)

if __name__ == "__main__":
    # Инициализируем приложение Qt
    app = qt.QApplication(sys.argv)

    # Создаём и настраиваем главное окно
    main_window = LissajousWindow()

    # Показываем окно
    main_window.show()

    # Запуск приложения
    # На этой строке выполнение основной программы блокируется
    # до тех пор, пока пользователь не закроет окно.
    # Вся дальнейшая работа должна вестись либо в отдельных потоках,
    # либо в обработчиках событий Qt.
    sys.exit(app.exec_())
