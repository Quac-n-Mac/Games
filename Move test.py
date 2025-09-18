import pgzrun
import random

WIDTH = 1152
HEIGHT = 648

char = Actor("char")
char.pos = (100,100)

ground = Actor("ground")
ground.pos = (WIDTH/2,648)

grav = 3

def draw():
    screen.fill("lightblue1")
    char.draw()
    ground.draw()

def update():
    global grav
    if keyboard.left and char.x >=40:
        char.x = char.x - 5
    if keyboard.right and char.x <= 710:
        char.x = char.x + 5
    if keyboard.up and char.y >=40:
        char.y = char.y - 5

    char.y = char.y + grav

    if abs(char.y - ground.y) <= 95:
        char.y = 550

pgzrun.go()