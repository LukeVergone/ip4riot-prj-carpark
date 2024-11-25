from sensor import Sensor
from display import Display
class CarPark:

    def __init__(self, location='Unknown', capacity=0, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        print(f"Car park at {self.location}, with {self.capacity} bays.")

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(Sensor)
        elif isinstance(component, Display):
            self.displays.append(Display)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_display()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_display()

    def update_display(self):
        data = {"available_bays": self.available_bays,
                "temperature": 25}
        for display in self.displays:
            display.update(data)

    @property
    def available_bays(self):
        if self.capacity - len(self.plates) <= 0:
            return 0
        else:
            return self.capacity - len(self.plates)






