from dataclasses import dataclass
from PySide6.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QApplication, QLabel, QPushButton

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
        
        tituloWidget = QLabel(self.titulo)
        layout.addWidget(tituloWidget)

        horaWidget = QLabel(self.hora)
        layout.addWidget(horaWidget)
        
        fechaWidget = QLabel(self.fecha)
        layout.addWidget(fechaWidget)

        botonCompletar = QPushButton("✓")
        botonCompletar.setFixedSize(40, 40)
        layout.addWidget(botonCompletar)

        botonCancelar = QPushButton("X")
        botonCancelar.setFixedSize(40, 40)
        layout.addWidget(botonCancelar)

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
        self.Estado = not self.Estado

    def getTitulo(self):
        return self.titulo

    def getHora(self):
        return self.hora
    
    def getFecha(self):
        return self.fecha

    def getEstado(self):
        return self.estado


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