from baseTarea import BaseTareas
from tarea import Tarea
from PySide6.QtWidgets import QApplication, QMainWindow

class Service():

    def __init__(self) -> None:    
        self.baseTareas = BaseTareas()
        self.listaBaseTareas = self.baseTareas.mostrarTodo()

    def getTareas(self):
        return self.baseTareas.mostrarTodo()


if __name__ == "__main__":
    app = QApplication()
    miServicio = Service()
    print(miServicio.getTareas())
    app.exec()