from email.charset import QP
from PySide6.QtWidgets import QApplication, QMainWindow, QFormLayout, QLabel,QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QGroupBox, QTabWidget, QGridLayout, QScrollArea, QFrame
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QRect

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

        self.setFixedSize(400,550
        )
        centralWidget = QWidget()
        centralWidget.setLayout(self.layout)
        self.setCentralWidget(centralWidget)

#Prueba
class TabTareasPendientes(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        self.initTab()
        self.scrollAreaTasks()

    def initTab(self):
        button_layout = QHBoxLayout()
        self.layout = QVBoxLayout()
        self.layout.addLayout(button_layout)
        
        
        buttonAdd = QPushButton("Agregar tarea")
        buttonAdd.setFont(QFont("Dosis",10))

        buttonDel = QPushButton("Eliminar tarea")
        buttonDel.setFont(QFont("Dosis",10))
        

        button_layout.addWidget(buttonAdd)
        button_layout.addWidget(buttonDel)
    

        centralWidget = QWidget() 
        centralWidget.setLayout(self.layout) 
        self.setCentralWidget(centralWidget)

    def scrollAreaTasks(self):
        tasks_layout = QFormLayout()

        groupBox = QGroupBox("Tareas")
        
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



class TabHistorial(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
  
        self.scroll = QScrollArea()             
        self.widget = QWidget()                 
        self.vbox = QVBoxLayout()               
        for i in range(1,50):
            objeto = QLabel("naxabuxi")
            self.vbox.addWidget(objeto)

        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')



if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
