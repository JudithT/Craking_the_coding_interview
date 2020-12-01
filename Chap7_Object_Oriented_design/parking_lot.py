# Design a parking lot 
#  how many slots/spots, 
#  how many levels? does it have many levels 
#  what does the parking look like? is it building or an open space ?
#  are other parking only accessible  if others are free 
# are the multiple levels ( concurrency )
# Should we optimize to fill certain areas first 
# what is the pricing strategy ?
# premuims parking spots, accessibility parking spots ? 

# Assuming : 
    #4 sizes ( small, meduim, large(large cars), xlarge(bus)
    #allow to put small cars in xlarge, large , meduim 

    #not allow to put large car into small space 

    # class hierachy: 
        # Abstract vehicle
        #     string licensePlate 
        #     enum color 
        # will create four classes(car, motorcycle, bus, truck ) that inherit from the abstract class vehicle 

        # class ParkingSlot(zipcode)
        #     Mathods: 
        #         def placecar (vehicle) - > spot 
        #         need 4 stacks( I think a dictionary might be better, fast placement and removal) to store the vehicles 

        # class spot(id, size, enum ):
        #     remove_vehicle(ticket)

        # n




class Vehicle:
    def __init__(self, name, license, c):
        self.licensePlate = license
        self.color = c
        self.name = name

class Car(Vehicle):
    def __init(self, name, license, c):
        super().__init__(name, license, c)
        

class Motorcycle(Vehicle):
    def __init(self, name, license, c):
        super().__init__(name, license, c)
        

class Bus(Vehicle):
    def __init(self, name, license, c):
        super().__init__(name, license, c)
        

class Truck(Vehicle):
    def __init(self, name, license, c):
        super().__init__(name, license, c)
        
class Parkinglot:
    def __init__(self, n):
        self.n = n 
        self.cars_parking_slots = {i: None for i in range(n)}
        self.motorcycle_parkind_slots = {i: None for i in range(n)}
        self.bus_parking_slots = {i: None for i in range(n)}
        self.truck_parking_slots = {i: None for i in range(n)}
        self.parkingslots_numbers = 20 # should be here bc parkinglot has many parkingslots
    
    def finding_a_parking_slot(self,vehicle):
        if isinstance(vehicle, Car):
            lookupdict = self.cars_parking_slots
        elif isinstance(vehicle, Motorcycle):
            lookupdict = self.motorcycle_parkind_slots
        elif isinstance(vehicle, Bus):
            lookupdict = self.bus_parking_slots
        elif isinstance(vehicle, Truck):
            lookupdict = self.truck_parking_slots

        for parking_number in range(self.n):
            if lookupdict[parking_number] == None:
            # assigned_parking_slot = vehicle.licensePlate
                return parking_number        
        raise Exception( "Parkinglot  is full")


    def park(self, vehicle):
        parking_number = self.finding_a_parking_slot(vehicle)
      
        if isinstance(vehicle, Motorcycle):
            self.motorcycle_parkind_slots[(parking_number)] = vehicle.licensePlate
            ticket = ("M", parking_number)
        elif isinstance(vehicle, Bus):
            self.bus_parking_slots[(parking_number)] = vehicle.licensePlate
            ticket = ("B", parking_number)
        elif isinstance(vehicle, Car):
            self.cars_parking_slots[parking_number] = vehicle.licensePlate
            ticket = ("C", parking_number)
        else:
            self.truck_parking_slots[(parking_number)] = vehicle.licensePlate
            ticket = ("T", parking_number)
        return ticket 

    def remove_vehicle(self, ticket):
        if ticket[1] == "C":
            self.cars_parking_slots[ticket[1]] = None
            return self.cars_parking_slots
        elif ticket == "M":
            self.motorcycle_parkind_slots[ticket[1]] = None
            return self.cars_parking_slots
        elif ticket == "B":
            self.bus_parking_slots[ticket[1]] = None
            return self.cars_parking_slots
        else: 
            self.truck_parking_slots[ticket[1]] = None
            return self.cars_parking_slots



# Testing 
car1 = Car("Mercedes",123,"White")
car2 = Car("Ashton Martin", 3439, "gold")
truck1 = Truck("Ford", 3456, "blue")
truck2 = Truck ("Toyota", 1278, "yellow")
motorcycle1= Motorcycle("Harley Davidson", 1111, "Black")
motorcycle2= Motorcycle("harley", 1111, "pink")
bus1 = Bus("Los Gatos Elementary School", 2345, "Yellow")
bus2 = Bus("Los Gatos kindergarten", 2345, "Yellow")

sillyparkinglot = Parkinglot(5)
sillyparkinglot.park(car1)
sillyparkinglot.park(car2)
sillyparkinglot.park(truck1)
sillyparkinglot.park(truck2)
sillyparkinglot.park(motorcycle1)
sillyparkinglot.park(bus1)
sillyparkinglot.park(bus2)
ticket1 = sillyparkinglot.park(car1)
ticket2 = sillyparkinglot.park(car2)
print(sillyparkinglot.remove_vehicle(ticket1))
print(sillyparkinglot.remove_vehicle(ticket2))






    



        


