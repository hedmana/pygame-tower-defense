import pygame

from tower import Tower
from iceprojectile import IceProjectile

CLOCK = 1
COOLDOWN = 75
RANGE = 150

### SUBCLASS INHERITING FROM THE TOWER CLASS TO IMPLEMENT THE ICE TOWER ###
class IceTower(Tower):
    def __init__(self, engine, image, x, y):
        super().__init__(engine, image, x, y)
        
        self.circle = pygame.Surface((1200, 800), pygame.SRCALPHA)
        self.circle_rect = pygame.draw.circle(self.circle, (255, 0, 0, 100), (self.x, self.y), RANGE)
        
    def get_circle_rect(self):
        return self.circle_rect
        
    def fire(self, enemy):
        self.cooldown_tracker += CLOCK
        if self.cooldown_tracker > COOLDOWN:
            self.cooldown_tracker = 0

        if self.cooldown_tracker == 10:
            projectile = IceProjectile(enemy, self.x, self.y, "assets/ice_projectile.png")
            self.engine.add_projectile(projectile)