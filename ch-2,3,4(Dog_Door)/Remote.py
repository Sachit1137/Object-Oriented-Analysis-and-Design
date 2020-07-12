class Remote:
    def __init__(self,dog_door):
        self.dog_door = dog_door
        
    def press_button(self,time):
        if self.dog_door.is_open():
            print("Closing the door...")
            self.dog_door.close()
        else:
            print("Opening the door...")
            self.dog_door.open(time)      