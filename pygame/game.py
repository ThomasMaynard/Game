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
       pou,right = 0
