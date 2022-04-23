# import classes
# print(classes.Motorcycle)
import time
import pytest

from classes import Motorcycle, Car

moto = Motorcycle('Yamaha', 'Ybr 125')
car = Car('Toyota', 'Auris')

for vehicle in [moto, car]:
    print(f'The time is {time.time()}')
    print(vehicle)
    vehicle.turn_engine_on()
    vehicle.turn_headlight_on()
    vehicle.start_driving()
    vehicle.turn('left')
    vehicle.turn('right')
    print(vehicle)
    vehicle.stop_driving()
    vehicle.turn_engine_off()
    vehicle.turn_headlight_off()
    print()
    time.sleep(10)