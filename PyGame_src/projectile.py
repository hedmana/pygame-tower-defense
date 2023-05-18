import pygame

### PARENT PROJECTILE CLASS ####
class Projectile:
    def __init__(self, enemy, x, y, image):
        self.enemy = enemy
        img = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(img, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
    
    # Sets a new location for the projectile's Rect object
    def set_rect(self):
        self.rect.center = (self.x, self.y)
    
    # Draws the projectile at it's current location
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
    # Returns the coordinates of the projectile
    def get_coords(self):
        return self.x, self.y
    
    # Returns the enemy object that the projectile is heading towards
    def get_enemy(self):
        return self.enemy
    
    # ABSTRACT METHODS - see description in the inherited class
    def move(self):
        pass
    
    def get_damage(self):
        pass
    