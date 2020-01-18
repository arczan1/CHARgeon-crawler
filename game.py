from objects import *
from graphic import *

def game_loop():
    while(True):
        break

game_loop()
GraphicSet.load_graphic_sets()
Player()
board = GameBoard()
Map()
board.generate_board()
while True:
    Frame.draw_game()
    sign = GameController.getch()
    if sign == 'q':
        break

    if sign == 'a':
        Player.player.direction -= 1
    elif sign == 'd':
        Player.player.direction += 1
    elif sign == 'w':
        if Player.player.direction % 4 == 0:
            if GameBoard.board.get_object_at(Player.player.x,
                Player.player.y + 1) is None:
                Player.player.y += 1
                Frame.frame_no += 1
        elif Player.player.direction % 4 == 1:
            if GameBoard.board.get_object_at(Player.player.x - 1,
                Player.player.y) is None:
                Player.player.x -= 1
                Frame.frame_no += 1
        elif Player.player.direction % 4 == 2:
            if GameBoard.board.get_object_at(Player.player.x,
                Player.player.y - 1) is None:
                Player.player.y -= 1
                Frame.frame_no += 1
        elif Player.player.direction % 4 == 3:
            if GameBoard.board.get_object_at(Player.player.x + 1,
                Player.player.y) is None:
                Player.player.x += 1
                Frame.frame_no += 1
    elif sign == 's':
        if Player.player.direction % 4 == 2:
            if GameBoard.board.get_object_at(Player.player.x,
                Player.player.y + 1) is None:
                Player.player.y += 1
                Frame.frame_no += 1
        elif Player.player.direction % 4 == 3:
            if GameBoard.board.get_object_at(Player.player.x - 1,
                Player.player.y) is None:
                Player.player.x -= 1
                Frame.frame_no += 1
        elif Player.player.direction % 4 == 0:
            if GameBoard.board.get_object_at(Player.player.x,
                Player.player.y - 1) is None:
                Player.player.y -= 1
                Frame.frame_no += 1
        elif Player.player.direction % 4 == 1:
            if GameBoard.board.get_object_at(Player.player.x + 1,
                Player.player.y) is None:
                Player.player.x += 1
                Frame.frame_no += 1

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
