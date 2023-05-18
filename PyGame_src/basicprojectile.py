from projectile import Projectile

SPEED = 10

class BasicProjectile(Projectile):
    def __init__(self, enemy, x, y, image):
        super().__init__(enemy, x, y, image)
        self.damage = 1
        
    # Moves the projectile towards it's designated enemy  
    def move(self):
        enemy_x, enemy_y = self.enemy.get_coords()
        x_dif = enemy_x - self.x
        y_dif = enemy_y - self.y

        if x_dif > 5:
            self.x += SPEED
        elif x_dif < -5:
            self.x -= SPEED
        else:
            self.x = enemy_x    
            
        if y_dif > 5:
            self.y += SPEED
        elif y_dif < -5:
            self.y -= SPEED
        else:
            self.y = enemy_y
            
        self.set_rect()
    
    # Returns projectile damage
    def get_damage(self):
        return self.damage