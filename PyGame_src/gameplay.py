import pygame 

import game
from button import Button
from bossenemy import BossEnemy
from basictower import BasicTower
from icetower import IceTower
from poisontower import PoisonTower
from basicprojectile import BasicProjectile
from iceprojectile import IceProjectile
from poisonprojectile import PoisonProjectile
from basictowerbutton import BasicTowerButton
from icetowerbutton import IceTowerButton
from poisontowerbutton import PoisonTowerButton

### CLASS RESPONSIBLE FOR THE GAME WINDOW ###
class GamePlay: 
    def __init__(self, surface, engine):
        self.surface = surface
        self.engine = engine
        
        self.game_rect = pygame.Rect((0, 0, (self.surface.get_width()// 4) * 3, self.surface.get_height()))
        self.menu_rect = pygame.Rect((self.surface.get_width()// 4) * 3, 0, self.surface.get_width()// 4, self.surface.get_height())
        
        play_img = pygame.image.load("assets/play_pause_button.png").convert_alpha()
        self.play_button = Button(self.engine, 1500, 600, play_img, 0.2)
        
        sell_towers_img = pygame.image.load("assets/sell_towers_button.png").convert_alpha()
        self.sell_towers_button = Button(self.engine, 1300, 600, sell_towers_img, 0.2)
        
        quit_img = pygame.image.load("assets/quit_button.png").convert_alpha()
        self.quit_button = Button(self.engine, 1400, 700, quit_img, 0.2)
        
        basic_tower_img = pygame.image.load("assets/basic_tower.png").convert_alpha()
        self.basic_tower_button = BasicTowerButton(self.engine, 1300, 175, basic_tower_img, 1)
        
        ice_tower_img = pygame.image.load("assets/ice_tower.png").convert_alpha()
        self.ice_tower_button = IceTowerButton(self.engine, 1500, 175, ice_tower_img, 2)
        
        poison_tower_img = pygame.image.load("assets/poison_tower.png").convert_alpha()
        self.poison_tower_button = PoisonTowerButton(self.engine, 1400, 350, poison_tower_img, 3)
              
    # Draws the current frame of the game window and checks for events
    def draw(self):
        self.surface.fill(game.BLACK, self.game_rect)
        self.surface.fill(game.BACKGROUND_COL, self.menu_rect)
        
        text = game.FONT_2.render("Towers:", True, game.TEXT_COL)
        text_rect = text.get_rect(center=(1400, 50))
        self.surface.blit(text, text_rect)
        
        text = "Cost: {cost}".format(cost=self.basic_tower_button.get_cost())
        text = game.FONT_3.render(text, True, game.TEXT_COL)
        text_rect = text.get_rect(center=(1300, 250))
        self.surface.blit(text, text_rect)
        
        text = "Cost: {cost}".format(cost=self.ice_tower_button.get_cost())
        text = game.FONT_3.render(text, True, game.TEXT_COL)
        text_rect = text.get_rect(center=(1500, 250))
        self.surface.blit(text, text_rect)
        
        text = "Cost: {cost}".format(cost=self.poison_tower_button.get_cost())
        text = game.FONT_3.render(text, True, game.TEXT_COL)
        text_rect = text.get_rect(center=(1400, 425))
        self.surface.blit(text, text_rect)
        
        text = "Money: {money}".format(money=self.engine.get_money())
        text = game.FONT_3.render(text, True, game.TEXT_COL)
        text_rect = text.get_rect(center=(1300, 475))
        self.surface.blit(text, text_rect)
        
        text = "Lives: {lives}/3".format(lives=self.engine.get_lives())
        text = game.FONT_3.render(text, True, game.TEXT_COL)
        text_rect = text.get_rect(center=(1500, 475))
        self.surface.blit(text, text_rect)
        
        text = "Current wave: {wave}/5".format(wave=(self.engine.get_wave() + 1))
        text = game.FONT_3.render(text, True, game.TEXT_COL)
        text_rect = text.get_rect(center=(1400, 525))
        self.surface.blit(text, text_rect)
        
        # Draws the grid of game tiles stored in the Map object of the game engine
        self.engine.get_map().draw()
        
        # Draws the buttons of the menu   
        if self.quit_button.draw(self.surface):
            self.engine.set_state(game.GameState.MAIN_MENU)
            self.engine.reset_game()
        
        # If pressed, all selected towers are sold
        if self.sell_towers_button.draw(self.surface):
            towers = self.engine.get_towers()
            idx = 0
            while idx < len(towers):
                tower = towers[idx]
                if tower.is_clicked():
                    if type(tower) == BasicTower:
                        self.engine.add_money(25)
                    elif type(tower) == IceTower:
                        self.engine.add_money(38)
                    elif type(tower) == PoisonTower:
                        self.engine.add_money(50)
                    del towers[idx]
                    idx -= 1
                idx += 1
            
        if self.play_button.draw(self.surface):
            self.engine.set_paused()
        
        # Draws the tower buttons used to place towers
        self.basic_tower_button.draw(self.surface)
        self.ice_tower_button.draw(self.surface)
        self.poison_tower_button.draw(self.surface)

        # Fetching current wave
        enemies = self.engine.get_enemies()[self.engine.get_wave()]

        # For loop responsible for drawing and moving enemies
        idx = 0
        for enemy in enemies:
            if idx == 0:
                if not self.engine.is_paused():
                    enemy.move()
            else:
                if enemies[idx - 1].get_node() > 1 or enemies[idx - 1].is_frozen():
                    if not self.engine.is_paused():
                        enemy.move()
            enemy.draw(self.surface)
            idx += 1
            
        # For loop making sure that the first enemy is also first in the enemy list.
        for i in range(0, len(enemies) - 1):
            for j in range(i + 1, len(enemies)):
                if (enemies[i].get_node() < enemies[j].get_node()):
                    enemies[i], enemies[j] = enemies[j], enemies[i]
        
        # For loop responsible for drawing the towers and checking if any enemies are in firing range
        towers = self.engine.get_towers()
        for tower in towers:
            tower.draw(self.surface)
            
            for enemy in enemies:
                if not self.engine.is_paused():
                    if tower.get_circle_rect().colliderect(enemy.get_rect()):
                        if type(tower) == BasicTower:
                            tower.fire(enemy)
                            break
                        elif type(tower) == IceTower:
                            if not enemy.is_frozen():
                                tower.fire(enemy)
                                break
                        elif type(tower) == PoisonTower:
                            if not enemy.is_poisoned():
                                tower.fire(enemy)
                                break
        
        # Draws active projectiles and moves them towards their designated enemies
        for projectile in self.engine.get_projectiles():
            projectile.draw(self.surface)
            if not self.engine.is_paused():
                projectile.move()
        
        # For loop checking for projectile hits and applying effects accordingly  
        idx = 0
        for projectile in self.engine.get_projectiles():          
            enemy = projectile.get_enemy()
            if enemy.get_coords() == projectile.get_coords():
                del self.engine.get_projectiles()[idx]
                if type(projectile) == BasicProjectile:
                    enemy.take_damage(projectile.get_damage())
                elif type(projectile) == IceProjectile:
                    enemy.freeze()
                elif type(projectile) == PoisonProjectile:
                    enemy.poison()
            idx += 1
        
        # For loop responsible for checking the current state of the enemies. 
        idx = 0
        for enemy in enemies:
            enemy.unfreeze()
            enemy.unpoison()
            
            pos_x, pos_y = enemy.get_coords() 
            last_node = self.engine.get_map().get_nodes()[-1]
            
            if enemy.get_hp() <= 0:
                if type(enemy) == BossEnemy:
                    x, y = enemy.get_coords()
                    node = enemy.get_node()
                    self.engine.spawn_enemies(x, y, node)
                del enemies[idx]
                self.engine.add_money(10)
            elif (pos_x, pos_y) == (last_node[0], last_node[1]):
                self.engine.take_damage()
                del enemies[idx]
            idx += 1
        
        # Draws a pause icon if the game is paused
        if self.engine.is_paused():
            pause_img = pygame.image.load("assets/pause.png").convert_alpha()
            image = pygame.transform.scale(pause_img, (200, 200))
            rect = image.get_rect()
            rect.center = (600, 400)
            self.surface.blit(image, rect)
        
        # Checks if all the enemies are defeated and the game is won
        if len(enemies) == 0 and self.engine.get_lives() > 0 and self.engine.get_wave() == (len(self.engine.get_enemies()) - 1):
            self.engine.set_state(game.GameState.WIN)   
            self.engine.reset_game()
        elif len(enemies) == 0 and self.engine.get_lives() > 0:
            self.engine.next_wave()
            self.engine.add_money(25)
            self.engine.set_paused()
        
        # Checks if the game is lost  
        if self.engine.get_lives() == 0:
            self.engine.set_state(game.GameState.GAME_OVER)
            self.engine.reset_game()
            
        