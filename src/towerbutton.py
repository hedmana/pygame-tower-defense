# Imports
import pygame

### TOWER BUTTON PARENT CLASS ###
class TowerButton:
    def __init__(self, engine, x, y, image, type):
        self.engine = engine
        self.type = type
        self.image = pygame.transform.scale(image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    # Returns the cost of the tower 
    def get_cost(self):
        return self.cost
    
    # ABSTRACT METHOD - see description in the inherited classes   
    def draw(self, surface):
        pass
        