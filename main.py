from PySide6.QtWidgets import QApplication, QTimeEdit, QMainWindow, QLabel,QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTabWidget, QCalendarWidget
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, QSize, QTime
from classes.functions import Functions
from classes.tarea import Tarea
from database.baseTarea import BaseTareas

bddTareas = BaseTareas()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGUI()
        
    def initGUI(self):
        self.layout = QVBoxLayout()
        self.headerLayout = QHBoxLayout()
        self.tasksLayout= QVBoxLayout()
        
        self.setWindowTitle("Tasky")
        self.setWindowIcon(QIcon('images/icon.png'))

        self.layout.addLayout(self.headerLayout)
        self.layout.addLayout(self.tasksLayout)
        #Esta parte requiere reestructura. Extraer todos los botones y demás.
        #Idealmente, quedarían sólo los:
        # self.<parte_de_la_ventana>.addwidget(<funcion_extraida>, etc)
        self.title = QLabel(" Tasky ©")
        self.title.setStyleSheet("font-size:26px;font-family:Segoe Script;")
        self.headerLayout.addWidget(self.title)

        self.refreshButton = QPushButton("")
        self.refreshButton.setFixedSize(30,30)
        self.refreshButton.clicked.connect(self.refreshAll)
        self.refreshButton.setIcon(QIcon('./images/refresh-ico.png'))
        self.refreshButton.setIconSize(QSize(25,25))
        self.headerLayout.addWidget(self.refreshButton,alignment= Qt.AlignRight)

        self.quitButton = QPushButton("")
        self.quitButton.setFixedSize(40,40)
        self.quitButton.clicked.connect(app.quit)
        self.quitButton.setIcon(QIcon('./images/exit-green-ico.png'))
        self.quitButton.setIconSize(QSize(30,30))
        self.headerLayout.addWidget(self.quitButton)

        tabs = QTabWidget()
        self.TabTareasPendientesObj = TabTareasPendientes()
        self.TabHistorialObj = TabHistorial()
        tabs.currentChanged.connect(self.refreshAll)
        tabs.addTab(self.TabTareasPendientesObj,"Tareas pendientes")
        tabs.addTab(self.TabHistorialObj,"Historial")
        self.tasksLayout.addWidget(tabs)

        self.setFixedSize(400,600)
        centralWidget = QWidget()
        centralWidget.setLayout(self.layout)
        self.setCentralWidget(centralWidget)

    def refreshAll(self):
        self.TabTareasPendientesObj.refreshTareasPendientes()
        self.TabHistorialObj.refreshTabs()


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
        self.win = interfaceAddTask(self)
        self.win.show()

    def refreshTareasPendientes(self):
        self.limpiarScrollArea()
        objetosTareas= []
        for tarea in bddTareas.getTareasOrderByFecha():
            if tarea[4] == 0 and tarea[5] == 0:
                tareaCompleta = Tarea(tarea[1],tarea[2],tarea[3], tarea[0])
                objetosTareas.append(tareaCompleta)

        for objTar in objetosTareas:
            self.tasks_layout.addWidget(objTar)

