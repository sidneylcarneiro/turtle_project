import turtle

cor = "green"
cor_bg = "white"

# Configura a tela com tamanho 1200x600
screen = turtle.Screen()
screen.setup(width=1200, height=600)
screen.title("Desenho do 'Olá Mundo!'")
screen.bgcolor(cor_bg)

# Cria uma tartaruga
t = turtle.Turtle()
t.speed(25)  # Define uma velocidade para visualização
t.penup()
t.hideturtle()

def draw_hollow_O(tartaruga, x, y, outer_radius, inner_radius, color=cor):
    """
    Desenha a letra "O" com um contorno oco.

    Args:
        tartaruga (turtle.Turtle): O objeto Turtle para desenhar.
        x (float): Coordenada x da posição inicial do "O".
        y (float): Coordenada y da posição inicial do "O".
        outer_radius (float): Raio do círculo externo do "O".
        inner_radius (float): Raio do círculo interno do "O".
        color (str): Cor do contorno do "O". Padrão é "black".
    """
    tartaruga.goto(x, y - outer_radius)  # Move para a base do círculo maior
    tartaruga.pendown()
    tartaruga.color(color)
    tartaruga.begin_fill()
    tartaruga.circle(outer_radius)  # Desenha o círculo externo
    tartaruga.end_fill()
    
    # Desenha o círculo interno
    tartaruga.goto(x, y - inner_radius)  # Move para a base do círculo interno
    tartaruga.color(cor_bg)
    tartaruga.begin_fill()
    tartaruga.circle(inner_radius)  # Desenha o círculo interno
    tartaruga.end_fill()
    
    tartaruga.penup()

def draw_l(tartaruga, x, y, width, height, color=cor):
    """
    Desenha a letra "L".

    Args:
        tartaruga (turtle.Turtle): O objeto Turtle para desenhar.
        x (float): Coordenada x da posição inicial do "L".
        y (float): Coordenada y da posição inicial do "L".
        width (float): Largura da base do "L".
        height (float): Altura do bastão do "L".
        color (str): Cor do "L". Padrão é "black".
    """
    tartaruga.goto(x, y)  # Move para o topo do "l"
    tartaruga.pendown()
    tartaruga.color(color)
    
    # Desenha o bastão do "l"
    tartaruga.begin_fill()
    tartaruga.left(90)
    tartaruga.forward(height)  # Desenha a parte vertical do bastão do "l"
    tartaruga.right(90)
    tartaruga.forward(width+20)  # Desenha a base do "l"
    tartaruga.right(90)
    tartaruga.forward(height)  # Completa a parte vertical do bastão
    tartaruga.right(90)
    tartaruga.forward(width+20)  # Completa a base do bastão
    tartaruga.end_fill()
    
    # Desenha a ponta do "l"
    tartaruga.penup()
    tartaruga.pendown()
    tartaruga.begin_fill()
    tartaruga.forward(width - 5)  # Desenha a base da ponta
    tartaruga.right(90)
    tartaruga.forward(15)  # Desenha a altura da ponta
    tartaruga.right(90)
    tartaruga.forward(width - 5)  # Completa a base da ponta
    tartaruga.right(90)
    tartaruga.forward(15)  # Completa a altura da ponta
    tartaruga.end_fill()
    
    tartaruga.penup()

def draw_lambda_A(tartaruga, x, y, size, thickness, color=cor):
    """
    Desenha a letra "A" estilizada como o símbolo Lambda.

    Args:
        tartaruga (turtle.Turtle): O objeto Turtle para desenhar.
        x (float): Coordenada x da posição inicial do "A".
        y (float): Coordenada y da posição inicial do "A".
        size (float): Tamanho do triângulo externo e interno do "A".
        thickness (float): Espessura da linha do retângulo horizontal no meio.
        color (str): Cor do "A". Padrão é "black".
    """
    half_size = size / 2
    inner_size = size - thickness
    inner_height = size - thickness * 1.5
    rect_length = inner_size * 0.7

    # Desenha o triângulo preto externo
    tartaruga.penup()
    tartaruga.goto(x - half_size, y)  # Move para a base do triângulo externo
    tartaruga.setheading(60)  # Define a orientação para cima
    tartaruga.pendown()
    tartaruga.color(color)
    tartaruga.begin_fill()
    tartaruga.forward(size)
    tartaruga.right(120)
    tartaruga.forward(size)
    tartaruga.right(120)
    tartaruga.forward(size)
    tartaruga.end_fill()

    # Desenha o triângulo branco interno
    tartaruga.penup()
    tartaruga.goto(x - (inner_size / 2), y - inner_height / 4)  # Move para a base do triângulo branco interno
    tartaruga.setheading(60)
    tartaruga.pendown()
    tartaruga.color(cor_bg)
    tartaruga.begin_fill()
    tartaruga.forward(inner_size)
    tartaruga.right(120)
    tartaruga.forward(inner_size)
    tartaruga.right(120)
    tartaruga.forward(inner_size)
    tartaruga.end_fill()

    # Desenha a linha horizontal preta no meio (retângulo)
    tartaruga.penup()
    tartaruga.goto(x - (rect_length / 2), y + thickness + 20)  # Ajusta a posição inicial
    tartaruga.setheading(0)
    tartaruga.pendown()
    tartaruga.color(color)
    tartaruga.begin_fill()
    tartaruga.forward(rect_length)
    tartaruga.right(90)
    tartaruga.forward(thickness)
    tartaruga.right(90)
    tartaruga.forward(rect_length)
    tartaruga.right(90)
    tartaruga.forward(thickness)
    tartaruga.end_fill()

    tartaruga.penup()

