#Clay Kynor
#12/14/17
#FinalProject.py - OTHELLO

from ggame import *

P1COLOR = Color (0x00FF00,1)
P2COLOR = Color(0xFF00FF,1)
P1CIRCLE = EllipseAsset(40,40,LineStyle(1,P1COLOR),P1COLOR)
P2CIRCLE = EllipseAsset(40,40,LineStyle(1,P2COLOR),P2COLOR)

def buildBoard():
    for i in range(0,8):
        data['board'].append(['']*8)
    return data['board']

'''
def redrawAll():
    for row in range(0,8):
        for col in range(0,8):
            for item in App().data['board'][:]:
                item.destroy()
            return data['board']
            '''
            
if __name__ == '__main__':
    
    data = {}
    data['board'] = ['d']
    data['yeet'] = []
    
    buildBoard()
    #redrawAll()
    print(data['board'])
    Sprite(P2CIRCLE,(50,50))
    Sprite(P1CIRCLE,(200,200))
    App().run()