from baseTarea import BaseTareas
from tarea import Tarea
from PySide6.QtWidgets import QApplication, QMainWindow

class Service():

    def __init__(self) -> None:    
        self.baseTareas = BaseTareas()
        self.listaBaseTareas = self.baseTareas.mostrarTodo()

    def getTareas(self):
        listaTareas = []
        for tarea in self.listaBaseTareas:
            nuevaTarea = Tarea(tarea[1],tarea[2],tarea[3])
            listaTareas.append(nuevaTarea)
        return listaTareas


if __name__ == "__main__":
    app = QApplication()
    miServicio = Service()
    print(miServicio.getTareas()[0].getTitulo())
    print(miServicio.getTareas()[0].getHora())
    print(miServicio.getTareas()[0].getFecha())
    print(miServicio.getTareas()[0].getEstado())
    print(miServicio.getTareas()[0].getVisible())
    app.exec()