def draw_accent(tartaruga, x, y, length, thickness, color=cor):
    """
    Desenha um acento agudo sobre a letra "A".

    Args:
        tartaruga (turtle.Turtle): O objeto Turtle para desenhar.
        x (float): Coordenada x da posição inicial do acento.
        y (float): Coordenada y da posição inicial do acento.
        length (float): Comprimento do acento.
        thickness (float): Espessura do acento.
        color (str): Cor do acento. Padrão é "black".
    """
    # Desenha o acento agudo como um retângulo fino com altura reduzida
    tartaruga.goto(x - length / 2, y)  # Move para o início do acento
    tartaruga.setheading(60)  # Define a inclinação do acento
    tartaruga.pendown()
    tartaruga.color(color)
    tartaruga.begin_fill()
    tartaruga.forward(length)
    tartaruga.right(90)
    tartaruga.forward(thickness / 2)
    tartaruga.right(90)
    tartaruga.forward(length)
    tartaruga.right(90)
    tartaruga.forward(thickness / 2)
    tartaruga.end_fill()
    tartaruga.penup()

def draw_m(tartaruga, x, y, size, color=cor):
    """
    Desenha a letra "M".

    Args:
        tartaruga (turtle.Turtle): O objeto Turtle para desenhar.
        x (float): Coordenada x da posição inicial do "M".
        y (float): Coordenada y da posição inicial do "M".
        size (float): Tamanho do "M".
        color (str): Cor do "M". Padrão é "black".
    """
    tartaruga.penup()
    tartaruga.goto(x, y)  # Move a tartaruga para a posição inicial
    tartaruga.pendown()
    tartaruga.width(size / 6)  # Define a espessura do traço, proporcional ao tamanho do "M"
    tartaruga.color(color)

    # Desenha o "M"
    tartaruga.setheading(90)  # Gira para cima
    tartaruga.forward(size)  # Linha vertical esquerda

    tartaruga.right(135)  # Prepara para desenhar a diagonal
    tartaruga.forward(size * 0.8)  # Linha diagonal esquerda para o meio

    tartaruga.left(90)  # Prepara para a segunda diagonal
    tartaruga.forward(size * 0.8)  # Linha diagonal direita para o meio

    tartaruga.right(135)  # Prepara para a linha vertical direita
    tartaruga.forward(size)  # Linha vertical direita

    tartaruga.penup()

def draw_u(tartaruga, x, y, size, color=cor):
    """
    Desenha a letra "U".

    Args:
        tartaruga (turtle.Turtle): O objeto Turtle para desenhar.
        x (float): Coordenada x da posição inicial do "U".
        y (float): Coordenada y da posição inicial do "U".
        size (float): Tamanho total do "U".
        color (str): Cor do "U". Padrão é "black".
    """
    tartaruga.penup()
    tartaruga.goto(x, y)  # Posição inicial
    tartaruga.pendown()
    tartaruga.color(color)

    tartaruga.pensize(size / 3.5)  # Define a largura da caneta proporcional ao tamanho

    # Ajusta a altura e raio da curva com base no tamanho
    height = size * 2 / 3
    radius = size / 2

    tartaruga.setheading(270)  # Direciona a tartaruga para baixo
    tartaruga.forward(height)  # Desenha a primeira linha reta para baixo

    tartaruga.circle(radius, 180)  # Desenha a curva da parte inferior

    tartaruga.forward(height)  # Desenha a segunda linha reta para cima

def draw_n(tartaruga, x, y, size, color=cor):
    """
    Desenha a letra "N".

    Args:
        tartaruga (turtle.Turtle): O objeto Turtle para desenhar.
        x (float): Coordenada x da posição inicial do "N".
        y (float): Coordenada y da posição inicial do "N".
        size (float): Tamanho total do "N".
        color (str): Cor do "N". Padrão é "black".
    """
    tartaruga.penup()
    tartaruga.goto(x, y)  # Move para a posição inicial
    tartaruga.pendown()
    tartaruga.color(color)
    tartaruga.pensize(size / 5)  # Define a espessura da linha
    
    # Desenha o "N"
    tartaruga.setheading(90)  # Define a direção inicial para cima
    tartaruga.forward(size)  # Desenha a linha vertical esquerda

    tartaruga.right(135)  # Ajusta a direção para desenhar a diagonal
    tartaruga.forward(size * 1.414)  # Desenha a linha diagonal (tamanho * sqrt(2))

    tartaruga.left(135)  # Ajusta a direção para desenhar a linha vertical direita
    tartaruga.forward(size)  # Desenha a linha vertical direita
    
    tartaruga.penup()

