# Imports
import pygame

### ENEMY PARENT CLASS ###
class Enemy:
    def __init__(self, image, hp, x, y, nodes):
        img = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(img, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.nodes = nodes
        self.hp = hp
        self.max_health = hp
        self.node = 0   
        self.frozen = False
        self.freeze_counter = 0
        self.poisoned = False
        self.poison_counter = 0
        
    # Sets a new location for the enemy's Rect object
    def set_rect(self, x, y):
        self.rect.center = (x, y)
    
    # Returns the Rect object of the enemy
    def get_rect(self):
        return self.rect
    
    # Sets the current node of the enemy
    def set_node(self, node):
        self.node = node
    
    # Returns the order of the node that the enemy is currently moving towards
    def get_node(self):
        return self.node
    
    # Return the current coordinates of the enemy
    def get_coords(self):
        return self.x, self.y
    
    # Returns the current HP of the enemy
    def get_hp(self):
        return self.hp
    
    # Subtracts a given amount of damage from the enemies current HP
    def take_damage(self, damage):
        self.hp -= damage
    
    # Moves the enemy between the given nodes of the map
    def move(self):                
        if self.node < len(self.nodes):
            if not self.is_frozen():
                if self.nodes[self.node][0] == self.x:
                    y_dif = self.y - self.nodes[self.node][1]
    
                    if -5 <= y_dif <= 5:
                        self.y = self.nodes[self.node][1]
                    elif self.y < self.nodes[self.node][1]:
                        self.y += self.speed
                    elif self.y > self.nodes[self.node][1]:
                        self.y -= self.speed
                
                if self.nodes[self.node][1] == self.y:
                    x_dif = self.x - self.nodes[self.node][0]
                        
                    if -5 <= x_dif <= 5:
                        self.x = self.nodes[self.node][0]
                    elif self.x < self.nodes[self.node][0]:
                        self.x += self.speed
                    elif self.x > self.nodes[self.node][0]:
                        self.x -= self.speed
                        
                if self.nodes[self.node][0] == self.x and self.nodes[self.node][1] == self.y:
                    self.node += 1
        
        self.set_rect(self.x, self.y)
    
    # ABSTRACT METHODS - see descriptions in the inherited classes
    def freeze(self):
        pass
    
    def unfreeze(self):
        pass
        
    def is_frozen(self):
        pass
    
    def poison(self):
        pass
        
    def unpoison(self):
        pass
    
    def is_poisoned(self):
        pass
    
    def draw(self, surface):
        pass