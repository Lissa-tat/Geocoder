import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPalette, QColor
from layout_colorwidget import Color
from PySide6.QtWidgets import QVBoxLayout 
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QListWidget


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



# TODO
# 1. Сделать виджет справа MapWidget
# 2. Убрать цветастые хуйни из левой панели
# 3. Добавить список в левую панель ниже QLlineEdit (Список это тоже базовый виджет типо QLineEdit. Называется QListWidget)

# Дополнительно.
# 1. Сделать так что бы при запуске приложения оно сразу открывалось в полном окне


class LeftPannel(QWidget):
   
    def __init__(self):
        super(LeftPannel, self).__init__()
        
        self.setFixedWidth(224)
        layout2 = QVBoxLayout()
       
        layout2.addWidget(QLineEdit())


        # Задача 2
        # Задача 3

        # layout2.addWidget(Color('red'))
        listwidget = QListWidget()
        layout2.addWidget(listwidget)
        listwidget.addItems(["One", "Two", "Three"])
        # layout2.addWidget(Color('yellow'))
        listwidget.currentTextChanged.connect(self.text_changed)

        self.setLayout(layout2)

      
    def text_changed(self, text):  # text is a str
        print(text)
        

        

# Задача 1
class MapWidget(QWidget):
    def __init__(self):
        super(MapWidget, self).__init__()
        
        layout3 = QHBoxLayout()
      
        layout3.addWidget(Color('green'))
        self.setLayout(layout3)




class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        widget = Color("red")
        self.setCentralWidget(widget)


        layout1 = QHBoxLayout()
        # layout1.addLayout( layout2 )
        layout1.addWidget( LeftPannel() )


        layout1.addWidget(MapWidget())
      

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()