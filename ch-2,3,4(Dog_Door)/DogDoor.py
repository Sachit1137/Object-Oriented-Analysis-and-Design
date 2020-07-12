import time
class DogDoor:
    def __init__(self):
        self.door_open = False
        self.bark = []
    
    #store the owner's dog's bark
    def store_bark(self,bark):
        self.bark = [brk for brk in bark]
        
    #open the door
    def open(self,t):
        self.door_open = True
        self.wait(t) 
        self.close()
        
    #close the door
    def close(self):               
        self.door_open = False
    
    #check if the door is open
    def is_open(self):
        return self.door_open
    
    # wait for 5 seconds and then close the door
    def wait(self,t):
        for i in range(t):
            time.sleep(1)
    