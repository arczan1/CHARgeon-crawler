from graphic import *


class GameObject:
    def __init__(self, _type):
        '''
            types:
                wall, boardend, enemy, player
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
    def __init__(self, width=10, height=10):
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
            return GameObject('boardend')

        try:
            return self.board[y][x]
        except IndexError:
            return None

    def generate_board(self):
        for i in range(self.height):
            self.board.append([Wall() for _ in range(self.width)]) 


class Player(GameObject):
    def __init__(self):
        super('player')
        self.direction = 0 # where player is looking (% 4)

    @classmethod
    def set_player(cls, player):
        cls.player = player

