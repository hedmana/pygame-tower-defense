import pygame
from enum import Enum

from mainmenu import MainMenu
from leveleditor import LevelEditor
from gameplay import GamePlay
from gameover import GameOver
from win import Win
from map import Map
from custommap import CustomMap
from basicenemy import BasicEnemy
from stealthenemy import StealthEnemy
from bossenemy import BossEnemy
from basictower import BasicTower
from icetower import IceTower
from poisontower import PoisonTower

# Initializes a PyGame application
pygame.init()

# PyGames Clock class used for FPS configuration
clock = pygame.time.Clock()

# Fixed parameters
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
FONT_1 = pygame.font.SysFont("arialblack", 140)
FONT_2 = pygame.font.SysFont("arialblack", 70)
FONT_3 = pygame.font.SysFont("arialblack", 30)
TEXT_COL = (255, 255, 255)
BACKGROUND_COL = (52, 78, 91)
POISON_COL = (0, 255, 0)
BLACK = (0, 0, 0)

### ENUM CLASS TO KEEP TRACK OF GAME STATES ###
class GameState(Enum):
    MAIN_MENU = 1
    LEVEL_EDITOR = 2
    GAME = 3
    GAME_OVER = 4
    WIN = 5
    
### CLASS RESPONSIBLE FOR GAME ENGINE ###
class GameEngine:
    # Sets up the pygame window
    def __init__(self):
        self.running = True
        self.state = GameState.MAIN_MENU
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tower Defence Game")
        
        self.enemies = []
        self.towers = []
        self.projectiles = []
        
        self.money = 300
        self.lives = 3
        self.wave = 0
        
        self.paused = True
        self.clicked = False
        self.basic_tower_button_clicked = False
        self.ice_tower_button_clicked = False
        self.poison_tower_button_clicked = False
    
        self.map = Map(self.window, self)
        self.custom_map = CustomMap(self, self.window)
        
        self.load_enemies()
       
    # Sets the game state to given parameter 
    def set_state(self, state):
        self.state = state 
    
    def click(self):
        self.clicked = True
    def unclick(self):
        self.clicked = False       
    
    # Returns the boolean value self.clicked. Used to check if the mouse is clicked or not
    def is_clicked(self):
        return self.clicked
    
    def click_basic_tower(self):
        self.basic_tower_button_clicked = True
        
    def unclick_basic_tower(self):
        self.basic_tower_button_clicked = False       
    
    # Returns the boolean value self.clicked. Used to check if a basic tower button is clicked or not
    def basic_tower_is_clicked(self):
        return self.basic_tower_button_clicked
    
    def click_ice_tower(self):
        self.ice_tower_button_clicked = True
        
    def unclick_ice_tower(self):
        self.ice_tower_button_clicked = False       
    
    # Returns the boolean value self.clicked. Used to check if an ice tower button is clicked or not
    def ice_tower_is_clicked(self):
        return self.ice_tower_button_clicked
    
    def click_poison_tower(self):
        self.poison_tower_button_clicked = True
        
    def unclick_poison_tower(self):
        self.poison_tower_button_clicked = False
    
    # Returns the boolean value self.clicked. Used to check if a poison tower button is clicked or not   
    def poison_tower_is_clicked(self):
        return self.poison_tower_button_clicked
    
    # Returns the Map objet of the game engine class
    def get_map(self):
        return self.map
    
    # Returns the CustomMap object of the game engine class
    def get_custom_map(self):
        return self.custom_map
    
    # Returns a list of Enemy objects
    def get_enemies(self):
        return self.enemies
    
    # Sets the self.paused variable to either True or False. Used to pause/unpause the game
    def set_paused(self):
        if self.paused:
            self.paused = False
        else:
            self.paused = True
    
    # Return the boolean value of self.paused    
    def is_paused(self):
        return self.paused
    
    # Return a list of Tower objects
    def get_towers(self):
        return self.towers
    
    # Initializes the list of enemy waves
    def load_enemies(self):
        self.enemies = [# ENEMY DEMOS
                        # [BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        # [BossEnemy("assets/boss_enemy.png", 10, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        # [StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes())],
                        
                        # Wave 1
                        [BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes())],
                        # Wave 2
                        [BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes())],
                        # Wave 3
                        [BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes())],
                        # Wave 4
                        [BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BossEnemy("assets/boss_enemy.png", 20, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BossEnemy("assets/boss_enemy.png", 20, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes())],
                        # Wave 5
                        [BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BasicEnemy("assets/basic_enemy.png", 5, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        StealthEnemy("assets/stealth_enemy.png", 3, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BossEnemy("assets/boss_enemy.png", 20, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BossEnemy("assets/boss_enemy.png", 20, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BossEnemy("assets/boss_enemy.png", 20, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes()),
                        BossEnemy("assets/boss_enemy.png", 20, self.map.get_nodes()[0][0], self.map.get_nodes()[0][1], self.map.get_nodes())]]
    
    def spawn_enemies(self, x, y, node):
        enemy_1 = BasicEnemy("assets/basic_enemy.png", 5, x, y, self.map.get_nodes())
        enemy_2 = StealthEnemy("assets/stealth_enemy.png", 3, x, y, self.map.get_nodes())
        enemy_1.set_node(node)
        enemy_2.set_node(node)
        self.enemies[self.wave].append(enemy_1)
        self.enemies[self.wave].append(enemy_2)
    
    # Places a Tower object at the given position   
    def place_tower(self, x, y, type):
        for row in self.map.get_grid():
            for tile in row:
                if tile.get_type() == 0:
                    coords = tile.get_coords()
                    if tile.get_rect().collidepoint((x, y)):
                        if type == 1:
                            self.towers.append(BasicTower(self, "assets/basic_tower.png", coords[0] + 50, coords[1] + 50))
                            self.money -= 50
                        elif type == 2:
                            self.towers.append(IceTower(self, "assets/ice_tower.png", coords[0] + 50, coords[1] + 50))
                            self.money -= 75
                        elif type == 3:
                            self.towers.append(PoisonTower(self, "assets/poison_tower.png", coords[0] + 50, coords[1] + 50))
                            self.money -= 100
                        return True
        return False
    
    # Resets the game window to it's initial state   
    def reset_game(self):
        self.load_enemies()
        self.towers = []
        self.projectiles = []
        self.paused = True
        self.lives = 3
        self.wave = 0
        self.money = 300
        
    def add_money(self, amount):
        self.money += amount
     
    # Adds a new Projectile object to the game engine           
    def add_projectile(self, projectile):
        self.projectiles.append(projectile)
    
    # Returns a list o Projectile objects   
    def get_projectiles(self):
        return self.projectiles

    # Returns the PyGame window
    def get_surface(self):
        return self.window
    
    # Returns the current amount of money
    def get_money(self):
        return self.money
    
    # Return the current amount of lives
    def get_lives(self):
        return self.lives
    
    # Returns the current wave of the game
    def get_wave(self):
        return self.wave
    
    def next_wave(self):
        self.wave += 1
    
    # Subtracts a life from the player
    def take_damage(self):
        self.lives -= 1
    
    # Draws the current FPS in the bottom right corner of the window
    def draw_fps(self):
        txt = "FPS: {fps}".format(fps = int(clock.get_fps()))
        text = FONT_3.render(txt, True, TEXT_COL)
        text_rect = text.get_rect(center=(1550, 780))
        self.window.blit(text, text_rect)
            
    # Updates the pygame window for each frame
    def update(self):
        # Checks for active state
        if self.state == GameState.MAIN_MENU:    
            main_menu = MainMenu(self.window, self)
            main_menu.draw()
           
        elif self.state == GameState.LEVEL_EDITOR:
            level_editor = LevelEditor(self.window, self)
            level_editor.draw()
             
        elif self.state == GameState.GAME:
            game_play = GamePlay(self.window, self)
            game_play.draw()
            
        elif self.state == GameState.GAME_OVER:
            game_over = GameOver(self.window, self)
            game_over.draw()
        elif self.state == GameState.WIN:
            win = Win(self.window, self)
            win.draw()
               
        self.draw_fps()
    
    # Runs the program 
    def run(self):
        while self.running:
            self.update()
                               
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()
            
            # Fixed framerate cap of 30 FPS
            clock.tick(30)
            
    # Terminates the program by setting the running variable to False     
    def terminate(self):
        self.running = False