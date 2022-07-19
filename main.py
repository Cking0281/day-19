from turtle import Turtle, Screen
import random


def main():
    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    colors = ("red", "orange", "yellow", "green", "blue", "purple")

    race_position = -100

    turtles = []

    for color in colors:
        new_turtle = (Turtle(shape="turtle"))
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=race_position)
        turtles.append(new_turtle)
        race_position += 40

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.color()[0]
                if winning_color != user_bet:
                    print(f"{winning_color.capitalize()} won the race. You lost.")
                elif winning_color == user_bet:
                    print(f"{winning_color.capitalize()} won the race. You won.")
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


if __name__ == "__main__":
    main()
