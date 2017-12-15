#Clay Kynor
#12/14/17
#FinalProject.py - OTHELLO

from ggame import *

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
    
    p1Color = Color(0x00FF00,1)
    p2Color = Color(0xFF00FF,1)
    p2Circle = EllipseAsset(40,40,LineStyle(1,p2Color),p2Color)
    
    buildBoard()
    #redrawAll()
    print(data['board'])
    Sprite(p2Circle,(50,50))
    App().run()