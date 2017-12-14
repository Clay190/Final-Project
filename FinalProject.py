#Clay Kynor
#12/14/17
#FinalProject.py - OTHELLO

from ggame import *

def buildBoard():
    data['board'] = [['']*8]*8
    return data['board']


if __name__ == '__main__':
    
    data = {}
    data['board'] = []
    
    p1Color = Color(0x00FF00,1)
    p2Color = Color(0xFF00FF,1)
    p2Circle = EllipseAsset(40,40,LineStyle(1,p2Color),p2Color)
    
    buildBoard()
    print(data['board'])
    Sprite(p2Circle)
    App().run()