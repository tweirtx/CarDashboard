import pygame
import obd

connection = obd.OBD()
# pygame init stuff

while True:
    # get values from the car
    coolant_temp = connection.query(obd.commands.COOLANT_TEMP).value
    fuel_level = connection.query(obd.commands.FUEL_LEVEL).value
    battery_voltage = connection.query(obd.commands.CONTROL_MODULE_VOLTAGE).value

    # update pygame fields
