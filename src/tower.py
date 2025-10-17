# Imports
import pygame

### PARENT TOWER CLASS ###
class Tower:
    def __init__(self, engine, image, x, y):
        img = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(img, (100, 100))
        self.rect = self.image.get_rect()
        self.engine = engine
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.cooldown_tracker = 0
        self.clicked = False
    
    # Draws the tower. If the tower is clicked, the range of the tower is drawn as a red circle 
    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.engine.is_clicked() and not self.clicked:
                self.clicked = True
                self.engine.click()
            elif pygame.mouse.get_pressed()[0] == 1 and not self.engine.is_clicked() and self.clicked:
                self.clicked = False
                self.engine.click()
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.engine.unclick()
            
        if self.clicked:    
            surface.blit(self.circle, (0, 0))
        
        surface.blit(self.image, (self.rect.x, self.rect.y))
    
    # Returns the boolean value of self.clicked
    def is_clicked(self):
        return self.clicked
    
    # ABSTRACT METHODS - see descriptions in the inherited classes
    def get_circle_rect(self):
        pass
    
    def fire(self):
        pass
               