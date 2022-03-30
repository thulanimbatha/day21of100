from turtle import Screen
import time
from car_manager import CarManager
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")    # when UP key is detected, use the player.go_up() method

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update() # update every 0.sec

    car_manager.create_car()
    car_manager.move_cars()