from turtle import Turtle, Screen


def main():
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    colors = ("red", "orange", "yellow", "green", "blue", "purple")

    race_position = -100

    turtles = {}

    for color in colors:
        turtles[color] = (Turtle(shape="turtle"))
        turtles[color].color(color)
        turtles[color].penup()
        turtles[color].goto(x=-230, y=race_position)
        race_position += 40

    screen.exitonclick()


if __name__ == "__main__":
    main()
