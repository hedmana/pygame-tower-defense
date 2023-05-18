# Imports
import pygame, csv, os

from gametile import GameTile

### CLASS RESPONSIBLE FOR MAP IMPLEMENTATION ###
class Map:
    def __init__(self, surface, engine):
        self.surface = surface
        self.engine = engine
        self.grid = []
        self.nodes = []
        self.path = 'assets/map.csv'
        self.grass_img = pygame.image.load("assets/grass.png").convert_alpha()
        self.road_img = pygame.image.load("assets/road.png").convert_alpha()
        self.home_img = pygame.image.load("assets/home.png").convert_alpha()
        self.cave_img = pygame.image.load("assets/cave.png").convert_alpha()
        self.read_map_from_csv()
      
    # Reads the map from "map.csv" and stores it as 2D list of GameTile objects
    def read_map_from_csv(self):
        with open(os.path.join(self.path)) as data:
            data = csv.reader(data, delimiter=',')
            x = 0
            y = 0
            for row in data:
                temp_row = []
                for i in row:
                    if i == '1':
                        temp_row.append(GameTile(self.road_img, x, y, 1))
                    elif i == '0':
                        temp_row.append(GameTile(self.grass_img, x, y, 0))
                    elif i == 'S':
                        temp_row.append(GameTile(self.cave_img, x, y, 2))
                    elif i == 'E':
                        temp_row.append(GameTile(self.home_img, x, y, 3))
                    x = x + 100
                y = y + 100
                x = 0
                self.grid.append(temp_row)
        self.set_nodes()
        
        if self.engine.get_enemies():
            self.engine.load_enemies()
     
    # Overwrites the current state of "map.csv" to initialize a default map and calls read_map_from_csv()
    def read_default_map(self):
        with open(self.path, 'w') as data:
            data = csv.writer(data)
            for y in range(0, 8):
                temp_row = []
                for x in range(0, 12):
                    if x == 0 and y == 4:
                        temp_row.append('S')
                    elif x == 11 and y == 4:
                        temp_row.append('E')
                    elif y == 4:
                        temp_row.append(1)
                    else:
                        temp_row.append(0)
                data.writerow(temp_row) 
        self.read_map_from_csv()

    # Converts a 2D list of MapButton objects stored in CustomMap to csv format and calls read_map_from_csv()
    def read_custom_map(self):
        custom_map = self.engine.get_custom_map().get_grid()
        
        with open(self.path, 'w') as data:
            data = csv.writer(data)
            for row in custom_map:
                temp_row = []
                for tile in row:
                    if tile.get_type() == 1:
                        temp_row.append(1)
                    elif tile.get_type() == 2:
                        temp_row.append('S')
                    elif tile.get_type() == 3:
                        temp_row.append('E')
                    else:
                        temp_row.append(0)
                data.writerow(temp_row)
    
        self.read_map_from_csv()
    
    # Sets up a list of coordinates for the enemies to follow
    def set_nodes(self):
        self.nodes = []
        pos_x = 0
        pos_y = 0
        x = 0
        y = 0
        for i in self.get_grid():
            for j in i:
                if j.get_type() == 2:
                    pos_x = x
                    pos_y = y
                x += 1
            x = 0
            y += 1
        
        grid = self.get_grid()
        
        len_x = len(grid[0]) - 1
        len_y = len(grid) - 1
        
        self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
        
        error = 0
        while(True):
            if 0 < pos_x < len_x and 0 < pos_y < len_y:
                if grid[pos_y + 1][pos_x].get_type() == 3:
                    pos_y += 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                elif grid[pos_y - 1][pos_x].get_type() == 3:
                    pos_y -= 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                elif grid[pos_y][pos_x + 1].get_type() == 3:
                    pos_x += 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                elif grid[pos_y][pos_x - 1].get_type() == 3:
                    pos_x -= 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                
                if grid[pos_y + 1][pos_x].get_type() == 1 and not grid[pos_y + 1][pos_x].is_checked():
                    pos_y += 1
                    grid[pos_y][pos_x].set_checked()
                elif grid[pos_y - 1][pos_x].get_type() == 1 and not grid[pos_y - 1][pos_x].is_checked():
                    pos_y -= 1
                    grid[pos_y][pos_x].set_checked()
                elif grid[pos_y][pos_x + 1].get_type() == 1 and not grid[pos_y][pos_x + 1].is_checked():
                    pos_x += 1
                    grid[pos_y][pos_x].set_checked()
                elif grid[pos_y][pos_x - 1].get_type() == 1 and not grid[pos_y][pos_x - 1].is_checked():
                    pos_x -= 1
                    grid[pos_y][pos_x].set_checked()
                
            elif pos_x == 0 and pos_y == 0:
                pass    
                
            elif pos_x == 0:
                if grid[pos_y + 1][pos_x].get_type() == 3:
                    pos_y += 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                elif grid[pos_y - 1][pos_x].get_type() == 3:
                    pos_y -= 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                elif grid[pos_y][pos_x + 1].get_type() == 3:
                    pos_x += 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                
                if grid[pos_y + 1][pos_x].get_type() == 1 and not grid[pos_y + 1][pos_x].is_checked():
                    pos_y += 1
                    grid[pos_y][pos_x].set_checked()
                elif grid[pos_y - 1][pos_x].get_type() == 1 and not grid[pos_y - 1][pos_x].is_checked():
                    pos_y -= 1
                    grid[pos_y][pos_x].set_checked()
                elif grid[pos_y][pos_x + 1].get_type() == 1 and not grid[pos_y][pos_x + 1].is_checked():
                    pos_x += 1
                    grid[pos_y][pos_x].set_checked()
                
            elif pos_y == 0:
                if grid[pos_y + 1][pos_x].get_type() == 3:
                    pos_y += 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break 
                elif grid[pos_y][pos_x + 1].get_type() == 3:
                    pos_x += 1 
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                elif grid[pos_y][pos_x - 1].get_type() == 3:
                    pos_x -= 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
            
                if grid[pos_y + 1][pos_x].get_type() == 1 and not grid[pos_y + 1][pos_x].is_checked():
                    pos_y += 1
                    grid[pos_y][pos_x].set_checked()
                elif grid[pos_y][pos_x + 1].get_type() == 1 and not grid[pos_y][pos_x + 1].is_checked():
                    pos_x += 1
                    grid[pos_y][pos_x].set_checked()
                elif grid[pos_y][pos_x - 1].get_type() == 1 and not grid[pos_y][pos_x - 1].is_checked():
                    pos_x -= 1
                    grid[pos_y][pos_x].set_checked()
                
            elif pos_x == len_x:
                if grid[pos_y + 1][pos_x].get_type() == 3:
                    pos_y += 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                elif grid[pos_y - 1][pos_x].get_type() == 3:
                    pos_y -= 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                elif grid[pos_y][pos_x - 1].get_type() == 3:
                    pos_x -= 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                
                if grid[pos_y + 1][pos_x].get_type() == 1 and not grid[pos_y + 1][pos_x].is_checked():
                    pos_y += 1
                    grid[pos_y][pos_x].set_checked()
                elif grid[pos_y - 1][pos_x].get_type() == 1 and not grid[pos_y - 1][pos_x].is_checked():
                    pos_y -= 1
                    grid[pos_y][pos_x].set_checked()
                elif grid[pos_y][pos_x - 1].get_type() == 1 and not grid[pos_y][pos_x - 1].is_checked():
                    pos_x -= 1
                    grid[pos_y][pos_x].set_checked()
            
            elif pos_y == len_y:
                if grid[pos_y - 1][pos_x].get_type() == 3:
                    pos_y -= 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                elif grid[pos_y][pos_x + 1].get_type() == 3:
                    pos_x += 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                elif grid[pos_y][pos_x - 1].get_type() == 3:
                    pos_x -= 1
                    self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])
                    break
                
                if grid[pos_y - 1][pos_x].get_type() == 1 and not grid[pos_y - 1][pos_x].is_checked():
                    pos_y -= 1
                    grid[pos_y][pos_x].set_checked()
                elif grid[pos_y][pos_x + 1].get_type() == 1 and not grid[pos_y][pos_x + 1].is_checked():
                    pos_x += 1
                    grid[pos_y][pos_x].set_checked()
                elif grid[pos_y][pos_x - 1].get_type() == 1 and not grid[pos_y][pos_x - 1].is_checked():
                    pos_x -= 1
                    grid[pos_y][pos_x].set_checked()
                    
            self.nodes.append([grid[pos_y][pos_x].get_coords()[0] + 50, grid[pos_y][pos_x].get_coords()[1] + 50])    

            if error == 95:
                self.read_default_map()
                break
            else:
                error += 1
    
    # Return a list of coordinates for the enemies to follow      
    def get_nodes(self):
        return self.nodes     
    
    # Returns a 2D list of GameTile objects   
    def get_grid(self):
        return self.grid
    
    # Draws the current map
    def draw(self):
        for row in self.get_grid():
            for tile in row:
                tile.draw(self.surface)