def draw_d(tartaruga, x, y, size, color=cor):
    """
    Desenha a letra "D".

    Args:
        tartaruga (turtle.Turtle): O objeto Turtle para desenhar.
        x (float): Coordenada x da posição inicial do "D".
        y (float): Coordenada y da posição inicial do "D".
        size (float): Tamanho total do "D".
        color (str): Cor do "D". Padrão é "black".
    """
    tartaruga.penup()
    tartaruga.goto(x, y)
    tartaruga.pendown()
    tartaruga.pensize(15)
    tartaruga.setheading(90)
    tartaruga.forward(size)
    tartaruga.right(90)
    tartaruga.goto(x, y)
    tartaruga.right(0)
    tartaruga.forward(size / 3)
    tartaruga.penup()
    tartaruga.goto(x, y + size)
    tartaruga.pendown()
    tartaruga.forward(size / 3)
    tartaruga.circle(-size / 2, 180)
    tartaruga.penup()
    
def draw_exclamation(tartaruga, x, y, size, color=cor):
    """
    Desenha o símbolo de exclamação "!".

    Args:
        tartaruga (turtle.Turtle): O objeto Turtle para desenhar.
        x (float): Coordenada x da posição inicial do símbolo.
        y (float): Coordenada y da posição inicial do símbolo.
        size (float): Tamanho total do símbolo.
        color (str): Cor do símbolo. Padrão é "black".
    """
    tartaruga.penup()
    tartaruga.goto(x, y)  # Move para a posição inicial
    tartaruga.pendown()
    tartaruga.color(color)
    tartaruga.pensize(size / 10)  # Define a espessura da linha
    
    tartaruga.setheading(90)  # Direção para cima
    tartaruga.forward(size - 50)  # Desenha a linha do ponto de exclamação
    
    tartaruga.setheading(0)  # Alinha para desenhar o ponto
    tartaruga.penup()
    tartaruga.goto(x, y - size * 0.2)  # Move para a posição do ponto
    tartaruga.pendown()
    tartaruga.dot(size / 5)  # Desenha o ponto
    
    tartaruga.penup()

def draw_b(tartaruga, x, y, size, color=cor):
    tartaruga.goto(x, y)  # Move para o topo do "b"
    tartaruga.pendown()
    tartaruga.color(color)
    # Desenha o bastão do "b"
    tartaruga.begin_fill()
    tartaruga.left(90)
    tartaruga.forward(size)  # Desenha a parte vertical do bastão do "l"
    tartaruga.right(90)
    tartaruga.forward(20)  # Desenha a base do "l"
    tartaruga.right(90)
    tartaruga.forward(size)  # Completa a parte vertical do bastão
    tartaruga.right(90)
    tartaruga.forward(20)  # Completa a base do bastão
    tartaruga.end_fill()
    tartaruga.penup()
    draw_d(tartaruga, x=x+10, y=y+103, size=size)
    draw_d(tartaruga, x=x+10, y=y+6, size=size)


# Desenha as letras e símbolo
draw_hollow_O(t, x=-500, y=0, outer_radius=80, inner_radius=60)
draw_hollow_O(t, x=450, y=-28, outer_radius=50, inner_radius=35)
draw_l(t, x=-380, y=-75, width=-40, height=100)
draw_lambda_A(t, x=-260, y=-75, size=120, thickness=20)
draw_accent(t, x=-230, y=50, length=30, thickness=40)
draw_m(t, x=-90, y=-70, size=120)
draw_u(t, x=85, y=15, size=70)
draw_n(t, x=190, y=-65, size=80)
draw_d(t, x=310, y=-65, size=80)
draw_exclamation(t, x=530, y=-30, size=150)


#desenhar Bom dia! 
"""
t.goto(0, 0)  # Move para o topo do "l"
t.pendown()
t.color(cor)
# Desenha o bastão do "b"
t.begin_fill()
t.left(90)
t.forward(200)  # Desenha a parte vertical do bastão do "l"
t.right(90)
t.forward(20)  # Desenha a base do "l"
t.right(90)
t.forward(200)  # Completa a parte vertical do bastão
t.right(90)
t.forward(20)  # Completa a base do bastão
t.end_fill()
t.penup()
draw_d(t, x=10, y=103, size=90)
draw_d(t, x=10, y=6, size=90)

draw_b(t, 0, 0, 300)
"""
# Fecha a tela ao clicar
screen.exitonclick()
