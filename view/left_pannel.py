from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout 
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QListWidget, QPushButton, QLabel, QApplication
import sys
from api import API


class LeftPannel(QWidget):
   
    def __init__(self, parent):
        super(LeftPannel, self).__init__()
        
        self._parent = parent
        self.setFixedWidth(224)
        layout2 = QVBoxLayout()
        
        self.input_field = QLineEdit()
        layout2.addWidget(self.input_field)

        self.input_field.returnPressed.connect(self.on_enter_pressed)
        
        self.listwidget = QListWidget()
        layout2.addWidget(self.listwidget)

        self.listwidget.currentTextChanged.connect(self.text_changed)

        self.setLayout(layout2)

      
    def text_changed(self, text):  # text is a str
        print(text)

    def on_enter_pressed(self):
        text = self.input_field.text()
        print(f"Введено: {text}")
        self.input_field.clear()
        self.listwidget.addItem(text)
        self._parent.geocode(text)
        

