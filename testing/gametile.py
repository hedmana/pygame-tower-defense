import pygame

class GameTile:
    def __init__(self, image, x, y, type):
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect = self.image.get_rect()
        self.coords = (x, y)
        self.rect.topleft = (x, y)
        self.type = type
        self.checked = False
        
    def set_checked(self):
        self.checked = True

    def is_checked(self):
        return self.checked
        
    def get_coords(self):
        return self.coords
    
    def get_rect(self):
        return self.rect
    
    def get_type(self):
        return self.type 
    
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))