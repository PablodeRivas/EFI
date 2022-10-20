from PySide6.QtWidgets import QApplication, QDateEdit, QTimeEdit, QMainWindow, QFormLayout, QLabel,QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGroupBox, QTabWidget, QGridLayout, QScrollArea, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QRect

from Service import Service
from tarea import Tarea
from baseTarea import BaseTareas

serviceTareas = Service()


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
        self.tasks_layout = QFormLayout()
        
        groupBox = QGroupBox(name)
        groupBox.setLayout(self.tasks_layout)

        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(450)
        self.getTareas()
        self.layout.addWidget(scroll)
    
    def getTareas(self):
        self.limpiarScrollArea()
        objetosTareas= []
        for tarea in serviceTareas.getTareas():
            objetosTareas.append(Tarea(tarea[1],tarea[2],tarea[3]))
            
        for objTar in objetosTareas:
            self.tasks_layout.addWidget(objTar)

    def limpiarScrollArea(self):
        for i in reversed(range(self.tasks_layout.count())): 
            self.tasks_layout.itemAt(i).widget().setParent(None)

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
        buttonRefresh = QPushButton("Refrescar")
        buttonRefresh.clicked.connect(self.getTareas)
        buttonAdd.setFont(QFont("Dosis",10))
        buttonAdd.clicked.connect(self.showAddTask)
        
        button_layout.addWidget(buttonAdd)
        button_layout.addWidget(buttonRefresh)

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
        self.inputTitle = QLineEdit()
        self.inputTitle.setPlaceholderText('Título de tarea')

        labelTime = QLabel('¿Cuándo y a qué hora debes realizar esta tarea?')
        self.inputDate = QDateEdit()
        self.inputTime = QTimeEdit()
        
        buttonAddDb = QPushButton('Agregar')
        buttonAddDb.clicked.connect(self.addDb)
        buttonCancel = QPushButton('Cancelar')
        buttonCancel.clicked.connect(self.close)

        form_layout.addWidget(label)
        form_layout.addWidget(self.inputTitle)
        form_layout.addWidget(labelTime)
        form_layout.addWidget(self.inputDate)
        form_layout.addWidget(self.inputTime)       

        buttons_layout.addWidget(buttonAddDb)
        buttons_layout.addWidget(buttonCancel)
        
        self.setLayout(layout)

    def addDb(self):
        print('debugeado')
        self.tareas=BaseTareas()
        self.tareas.insert(self.inputTitle.text(),self.inputTime.text(),self.inputDate.text())
        self.close()

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
