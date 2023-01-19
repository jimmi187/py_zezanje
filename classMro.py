class Baza:
    def greet(self): pass

class Plivajuce(Baza):
    def __init__(self, name):
        self.name=name
    
    def swim(self):
        return "{} im swimming".format(self.name)
        
    def greet(self):
        super().greet()
        return("im {} of sea".format(self.name))

class Zemljane(Baza):
    def __init__(self, name):
        self.name=name
    
    def walk(self):
        return "{} im walking".format(self.name)
        
    def greet(self):
        super().greet()
        return ("im {} of land".format(self.name))


class Penguin(Zemljane, Plivajuce):
    def __init__(self, name):
        super().__init__( name = name)
    
    def greet(self):
        
        return(super().greet())




n = Penguin("djura")
print(n.greet())