# Imports
import pygame

from tower import Tower
from poisonprojectile import PoisonProjectile

# Static variables
CLOCK = 1
COOLDOWN = 75
RANGE = 150

### SUBCLASS INHERITING FROM THE TOWER CLASS TO IMPLEMENT THE POISON TOWER ###
class PoisonTower(Tower):
    def __init__(self, engine, image, x, y):
        super().__init__(engine, image, x, y)
        
        self.circle = pygame.Surface((1200, 800), pygame.SRCALPHA)
        self.circle_rect = pygame.draw.circle(self.circle, (255, 0, 0, 100), (self.x, self.y), RANGE)
    
    # Returns a circular Rect object defined by the range of the tower 
    def get_circle_rect(self):
        return self.circle_rect
    
    # Fires a Projectile object at a given enemy     
    def fire(self, enemy):
        self.cooldown_tracker += CLOCK
        if self.cooldown_tracker > COOLDOWN:
            self.cooldown_tracker = 0

        if self.cooldown_tracker == 10:
            projectile = PoisonProjectile(enemy, self.x, self.y, "assets/poison_projectile.png")
            self.engine.add_projectile(projectile)