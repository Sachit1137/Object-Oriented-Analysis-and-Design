class Tile:
    def __init__(self):
        self.units = []
    
    def add_unit(self,unit):
        self.units.append(unit)
    
    def get_unit(self):
        return self.units
    
    def remove_unit(self,inp_unit):
        for i in range(len(self.units)):
            if self.units[i] == inp_unit:
                self.units.pop(i)
                break
    
    def remove_all_units(self):
        self.units.clear()