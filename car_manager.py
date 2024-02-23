from turtle import Turtle
import random as r
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    def create_cars(self):
        chance=r.randint(1,6)
        if chance == 1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(r.choice(COLORS))
            y_cor=r.randint(-250,250)
            new_car.goto(300, y_cor)
            self.all_cars.append(new_car)
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def speed_up(self):
        self.car_speed +=MOVE_INCREMENT
        for car in self.all_cars:
            car.backward(self.car_speed)



