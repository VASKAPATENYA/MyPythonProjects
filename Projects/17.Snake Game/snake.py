import turtle as t
MOVE_DISTANCE=20
STARTING_POSITIONS=[(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.segments=[]
        self.segment_position=0
        self.create_snake()
        self.head=self.segments[0]
        self.head.speed(0)
    

    # Creating The Snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            

    def add_segment(self,position):
        new_segment=t.Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        new_segment.speed(0)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    # Moving The Snake
    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1 ):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    #  Snake Up
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        

    #  Snake Down
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        

    #  Snake Right
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        

    #  Snake Left
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        