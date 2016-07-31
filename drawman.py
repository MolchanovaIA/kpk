from turtle import Turtle

def init_drawman():
    global t, x_current, y_current, _drawman_scale
    t=Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    _drawman_scale = 2


def drawman_scale(scale):
    global _drawman_scale
    _drawman_scale = scale


def test_drawman():
    """
    РўРµСЃС‚РёСЂРѕРІР°РЅРёРµ СЂР°Р±РѕС‚С‹ С‡РµСЂС‚С‘Р¶РЅРёРєР°
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



init_drawman()
if __name__== '__main__':
    import time
    test_drawman()
    time.sleep(10)

