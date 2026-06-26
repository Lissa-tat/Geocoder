from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout 
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QListWidget, QPushButton


class LeftPannel(QWidget):
   
    def __init__(self):
        super(LeftPannel, self).__init__()
        
        self.setFixedWidth(224)
        layout2 = QVBoxLayout()
       
        layout2.addWidget(QLineEdit())
        # layout2.addWidget(self.line_edit)
        # text = QLineEdit().text()
        # save_button = QPushButton("Сохранить", window)
        # save_button.clicked.connect(QLineEdit().text())
        # print(text)


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
