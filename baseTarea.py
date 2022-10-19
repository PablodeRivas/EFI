from database import Database
from tarea import Tarea

class BaseTareas(Database):
    def __init__(self) -> None:
        super().__init__("Tareas", "Titulo", "Hora", "Fecha", "Estado")

    def insert(self, *args):
        args = args + (False,)
        return super().insert(*args)

    def getEntrada(self, id):
        lista = super().select()
        print (lista[id+1])

    def mostrarTodo(self):
        lista=super().select()
        return lista

   
if __name__ == '__main__':
    tarea = BaseTareas()
    # tarea.insert("Pasear al perro","10:00","12/10")
    # tarea.insert("Hacer la comida","11:30","12/10")
    #tarea.getEntrada(0)
    #id = input("Que tarea desea borrar? ")
    #tarea.delete(id)
    #tarea.update(4, "Lavar los platos", "14:30","12/10",False)#al updatear hace falta el Bool
    tarea.mostrarTodo()