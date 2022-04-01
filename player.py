from turtle import Turtle

STARING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")    # set shape
        self.penup()    # penup
        self.go_to_start() # go to the starting position
        self.setheading(90) # face north

    # move the player forward
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # reset player position
    def go_to_start(self):
        self.goto(STARING_POSITION)

    # successful crossing?
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False