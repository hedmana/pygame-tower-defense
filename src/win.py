import pygame

import game
from button import Button

### CLASS RESPONSIBLE FOR DRAWING THE WIN FRAME ###
class Win:
    def __init__(self, surface, engine):
        self.surface = surface
        self.engine = engine
        
        quit_img = pygame.image.load("assets/quit_button.png").convert_alpha() 
        self.quit_button = Button(self.engine, game.SCREEN_WIDTH/2, game.SCREEN_HEIGHT/2 + 100, quit_img, 0.25)

    def draw(self):
        self.surface.fill(game.BACKGROUND_COL)
        
        text = game.FONT_1.render("CONGRATULATIONS!", True, game.TEXT_COL)
        text_rect = text.get_rect(center=(game.SCREEN_WIDTH/2, game.SCREEN_HEIGHT/2 - 200))
        self.surface.blit(text, text_rect)
        
        text = game.FONT_1.render("YOU WON :D", True, game.TEXT_COL)
        text_rect = text.get_rect(center=(game.SCREEN_WIDTH/2, game.SCREEN_HEIGHT/2 - 50))
        self.surface.blit(text, text_rect)
        
        if self.quit_button.draw(self.surface):
            self.engine.set_state(game.GameState.MAIN_MENU)