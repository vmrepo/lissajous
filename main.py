import sys
import os
import PyQt5.QtWidgets as qt
from PyQt5 import uic, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAggBase as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import json

from lissajousgen import LissajousGenerator,  lissajous_figure


# Настройки фигуры по умолчанию
default_settings = {
    "freq_x": 2,
    "freq_y": 3,
    "color": "midnightblue",
    "width": 2
}


# Цвета для matplotlib
mpl_color_dict = {
    "Красный": "crimson",
    "Зелёный": "navy",
    "Жёлтый": "gold",
    "Синий": "midnightblue"
}


class LissajousWindow(qt.QMainWindow):
    def __init__(self):
        super(LissajousWindow, self).__init__()

        # Загружаем интерфейс из файла
        uic.loadUi("main_window.ui", self)

        # Ставим версию и иконку
        self.setWindowTitle("Генератор фигур Лиссажу. Версия 0.1.0. CC BY-SA 4.0 Ivanov")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + "icon.bmp"))

        self.plot_button.clicked.connect(self.plot_button_click_handler)


    def plot_button_click_handler(self):
        """
        Обработчик нажатия на кнопку применения настроек
        """
        print("plot_button_click_handler()")
        self.plot_lissajous_figure()

    def plot_lissajous_figure(self):
        """
        Обновление фигуры
        """
        print("plot_lissajous_figure()")



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
