import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager(screen)
scoreboard = Scoreboard(screen)

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    # Create new cars randomly
    car_manager.create_car()
    
    # Move all cars
    car_manager.move_cars()
    
    # Remove cars that have gone off screen
    car_manager.remove_offscreen_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            player.game_over()
            scoreboard.game_over()
            break

    # Check if player reached finish line
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()