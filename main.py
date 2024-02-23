import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
cars = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.onkey(player.move_up, "Up")
# screen.onkey(car.move_car,"m")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_car()
    if player.is_on_finish_line():
        player.goto_start()
        scoreboard.increase_level()
        cars.speed_up()
    # detect collision with cars
    for i in cars.all_cars:
        if i.distance(player) <= 20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
