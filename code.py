from turtle import Turtle, Screen
import pandas as pd
import time

IMAGE = ["./pop_stars/1.gif", "./pop_stars/2.gif"]


class Methods:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(400, 400)
        self.turtle = Turtle()
        self.turtle.hideturtle()  # Hide main turtle by default
        self.number = 0

    def welcome(self):
        self.screen.title("Welcome to Celebrity Quiz Game")
        image = "welcome.gif"
        self.screen.addshape(image)
        self.turtle.shape(image)
        self.turtle.showturtle()  # Show turtle with welcome image
        time.sleep(5)
        self.turtle.hideturtle()  # Hide after welcome message

    def quiz(self):
        self.screen.title("Celebrity Quiz")
        self.screen.addshape(IMAGE[self.number])
        self.turtle.shape(IMAGE[self.number])
        self.turtle.showturtle()  # Show turtle with quiz image


# Setting up class
methods = Methods()
screen = methods.screen

# Setting welcome message
methods.welcome()

# Setting pandas
data = pd.read_csv("quiz1.csv")
star_name_list = data["Star Name"]

guessed_names = []

while len(guessed_names) < 4:
    methods.quiz()
    answer = screen.textinput(title="Guess the Celebrity", prompt="Who are they?")

    if answer is None:
        continue

    answer = answer.strip()
    if answer.lower() == "exit":
        missing_stars = [name for name in star_name_list if name not in guessed_names]
        pd.DataFrame({"Missing Star Names": missing_stars}).to_csv("missing_stars.csv", index=False)
        break
    elif answer in star_name_list.values and answer not in guessed_names:
        guessed_names.append(answer)
        t = Turtle()
        t.hideturtle()
        t.penup()
        star_data = data[data["Star Name"] == answer]
        if not star_data.empty:
            t.goto(star_data["x"].item(), star_data["y"].item())
            t.color("black")
            t.write(answer, align="center", font=("Roboto", 10, "bold"))
