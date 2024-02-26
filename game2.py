import pgzrun
import random

class Hero(Actor):
    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
    pass

HEIGHT = 500
WIDTH = 800

p = Hero('ironman', (100, 100))
b = Rect((300, 100), (50, 50))
def draw():
    screen.fill('white')
    p.draw()
    screen.draw.filled_rect(b, 'blue')
def update():
    p.move(dx=3)
    pass
pgzrun.go()