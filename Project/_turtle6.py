import turtle

def draw_circle(t):
    t.circle(100,60)
    t.left(120)
    t.circle(100,60)

def draw_cort():
    window = turtle.Screen()
    window.bgcolor('#ff0084')
    t = turtle.Turtle()
    t.color('#fff')
    t.shape('turtle')
    t.speed(5)
    for i in range(1,37):
        draw_circle(t)
        t.right(10)
    
    window.exitonclick()

draw_cort()
    
