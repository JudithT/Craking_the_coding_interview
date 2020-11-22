# Design a parking lot 
#  how many slots/spots, 
#  how many levels? does it have many levels 
#  what does the parking look like? is it building or an open space ?
#  are other parking only accessible  if others are free 
# are the multiple levels ( concurrency 
# Should we optimize to fill certain areas first 
# what is the pricing strategy ?
# premuis parking spots, accessibility parking spots ? 

# Assuming : 
    #4 sizes ( small, meduim, large(large cars), xlarge(bus)
    #allow to put small cars in xlarge, large , meduim 

    #not allow to put large car into small space 

    # class hierachy: 
        Abstract vehicle
            string licensePlate 
            enum color 
        will create four classes(car, motorcycle, bus, truck ) that inherit from the abstract class vehicle 

        class ParkingSlot(zipcode)
            Mathods: 
                def placecar (vehicle) - > spot 
                need 4 stacks( I think a dictionary might be better, fast placement and removal) to store the vehicles 

        class spot(id, size, enum ):
            remove_vehicle(ticket)

        n




class Vehicle:
    def __init__(self, name, license, c):
        self.licensePlate = license
        self.color = color
        self.name = name

class Car(Vehicle):
    def __init(self, name, license, c):
        super().__init__(name, 'car')

class Motorcycle(Vehicle):
    def __init(self, name, license, c):
        super().__init__(name, 'motorcycle')

class Bus(Vehicle):
    def __init(self, name, license, c):
        super().__init__(name, 'bus')

class Truck(Vehicle):
    def __init(self, name, license, c):
        super().__init__(name, 'truck')

class ParkingSlot:
    def __init__(self):
        self.cars_parking_slots = {}
        self.motorcycle_parkind_slots = {}
        self.bus_parking_slots = {}
        self.truck_parking_slots = {}

    def parking(self, vehicle):
        def __init__(self):
            self.parking_number = random.randint(5)
        if vehicle == car:   # not sure if this is right 
            self.cars_parking_slots[self.parking_number] = car.licensePlate
            ticket = ("C", self.parking_number)
        elif vehicle == Motorcycle:
            self.motorcycle_parkind_slots[(self.parking_number)] = Motorcycle.licensePlate
            ticket = ("M", self.parking_number)
        elif vehicle == Bus:
            self.bus_parking_slots[(self.parking_number)] = Bus.licensePlate
            ticket = ("B", self.parking_number)
        else:
            self.truck_parking_slots[(self.parking_number)] = Truck.licensePlate
            ticket = ("T", self.parking_number)
        return ticket 

    def remove_vehicle(self, ticket):
        if ticket[1] == "C":
            self.cars_parking_slots[ticket[1]] = None
        elif ticket == "M":
            self.motorcycle_parkind_slots[ticket[1]] = None
        elif ticket == "B":
            self.bus_parking_slots[ticket[1]] = None
        else: 
            self.truck_parking_slots[ticket[1]] = None


        


