class Usuario:
    def __init__(self, nombre, apellido, genero, username, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.username = username
        self.email = email
        self.password = password

    def getNombre (self):
        return self.nombre
    
    def getApellido (self):
        return self.apellido
    
    def getGenero (self):
        return self.genero
    
    def getUsername (self):
        return self.username
    
    def getEmail (self):
        return self.email
    
    def getPassword (self):
        return self.password
    
    def setNombre (self, nombre):
        self.nombre=nombre
    
    def setApellido (self, apellido):
        self.apellido=apellido
    
    def setGenero (self, genero):
        self.genero=genero
    
    def setUsername (self, username):
        self.username= username
    
    def setEmail (self, email):
        self.email= email
    
    def setPassword (self,password):
        self.password=password
