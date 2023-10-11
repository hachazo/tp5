import sqlite3

class Tabla:
    def creartabla(self):
        conn = sqlite3.connect('usuarios.db')
        conn.execute('''CREATE TABLE usuarios
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    usuario TEXT NOT NULL,
                    contraseña TEXT NOT NULL);''')
        conn.commit()
        conn.close()
        
class Persona:
    def __init__(self,id,nombre,usuario,contraseña):
        self._id = id
        self._nombre = nombre
        self._usuario = usuario
        self._contraseña = contraseña
    
    def mostrarnombre(self):
        return self._nombre
    
    def mostrarusuario(self):
        return self._usuario
    
    def mostrarcontraseña(self):
        return self._contraseña
    
    #def __str__(self):
    #      return f"User(id={self._id}, nombre={self._nombre}, usuario={self._usuario}, contraseña={self._contraseña})"

class PersonaDao:
    def __init__(self):
        self._conn = sqlite3.connect('usuarios.db')
        self._cursor = self._conn.cursor()
    
    def crear(self,persona):
        self._cursor.execute("INSERT INTO usuarios (nombre, usuario, contraseña) VALUES (?,?,?)",(persona._nombre,persona._usuario,persona._contraseña)) 
        self._conn.commit()
        
    def leer(self,id):
        self._cursor.execute("SELECT * FROM usuarios WHERE id=?",(id,))
        row = self._cursor.fetchone()
        return Persona(row[0],row[1],row[2],row[3])
        
    def actualizar(self,persona):
        self._cursor.execute("UPDATE usuarios SET nombre=?, usuario=?, contraseña=? WHERE id=?",(persona._nombre,persona._usuario,persona._contraseña,persona._id))
        self._conn.commit()
    
    def borrado(self,id):
        self._cursor.execute("DELETE FROM usuarios WHERE id=?",(id,))
        self._conn.commit()
    
    #def __del__(self):
        self._conn.close()


tabla1 = Tabla()
tabla1.creartabla()
     
usuarioDao = PersonaDao()
usuarionuevo = Persona(1,"lucia","lucia123","1234")
#usuarioDao.crear(usuarionuevo)
usuario_leido = usuarioDao.leer(1)
print(usuario_leido.mostrarnombre())
print(usuario_leido.mostrarusuario())