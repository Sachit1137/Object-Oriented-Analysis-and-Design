import Tile
class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [[Tile.Tile() for _ in range(width)] for _ in range(height)]

    def get_tile(self, x, y):
        return self.board[x-1][y-1]

    def add_unit(self,unit, x, y):
        tile = self.get_tile(x,y)
        tile.add_unit(unit)

    def get_unit(self, x, y):
        tile = self.get_tile(x,y)
        return tile.get_unit()
    
    #remove given unit from one tile
    def remove_unit(self,unit,x,y):
        tile = self.get_tile(x,y)
        tile.remove_unit(unit)
    
    #remove all units from one tile
    def remove_all_units(self,x,y):
        tile = self.get_tile(x,y)
        tile.remove_all_units()