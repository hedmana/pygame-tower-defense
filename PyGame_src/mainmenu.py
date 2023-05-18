# Imports
import pygame

import game
from button import Button

### CLASS RESPONSIBLE FOR THE MAIN MENU ###
class MainMenu:
    def __init__(self, surface, engine):
        self.surface = surface
        self.engine = engine
        
        start_img = pygame.image.load("assets/start_button.png").convert_alpha()
        quit_img = pygame.image.load("assets/quit_button.png").convert_alpha()
        le_img = pygame.image.load("assets/le_button.png").convert_alpha() 
        self.start_button = Button(self.engine, game.SCREEN_WIDTH/2, game.SCREEN_HEIGHT/2, start_img, 0.25)
        self.le_button = Button(self.engine, game.SCREEN_WIDTH/2, game.SCREEN_HEIGHT/2 + 125, le_img, 0.25)
        self.quit_button = Button(self.engine, game.SCREEN_WIDTH/2, game.SCREEN_HEIGHT/2 + 250, quit_img, 0.25)
        
    # Draws the current frame of the main menu and checks for events
    def draw(self):
        self.surface.fill(game.BACKGROUND_COL)
        
        text = game.FONT_1.render("Main Menu", True, game.TEXT_COL)
        text_rect = text.get_rect(center=(game.SCREEN_WIDTH/2, game.SCREEN_HEIGHT/2 - 150))
        enemy_img = pygame.image.load("assets/basic_enemy.png").convert_alpha()
        enemy_img = pygame.transform.scale(enemy_img, (400, 400))
        enemy_rect = enemy_img.get_rect()
        enemy_rect.center = (game.SCREEN_WIDTH/5, 500)
        boss_img = pygame.image.load("assets/boss_enemy.png").convert_alpha()
        boss_img = pygame.transform.scale(boss_img, (400, 400))
        boss_rect = boss_img.get_rect()
        boss_rect.center = ((game.SCREEN_WIDTH/5)*4, 500)
    
        self.surface.blit(text, text_rect)
        self.surface.blit(enemy_img, enemy_rect)
        self.surface.blit(boss_img, boss_rect)
        
        if self.start_button.draw(self.surface):
            self.engine.set_state(game.GameState.GAME)
        if self.le_button.draw(self.surface):
            self.engine.set_state(game.GameState.LEVEL_EDITOR)
        if self.quit_button.draw(self.surface):
            self.engine.terminate()