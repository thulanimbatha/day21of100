from turtle import Screen
import time
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update() # update every 0.sec