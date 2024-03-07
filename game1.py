<<<<<<< HEAD
from turtle import Screen
=======
# pip install pgzero
>>>>>>> d5e9b39cb9910f3de65af2522a3b16be51dfd2cf
import pgzrun

WIDTH = 800
HEIGHT = 500

def draw():
<<<<<<< HEAD
    Screen.draw.text(
=======
    screen.draw.text(
>>>>>>> d5e9b39cb9910f3de65af2522a3b16be51dfd2cf
        "Hello, Pygame Zero!",
        center=(WIDTH/2, HEIGHT/2),
        fontsize=32,
        color="white"
    )

def update():
    pass

pgzrun.go()