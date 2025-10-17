# Imports
import pygame

import game
from enemy import Enemy

# Static variables 
FREEZE_TIMER = 50
POISON_TIMER = 150

### SUBCLASS INHERITING FROM THE ENEMY CLASS TO IMPLEMENT THE STEALTH ENEMY ###
class StealthEnemy(Enemy):
    def __init__(self, hp, image, x, y, nodes):
        super().__init__(hp, image, x, y, nodes)
        self.speed = 5
        
    # Sets self.frozen to True to allow the game engine to freeze enemies
    def freeze(self):
        self.frozen = True
        
    # Sets self.frozen to False ONLY IF the freeze timer has timed out
    def unfreeze(self):
        if self.is_frozen() and self.freeze_counter < FREEZE_TIMER:
            self.freeze_counter += 1
        else:
            self.freeze_counter = 0
            self.frozen = False
        
    # Returns the self.frozen variable (boolean)
    def is_frozen(self):
        return self.frozen
    
    # Stealth enemies are immune to poison
    def poison(self):
        pass
    
    def unpoison(self):
        pass

    def is_poisoned(self):
        pass
    
    # Draws the enemy and it's current HP
    def draw(self, surface):
        hp_txt = "hp: {hp}/{max_health}".format(hp=self.hp, max_health=self.max_health)
        text = game.FONT_3.render(hp_txt, True, game.TEXT_COL)
        text_rect = text.get_rect(center=(self.x, self.y - 50))
        surface.blit(text, text_rect)
            
        if self.is_frozen():
            img = pygame.image.load('assets/froze_stealth_enemy.png').convert_alpha()
            img = pygame.transform.scale(img, (100, 100))
            surface.blit(img, (self.rect.x, self.rect.y))
        else:

            surface.blit(self.image, (self.rect.x, self.rect.y))