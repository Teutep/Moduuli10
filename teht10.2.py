class Elevator:
    def __init__(self, minfloor, maxfloor):
        self.maxfloor = maxfloor
        self.minfloor = minfloor
        self.currentloc = minfloor

    def use_elevator(self, floor):
        if floor > self.currentloc:
            count = floor - self.currentloc
            for i in range(count):
                if self.currentloc == self.maxfloor:
                    return
                else:
                    self.higher_floor()

        elif self.currentloc > floor:
            count = self.currentloc - floor
            for i in range(count):
                if self.currentloc == self.minfloor:
                    return
                else:
                    self.lower_floor()

    def higher_floor(self):
        self.currentloc += 1
        print(f"Tämänhetkinen kerroksesi on {self.currentloc}")
        return

    def lower_floor(self):
        self.currentloc -= 1
        print(f"Tämänhetkinen kerroksesi on {self.currentloc}")
        return

class House:
    def __init__(self, minfloor, maxfloor, elevatorqty):
        self.elevators = []
        self.minfloor = minfloor
        self.maxfloor = maxfloor

        for i in range(elevatorqty):
            quantity = Elevator(self.minfloor, self.maxfloor)
            quantity.number = i + 1
            self.elevators.append(quantity)

    def use_elevator(self, elevator_number, floor):
        current_elevator = self.elevators[elevator_number-1]
        print(f"Olet hississä {current_elevator.number}")
        current_elevator.use_elevator(floor)

house = House(1, 10, 2)
house.use_elevator(1, 5)
house.use_elevator(2, 8)