import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPalette, QColor
from layout_colorwidget import Color
from PySide6.QtWidgets import QVBoxLayout 
from PySide6.QtWidgets import QHBoxLayout, QLineEdit


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
        
        self.setFixedWidth(111)
        layout2 = QVBoxLayout()
       
        layout2.addWidget(QLineEdit())


        # Задача 2
        # Задача 3

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))

        

        self.setLayout(layout2)


# Задача 1
# class ...


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        widget = Color("red")
        self.setCentralWidget(widget)


        # layout2 = QVBoxLayout()
        # # layout2.setFixedWidth(400)

        # # layout2.addWidget(QLineEdit())
        # layout2.addWidget(Color('red'))
        # layout2.addWidget(Color('yellow'))
        # layout2.addWidget(Color('purple'))

        layout1 = QHBoxLayout()
        # layout1.addLayout( layout2 )
        layout1.addWidget( LeftPannel() )


        # Задача 1
        layout1.addWidget(Color('green'))

        # layout3.addWidget(Color('red'))
        # layout3.addWidget(Color('purple'))

        # layout1.addLayout( layout3 )
        # top_line_edit = QLineEdit(parent=self)
        # layout2.addWidget(top_line_edit)
       
        # self.setLayout(layout)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()