# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    def __inti___(self, move)
        self.move = move

class FlightVehicle(Vehicle):
    def __inti__(self, move, fly):
        super().__init__(move)
        self.fly = fly

class Airplane(FlightVehicle):
    def __init__(self, move, fly, fuel)
        super().__init__(move, fly)
        self.fuel = fuel

class GroundVehicle(Vehicle):
    def __init__(self, move, wheels):
        super().__init__(move)
        self.wheels = wheels

class Car(GroundVehicle):
    def __init__(self, move, wheels, make, model):
    super().__init__(move, wheels)
    self.make = make
    self.model = model

class Motorcycle(GroundVehicle):
    def __init__(self, move, handlebarType):
        super().__init__(move)
        self.handlebarType = handlebarType