class interfaceAddTask(QWidget):
    def __init__(self, parent) -> None:
        super().__init__()
        self.parent = parent
        self.initInterface()
    
    def initInterface(self):
        self.completado = False
        self.setGeometry(650,300,100,100)
        self.setWindowTitle('Agregar tarea')

        layout = QVBoxLayout()
        self.form_layout = form_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()
        layout.addLayout(form_layout)
        layout.addLayout(buttons_layout)

        label = QLabel("Inserte el nombre de su tarea:")
        self.inputTitle = QLineEdit()
        self.inputTitle.setPlaceholderText('Título de la tarea')

        labelDate = QLabel('Seleccione la fecha de la tarea:')
        labelTime= QLabel('Seleccione la hora de la tarea:')

        self.inputDate = QCalendarWidget()
        self.inputDate.setGridVisible(True)
        self.inputTime = QTimeEdit()
        self.inputTime.setTime(QTime(00, 00))
        
        buttonAddDb = QPushButton('Agregar')
        buttonAddDb.clicked.connect(self.addDb)
        buttonCancel = QPushButton('Cancelar')
        buttonCancel.clicked.connect(self.close)

        form_layout.addWidget(label)
        form_layout.addWidget(self.inputTitle)
        form_layout.addWidget(labelDate)
        form_layout.addWidget(self.inputDate)
        form_layout.addWidget(labelTime)
        form_layout.addWidget(self.inputTime)       

        buttons_layout.addWidget(buttonAddDb)
        buttons_layout.addWidget(buttonCancel)
        
        self.setLayout(layout)

    def addDb(self):
        if self.inputTitle.text() == "" :
            errorMessage=QLabel('La tarea debe tener título.')
            errorMessage.setStyleSheet("color: red;font-weight:700;")
            if len(self.findChildren(QLabel)) <4:
                self.form_layout.addWidget(errorMessage) 
        else:
            self.tareas=BaseTareas()
            self.tareas.insert(
                self.inputTitle.text(),
                self.inputTime.text(),
                self.inputDate.selectedDate().toString("dd/MM/yyyy"))
            self.parent.refreshTareasPendientes()
            self.close()

    def getCompletado(self):
        return self.completado


class TabHistorial(QMainWindow, Functions):
    def __init__(self) -> None:
        super().__init__()
        self.initTab() 

    def initTab(self):
        self.layout = QVBoxLayout()
        tabs = QTabWidget()

        self.tabCompletasObj = tabCompletas()
        self.tabIncompletasObj = tabIncompletas()
        tabs.addTab(self.tabCompletasObj,"Completas")
        tabs.addTab(self.tabIncompletasObj,"Incompletas")
        self.layout.addWidget(tabs)

        centralWidget = QWidget() 
        centralWidget.setLayout(self.layout) 
        self.setCentralWidget(centralWidget) 
        self.refreshTabs()

    def refreshTabs(self):
        self.tabCompletasObj.getTareasCompletas()
        self.tabIncompletasObj.getTareasIncompletas()


class tabCompletas(QMainWindow, Functions):
    def __init__(self) -> None:
        super().__init__()
        self.initTab()

    def initTab(self):
        self.layout = QVBoxLayout()
        self.scrollArea("")
        self.getTareasCompletas()
        
        centralWidget = QWidget() 
        centralWidget.setLayout(self.layout) 
        self.setCentralWidget(centralWidget)

    def getTareasCompletas(self):
        self.limpiarScrollArea()
        objetosTareas= []
        for tarea in bddTareas.getTareas():
            if tarea[4] == 1 and tarea[5] == 0:
                tareaCompleta = Tarea(tarea[1],tarea[2],tarea[3], tarea[0])
                tareaCompleta.destruirBotones()
                objetosTareas.append(tareaCompleta)
            
        for objTar in objetosTareas:
            self.tasks_layout.addWidget(objTar)
            


class tabIncompletas(QMainWindow,Functions):
    def __init__(self) -> None:
        super().__init__()
        self.initTab()

    def initTab(self):
        self.layout = QVBoxLayout()
        self.scrollArea("")
        self.getTareasIncompletas()

        centralWidget = QWidget() 
        centralWidget.setLayout(self.layout) 
        self.setCentralWidget(centralWidget)

    def getTareasIncompletas(self):
        self.limpiarScrollArea()
        objetosTareas= []
        for tarea in bddTareas.getTareas():
            if tarea[4] == 0 and tarea[5] == 1:
                tareaIncompleta = Tarea(tarea[1],tarea[2],tarea[3], tarea[0])
                tareaIncompleta.destruirBotones()
                objetosTareas.append(tareaIncompleta)
            
        for objTar in objetosTareas:
            self.tasks_layout.addWidget(objTar)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
