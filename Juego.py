class Juego:
    def __init__(self,modelo,titulo,precio,status,hashed):
        self.modelo = modelo
        self.titulo = titulo
        self.precio = precio
        self.status = status
        self.hashed = hashed

    def mostrar_juego(self):
        print(f'''
    ================ {self.titulo} ===================
    Modelo --> {self.modelo}  
    Nombre del juego --> {self.titulo}
    Precio de alquiler --> {self.precio}
    Estatus del juego --> {self.status}
    Codigo Hash --> {self.hashed}

    ===================================================  
        ''')