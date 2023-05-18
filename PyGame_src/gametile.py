# Imports
import pygame

### CLASS RESPONSIBLE FOR IMPLEMENTING GAME TILE FUNCTIONALITY FOR THE MAP TO USE ###
class GameTile:
    def __init__(self, image, x, y, type):
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect = self.image.get_rect()
        self.coords = (x, y)
        self.rect.topleft = (x, y)
        self.type = type
        self.checked = False
    
    # Sets self.checked to True. Used by the path finding algorithm.   
    def set_checked(self):
        self.checked = True

    # Returns the boolean value of self.checked
    def is_checked(self):
        return self.checked
    
    # Returns the coordinates of the game tile    
    def get_coords(self):
        return self.coords
    
    # Returns the Rect object of the game tile
    def get_rect(self):
        return self.rect
    
    # Returns the game tile type. Used to differ between grass, road, start, and finnish.
    def get_type(self):
        return self.type 
    
    # Draws the game tile
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))