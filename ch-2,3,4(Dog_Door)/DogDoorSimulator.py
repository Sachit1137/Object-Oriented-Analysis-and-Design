import DogDoor
# import Remote
import BarkRecognizer
import Bark
class DogDoorSimulator:
    
    def main(self):
        no_of_barks = 3
        dog_door = DogDoor.DogDoor()
        # store multiple barks in the dog door
        barks = []
        for i in range(no_of_barks):
            barks.append(Bark.Bark("bark"+str(i+1)))
        dog_door.store_bark(barks)
        print("Bruce starts barking")
        #call bark recognizer to recognize the sound
        bark_recognizer = BarkRecognizer.BarkRecognizer(dog_door)
        bark_recognizer.recognize(Bark.Bark("bark2"),3)
        print("Bruce has gone outside...")
        print("Bruce's all done ...")
        print("... but he is stuck outside")
        
        #Simulate a bark of neighbor's dog
        print("Neighbor's dog start barking")
        bark_recognizer.recognize(Bark.Bark("yip"),3)
        
        #Simulate hardware hearing another bark
        print("Bruce starts barking")
        bark_recognizer.recognize(Bark.Bark("bark1"),3)
        print("Bruce is back inside")
        # print("Check if door is closed")
        # print("Door is open") if dog_door.is_open() else print("Door is closed")        

obj = DogDoorSimulator()
obj.main()