import pgzrun, random, time

WIDTH = 1200
HEIGHT = 800

nameitems = ["paper", "bottle", "battery", "chips"]

animations = []
curlv = 1
gameover = False
gamewin = False
startspeed = 10
decrease_duration = 0.5
collected = 0
items = []

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create = ["paper"]
    for i in range(number_of_extra_items):
        item = random.choice(nameitems)
        items_to_create.append(item)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for i in items_to_create:
        item = Actor(i)
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    random.shuffle(items_to_layout)
    number_of_gaps = len(items_to_layout)+1
    gap_size = WIDTH/number_of_gaps
    for index, item in enumerate(items_to_layout):
        new_x_pos = (index + 1) * gap_size
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations, decrease_duration
    for item in items_to_animate:
        duration = startspeed - curlv - decrease_duration
        item.anchor = ("center", "bottom")
        animation = animate(item, duration = duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global gameover
    gameover = True

def on_mouse_down(pos):
    global items, curlv, collected
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
                collected = collected + 1
            else:
                handle_game_over()

def handle_game_complete():
    global gamewin, items, animations, curlv, decrease_duration
    stop_animations(animations)
    if curlv == 5:
        gamewin=True
    else:
        curlv = curlv+1
        items = []
        animations = []
        decrease_duration = decrease_duration + 0.5

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()


def draw():
    screen.clear()
    screen.blit("ecobg", (0,0))
    if gameover == True:
        screen.draw.text("Game Over", center = (600, 400), fontsize=100, color = "blue")
        screen.draw.text("You got "+str(collected), center = (600, 200), fontsize=80, color = "blue")
    elif gamewin == True:
        screen.draw.text("You Win", center = (600,400), fontsize=100, color = "yellow")
        screen.draw.text("You got all 5", center = (600,200), fontsize=80, color = "yellow")
    else:
        for item in items:
            item.draw()


def update():
    global items
    if len(items)==0:
        items = make_items(curlv)

pgzrun.go()