from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

#create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
moondalup_car_park = CarPark("moondalup", 100,None,None,None,"moondalup.txt")

#create an entry sensor object with id 1, is_active True, and car_park car_park
sensor_1 = EntrySensor(1, True, moondalup_car_park)

#create an exit sensor object with id 2, is_active True, and car_park car_park
sensor_2 = ExitSensor(2, True, moondalup_car_park)

#create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display_1 = Display(1, "Welcome to Moondalup!", True, moondalup_car_park)

#drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for i in range(10):
    sensor_1.detect_vehicle()


#drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for i in range(2):
    sensor_2.detect_vehicle()