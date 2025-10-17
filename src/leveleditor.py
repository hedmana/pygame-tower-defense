# Imports
import pygame

import game
from button import Button 

### CLASS RESPONSIBLE FOR THE LEVEL EDITOR ### 
class LevelEditor:
    def __init__(self, surface, engine):
        self.surface = surface
        self.engine = engine
        
        self.le_rect = pygame.Rect((0, 0, (self.surface.get_width()// 4) * 3, self.surface.get_height()))
        self.menu_rect = pygame.Rect((self.surface.get_width()// 4) * 3, 0, self.surface.get_width()// 4, self.surface.get_height())

        save_map_img = pygame.image.load("assets/save_map_button.png").convert_alpha()
        self.save_map_button = Button(self.engine, 1400, 300, save_map_img, 0.25)
        quit_img = pygame.image.load("assets/quit_button.png").convert_alpha()
        self.quit_button = Button(self.engine, 1400, 500, quit_img, 0.25)
    
    # Draws the current frame of the level editor and checks for events
    def draw(self):
        self.surface.fill(game.BLACK, self.le_rect)
        self.surface.fill(game.BACKGROUND_COL, self.menu_rect)
        
        self.engine.get_custom_map().draw()
        
        if self.save_map_button.draw(self.surface):
            print("Saving map...")
            self.engine.get_map().read_custom_map()
        
        if self.quit_button.draw(self.surface):
            self.engine.get_custom_map().setup_grid()
            self.engine.set_state(game.GameState.MAIN_MENU)