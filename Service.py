from baseTarea import BaseTareas
from tarea import Tarea

class Service():

    def __init__(self) -> None:    
        self.baseTareas = BaseTareas()
        self.listaBaseTareas = baseTareas.mostrarTodo()
        self.listaTareas = []

    def getTareas(self):
        for tarea in self.listaBaseTareas:
            nuevaTarea = Tarea(tarea[0],tarea[1],tarea[2],True,tarea[3])
            self.listaTareas.append(nuevaTarea)
