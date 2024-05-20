print("como pasa el tiempo")
import turtle

window = turtle.Screen()

tortuga = turtle.Turtle()
tortuga.speed(0)
tortuga.left(90)

def dibujarFractal(tamañoDeRama, tortuga):
    if(tamañoDeRama < 10):
        return
    tortuga.forward(tamañoDeRama)
    tortuga.left(30)
    dibujarFractal(tamañoDeRama/1.5, tortuga)
    tortuga.right(60)
    dibujarFractal(tamañoDeRama/1.5, tortuga)
    tortuga.left(30)
    tortuga.left(10)
    dibujarFractal(tamañoDeRama/1.5, tortuga)
    tortuga.right(20)
    dibujarFractal(tamañoDeRama/1.5, tortuga)
    tortuga.left(10)
    tortuga.backward(tamañoDeRama)
    
tortuga.setpos(0, -60)   
dibujarFractal(60, tortuga)


