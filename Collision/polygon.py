class Polygon():

    def __init__(self):
        self.polygons = []
    
    def add_polygons_in_objects(self, objects):

        for collider_polygon in objects:
            if collider_polygon.type == 'polygon' :
                self.polygons.append(collider_polygon)

    def get(self):
        return self.polygons