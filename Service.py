from baseTarea import BaseTareas
from tarea import Tarea

class Service():

    def __init__(self) -> None:    
        self.baseTareas = BaseTareas()
        self.listaBaseTareas = self.baseTareas.mostrarTodo()

    def getTareas(self):
        listaTareas = []
        for tarea in self.listaBaseTareas:
            nuevaTarea = Tarea(tarea[0],tarea[1],tarea[2],True,tarea[3])
            listaTareas.append(nuevaTarea)
        return listaTareas


if __name__ == "__main__":
    miServicio = Service()
    print(miServicio.getTareas()[0].getTitulo())