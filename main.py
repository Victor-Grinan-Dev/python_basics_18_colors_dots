from turtle import Turtle, Screen, colormode
from random import choice, randint

screen = Screen()

tim = Turtle()
tim.shape("turtle")
tim.speed(100)


def turtle_start_learn():
    tim.color("red")

    for _ in range(4):
        tim.forward(100)
        tim.right(90)
        tim.end_fill()

    tim.penup()
    tim.goto(-200, 200)
    tim.pendown()

    tim.clear()

    for _ in range(20):
        tim.penup()
        tim.forward(10)
        tim.pendown()
        tim.forward(10)

    tim.penup()
    tim.goto(-10, 10)
    tim.clear()


def turtle_poligons():
    sides = 3
    length = 20
    colours = ["red", "yellow", "blue", "green", "orange", "royal blue", "firebrick", "dark magenta", "green yellow",
               "black"]

    tim.pendown()
    for i in range(len(colours)):
        color = choice(colours)
        tim.color(color)
        colours.remove(color)
        for j in range(sides):
            tim.forward(length)
            tim.right(360 / sides)
        sides += 1


def turtle_random_walk():
    distance = 20
    directions = ["right", "left", "forward"]
    colours = ["red", "yellow", "blue", "green", "orange", "royal blue", "firebrick", "dark magenta", "green yellow",
               "black"]
    tim.pensize(5)
    tim.speed(100)
    while True:
        tim.pencolor(choice(colours))
        move = choice(directions)
        if move == "right":
            tim.right(90)
            tim.forward(distance)
        elif move == "left":
            tim.left(90)
            tim.forward(distance)
        elif move == "backward":
            tim.backward(distance)
        else:
            tim.forward(distance)


def color_generator():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def turtle_random_walk_answer():
    distance = 30
    direction = [0, 90, 180, 270]
    tim.pensize(15)
    tim.speed(100)
    colormode(255)

    for _ in range(10000):
        tim.color(color_generator())
        tim.forward(distance)
        tim.setheading(choice(direction))


def spiral_square():
    tim.reset()
    for i in range(500):  # this "for" loop will repeat these functions 500 times
        tim.forward(i)
        tim.left(91)


def spiral_rainbow_exagons():
    tim.reset()
    colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
    for x in range(360):
        tim.pencolor(colors[x % 6])
        tim.width(int(x / 100 + 1))
        tim.forward(x)
        tim.left(59)


def flowers():
    colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
    tim.reset()
    screen.bgcolor("dark grey")
    for n in range(60):
        actual_color = choice(colors)
        tim.pencolor(actual_color)
        tim.penup()
        tim.goto(randint(-400, 400), randint(-400, 400))
        tim.pendown()

        # red_amount = randint(0, 30) / 100.0
        # blue_amount = randint(50, 100) / 100.0
        # green_amount = randint(0, 30) / 100.0
        # tim.pencolor((red_amount, green_amount, blue_amount))

        circle_size = randint(10, 40)
        tim.pensize(randint(1, 5))

        for i in range(6):
            tim.circle(circle_size)
            tim.left(60)


def draw_a_spirograph(size_of_gap):
    tim.speed(100)
    colormode(255)
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(color_generator())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(int(current_heading + size_of_gap))


def extract_colors(file, amount=30):
    """returns all(amount) colors in rgb integers from the argument(file)"""
    import colorgram
    rgb_colors = []
    colors = colorgram.extract(file, amount)

    for color in colors:
        r = color.rgb.r  # didn't understand from where the method rgb come from (and r, g, b)
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))

    return rgb_colors


def hirst_painting(size=20):
    colormode(255)
    color_list = [(233, 240, 247), (134, 167, 191), (211, 156, 106), (197, 143, 166), (29, 110, 168), (234, 214, 86),
                  (127, 74, 92), (187, 178, 19), (26, 136, 66), (55, 18, 26), (142, 20, 40), (38, 175, 113),
                  (225, 170, 196), (116, 188, 144), (231, 77, 50), (172, 70, 46), (238, 218, 5), (37, 17, 16),
                  (186, 91, 110), (9, 102, 52), (34, 167, 189), (20, 20, 28), (183, 185, 213), (234, 171, 159),
                  (154, 215, 172), (142, 20, 16), (89, 124, 182)]

    tim.pensize(size)
    jumps = int(size * 1.5)
    x_coord = -600
    y_coord = 300
    tim.penup()
    tim.hideturtle()

    tim.speed("fastest")
    for y in range(20):
        tim.goto(x_coord, y_coord)
        for x in range(40):
            tim.dot(size, choice(color_list))
            tim.forward(jumps)
        y_coord -= jumps


def hirst_painting_spiral(size=20):
    """TODO: the idea is to take the spirals created before and make them dots"""
    pass


# turtle_poligons()
# spiral_rainbow_exagons()
# draw_a_spirograph(2)
hirst_painting()
# spiral_square()

screen.exitonclick()
