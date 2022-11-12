from PySide6.QtWidgets import QApplication, QTimeEdit, QMainWindow, QFormLayout, QLabel,QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGroupBox, QTabWidget, QCalendarWidget, QScrollArea
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, QSize, QTime

class Functions():
    def scrollArea(self,name):
        self.tasks_layout = QFormLayout()
        
        groupBox = QGroupBox(name)
        groupBox.setLayout(self.tasks_layout)

        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(450)
  
        self.layout.addWidget(scroll)

    def limpiarScrollArea(self):
        for i in reversed(range(self.tasks_layout.count())): 
            self.tasks_layout.itemAt(i).widget().setParent(None)
