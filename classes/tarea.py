from dataclasses import dataclass

from PySide6.QtWidgets import QWidget,QCalendarWidget, QHBoxLayout, QVBoxLayout, QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QDateEdit, QTimeEdit
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import QTime
from database.baseTarea import BaseTareas

@dataclass
class Tarea(QWidget):
    titulo: str
    hora: str
    fecha: str
    id: int = 1
    visible: int = 0
    estado: int = 0

    def __post_init__(self):
        super().__init__()
        self.layout = layout = QHBoxLayout()
        self.base=BaseTareas()
        
        self.descripcion = descripcion = DescripcionTarea(self.titulo, self.hora, self.fecha)
        layout.addWidget(descripcion)

        #Creacion del boton para completar una tarea
        self.botonCompletar = botonCompletar = QPushButton("✓")
        botonCompletar.setFixedSize(30, 30)
        botonCompletar.setStyleSheet("background-color: green; color: white;font-weight:700;")
        layout.addWidget(botonCompletar)
        botonCompletar.clicked.connect(self.switchEstado)

        #Creacion del boton para cancelar una tarea
        self.botonCancelar = botonCancelar = QPushButton("X")
        botonCancelar.setFixedSize(30, 30)
        botonCancelar.setStyleSheet("background-color: maroon; color: white;font-weight:700;")
        layout.addWidget(botonCancelar)
        botonCancelar.clicked.connect(self.switchVisible)

        #Seteo de color de fondo por tarea
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(248, 249, 249))
        self.setPalette(p)
    
        self.setLayout(self.layout)
    
    def setTitulo(self,t):
        self.titulo = t

    def setHora(self,h):
        self.hora = h
    
    def setFecha(self,f):
        self.fecha = f

    #Funcion utilizada para marcar una tarea como incompleta
    #Updateo la base de datos y elimino el widget para que no aparezca en el programa principal
    def switchVisible(self):
        self.visible = not self.visible
        self.base.cancelTask(self.id)
        self.deleteLater()

    #Funcion utilizada para marcar una tarea como completa
    #Updateo la base de datos y elimino el widget para que no aparezca en el programa principal
    def switchEstado(self):
        self.estado = not self.estado
        self.base.completeTask(self.id)
        self.deleteLater()

    def getTitulo(self):
        return self.titulo

    def getHora(self):
        return self.hora
    
    def getFecha(self):
        return self.fecha

    def getEstado(self):
        return self.estado
    
    def getVisible(self):
        return self.visible

    #Función utilizada para elimina los botones antes de meterlos al historial de tareas
    def destruirBotones(self):
        self.botonCancelar.deleteLater()
        self.botonCompletar.deleteLater()

        self.botonRepetir = botonRepetir = QPushButton("♻️")
        botonRepetir.setFixedSize(30, 30)
        botonRepetir.setStyleSheet("color: red; font-weight:700;")
        self.layout.addWidget(botonRepetir)
        botonRepetir.clicked.connect(self.repetirTarea)

        self.botonBorrar = botonBorrar = QPushButton("❌")
        botonBorrar.setFixedSize(30, 30)
        self.layout.addWidget(self.botonBorrar)
        botonBorrar.clicked.connect(self.deleteTarea)
    
    def deleteTarea(self):
        self.base.delete(self.id)
        self.deleteLater()

    #De repetir la tarea, la original en base a la cual se usó se queda.
    #De terminar la renovada, quedan las dos.
    def repetirTarea(self):
        self.win = interfaceAddTask(self.titulo)
        self.win.show()
        

class interfaceAddTask(QWidget):
    #TODO: meterle el ícono de reciclaje

    def __init__(self, nombre) -> None:
        super().__init__()
        self.nombre = nombre
        self.initInterface()
    
    def initInterface(self):
        self.completado = False
        self.setGeometry(650,300,100,100)
        self.setWindowTitle('Repetir tarea')

        layout = QVBoxLayout()
        form_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()
        layout.addLayout(form_layout)
        layout.addLayout(buttons_layout)


        self.task = QLabel("Tarea a repetir:")
        self.inputTitle = QLabel(self.nombre)
        self.inputTitle.setStyleSheet("font-weight:700;")

        labelDate = QLabel('Seleccione la fecha de la tarea:')
        labelTime= QLabel('Seleccione la hora de la tarea:')
        self.inputDate = QCalendarWidget()
        self.inputTime = QTimeEdit()
        self.inputTime.setTime(QTime(00, 00))
        
        buttonAddDb = QPushButton('Agregar')
        buttonAddDb.clicked.connect(self.addDb)
        buttonCancel = QPushButton('Cancelar')
        buttonCancel.clicked.connect(self.close)

        form_layout.addWidget(self.task)
        form_layout.addWidget(self.inputTitle)
        form_layout.addWidget(labelDate)
        form_layout.addWidget(self.inputDate)
        form_layout.addWidget(labelTime)
        form_layout.addWidget(self.inputTime)       

        buttons_layout.addWidget(buttonAddDb)
        buttons_layout.addWidget(buttonCancel)
        
        self.setLayout(layout)

    def addDb(self):
        self.tareas=BaseTareas()
        self.tareas.insert(self.inputTitle.text(),self.inputTime.text(),self.inputDate.selectedDate().toString("dd/MM/yyyy"))
        self.close()

    def getCompletado(self):
        return self.completado

#Clase para poner la descripcion de la tarea en el widget
@dataclass
class DescripcionTarea(QWidget):
    titulo: str
    hora: str
    fecha: str

    #Funcion que crea y agrega una label solo con un texto. Usada para ahorrar lineas de codigo
    def addLabel(self, texto, fuente, tamano):
        label = QLabel(texto)
        label.setFont(QFont(fuente, tamano))
        self.layout.addWidget(label)

    def __post_init__(self):
        super().__init__()
        self.layout = layout = QVBoxLayout()
        self.addLabel(self.titulo, "Lucida Bright", 10)
        tiempo = f"A las {self.hora} el día {self.fecha}"
        self.addLabel(tiempo, "Franklin Gothic", 8)
        
        self.setLayout(layout)
