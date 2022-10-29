from database import Database


class BaseTareas(Database):
    def __init__(self) -> None:
        super().__init__("Tareas", "Titulo", "Hora", "Fecha", "Completado", "Cancelada")

    def insert(self, *args):
        args = args + (False, False,)
        return super().insert(*args)

    def getEntrada(self, id):
        lista = super().select()
        return lista[id-1]

    def mostrarTodo(self):
        lista=super().select()
        return lista

    def getIdByTitle(self,tituloTarea):
        tupla=super().select()
        for tarea in tupla:
            if tituloTarea==tarea[1]:
                idEncontrada=tarea[0]
                return idEncontrada 
        return "error"
        

    def cancelTask(self,id):
        tupla=self.getEntrada(id)
        tupla=tupla[:-1]
        super().update(*tupla,1)

    def completeTask(self,id):
        tupla=self.getEntrada(id)
        tupla=tupla[:-2]
        super().update(*tupla,1,0)
  
   
if __name__ == '__main__':
    tarea = BaseTareas()
    #tarea.insert("Pasear al perro","10:00","12/10")
    #tarea.insert("Hacer la comida","11:30","12/10")
    #print(tarea.getEntrada(1))
    ide=tarea.getIdByTitle("sos re tonto naza") 
    print(ide)
    print(tarea.getEntrada(ide))
    tarea.cancelTask(ide)
    print(tarea.getEntrada(ide))
    #id = input("Que tarea desea borrar? ")
    #tarea.delete(1)
    #tarea.update(4, "Lavar los platos", "14:30","12/10",False)#al updatear hace falta el Bool
    #tarea.mostrarTodo()