import pgzrun, random, itertools, time

WIDTH = 400
HEIGHT = 400

blockpos = [(50,50), (350,50), (350, 350), (50,350)]

blockcycle = itertools.cycle(blockpos)
Rock = Actor("rat")
Block = Actor("animmetal")
Rock.pos = (150,150)
Block.pos = (50,50)

def moveblock():
    animate(Block, "bounce_end", duration=1, pos=next(blockcycle))
moveblock()
clock.schedule_interval(moveblock,0.9)

def shipposangle():
    x =random.randint(80,320)
    y =random.randint(80,320)
    Rock.target=x,y
    targetangle=Rock.angle_to(Rock.target)
    targetangle+=360*((Rock.angle-targetangle+180)//360)
    animate(Rock, angle=targetangle, duration=1, on_finished=moverock)

def moverock():
    animate(Rock,tween="accel_decel", pos=Rock.target, duration=Rock.distance_to(Rock.target)/300, on_finished=shipposangle)
shipposangle()


def draw():
    screen.fill("black")
    Rock.draw()
    Block.draw()
def update():
    pass

pgzrun.go()