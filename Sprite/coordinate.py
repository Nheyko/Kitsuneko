class Coordinate:

    def __init__(self) -> None:
        
        self.x = 0
        self.y = 0

    def setX(self, newX):
        self.x = newX
    
    def setY(self, newY):
        self.y = newY

    def set_coordinate(self, x , y):
        self.setX(x)
        self.setY(y)

    def x(self):
        return self.x
    
    def y(self):
        return self.y
    
    def get_coordinate(self):
        return [self.x,self.y]