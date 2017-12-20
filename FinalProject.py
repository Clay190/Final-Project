#Clay Kynor
#12/14/17
#FinalProject.py - OTHELLO

from ggame import *

RADIUS = 30
LINESIZE = .14
P1COLOR = Color(0x00F300,1)
P2COLOR = Color(0x0080FF,1)
WHITE = Color(0xFFFFFF,1)
BLACK = Color(0x000000,1)

P1CIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),P1COLOR)
P2CIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),P2COLOR)
WHITECIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),WHITE)

def buildBoard():
    for i in range(0,8):
        data['board'].append(['']*8)
    data['board'][4][3] = 1
    data['board'][3][4] = 1
    data['board'][3][3] = 2
    data['board'][4][4] = 2
    return data['board']

def boardFull():
    if '' in data['board']:
        print("CLAY")
        return False
    else:
        print("BOARD FULL DOESNT WR+ORK")
        return True
        

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,8):
        for col in range(0,8):
            if data['board'][row][col] == '':
                Sprite(WHITECIRCLE,(RADIUS+(col*(RADIUS*2)),RADIUS+(row*RADIUS*2)))
            elif data['board'][row][col] == 1:
                Sprite(P1CIRCLE,((row*RADIUS*2)+RADIUS,RADIUS+(col*RADIUS*2)))
            else:
                Sprite(P2CIRCLE,((row*RADIUS*2)+RADIUS,RADIUS+(col*RADIUS*2)))
    
    
if __name__ == '__main__':
    
    data = {}
    data['board'] = []
    
    buildBoard()
    print(data['board'])
    redrawAll()
    boardFull()
    App().run()