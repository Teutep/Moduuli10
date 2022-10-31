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

call = Elevator(0, 10)
call.use_elevator(1)
call.use_elevator(7)
call.use_elevator(5)
call.use_elevator(9)