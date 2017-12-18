#Clay Kynor
#12/14/17
#FinalProject.py - OTHELLO

from ggame import *

RADIUS = 20
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
    data['board'][3][2] = 1
    return data['board']


def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,8):
        for col in range(0,8):
            if data['board'][row][col] == '':
                Sprite(WHITECIRCLE,(RADIUS+(col*(RADIUS*2)),RADIUS+(row*RADIUS*2)))
            elif data['board'][row][col] == 1:
                Sprite(P1CIRCLE,([row]*RADIUS,[col]*RADIUS))
            else:
                Sprite(P2CIRCLE,((RADIUS*7),RADIUS*9))
    
    
if __name__ == '__main__':
    
    data = {}
    data['board'] = []
    data['yeet'] = []
    buildBoard()
    print(data['board'])
    redrawAll()
    App().run()