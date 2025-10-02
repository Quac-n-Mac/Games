import pgzrun
import random

WIDTH = 1152
HEIGHT = 648

char = Actor("char")
char.pos = (100,100)

enemy1 = Actor("enemy")
enemy1.pos = (300,550)

enemy2 = Actor("enemy")
enemy2.pos = (400,550)

enemy3 = Actor("enemy")
enemy3.pos = (500,550)

enemy4 = Actor("enemy")
enemy4.pos = (600,550)

enemy5 = Actor("enemy")
enemy5.pos = (700,550)

ground = Actor("ground")
ground.pos = (WIDTH/2,648)

powerup = Actor("powerup")
powerup.pos = (800, 550)

grav = 3
enespeed = 3

HORIZ_COLLIDE_DIST = 60
VERTICAL_DEFEAT_DIST = 85

enemies_defeated = 0
powerup_active = False
game_over = False
you_won = False

def draw():
    global game_over
    global you_won

    if game_over:
        screen.fill("brown2")
        screen.draw.text("Game over", center=(WIDTH/2, HEIGHT/2), color="black", fontsize=100)
    elif you_won:
        screen.fill("chartreuse")
        screen.draw.text("You Won!", center=(WIDTH/2, HEIGHT/2), color="darkgoldenrod1", fontsize=100)
    else:
        screen.blit('sky', (0, 0))
        char.draw()
        if enemy1.x != -1000:
            enemy1.draw()
        if enemy2.x != -1000:
            enemy2.draw()
        if enemy3.x != -1000:
            enemy3.draw()
        if enemy4.x != -1000:
            enemy4.draw()
        if enemy5.x != -1000:
            enemy5.draw()
        ground.draw()
        if not powerup_active:
            powerup.draw()
        screen.draw.text(f"Enemies defeated: {enemies_defeated}", center=(WIDTH/2, 30), color="black", fontsize=40)

