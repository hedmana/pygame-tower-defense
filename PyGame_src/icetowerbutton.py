import pygame

from towerbutton import TowerButton

class IceTowerButton(TowerButton):
    def __init__(self, engine, x, y, image, type):
        super().__init__(engine, x, y, image, type)
        
        self.cost = 75
    
    # Draws the tower button and checks for mouse press events    
    def draw(self, surface):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        if self.get_cost() <= self.engine.get_money():
            if self.rect.collidepoint((mouse_x, mouse_y)):
                if pygame.mouse.get_pressed()[0] == 1 and not self.engine.is_clicked() and not self.engine.ice_tower_is_clicked():
                    self.engine.click_ice_tower()
                    self.engine.click()
                    
            if pygame.mouse.get_pressed()[0] == 0:
                self.engine.unclick()
            
            if pygame.mouse.get_pressed()[0] == 1 and not self.engine.is_clicked() and self.engine.ice_tower_is_clicked():
                if self.engine.place_tower(mouse_x, mouse_y, self.type):
                    self.engine.unclick_ice_tower()
                    self.engine.click()
                    
            if pygame.mouse.get_pressed()[0] == 0:
                self.engine.unclick()
                
            if self.engine.ice_tower_is_clicked():
                surface.blit(self.image, (mouse_x - 50, mouse_y - 50))
        
        surface.blit(self.image, (self.rect.x, self.rect.y))