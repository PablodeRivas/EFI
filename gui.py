from PySide6.QtWidgets import QApplication, QDateEdit, QTimeEdit, QMainWindow, QFormLayout, QLabel,QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGroupBox, QTabWidget, QGridLayout, QScrollArea, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QRect

from baseTarea import BaseTareas

tareas = BaseTareas.mostrarTodo()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGUI()
        
    def initGUI(self):
        self.layout = QVBoxLayout()
        self.setWindowTitle("Tasky")

        tab = QTabWidget()
        tab.addTab(TabTareasPendientes(),"Tareas pendientes")
        tab.addTab(TabHistorial(),"Historial")
        self.layout.addWidget(tab)

        self.setFixedSize(400,550)
        centralWidget = QWidget()
        centralWidget.setLayout(self.layout)
        self.setCentralWidget(centralWidget)

class Functions():
    def scrollArea(self,name):
        tasks_layout = QFormLayout()
        
        groupBox = QGroupBox(name)
        groupBox.setLayout(tasks_layout)

        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(450)

        for i in range(50):
            frame = QFrame()
            frame.setStyleSheet("background-color: 'lightgreen';margin:4px; min-height:50px;")
            tasks_layout.addRow(frame)

        self.layout.addWidget(scroll)

class TabTareasPendientes(QMainWindow,Functions):
    def __init__(self) -> None:
        super().__init__()
        self.initTab()
        self.scrollArea('Tareas')

    def initTab(self):
        button_layout = QHBoxLayout()
        self.layout = QVBoxLayout()
        self.layout.addLayout(button_layout)
        
        buttonAdd = QPushButton("Agregar tarea")
        buttonAdd.setFont(QFont("Dosis",10))
        buttonAdd.clicked.connect(self.showAddTask)
        
        button_layout.addWidget(buttonAdd)

        centralWidget = QWidget() 
        centralWidget.setLayout(self.layout) 
        self.setCentralWidget(centralWidget)

    def showAddTask(self):
        self.win = interfaceAddTask()
        self.win.show()

class interfaceAddTask(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initInterface()
    
    def initInterface(self):
        self.setGeometry(650,300,100,100)
        self.setWindowTitle('Agregar tarea')

        layout = QVBoxLayout()
        form_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()
        layout.addLayout(form_layout)
        layout.addLayout(buttons_layout)

        label = QLabel("Inserte en los campos los detalles de la tarea")
        inputTitle = QLineEdit()
        inputTitle.setPlaceholderText('Título de tarea')

        labelTime = QLabel('¿Cuándo y a qué hora debes realizar esta tarea?')
        inputDate = QDateEdit()
        inputTime = QTimeEdit()
        
        buttonAdd = QPushButton('Agregar')
        buttonCancel = QPushButton('Cancelar')
        buttonCancel.clicked.connect(self.close)

        form_layout.addWidget(label)
        form_layout.addWidget(inputTitle)
        form_layout.addWidget(labelTime)
        form_layout.addWidget(inputDate)
        form_layout.addWidget(inputTime)       

        buttons_layout.addWidget(buttonAdd)
        buttons_layout.addWidget(buttonCancel)
        
        self.setLayout(layout)

class TabHistorial(QMainWindow, Functions):
    def __init__(self) -> None:
        super().__init__()
        self.initTab()    

    def initTab(self):
        self.layout = QVBoxLayout()
        self.scrollArea('Historial de tareas')

        centralWidget = QWidget() 
        centralWidget.setLayout(self.layout) 
        self.setCentralWidget(centralWidget)  

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
