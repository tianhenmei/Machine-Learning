import turtle

def draw_triangle(t,color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(20)
    t.left(120)
    t.forward(20)
    t.left(120)
    t.forward(20)
    t.end_fill()

def draw_cort():
    window = turtle.Screen()
    window.bgcolor('#ff0084')
    t = turtle.Turtle()
    t.color('#fff')
    t.shape('turtle')
    t.speed(5)
    for p in range(1,4):
        for a in range(p,5):
            for i in range(1,4):
                draw_triangle(t,'#ff0')
                t.left(120*i)
                t.penup()
                t.forward(20)
                t.pendown()
                t.right(120*(i-1))
            t.penup()
            t.forward(20)
            t.left(60)
            t.pendown()
            draw_triangle(t,'#fff')
            t.penup()
            t.left(60)
            t.forward(20)
            t.pendown()
        t.left(120)
        t.penup()
        t.forward(40)
        t.pendown()
            
    window.exitonclick()

draw_cort()
    
