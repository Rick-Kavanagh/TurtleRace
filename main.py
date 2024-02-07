import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
starting_y = -90
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.teleport(-240, starting_y)
    all_turtles.append(new_turtle)
    starting_y += 30

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        rand_distance = random.randint(0, 14)
        turtle.forward(rand_distance)

    for turtle in all_turtles:
        if turtle.xcor() >= 225:
            is_race_on = False
            winning_color = turtle.pencolor()

            if user_bet == winning_color:
                print(f"You win! You bet on the {winning_color} turtle and they won!")
            else:
                print(f"You lost! You bet on the {user_bet} turtle and the {winning_color} turtle won!")

screen.exitonclick()

