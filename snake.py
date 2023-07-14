from turtle import Turtle
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        position = 0
        coordinates = (position, 0)
        for _ in range(0, 3):
            self.add_segment(coordinates)
            position += -20

    def add_segment(self, coordinates):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(coordinates)
        self.segments.append(segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[segment_num - 1].xcor()
            y_cor = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.segments[0].heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.segments[0].heading() != 90:
            self.head.setheading(270)

    def turn_left(self):
        if self.segments[0].heading() != 0:
            self.head.setheading(180)


    def turn_right(self):
        if self.segments[0].heading() != 180:
            self.head.setheading(0)