def update():
    global grav
    global enespeed
    global enemies_defeated
    global powerup_active
    global game_over
    global you_won

    if game_over or you_won:
        return

    if keyboard.left and char.x >=40:
        char.x = char.x - 5
    if keyboard.right and char.x <= 1100:
        char.x = char.x + 5
    if keyboard.up and char.y >=40:
        char.y = char.y - 5

    if not powerup_active and char.colliderect(powerup):
        powerup_active = True
        powerup.pos = (-1000, -1000)

    player_on_ground = False
    if abs(char.y - ground.y) <= 95:
        char.y = 553
        player_on_ground = True

    if not player_on_ground:
        char.y = char.y + grav

    if enemy1.x != -1000:
        move_e1_x = 0
        if enemy1.x >= char.x:
            move_e1_x = -enespeed
        elif enemy1.x <= char.x:
            move_e1_x = enespeed

        can_e1_move = True
        new_e1_x = enemy1.x + move_e1_x

        if abs(new_e1_x - char.x) < HORIZ_COLLIDE_DIST and abs(enemy1.y - char.y) < VERTICAL_DEFEAT_DIST:
            can_e1_move = False
        if enemy2.x != -1000 and abs(new_e1_x - enemy2.x) < HORIZ_COLLIDE_DIST and abs(enemy1.y - enemy2.y) < VERTICAL_DEFEAT_DIST:
            can_e1_move = False
        if enemy3.x != -1000 and abs(new_e1_x - enemy3.x) < HORIZ_COLLIDE_DIST and abs(enemy1.y - enemy3.y) < VERTICAL_DEFEAT_DIST:
            can_e1_move = False
        if enemy4.x != -1000 and abs(new_e1_x - enemy4.x) < HORIZ_COLLIDE_DIST and abs(enemy1.y - enemy4.y) < VERTICAL_DEFEAT_DIST:
            can_e1_move = False
        if enemy5.x != -1000 and abs(new_e1_x - enemy5.x) < HORIZ_COLLIDE_DIST and abs(enemy1.y - enemy5.y) < VERTICAL_DEFEAT_DIST:
            can_e1_move = False

        if can_e1_move:
            enemy1.x = new_e1_x

    if enemy2.x != -1000:
        move_e2_x = 0
        if enemy2.x >= char.x:
            move_e2_x = -enespeed
        elif enemy2.x <= char.x:
            move_e2_x = enespeed

        can_e2_move = True
        new_e2_x = enemy2.x + move_e2_x

        if abs(new_e2_x - char.x) < HORIZ_COLLIDE_DIST and abs(enemy2.y - char.y) < VERTICAL_DEFEAT_DIST:
            can_e2_move = False
        if enemy1.x != -1000 and abs(new_e2_x - enemy1.x) < HORIZ_COLLIDE_DIST and abs(enemy2.y - enemy1.y) < VERTICAL_DEFEAT_DIST:
            can_e2_move = False
        if enemy3.x != -1000 and abs(new_e2_x - enemy3.x) < HORIZ_COLLIDE_DIST and abs(enemy2.y - enemy3.y) < VERTICAL_DEFEAT_DIST:
            can_e2_move = False
        if enemy4.x != -1000 and abs(new_e2_x - enemy4.x) < HORIZ_COLLIDE_DIST and abs(enemy2.y - enemy4.y) < VERTICAL_DEFEAT_DIST:
            can_e2_move = False
        if enemy5.x != -1000 and abs(new_e2_x - enemy5.x) < HORIZ_COLLIDE_DIST and abs(enemy2.y - enemy5.y) < VERTICAL_DEFEAT_DIST:
            can_e2_move = False

        if can_e2_move:
            enemy2.x = new_e2_x

    if enemy3.x != -1000:
        move_e3_x = 0
        if enemy3.x >= char.x:
            move_e3_x = -enespeed
        elif enemy3.x <= char.x:
            move_e3_x = enespeed

        can_e3_move = True
        new_e3_x = enemy3.x + move_e3_x

        if abs(new_e3_x - char.x) < HORIZ_COLLIDE_DIST and abs(enemy3.y - char.y) < VERTICAL_DEFEAT_DIST:
            can_e3_move = False
        if enemy1.x != -1000 and abs(new_e3_x - enemy1.x) < HORIZ_COLLIDE_DIST and abs(enemy3.y - enemy1.y) < VERTICAL_DEFEAT_DIST:
            can_e3_move = False
        if enemy2.x != -1000 and abs(new_e3_x - enemy2.x) < HORIZ_COLLIDE_DIST and abs(enemy3.y - enemy2.y) < VERTICAL_DEFEAT_DIST:
            can_e3_move = False
        if enemy4.x != -1000 and abs(new_e3_x - enemy4.x) < HORIZ_COLLIDE_DIST and abs(enemy3.y - enemy4.y) < VERTICAL_DEFEAT_DIST:
            can_e3_move = False
        if enemy5.x != -1000 and abs(new_e3_x - enemy5.x) < HORIZ_COLLIDE_DIST and abs(enemy3.y - enemy5.y) < VERTICAL_DEFEAT_DIST:
            can_e3_move = False

        if can_e3_move:
            enemy3.x = new_e3_x

    if enemy4.x != -1000:
        move_e4_x = 0
        if enemy4.x >= char.x:
            move_e4_x = -enespeed
        elif enemy4.x <= char.x:
            move_e4_x = enespeed

        can_e4_move = True
        new_e4_x = enemy4.x + move_e4_x

        if abs(new_e4_x - char.x) < HORIZ_COLLIDE_DIST and abs(enemy4.y - char.y) < VERTICAL_DEFEAT_DIST:
            can_e4_move = False
        if enemy1.x != -1000 and abs(new_e4_x - enemy1.x) < HORIZ_COLLIDE_DIST and abs(enemy4.y - enemy1.y) < VERTICAL_DEFEAT_DIST:
            can_e4_move = False
        if enemy2.x != -1000 and abs(new_e4_x - enemy2.x) < HORIZ_COLLIDE_DIST and abs(enemy4.y - enemy2.y) < VERTICAL_DEFEAT_DIST:
            can_e4_move = False
        if enemy3.x != -1000 and abs(new_e4_x - enemy3.x) < HORIZ_COLLIDE_DIST and abs(enemy4.y - enemy3.y) < VERTICAL_DEFEAT_DIST:
            can_e4_move = False
        if enemy5.x != -1000 and abs(new_e4_x - enemy5.x) < HORIZ_COLLIDE_DIST and abs(enemy4.y - enemy5.y) < VERTICAL_DEFEAT_DIST:
            can_e4_move = False

        if can_e4_move:
            enemy4.x = new_e4_x

    if enemy5.x != -1000:
        move_e5_x = 0
        if enemy5.x >= char.x:
            move_e5_x = -enespeed
        elif enemy5.x <= char.x:
            move_e5_x = enespeed

        can_e5_move = True
        new_e5_x = enemy5.x + move_e5_x

        if abs(new_e5_x - char.x) < HORIZ_COLLIDE_DIST and abs(enemy5.y - char.y) < VERTICAL_DEFEAT_DIST:
            can_e5_move = False
        if enemy1.x != -1000 and abs(new_e5_x - enemy1.x) < HORIZ_COLLIDE_DIST and abs(enemy5.y - enemy1.y) < VERTICAL_DEFEAT_DIST:
            can_e5_move = False
        if enemy2.x != -1000 and abs(new_e5_x - enemy2.x) < HORIZ_COLLIDE_DIST and abs(enemy5.y - enemy2.y) < VERTICAL_DEFEAT_DIST:
            can_e5_move = False
        if enemy3.x != -1000 and abs(new_e5_x - enemy3.x) < HORIZ_COLLIDE_DIST and abs(enemy5.y - enemy3.y) < VERTICAL_DEFEAT_DIST:
            can_e5_move = False
        if enemy4.x != -1000 and abs(new_e5_x - enemy4.x) < HORIZ_COLLIDE_DIST and abs(enemy5.y - enemy4.y) < VERTICAL_DEFEAT_DIST:
            can_e5_move = False

        if can_e5_move:
            enemy5.x = new_e5_x

    if enemy1.x != -1000 and abs(char.y - enemy1.y) <= VERTICAL_DEFEAT_DIST and abs(char.x - enemy1.x) <= HORIZ_COLLIDE_DIST:
        if powerup_active:
            enemies_defeated += 1
            enemy1.x = -1000
            enemy1.y = -1000
        else:
            game_over = True

    if enemy2.x != -1000 and abs(char.y - enemy2.y) <= VERTICAL_DEFEAT_DIST and abs(char.x - enemy2.x) <= HORIZ_COLLIDE_DIST:
        if powerup_active:
            enemies_defeated += 1
            enemy2.x = -1000
            enemy2.y = -1000
        else:
            game_over = True

    if enemy3.x != -1000 and abs(char.y - enemy3.y) <= VERTICAL_DEFEAT_DIST and abs(char.x - enemy3.x) <= HORIZ_COLLIDE_DIST:
        if powerup_active:
            enemies_defeated += 1
            enemy3.x = -1000
            enemy3.y = -1000
        else:
            game_over = True

    if enemy4.x != -1000 and abs(char.y - enemy4.y) <= VERTICAL_DEFEAT_DIST and abs(char.x - enemy4.x) <= HORIZ_COLLIDE_DIST:
        if powerup_active:
            enemies_defeated += 1
            enemy4.x = -1000
            enemy4.y = -1000
        else:
            game_over = True

    if enemy5.x != -1000 and abs(char.y - enemy5.y) <= VERTICAL_DEFEAT_DIST and abs(char.x - enemy5.x) <= HORIZ_COLLIDE_DIST:
        if powerup_active:
            enemies_defeated += 1
            enemy5.x = -1000
            enemy5.y = -1000
        else:
            game_over = True

    if enemies_defeated == 5:
        you_won = True


pgzrun.go()