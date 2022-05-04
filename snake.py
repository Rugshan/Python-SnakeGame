# Imports
from turtle import Turtle

# Constants
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SPEED = "fastest"
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
LEFT_WALL = -290
RIGHT_WALL = 290
TOP_WALL = 290
BOTTOM_WALL = -290


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        tail_index = len(self.segments) - 1
        self.tail = self.segments[tail_index]
        self.is_paused = False

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.speed(SPEED)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.tail.position())

    def move(self):

        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def toggle_pause(self):

        if self.is_paused:
            self.is_paused = False
        else:
            self.is_paused = True

    def detect_wall_collision(self):
        return (self.head.xcor() > RIGHT_WALL or self.head.xcor() < LEFT_WALL or
                self.head.ycor() > TOP_WALL or self.head.ycor() < BOTTOM_WALL)

    def detect_food_collision(self, food):
        if self.head.distance(food) < 15:
            self.extend()
            return True
        return False

    def detect_tail_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False
