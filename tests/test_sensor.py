import unittest
from sensor import Sensor, EntrySensor, ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.entry_sensor = EntrySensor(42, True, CarPark(...))
        self.exit_sensor = ExitSensor(64, True, CarPark(...))

    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, Sensor)
        self.assertEqual(self.entry_sensor.id, 42)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)

    def test_exit_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, Sensor)
        self.assertEqual(self.exit_sensor.id, 64)
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertIsInstance(self.exit_sensor.car_park, CarPark)

    def test_detect_vehicle(self):
        self.entry_sensor.detect_vehicle = "FAKE-123"
        self.assertIsInstance(self.entry_sensor.detect_vehicle, str)
