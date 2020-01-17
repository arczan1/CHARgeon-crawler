from objects import *
from graphic import *

def game_loop():
    while(True):
        break

game_loop()
GraphicSet.load_graphic_sets()
board = GameBoard()
board.generate_board()

'''import time

w, h = 70, 40
for i in range(1000):
    tab = [[i % 10 for _ in range(w)] for _ in range(h)]
    print('\u001b[{}m'.format(i % 40))
    print('\033[1;1H', end='')
    for row in tab:
        for pixel in row:
            print(pixel, end='')
        print('')
    time.sleep(0.05)
'''
