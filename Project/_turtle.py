import turtle

def draw_square(t):
    for i in range(1,5):
        t.forward(100)
        t.right(90)

def draw_cort():
    window = turtle.Screen()
    window.bgcolor('#ff0084')
    t = turtle.Turtle()
    t.color('#fff')
    t.shape('turtle')
    t.speed(5)
    for i in range(1,37):
        draw_square(t)
        t.right(10)
    window.exitonclick()

draw_cort()
    
