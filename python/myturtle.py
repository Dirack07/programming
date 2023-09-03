import time
import turtle
import random

t = turtle.Turtle()
t.speed(0) # Curiosamente speed 0 es lo más rápido
t.penup() 
t.goto(-140, 140) # # Es lo mismo que setpos()

# Dibujar marcas 

for marca in range(15): 
# Escribe los numeritos
    t.write(marca, align ='center') 
    t.right(90) 

    # Dibuja las líneas discontinuas (marcas) 
    for num in range(8): 
        t.penup() 
        t.forward(10) 
        t.pendown() 
        t.forward(10)
# Regresa para avanzar a la siguiente línea  
    t.penup() 
    t.backward(160) 
    t.left(90) 
    t.forward(20) 
  
# Tortuga roja 
troja = turtle.Turtle() 
troja.color('red') 
troja.shape('turtle') 
   
# La tortuga roja toma su lugar 
troja.penup() 
troja.goto(-160, 100) 
troja.pendown() 
   
# La tortuga roja hace calentamiento
for giro in range(10): # Gira diez veces
    troja.right(36)    # 36 grados a la derecha
  
# Tortuga azul 
tazul = turtle.Turtle() 
tazul.color('blue') 
tazul.shape('turtle')
# La tortuga azul toma su lugar 
tazul.penup() 
tazul.goto(-160, 70) 
tazul.pendown() 
   
# La tortuga azul hace calentamiento 
for giro in range(10): 
    tazul.left(36)      
  
## A partir de aquí debes agregar dos tortugas más...

# Las tortugas corren a su velocidad (aleatoria)
# Cada tortuga da cien pasos de longitud variable

# Tortuga amarilla 
tamarilla = turtle.Turtle() 
tamarilla.color('yellow') 
tamarilla.shape('turtle')

# La tortuga amarilla toma su lugar 
tamarilla.penup() 
tamarilla.goto(-160, 40) 
tamarilla.pendown() 

# La tortuga amarilla hace calentamiento
for giro in range(10): # Gira diez veces
    tamarilla.right(36)    # 36 grados a la derecha

# Tortuga naranja 
tnaranja = turtle.Turtle() 
tnaranja.color('orange') 
tnaranja.shape('turtle')
# La tortuga naranja toma su lugar 
tnaranja.penup() 
tnaranja.goto(-160, 10) 
tnaranja.pendown() 

# La tortuga naranja hace calentamiento
for giro in range(10): # Gira diez veces
    tnaranja.right(36)    # 36 grados a la derecha

for turno in range(100): 
    troja.forward(random.randint(1, 5)) 
    tazul.forward(random.randint(1, 5))  
    tamarilla.forward(random.randint(1, 5)) 
    tnaranja.forward(random.randint(1, 5)) 
## Agrega las dos tortugas adicionales arriba

if troja.xcor() > tazul.xcor() and troja.xcor() > tamarilla.xcor() and troja.xcor() > tnaranja.xcor():
    troja.write("      TORTUGA ROJA GANADORA!")
    time.sleep(3)
elif t.azul.xcor() > troja.xcor() and tazul.xcor() > tamarilla.xcor() and tazul.xcor() > tnaranja.xcor():
    tazul.write("      TORTUGA AZUL GANADORA!")
    time.sleep(3)
elif t.amarilla.xcor() > troja.xcor() and tamarilla.xcor() > tazul.xcor() and tamarilla.xcor() > tnaranja.xcor():
    tamarilla.write("      TORTUGA AMARILLA GANADORA!")
    time.sleep(3)
elif t.naranja.xcor() > troja.xcor() and tnaranja.xcor() > tamarilla.xcor() and tnaranja.xcor() > tazul.xcor():
    tnaranja.write("      TORTUGA NARANJA GANADORA!")
    time.sleep(3)

## Opcional: Poner la tortuga ganadora de las 4
pensize(1)
fillcolor("black")
begin_fill()
goto(-160,0)
goto(-100,-50)
goto(0,-50)
goto(0,0)
end_fill()
