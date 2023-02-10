import time

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

def set_pou_normal():
    pou.image = 'character'

def set_pou_hurt():
    pou.image = 'click'
    sounds.clicked.play()


def on_mouse_down(pos, button):
    if button == mouse.LEFT and pou.collidepoint(pos):
        print("Eek!")
    if pou.collidepoint(pos):
        sounds.clicked.play()
        set_pou_hurt()
        pou.image = 'click'
        time.sleep(3)
        clock.schedule_unique(set_pou_normal, 1.0)
        pou.image = 'character'
