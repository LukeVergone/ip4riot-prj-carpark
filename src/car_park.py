class CarPark:

    def __init__(self, location='Unknown', capacity=0, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.sensors = sensors or []
        self.displays = displays

    def __str__(self):
        print(f"Car park at {self.location}, with {self.capacity} bays.")


