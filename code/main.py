from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

from menu import start

# Criando a Janela:
janela = Window(1200, 704)
janela.set_title("Menu")

comprimento_janela = janela.width
altura_janela = janela.height

# Criando imagem de fundo:
img_fundo = GameImage("sprites/1200x704.jpeg")

# Criando o Zeca
zeca = Sprite("sprites/Parado.png")
zeca.set_position(250, 500)

velocidade_zeca = 500

contador_tempo = 0
vazio = False
# Game Loop:
while True:

    # Entrada de dados:
    if janela.get_keyboard().key_pressed("enter"):
        start()

    if janela.get_keyboard().key_pressed("right"):
        zeca.x += velocidade_zeca*janela.delta_time()
    # Update:
    contador_tempo += janela.delta_time()
    if contador_tempo >= 0.25:
        vazio = not vazio
        contador_tempo = 0

    # Desenho:

    # Desenhando imagem de fundo:
    img_fundo.draw()

    # Desenhando o sprite:
    zeca.draw()

    # Desenhando o texto:
    janela.draw_text("Sacode's Gang", (janela.width - 450) / 2, 200, size=100, color=("yellow"),
                     font_name="Ancient Modern Tales",
                     bold=False, italic=False)

    janela.draw_text("Pressione <Enter> para iniciar", (janela.width - 500) / 2, 450, size=35,
                     color=("black" if not vazio else "white"), font_name="connection ii",
                     bold=False, italic=False)

    # Swap Buffer:
    janela.update()
