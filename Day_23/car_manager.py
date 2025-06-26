from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self, screen):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.screen = screen


    def create_car(self):
        """Create a car with a 1 in 6 chance"""
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            new_car.setheading(180)  
            self.all_cars.append(new_car)


    def move_cars(self):
        """Move all cars forward"""
        for car in self.all_cars:
            car.forward(self.car_speed)


    def level_up(self):
        """Increase car speed"""
        self.car_speed += MOVE_INCREMENT
    

    def remove_offscreen_cars(self):
        """Remove cars that have moved off the left side of the screen"""
        for car in self.all_cars[:]:  
            if car.xcor() < -320:
                car.hideturtle()
                self.all_cars.remove(car)


    def get_car_count(self):
        """Get the number of cars"""
        return len(self.all_cars)