from turtle import Turtle, Screen


def main():
    turtle = Turtle()

    def move_forward():
        turtle.forward(10)

    def move_backward():
        turtle.back(10)

    def move_counter_clockwise():
        turtle.left(10)

    def move_clockwise():
        turtle.right(10)

    def clear_drawing():
        turtle.reset()

    screen = Screen()
    screen.listen()

    screen.onkeypress(move_forward, "w")
    screen.onkeypress(move_backward, "s")
    screen.onkeypress(move_counter_clockwise, "a")
    screen.onkeypress(move_clockwise, "d")
    screen.onkeypress(clear_drawing, "c")

    screen.exitonclick()


if __name__ == "__main__":
    main()
