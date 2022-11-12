import sqlite3

class Database:
    def __init__(self, base, *args) -> None:
        """ Params: Nombre de la base de datos y nombres de los atributos """
        self.base = base
        self.fields = args
        conn = sqlite3.connect(f"{base}.db")
        if len(args) != 0:
            sArgs = ""
            for arg in args: sArgs += arg + ", " 
            self.sArgs = sArgs[:-2]
            print(f'Debugging ######## {self.sArgs=} #########')
            self.params = params = f"('id' integer primary key autoincrement, {self.sArgs})"
            try:
                sql = f"create table {base} {params}"
                #print(sql)
                conn.execute(sql)
                #print(f"Se creó la tabla {base}")                        
            except sqlite3.OperationalError:
                pass
        conn.close()

    def insert(self, *args):
        conn = sqlite3.connect(f"{self.base}.db")
        if self.sArgs.startswith('id'): self.sArgs = self.sArgs[4:]
        sql = f"INSERT INTO {self.base}({self.sArgs}) VALUES {args}"
        print(sql)
        conn.execute(sql)
        conn.commit()
        conn.close()

    def select(self):
        conn = sqlite3.connect(f"{self.base}.db")
        rs = conn.execute(f"SELECT * FROM {self.base}")
        lista = []
        for r in rs: 
            lista.append(r)
        conn.close()
        return lista

    def selectOrderByFecha(self):
        conn = sqlite3.connect(f"{self.base}.db")
        rs = conn.execute(f"SELECT * FROM {self.base} ORDER BY Fecha")
        lista = []
        for r in rs: 
            lista.append(r)
        conn.close()
        return lista
        
    def delete(self, id):
        id = 0 if id=="" else id
        conn = sqlite3.connect(f"{self.base}.db")
        sql = f"DELETE FROM {self.base} WHERE id={id}"
        #print(sql)
        rs = conn.execute(sql)
        conn.commit()
        conn.close()

    def update(self, *args):
        #id = 0 if id=="" else id
        conn = sqlite3.connect(f"{self.base}.db")
        print(self.fields)
        updating = f""
        for f in self.fields:
            updating += f"{f} = ?,"
        updating = updating[:-1]
        id = args[0]
        sql = f"Update {self.base} set {updating} where id = {id}"
        columnValues = args[1:]
        print(f'Debugging ######## {columnValues=} #########')
        conn.execute(sql, columnValues)
        conn.commit()
        conn.close()
    
if __name__ == '__main__':
    alumnos = Database("Persona", "nombre", "fecha_nac")
    alumnos.insert("Juan", "2001-02-02")
    alumnos.insert("Pipo", "1991-02-03")
    alumnos.insert("Luis", "2111-02-04")
    data = alumnos.select()
    print(data)
    id = input("A quien desea borrar? ")
    alumnos.delete(id)
    alumnos.update(2, "Quico", "1987-11-11")
    alumnos.select()


