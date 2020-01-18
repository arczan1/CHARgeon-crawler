from graphic import *
import tty
import sys
import termios
import random


class GameObject:
    def __init__(self, _type):
        '''
            types:
                wall, boardend, enemy
        '''
        self.type = _type
        self.graphic_set = GraphicSet.graphic_sets[_type]


    def get_type(self):
        '''
            Return LOWERCASE type(Wall == wall...)
        '''
        return lower(self.type)


class Wall(GameObject):
    def __init__(self):
        super().__init__('wall')


class Enemy(GameObject):
    def __init__(self):
        super('enemy')


class GameBoard:
    def __init__(self, width=23, height=13):
        self.width = width
        self.height = height
        self.board = list()
        GameBoard.set_board(self)

    @classmethod
    def set_board(cls, board):
        cls.board = board

    def is_in_board(self, x: int, y: int):
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return True

    def get_object_at(self, x: int, y: int):
        if not self.is_in_board(x, y):
            return Wall()
        try:
            return self.board[y][x]
        except IndexError:
            return None

    def generate_board(self):
        for i in range(self.height):
            self.board.append([Wall() for _ in range(self.width)]) 
        x, y = 6, 6
        self.board[y][x] = None
        for i in range(70):
            direction = random.randint(0,4)
            if direction == 0:
                if self.is_in_board(x+2, y):
                    self.board[y][x+1] = None
                    self.board[y][x+2] = None
                    x+=2
            elif direction == 1:
                if self.is_in_board(x-2, y):
                    self.board[y][x-1] = None
                    self.board[y][x-2] = None
                    x-=2
            elif direction == 2:
                if self.is_in_board(x, y+2):
                    self.board[y+1][x] = None
                    self.board[y+2][x] = None
                    y+=2
            elif direction == 3:
                if self.is_in_board(x, y-2):
                    self.board[y-1][x] = None
                    self.board[y-2][x] = None
                    y-=2

    def draw_map(self):
        for row in self.board:
            for x in row:
                pass


class Player:
    def __init__(self):
        Player.set_player(self)
        self.x = 6
        self.y = 6
        self.direction = 0 # where player is looking (% 4)

    @classmethod
    def set_player(cls, player):
        cls.player = player

class GameController:
    @classmethod
    def getch(cls):
        file_descriptor = sys.stdin.fileno()
        settings = termios.tcgetattr(file_descriptor)
        tty.setraw(file_descriptor)
        sign = sys.stdin.read(1)# Read one char
        # Restore old settings
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, settings)
        return sign
