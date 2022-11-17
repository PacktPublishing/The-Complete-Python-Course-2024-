# Class and Objects in Python
# Code by studyopedia

class Bike:

    # attributes
    name = "Hayabusa"
    body = "GEN III"
    engine = 1340

    # custom function
    def demoFunc(self):
        print("\nBike = ",self.name)
        print("Body = ", self.body)
        print("Engine = ", self.engine)

# Objects
b1 = Bike()
b2 = Bike()

# Accessing using the 1st object
print("Bike Name = ",b1.name)
print("Bike Engine = ",b1.engine)

# Calling using the 2nd object
b2.demoFunc()








