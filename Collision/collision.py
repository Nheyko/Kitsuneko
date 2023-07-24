import pygame

class Collision:

    def __init__(self) -> None:
        self.collider_list = []

    def get_all_collider_objects(self, tmx_data):

        object_layer = tmx_data.get_layer_by_name('objects')
        # print(object_layer)
        
        # Two ways doing the same way but better to use the object layer because more selective.
        for obj in object_layer:
        # for obj in tmx_data.objects:

            # Montre toute les méthodes de obj
            # print(dir(obj))

            # Montre l'attribut class de obj
            # print(obj.type)
            if 'collision' in obj.properties.keys():
                if obj.properties['collision'] == True:

                    # print("Obj.name = ", obj.name)
                    # print("Obj.image = ", obj.image)
                    # print("Obj.x = ", obj.x)
                    # print("Obj.y = ", obj.y)
                    # print("Obj.width = ", obj.width)
                    # print("Obj.height = ", obj.height)
                    
                    # Bounding box of the rectangles
                    # print("Obj.as_points = ", obj.as_points)
                    
                    # Each point of the polygon
                    # print("Obj.points = ", obj.points)
                    
                    # self.collider_list.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                    self.collider_list.append(obj)

        return self.collider_list
    
    def create_collider(x, y, width, height):
        rect = pygame.Rect(x, y, width, height)
        return rect

    def detect_collision(self, characterList, collider_list):
        for character in characterList:
            if character.get_sprite().get_collider().collidelist(collider_list) > -1:
                return True
        pass
            
    def draw_colliders_on_surface(self, map_surface, collider_list):

        for collider in collider_list:
            # print(dir(collider))
            points = [(point.x, point.y) for point in collider.points]
            pygame.draw.polygon(map_surface, 'red', points)

        return map_surface