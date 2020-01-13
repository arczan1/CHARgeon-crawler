class Sprite:
    pass


class GameObject:
    def __init__(self, type):
        '''
            types:
                wall, boardend, enemy
        '''
        self._type = type

    def get_type(self):
        '''
            Return LOWERCASE type(Wall == wall...)
        '''
        return lower(self._type)


class Wall(GameObject):
    def __init__(self):
        super('wall')


class Enemy(GameObject):
    def __init__(self):
        super('enemy')


class GameBoard:
    def __init__(self, width=10, height=10):
        self._width = width
        self._height = height
        self._board = list()

    def is_in_board(self, x: int, y: int):
        if x < 0 or x >= self._width:
            return False
        if y < 0 or y >= self._height:
            return False
        return True

    def get_object_at(self, x: int, y: int):
        if not self.is_in_board(x, y):
            return GameObject('boardend')

        try:
            return self._board[y][x]
        except IndexError:
            return None
