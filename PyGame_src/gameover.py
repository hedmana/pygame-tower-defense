# Imports 
import pygame

import game
from button import Button

### CLASS RESPONSIBLE FOR DRAWING THE GAME OVER FRAME ###
class GameOver:
    def __init__(self, surface, engine):
        self.surface = surface
        self.engine = engine

        quit_img = pygame.image.load("assets/quit_button.png").convert_alpha() 
        self.quit_button = Button(self.engine, game.SCREEN_WIDTH/2, game.SCREEN_HEIGHT/2 + 50, quit_img, 0.25)
        
    def draw(self):
        self.surface.fill(game.BACKGROUND_COL)
        
        text = game.FONT_1.render("GAME OVER :(", True, game.TEXT_COL)
        text_rect = text.get_rect(center=(game.SCREEN_WIDTH/2, game.SCREEN_HEIGHT/2 - 100))
        self.surface.blit(text, text_rect)

        if self.quit_button.draw(self.surface):
            self.engine.set_state(game.GameState.MAIN_MENU)