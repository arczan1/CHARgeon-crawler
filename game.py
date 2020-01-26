from objects import *
from graphic import *
import time
import random


def game_loop():
    while True:
        Frame.draw_game()
        sign = GameController.getch()
        if sign == 'q':
            break

        move(sign)

def fight():
    player = Player.player
    Frame.draw_game(GraphicSet.fight_box[3])
    time.sleep(1)
    Frame.draw_game(GraphicSet.fight_box[2])
    time.sleep(1)
    Frame.draw_game(GraphicSet.fight_box[1])
    time.sleep(1)
    while(True):
        pos_x = random.randint(2, 47)
        pos_y = random.randint(0, 5)
        direction = random.randint(0, 3)
        direction_signs = ('s', 'a', 'w', 'd',)
        bottom = [ [ ' ' for _ in range(50)] for _ in range(6) ]
        direction_arrows = ['v', '<', '^', '>',]

        extras = ('u', 'd', 'p', 'c', )
        for _ in range(GameController.lvl):
            bottom[random.randint(0,5)][random.randint(2, 47)] = extras[random.randint(0, len(extras)-1)]
        bottom[pos_y][pos_x] = direction_arrows[direction] 

        # HP bars
        enemy_hp = (int)((player.enemy.hp/100) * 5)
        player_hp = (int)((player.hp/player.max_hp) * 5)
        for y in range(enemy_hp+1):
            bottom[5-y][0] = '\u001b[31m#'
        for y in range(player_hp+1):
            bottom[5-y][49] = '\u001b[35m#'

        for y in range(6):
            bottom[y][1] = '\u001b[37m|'
            bottom[y][48] = '\u001b[37m|'


        Frame.draw_game(bottom)
        start = time.time() 
        sign = GameController.getch()
        end = time.time()
        elapsed = end - start
        if sign == direction_signs[direction]:
            if elapsed < 1:
                player.enemy.hp -= player.dmg
            elif elapsed < 1.5:
                player.enemy.hp -= player.dmg // 3
            elif elapsed < 2:
                player.hp -= player.enemy.dmg // 3
            else:
                player.hp -= player.enemy.dmg
        else:
            player.hp -= player.enemy.dmg

        if player.enemy.hp <= 0:
            if player.direction % 4 == 0:
                GameBoard.board.board[player.y+1][player.x] = None
            elif player.direction % 4 == 1:
                GameBoard.board.board[player.y][player.x-1] = None
            elif player.direction % 4 == 2:
                GameBoard.board.board[player.y-1][player.x] = None
            elif player.direction % 4 == 3:
                GameBoard.board.board[player.y][player.x+1] = None
            break
        if player.hp <= 0:
            game_over()

def game_over():
    print("NIE ŻYJESZ!!!!")
    exit()

def move(sign: str):
    player = Player.player
    board = GameBoard.board
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
            elif GameBoard.board.get_object_at(Player.player.x,
                Player.player.y + 1).type == 'portal':
                GameController.next_dungeon()
                return
        elif Player.player.direction % 4 == 1:
            if GameBoard.board.get_object_at(Player.player.x - 1,
                Player.player.y) is None:
                Player.player.x -= 1
                Frame.frame_no += 1
            elif GameBoard.board.get_object_at(Player.player.x - 1,
                Player.player.y).type == 'portal':
                GameController.next_dungeon()
                return
        elif Player.player.direction % 4 == 2:
            if GameBoard.board.get_object_at(Player.player.x,
                Player.player.y - 1) is None:
                Player.player.y -= 1
                Frame.frame_no += 1
            elif GameBoard.board.get_object_at(Player.player.x,
                Player.player.y - 1).type == 'portal':
                GameController.next_dungeon()
                return
        elif Player.player.direction % 4 == 3:
            if GameBoard.board.get_object_at(Player.player.x + 1,
                Player.player.y) is None:
                Player.player.x += 1
                Frame.frame_no += 1
            elif GameBoard.board.get_object_at(Player.player.x + 1,
                Player.player.y).type == 'portal':
                GameController.next_dungeon()
                return
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

    if board.get_object_at(player.x, player.y+1) is not None and board.get_object_at(player.x, player.y+1).type == 'enemy':
        player.is_fighting = True
        player.enemy = board.get_object_at(player.x, player.y+1) 
        Frame.draw_game()
        time.sleep(0.3)
        player.direction = 0
        Frame.draw_game()
        fight()
    elif board.get_object_at(player.x, player.y-1) is not None and board.get_object_at(player.x, player.y-1).type == 'enemy':
        player.is_fighting = True
        player.enemy = board.get_object_at(player.x, player.y-1) 
        Frame.draw_game()
        time.sleep(0.3)
        player.direction = 2
        Frame.draw_game()
        fight()
    elif board.get_object_at(player.x-1, player.y) is not None and board.get_object_at(player.x-1, player.y).type == 'enemy':
        player.is_fighting = True
        player.enemy = board.get_object_at(player.x-1, player.y) 
        Frame.draw_game()
        time.sleep(0.3)
        player.direction = 1
        Frame.draw_game()
        fight()
    elif board.get_object_at(player.x+1, player.y) is not None and board.get_object_at(player.x+1, player.y).type == 'enemy':
        player.is_fighting = True
        player.enemy = board.get_object_at(player.x+1, player.y) 
        Frame.draw_game()
        time.sleep(0.3)
        player.direction = 3
        Frame.draw_game()
        fight()


GraphicSet.load_graphic_sets()
Player()
GameBoard()
Map()
Map.map.tab[Player.player.y][Player.player.x] = ' '
GameBoard.board.generate_board()
with open('./graphics/manual.txt') as file:
    print(file.read())
GameController.getch()
game_loop()

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
