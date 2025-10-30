import pgzrun, time

WIDTH = 1200
HEIGHT = 800

bullet = Actor("bullet")
rock = Actor("rocket")
rock.pos = 600,750
bee = Actor("fly")

bees=[]
bullets=[]
frames=["space_won1","space_won2","space_won3","space_won4","space_won5","space_won6","space_won7","space_won8"]
curframe = 0
winner=Actor(frames[curframe],(0,0))

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
        bees.append(Actor("fly"))
        bees[-1].y = 10+90*i
        bees[-1].x =440+85*e

def draw():
    screen.blit("space", (0,0))
    for i in bees:
        i.draw()
    rock.draw()
    for i in bullets:
        i.draw()
    screen.draw.text(str(hit), center = (20,20), fontsize = 50)
    if gameover == True:
        screen.blit("space_over", (0,0))
    # elif len(bees) == 0:
    #     screen.blit("space_won1",(0,0))
    #     time.sleep(1)
    #     screen.blit("space_won2",(0,0))
    #     time.sleep(1)
    #     screen.blit("space_won3",(0,0))
    #     time.sleep(0.1)
    #     screen.blit("space_won4",(0,0))
    #     time.sleep(0.1)
    #     screen.blit("space_won5",(0,0))
    #     time.sleep(0.1)
    #     screen.blit("space_won6",(0,0))
    #     time.sleep(0.1)
    #     screen.blit("space_won7",(0,0))
    #     time.sleep(0.1)
    #     screen.blit("space_won8",(0,0))
    if len(bees)==0:
        winner.draw()

def update():
    global r1,r2, r3, r4, r5, nextrow, move_target_y, hit,gameover,curframe
    if len(bees) == 0:
        curframe = (curframe+1)%len(frames)
        winner.image = frames[curframe]

    if keyboard.left and rock.x>50:
        rock.x = rock.x - 7
    if keyboard.right and rock.x<1150:
        rock.x = rock.x + 7
    for b in bullets:
        if b.y <= 0:
            bullets.remove(b)
        else:
            b.y = b.y - 5

    

    # if r1 == True:
        # if nextrow == True:
        #     move_target_y = bees[0].y + bspeed
        #     nextrow = False
        # if bees[0].y < move_target_y:
        #     for i in range(0, 4):
        #         bees[i].y += 1
    #     else:
    #         r1 = False
    #         r2 = True
    #         nextrow = True
    # elif r2 == True:
    #     if nextrow == True:
    #         move_target_y = bees[4].y + bspeed
    #         nextrow = False
    #     if bees[4].y < move_target_y:
    #         for i in range(4, 8):
    #             bees[i].y += 1
    #     else:
    #         r2 = False
    #         r3 = True
    #         nextrow = True
    # elif r3 == True:
    #     if nextrow == True:
    #         move_target_y = bees[8].y + bspeed
    #         nextrow = False
    #     if bees[8].y < move_target_y:
    #         for i in range(8, 12):
    #             bees[i].y += 1
    #     else:
    #         r3 = False
    #         r4 = True
    #         nextrow = True
    # elif r4 == True:
    #     if nextrow == True:
    #         move_target_y = bees[12].y + bspeed
    #         nextrow = False
    #     if bees[12].y < move_target_y:
    #         for i in range(12, 16):
    #             bees[i].y += 1
    #     else:
    #         r4 = False
    #         r5 = True
    #         nextrow = True
    # elif r5 == True:
    #     if nextrow == True:
    #         move_target_y = bees[16].y + bspeed
    #         nextrow = False
    #     if bees[16].y < move_target_y:
    #         for i in range(16, 20):
    #             bees[i].y += 1
    #     else:
    #         r5 = False
    #         r1 = True
    #         nextrow = True
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
        bullets.append(Actor("bullet"))
        bullets[-1].x = rock.x
        bullets[-1].y = rock.y


pgzrun.go()