from dataclasses import dataclass
from winreg import DeleteValue
import PySide6
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QMainWindow, QApplication, QLabel, QPushButton, QFrame
from PySide6.QtGui import QFont, QColor
from baseTarea import BaseTareas

@dataclass
class Tarea(QWidget):
    titulo: str
    hora: str
    fecha: str
    id: int = 0
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
        #ide=self.base.getIdByTitle(self.titulo)
        self.base.cancelTask(self.id)
        self.deleteLater()

    #Funcion utilizada para marcar una tarea como completa
    #Updateo la base de datos y elimino el widget para que no aparezca en el programa principal
    def switchEstado(self):
        self.estado = not self.estado
        #ide=self.base.getIdByTitle(self.titulo)
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

#MainWindow solo es creada para hacer pruebas de la clase, nunca es usada en el programa principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = layout = QHBoxLayout()
        t = Tarea("sos re tonto naza", "16:00", "15/10/2022")
        layout.addWidget(t)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        
        self.setCentralWidget(centralWidget)
        

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()