import pgzrun

WIDTH = 1200
HEIGHT = 800

bullet = Actor("bullet")
rock = Actor("rocket")
rock.pos = 600,750
bee = Actor("fly")

bees=[]
bullets=[]
for i in range(5):
    for e in range(4):
        bees.append(Actor("fly"))
        bees[-1].y = 100+60*i
        bees[-1].x =440+80*e

def draw():
    screen.blit("space", (0,0))
    for i in bees:
        i.draw()
    rock.draw()
    for i in bullets:
        i.draw()

def update():
    if keyboard.left and rock.x>50:
        rock.x = rock.x - 7
    if keyboard.right and rock.x<1150:
        rock.x = rock.x + 7
    for b in bullets:
        if b.y <= 0:
            bullets.remove(b)
        else:
            b.y = b.y - 5
    for i in range(0,5):
        bees[i].y= bees[i].y + 0.4
    for i in range(5,8):
        bees[i].y= bees[i].y + 0.4

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = rock.x
        bullets[-1].y = rock.y


pgzrun.go()
