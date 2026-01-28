# Code Journal 1.4

'''
Write a Python program that declares a class describing your favorite animal. Have the data
members of the class represent the following physical parameters of the animal: length of 
the arms (float), length of the legs (float), number of eyes (int), does it have a tail? 
(bool), is it furry? (bool). Write an initialization function that sets the values of the 
data members when an instance of the class is created. Write a member function of the class 
to print out and describe the data members representing the physical characteristics of the 
animal.
'''

class Animal:
    def __init__(self, name, armLength, legLength, eyeCount, hasTail, hasFur):
        self.name = name
        self.armLength = armLength
        self.legLength = legLength
        self.eyeCount = eyeCount
        self.hasTail = hasTail
        self.hasFur = hasFur

    def describe_animal(self):
        print(f"{self.name}")
        print(f"Arm Length: {self.armLength} cm")
        print(f"Leg Length: {self.legLength} cm")
        print(f"Eyes:       {self.eyeCount}")
        print(f"Has Tail:   {self.hasTail}")
        print(f"Has Fur:    {self.hasFur}")


def main():
    dog = Animal("Dog", 55, 60, 2, True, True)
    dog.describe_animal()


if __name__ == "__main__":
    main()
