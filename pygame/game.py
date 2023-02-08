pou = Actor ('character')
pou.pos = 100, 50


WIDTH = 500
HEIGHT = 300

def draw():
    screen.fill((5, 102, 8))
    pou.draw()
def update ():
    pou.left = pou.left + 2
    if pou.left > WIDTH:
       pou.right = 0

def on_mouse_down(pos, button):
    if button == mouse.LEFT and pou.collidepoint(pos):
        print("Eek!")

def on_mouse_down(pos):
    if pou.collidepoint(pos):
        click.wav.play()
        pou.image = 'character_click'
        time.sleep(1)
        pou.image = 'character'
