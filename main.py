from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height= 400) # setting screen size
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter the colour: ")

colors = ["red", "purple", "brown", "blue", "orange", "green"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x= -230, y = y_position[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while(is_race_on):
    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")

        random_no = random.randint(0, 10)
        turtle.forward(random_no)

screen.exitonclick()

# Project by Shivani Verma