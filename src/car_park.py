from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime # we'll use this to timestamp entries
class CarPark:

    def __init__(self, location='Unknown', capacity=0, plates=None, sensors=None, displays=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)


    @property
    def available_bays(self):
        if self.capacity - len(self.plates) <= 0:
            return 0
        else:
            return self.capacity - len(self.plates)

    def __str__(self):
        print(f"Car park at {self.location}, with {self.capacity} bays.")

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(Sensor)
        elif isinstance(component, Display):
            self.displays.append(Display)

    def update_display(self):
        data = {"available_bays": self.available_bays,
                "temperature": 25}
        for display in self.displays:
            display.update(data)
    def add_car(self, plate):
        self.plates.append(plate)
        self.update_display()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_display()
        self._log_car_activity(plate, "exited")

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")








