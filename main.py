from turtle import Turtle, Screen
import pandas as pd
import time

#setting screen 1 Welcome!
screen = Screen()
screen.title("Welcome to Celibrity Quiz Game")  
image = "welcome.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)
time.sleep(5)

screen = Screen()
screen.title("Welcome to Celibrity Quiz Game")  
image = "./pop_stars/1.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)
screen.textinput(title="Guess the Celebrity", prompt="Who are they?")





screen.exitonclick()