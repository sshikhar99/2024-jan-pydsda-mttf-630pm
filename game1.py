from turtle import Screen
import pgzrun

WIDTH = 800
HEIGHT = 500

def draw():
    Screen.draw.text(
        "Hello, Pygame Zero!",
        center=(WIDTH/2, HEIGHT/2),
        fontsize=32,
        color="white"
    )

def update():
    pass

pgzrun.go()