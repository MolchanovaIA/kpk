from turtle import Turtle

def init_drawman():
    global t, x_current, y_current, _drawman_scale
    t=Turtle()
    t.speed(100)
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    _drawman_scale = 10





def drawman_scale(scale):
    global _drawman_scale
    _drawman_scale = scale


def test_drawman():
    """
    Моделирование работы Чертёжника с помощью Черепахи
    :return: None
    """

    pen_down()
    for i in range (5):
        on_vector(100, 200)
        on_vector(0, -200)
    pen_up()
    to_point(0, 0)

def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(dx, dy):
    global x_current, y_current, _drawman_scale
    x_current+=dx*_drawman_scale
    y_current +=dy*_drawman_scale
    t.goto(x_current, y_current)

def to_point(x, y):
    global x_current, y_current, _drawman_scale
    x_current = x*_drawman_scale
    y_current = y*_drawman_scale
    t.goto(x_current, y_current)


def coord():
    global _drawman_scale

    for i in range(-100, 100):
        x_current = i
        y_current = 100
        to_point(x_current, y_current)
        pen_down()
        on_vector(0, -200)
        pen_up()
    for i in range(-100, 100):
        x_current = 100
        y_current = i
        to_point(x_current, y_current)
        pen_down()
        on_vector(-200, 0)
        pen_up()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)

    t.color('red')
    t.width(3)
    to_point(0, 0)
    pen_down()
    on_vector(-100, 0)
    pen_up()
    to_point(0, 0)
    pen_down()
    on_vector(100, 0)
    pen_up()
    to_point(0, 0)
    pen_down()
    on_vector(0, -100)
    pen_up()
    to_point(0, 0)
    pen_down()
    on_vector(0, 100)
    pen_up()
    to_point(0, 0)

    t.color('green')
    t.width(4)

init_drawman()
if __name__== '__main__':
    import time

    test_drawman()
    time.sleep(10)

