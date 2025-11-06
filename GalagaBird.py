import pgzrun, time

WIDTH = 1200
HEIGHT = 800

bullet = Actor("bird")
rock = Actor("slingshot")
rock.pos = 600,750
bee = Actor("piggy")

bees=[]
bullets=[]
winner=Actor("galagawon2")

r1 = True
r2 = False
r3 = False
r4 = False
r5 = False

gameover = False
nextrow = True
move_target_y = 0
bspeed = 1
hit = 0

for i in range(5):
    for e in range(4):
        bees.append(Actor("piggy"))
        bees[-1].y = 10+90*i
        bees[-1].x =440+85*e

def draw():
    screen.blit("galagabg2", (0,0))
    for i in bees:
        i.draw()
    rock.draw()
    for i in bullets:
        i.draw()
    screen.draw.text(str(hit), center = (20,20), fontsize = 50)
    if gameover == True:
        screen.blit("galagaover2", (0,0))
    if len(bees)==0:
        winner.draw()

def update():
    global r1,r2, r3, r4, r5, nextrow, move_target_y, hit,gameover
    if keyboard.left and rock.x>50:
        rock.x = rock.x - 7
    if keyboard.right and rock.x<1150:
        rock.x = rock.x + 7
    for b in bullets:
        if b.y <= 0:
            bullets.remove(b)
        else:
            b.y = b.y - 5

    for be in bees:
        be.y += bspeed
        for b in bullets:
            if be.colliderect(b):
                bullets.remove(b)
                bees.remove(be)
                hit = hit + 1
                
        if rock.colliderect(be):
            gameover = True
            bees.remove(be)
            rock.pos = (1000,1000)


def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bird"))
        bullets[-1].x = rock.x
        bullets[-1].y = rock.y


pgzrun.go()