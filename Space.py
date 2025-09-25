import pgzrun
import random
from time import time

WIDTH = 800
HEIGHT=600

nextsat = 0
linepoints=[]
starttime = 0
totaltime = 0
endtime=0
starttime=time()
sats = []
for i in range(8):
    sat = Actor("sat")
    sat.pos=(random.randint(50,750),random.randint(50,550))
    sats.append(sat)

def draw():
    screen.blit("space", (0,0))
    for i in range(8):
        sats[i].draw()
        screen.draw.text(str(i+1), center = (sats[i].x, sats[i].y+30), fontsize = 30)
    totaltime=round(time()-starttime)
    screen.draw.text(str(totaltime), center = (50,50), fontsize = 50)

    # screen.draw.line((7,3), (80,500), "white")
    for i in linepoints:
        screen.draw.line(i[0], i[1], "white")

def update():
    pass

def on_mouse_down(pos):
    global nextsat, linepoints
    if nextsat < 8:
        if sats[nextsat].collidepoint(pos):
            if nextsat:
                linepoints.append((sats[nextsat-1].pos, sats[nextsat].pos))
            nextsat = nextsat+1
        else:
            nextsat = 0
            linepoints = []
        for i in linepoints:
            print(i)
pgzrun.go()