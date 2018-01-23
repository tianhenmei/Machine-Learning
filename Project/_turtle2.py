import turtle

def draw_rhombus(t):
    t.forward(50)
    t.right(60)
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.right(60)
    t.forward(50)

def draw_cort():
    window = turtle.Screen()
    window.bgcolor('#ff0084')
    t = turtle.Turtle()
    t.color('#fff')
    t.shape('turtle')
    t.speed(5)
    for i in range(1,37):
        draw_rhombus(t)
        t.right(10)
    t.right(90)
    t.forward(200)
    t.left(180)
    t.right(15)
    draw_rhombus(t)
    t.right(30)
    draw_rhombus(t)
    t.right(15)
    t.forward(20)
    
    window.exitonclick()

draw_cort()
    
