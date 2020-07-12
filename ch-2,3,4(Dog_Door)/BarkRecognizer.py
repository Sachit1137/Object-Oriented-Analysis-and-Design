import DogDoor
import Bark
class BarkRecognizer:
    def __init__(self,dog_door):
        self.dog_door = dog_door
        
    # Listens to the barking and sends the request to the DogDoor class to open the door
    def recognize(self,bark_heard,time):
        # check if bark_heard is stored in the dog door
        for bark in self.dog_door.bark:            
            if bark_heard.equals(bark):
                print("Door opens after hearing Bruce bark")
                self.dog_door.open(time)
                return 

        print("Bark not recognized")