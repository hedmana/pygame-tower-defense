import pygame

### CLASS RESPONSIBLE FOR BUTTON FUNCTIONALITY ###
class Button:
    def __init__(self, engine, x, y, image, scale):
        self.engine = engine
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int((height) * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    # Draws the button object to a given surface and checks for mouse press events
    def draw(self, surface):
        action = False
        mouse_pos = pygame.mouse.get_pos()
        
        # Checks for mouse press events
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.engine.is_clicked():
                self.engine.click()
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.engine.unclick()
            
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
        # Returns True if the button is pressed
        return action
        