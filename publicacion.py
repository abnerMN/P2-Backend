
class Publicacion:
    def __init__(self,id, tipo, categoria, author, url,date):
        self.id=id
        self.tipo=tipo
        self.categoria=categoria
        self.author=author
        self.date=date    
        self.url=url

    def getId(self):
        return self.id

    def getTipo (self):
        return self.tipo
    
    def getCategoria(self):
        return self.categoria
    
    def getAuthor(self):
        return self.author
    
    def getUrl (self):
        return self.url
    
    def getDate (self):
        return self.date
    
    def setTipo (self, tipo):
        self.tipo=tipo
    
    def setCategoria(self, categoria):
        self.categoria=categoria
    
    def setAuthor (self, author):
        self.author=author
    
    def setUrl (self,url):
        self.url=url
