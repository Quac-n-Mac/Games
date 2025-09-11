import pgzrun
import random

WIDTH = 750
HEIGHT = 750

bee = Actor("bee")
bee.pos = (100,100)

flower = Actor("flower")
flower.pos = (random.randint(40, 710), random.randint(40, 710))

score = 0
messege = "Pollen: " + str(score)

gameover = False
def gametime():
    global gameover
    gameover = True

def draw():
    global score
    screen.blit("grass_bg", (0,0))
    bee.draw()
    flower.draw()
    screen.draw.text(messege, center = (660, 30), fontsize = 45)

    if gameover == True:
        screen.fill("palegreen2")
        screen.draw.text(("Game Over, collected Pollen: " + str(score)), center = (350, 50), fontsize = 50)

def update():
    global score,messege
    if keyboard.left and bee.x >=40:
        bee.x = bee.x - 5
    if keyboard.right and bee.x <= 710:
        bee.x = bee.x + 5
    if keyboard.up and bee.y >=40:
        bee.y = bee.y - 5
    if keyboard.down and bee.y <= 710:
        bee.y = bee.y + 5
    if abs(bee.x - flower.x)  <= 25 and abs(bee.y - flower.y) <= 45:
        flower.pos = (random.randint(40, 710), random.randint(40, 710))
        score = score + 10
        messege = "Pollen: " + str(score)
        
clock.schedule(gametime, 10.0)
pgzrun.go()