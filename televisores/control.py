class Control:

    def __init__(self):
        self.tv = 0

    def enlazar(self, tv):
        self.tv = tv
    
    def setTv(self, tv):
        self.tv = tv

    def getTv(self):
        return self.tv
    
    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp()

    def volumenUp(self):
        self.tv.volumenUp()

    def canalDown(self):
        self.tv.canalDown()

    def volumenDown(self):
        self.tv.volumenDown()