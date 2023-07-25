class Entity:

    def __init__(self) -> None:
        self.name = ""

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name