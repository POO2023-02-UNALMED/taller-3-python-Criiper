class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = 0

        self.numTV += 1

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False
    
    def canalUp(self):
        if (self.canal >= 1 and self.canal < 120 and self.estado == True):
            self.canal += 1
    
    def volumenUp(self):
        if (self.volumen >= 0 and self.volumen < 7 and self.estado == True):
            self.volumen += 1
    
    def canalDown(self):
        if (self.canal > 1 and self.canal <= 120 and self.estado == True):
            self.canal -= 1

    def volumenDown(self):
        if (self.volumen > 0 and self.volumen <= 7 and self.estado == True):
            self.volumen -= 1

    def setMarca(self, marca):
        self.marca = marca

    def setCanal(self, canal):
        self.canal = canal
    
    def setVolumen(self, volumen):
        self.volumen = volumen
    
    def setPrecio(self, precio):
        self.precio = precio
    
    def setControl(self, control):
        self.control = control
    
    def getMarca(self):
        return self.marca
    
    def getCanal(self):
        return self.canal
    
    def getVolumen(self):
        return self.volumen
    
    def getPrecio(self):
        return self.precio
    
    def getControl(self):
        return self.control
    
    def getEstado(self):
        return self.estado
    

    @classmethod
    def setNumTV(cls, canttv):
        cls.numTV = canttv

    @classmethod
    def getNumTV(cls):
        return cls.numTV
    
    