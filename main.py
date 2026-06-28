import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPalette, QColor
from layout_colorwidget import Color
from PySide6.QtWidgets import QVBoxLayout 
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QListWidget, QPushButton
from PySide6.QtWebEngineWidgets import QWebEngineView

import folium
import io


from geopy.geocoders import Nominatim

from view.map_widget import MapWidget
from view.left_pannel import LeftPannel


from api import API

import json
# Что такое super() ?
# -------------------------------------------------------

# class A():
#     def __init__(self):
#         print("A object is builded!")


# # class C():
# #     def __init__(self):
# #         print("C object is builded!")

# # a = A()

# # -- A object is builded!


# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B object is builded!")


# b = B()

# # -- B object is builded!

# exit()
# -------------------------------------------------------


# View

# TODO I
# 1. Сделать виджет справа MapWidget
# 2. Убрать цветастые хуйни из левой панели
# 3. Добавить список в левую панель ниже QLlineEdit (Список это тоже базовый виджет типо QLineEdit. Называется QListWidget)

# Дополнительно.
# 1. Сделать так что бы при запуске приложения оно сразу открывалось в полном окне


# TODO II
# 1. Сделать метод в классе MapWidget который принимает координаты и меняет местоположение маркера (высавляет переданные координаты)
# 2. Поправить баг с несколькими маркерами
# 3. Сделать функцию, которая устанавливает локацию камеры в нужной точке

   
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        with open('config.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

      
        self.api = API(data['2gis_api_key'])

        self.setWindowTitle("My App")
        widget = Color("red")
        self.setCentralWidget(widget)


        layout1 = QHBoxLayout()
        # layout1.addLayout(layout2)
        layout1.addWidget(LeftPannel(self))
       
        self.map_widget = MapWidget(self.api.get_coordinates('Москва, Садовническая, 25'))
        layout1.addWidget(self.map_widget)
     
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

    def geocode(self, address):
        coordinates = self.api.get_coordinates(address)             
        self.map_widget.set_coordinates(*coordinates)
      


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
# a = Geocoder().location()
# print(a)

