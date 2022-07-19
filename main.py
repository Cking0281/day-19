from turtle import Turtle, Screen


def main():
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    colors = ("red", "orange", "yellow", "green", "blue", "purple")

    starting_position = -100

    # TODO Need to fix loop variable name
    for color in colors:
        color = Turtle(shape="turtle")
        color.penup()
        color.goto(x=-230, y=starting_position)
        starting_position += 40

    screen.exitonclick()


if __name__ == "__main__":
    main()
