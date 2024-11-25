class Display:
    def __init__(self, id, message = "", is_on = False, car_park=None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        print(f"Display {self.id}: Welcome top the car park.")

    def update(self, data):
        self.message = data['message']
        for key, value in data.items():
            print(f"{key}: {value}")



