from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QMainWindow, QApplication, QLabel, QPushButton, QFrame
from PySide6.QtGui import QFont

@dataclass
class Tarea(QWidget):
    titulo: str
    hora: str
    fecha: str
    visible: bool = True
    estado: bool = False

    def __post_init__(self):
        super().__init__()
        self.layout = layout = QHBoxLayout()
        
        self.descripcion = descripcion = DescripcionTarea(self.titulo, self.hora, self.fecha)
        layout.addWidget(descripcion)

        selfbotonCompletar = botonCompletar = QPushButton("✓")
        botonCompletar.setFixedSize(40, 40)
        botonCompletar.setStyleSheet("background-color: green")
        layout.addWidget(botonCompletar)
        botonCompletar.clicked.connect(self.switchEstado)

        selfbotonCancelar = botonCancelar = QPushButton("X")
        botonCancelar.setFixedSize(40, 40)
        botonCancelar.setStyleSheet("background-color: red")
        layout.addWidget(botonCancelar)
        botonCancelar.clicked.connect(self.switchVisible)

        self.setLayout(self.layout)
    
    def setTitulo(self,t):
        self.titulo = t

    def setHora(self,h):
        self.hora = h
    
    def setFecha(self,f):
        self.fecha = f

    def switchVisible(self):
        self.visible = not self.visible

    def switchEstado(self):
        self.estado = not self.estado

    def getTitulo(self):
        return self.titulo

    def getHora(self):
        return self.hora
    
    def getFecha(self):
        return self.fecha

    def getEstado(self):
        return self.estado

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
        self.addLabel(self.titulo, "Lucida Bright", 12)
        tiempo = f"A las {self.hora} el día {self.fecha}"
        self.addLabel(tiempo, "Franklin Gothic", 8)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = layout = QHBoxLayout()
        t = Tarea("Sacar la basura", "16:00", "15/10/2022")
        layout.addWidget(t)

        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        

if __name__ == "__main__":
    app = QApplication()
    t = Tarea("Sacar la basura", "16:00", "15/10/2022")
    window = MainWindow()
    window.show()
    app.exec()