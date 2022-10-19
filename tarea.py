from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QApplication, QLabel, QPushButton

@dataclass
class Tarea(QWidget):
    titulo: str
    hora: str
    fecha: str
    visible: bool = True
    estado: bool = False

    #Funcion que crea y agrega una label solo con un texto. Usada para ahorrar lineas de codigo
    def addLabel(self, texto):
        label = QLabel(texto)
        self.layout.addWidget(label)

    def __post_init__(self):
        super().__init__()
        self.layout = layout = QHBoxLayout()
        
        #Lista que contiene los elementos importantes a representar, llamados en un ciclo for para imprimir en pantalla
        elementosMostrar = [self.titulo, self.hora, self.fecha]
        for elemento in elementosMostrar:
            self.addLabel(elemento)

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

class DescripcionTarea(QWidget):
    pass
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