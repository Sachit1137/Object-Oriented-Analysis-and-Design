class Bark:
    def __init__(self,bark_sound):
        self.bark_sound = bark_sound
    
    def get_sound(self):
        return self.bark_sound
    
    #compares 2 bark objects
    def equals(self,stored_bark):
        return True if self.get_sound().lower().__eq__(stored_bark.get_sound().lower()) else False