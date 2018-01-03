#Clay Kynor
#12/14/17
#FinalProject.py - OTHELLO

from ggame import *

RADIUS = 30
LINESIZE = 1.4
P1COLOR = Color(0xFFFFFF,1)
P2COLOR = Color(0x000000,1)
BOARDCOLOR = Color(0x999999,0.5)
BLACK = Color(0x000000,1)

P1CIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),P1COLOR)
P2CIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),P2COLOR)
BOARDCIRCLE = EllipseAsset(RADIUS,RADIUS,LineStyle(LINESIZE,BLACK),BOARDCOLOR)

def buildBoard():
    for i in range(0,8):
        data['board'].append(['']*8)
    data['board'][4][3] = 1
    data['board'][3][4] = 1
    data['board'][3][3] = 2
    data['board'][4][4] = 2
    return data['board']

def boardFull():
    for i in range(0,8):
        if '' in data['board'][i]:
            print('yea')
            return False
    else:
        return True
 
def winner():
    p1Points = 0
    p2Points = 0
    for row in range(0,8):
        for col in range(0,8):
            if data['board'][row][col] == 1:
                p1Points += 1
            elif data['board'][row][col] == 2:
                p2Points += 1
    print("Player 1 has", p1Points)
    print("Player 2 has", p2Points)
    if p1Points>p2Points:
        print('Player 1 wins!')
    elif p1Points<p2Points:    
        print('Player 2 wins!')
    else:
        print("This game is a draw!")
    
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,8):
        for col in range(0,8):
            if data['board'][row][col] == '':
                Sprite(BOARDCIRCLE,(RADIUS+(row*(RADIUS*2)),RADIUS+(col*RADIUS*2)))
            elif data['board'][row][col] == 1:
                Sprite(P1CIRCLE,((row*RADIUS*2)+RADIUS,RADIUS+(col*RADIUS*2)))
            else:
                Sprite(P2CIRCLE,((row*RADIUS*2)+RADIUS,RADIUS+(col*RADIUS*2)))
'''
def flipNorth(x,y):
    if data['board'][x][y] == 1:
        data['board'][x][y-1] = 2
    elif data['board'][x][y] == 2:
        data['board'][x][y-1] = 1
    else:
        print('flipNorth didnt work')
    redrawAll()

def flipSouth(x,y):
    if data['board'][x][y] == 1:
        data['board'][x][y+1] = 2
    elif data['board'][x][y] == 2:
        data['board'][x][y+1] = 1
    else:
        print('flipSouth didnt work')
    redrawAll()
'''
def flipEast(x,y):
    i=1
    while data['board'][x][y+i] == 1:
        i+=1
    if data['board'][x][y+i] != '':
        data['board'][x][y+i] = 2
        redrawAll()
    
'''    
def flipWest(x,y):
    if data['board'][x][y] == 1:
        data['board'][x-1][y] = 2
    elif data['board'][x][y] == 2:
        data['board'][x-1][y] = 1
    else:
        print('flipWest didnt work')
    redrawAll()

def flipNorthEast(x,y):
    if data['board'][x][y] == 1:
        data['board'][x+1][y-1] = 2
    elif data['board'][x][y] == 2:
        data['board'][x+1][y-1] = 1
    else:
        print('flipNorthEast didnt work')
    redrawAll()

def flipNorthWest(x,y):
    if data['board'][x][y] == 1:
        data['board'][x-1][y-1] = 2
    elif data['board'][x][y] == 2:
        data['board'][x-1][y-1] = 1
    else:
        print('flipNorthWest didnt work')
    redrawAll()
    
def flipSouthEast(x,y):
    if data['board'][x][y] == 1:
        data['board'][x+1][y+1] = 2
    elif data['board'][x][y] == 2:
        data['board'][x+1][y+1] = 1
    else:
        print('flipSouthEast didnt work')
    redrawAll()

def flipSouthWest(x,y):
    if data['board'][x][y] == 1:
        data['board'][x-1][y+1] = 2
    elif data['board'][x][y] == 2:
        data['board'][x-1][y+1] = 1
    else:
        print('flipSouthWest didnt work')
    redrawAll()
    '''
def flipPieces(x,y):
    print('Do flipPieces function')
    
if __name__ == '__main__':
    
    data = {}
    data['board'] = []
    data['row'] = 4
    data['col'] = 4
    
    buildBoard()
    flipPieces(data['col'],data['row'])
    flipEast(data['col'],data['row'])
    print(data['board'])
    redrawAll()
    boardFull()
    winner()
    App().run()