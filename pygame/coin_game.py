from random import randint
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
pou = Actor("character")
pou.pos = 100, 100
coin = Actor("coin")
coin.pos = 200, 200
def draw():
    screen.fill("green")
    pou.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))
def time_up():
    pass
def update():
    pass

game_over = True
clock.schedule(time_up, 7.0)
if game_over:
    screen.fill("pink")
    screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

if keyboard.left:
    pou.x = pou.x - 2
