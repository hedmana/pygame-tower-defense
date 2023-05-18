# Imports
from mapbutton import MapButton

### CLASS RESPONSIBLE FOR HANDLING THE TILE GRID IN THE LEVEL EDITOR ###
class CustomMap:
    def __init__(self, engine, surface):
        self.engine = engine
        self.surface = surface
        self.grid = []
        self.setup_grid()
     
    # Sets up a grid of MapButton objects for drawing a custom map   
    def setup_grid(self):
        self.grid = []
        for y in range(0, 800, 100):
            row = []
            for x in range(0, 1200, 100):
                row.append(MapButton(self.engine, x, y))
            self.grid.append(row)
     
    # Returns the grid of MapButton objects   
    def get_grid(self):
        return self.grid
    
    # Draws the grid of MapButton objects
    def draw(self):
        for row in self.get_grid():
            for button in row:
                button.draw(self.surface)