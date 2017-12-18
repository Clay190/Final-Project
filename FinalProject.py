#Clay Kynor
#12/14/17
#FinalProject.py - OTHELLO

from ggame import *

RADIUS = 28
LINESIZE = 1.5
P1COLOR = Color(0x00FF00,1)
P2COLOR = Color(0xFF00FF,1)
WHITE = Color(0xFFFFFF,1)
BLACK = Color(0x000000,1)
P1CIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),P1COLOR)
P2CIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),P2COLOR)
WHITECIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),WHITE)

def buildBoard():
    for i in range(0,8):
        data['board'].append(['']*8)
    return data['board']


def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,8):
        for col in range(0,8):
            Sprite(WHITECIRCLE,(RADIUS+(col*(RADIUS*2)),RADIUS+(row*RADIUS*2)))
if __name__ == '__main__':
    
    data = {}
    data['board'] = []
    data['yeet'] = []
    
    buildBoard()
    #redrawAll()
    print(data['board'])
    redrawAll()
    Sprite(P1CIRCLE,((RADIUS*9),RADIUS*9))
    Sprite(P2CIRCLE,((RADIUS*9),RADIUS*7))
    Sprite(P1CIRCLE,((RADIUS*7),RADIUS*7))
    Sprite(P2CIRCLE,((RADIUS*7),RADIUS*9))
    App().run()