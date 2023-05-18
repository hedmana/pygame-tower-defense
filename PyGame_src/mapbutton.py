# Imports
import pygame

### CLASS RESPONSIBLE FOR MAP BUTTON FUNCTIONALITY ###
class MapButton:
    def __init__(self, engine, x, y):
        self.engine = engine
        self.image = pygame.transform.scale(pygame.image.load("assets/grass.png").convert_alpha(), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.type = 0
    
    # Draws the map button in it's current state depending on how many times it has been clicked  
    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mouse_pos):
            if not self.engine.is_clicked():
                self.engine.click()
                if pygame.mouse.get_pressed()[0] == 1 and self.type == 0:
                    self.image = pygame.transform.scale(pygame.image.load("assets/road.png").convert_alpha(), (100, 100))
                    self.start_bool = False
                    self.end_bool = False
                    self.type += 1
                elif pygame.mouse.get_pressed()[0] == 1 and self.type == 1:
                    self.image = pygame.transform.scale(pygame.image.load("assets/start.png").convert_alpha(), (100, 100))
                    self.start_bool = True
                    self.end_bool = False
                    self.type += 1
                elif pygame.mouse.get_pressed()[0] == 1 and self.type == 2:
                    self.image = pygame.transform.scale(pygame.image.load("assets/end.png").convert_alpha(), (100, 100))
                    self.start_bool = False
                    self.end_bool = True
                    self.type += 1
                elif pygame.mouse.get_pressed()[0] == 1 and self.type == 3:
                    self.image = pygame.transform.scale(pygame.image.load("assets/grass.png").convert_alpha(), (100, 100))
                    self.start_bool = False
                    self.end_bool = False
                    self.type = 0
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.engine.unclick()
                
        surface.blit(self.image, (self.rect.x, self.rect.y))
    
    # Returns the type of the map button
    def get_type(self):
        return self.type