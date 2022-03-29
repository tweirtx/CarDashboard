import pygame
import obd

connection = obd.OBD()
# pygame init stuff
pygame.init()
screen = pygame.display.set_mode([800, 480]) # 800x480 is my target because that is what the screen in my car uses.
screen.fill(color=pygame.color.Color(0, 0, 0))

while True:
    # get values from the car
    coolant_temp = 50
    fuel_level = 100
    battery_voltage = 11.5
    # TODO switch values back to reading from OBDII port
    # coolant_temp = connection.query(obd.commands.COOLANT_TEMP).value
    # fuel_level = connection.query(obd.commands.FUEL_LEVEL).value
    # battery_voltage = connection.query(obd.commands.CONTROL_MODULE_VOLTAGE).value

    # update pygame fields
