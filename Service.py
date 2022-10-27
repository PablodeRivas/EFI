from baseTarea import BaseTareas
from tarea import Tarea
from PySide6.QtWidgets import QApplication, QMainWindow

class Service():

    def __init__(self) -> None:    
        self.baseTareas = BaseTareas()
        self.listaBaseTareas = self.baseTareas.mostrarTodo()

    def getTareasService(self):
        return self.baseTareas.mostrarTodo()

    def getIdByTitle(self,title):
        self.baseTareas.getIdByTitle(title)
    
    

if __name__ == "__main__":
    app = QApplication()
    miServicio = Service()
    print(miServicio.getTareas())
    app.exec()