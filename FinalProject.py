#Clay Kynor
#12/14/17
#FinalProject.py - OTHELLO

from ggame import *

P1COLOR = Color (0x00FF00,1)
P2COLOR = Color(0xFF00FF,1)
WHITE = Color(0xFFFFFF,1)
BLACK = Color(0x000000,1)
P1CIRCLE = EllipseAsset(30,30,LineStyle(1,P1COLOR),P1COLOR)
P2CIRCLE = EllipseAsset(30,30,LineStyle(1,P2COLOR),P2COLOR)
WHITECIRCLE = EllipseAsset(30,30,LineStyle(2,BLACK),WHITE)

def buildBoard():
    for i in range(0,8):
        data['board'].append(['']*8)
    return data['board']


def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,8):
        for col in range(0,8):
            Sprite(WHITECIRCLE, (30+(col*60),30+(row*60) ))
if __name__ == '__main__':
    
    data = {}
    data['board'] = []
    data['yeet'] = []
    
    buildBoard()
    #redrawAll()
    print(data['board'])
    redrawAll()
   #Sprite(P1CIRCLE(45,45))
    App().run()