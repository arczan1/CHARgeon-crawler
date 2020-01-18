import objects


class Sprite:
    sprites_dir = './graphics/'

    def __init__(self, path: str, color='\u001b[37m'):
        self.tab = list()
        self.color = color
        self.load(path)

    def load(self, path: str):
        with open(Sprite.sprites_dir + path) as file:
            sprite = file.read() 
            self.tab.append(list())
            line = 0
            for sign in sprite:
                if sign == '\n':
                    line += 1
                    self.tab.append(list())
                    continue
                self.tab[line].append(self.color + sign)


class GraphicSet:
    '''
        Special class that contains all Sprites of concrete GameObject
        Graphic numbers:

          ### - 0,1,2
          ### - 3,4,5
          ### - 6,7,8
          #P# - 9, player, 10
    '''
    def __init__(self):
        self.sprite_list = [None for _ in range(11)] 

    @classmethod
    def load_graphic_sets(cls):
        cls.graphic_sets = dict()

        # Load wall graphics
        wall = GraphicSet()
        wall.sprite_list[0] = (Sprite('wall/wall0.txt'), 14, 6)
        wall.sprite_list[1] = (Sprite('wall/wall1.txt'), 18, 6)
        wall.sprite_list[2] = (Sprite('wall/wall2.txt'), 31, 6)
        wall.sprite_list[3] = (Sprite('wall/wall3.txt'), 5, 5)
        wall.sprite_list[4] = (Sprite('wall/wall4.txt'), 13, 5)
        wall.sprite_list[5] = (Sprite('wall/wall5.txt'), 31, 5)
        wall.sprite_list[6] = (Sprite('wall/wall6.txt'), 0, 2)
        wall.sprite_list[7] = (Sprite('wall/wall7.txt'), 4, 2)
        wall.sprite_list[8] = (Sprite('wall/wall8.txt'), 36, 2)
        wall.sprite_list[9] = (Sprite('wall/wall9.txt'), 0, 0)
        wall.sprite_list[10] = (Sprite('wall/wall10.txt'), 45, 0)
        cls.graphic_sets['wall'] = wall


class Frame:
    def __init__(self):
        self.tab=[['\u001b[37m,' for _ in range(50)] for _ in range(20)]

    frame_no = 0

    def add_sprite(self, sprite: list):
        s_tab = sprite[0].tab 
        x_0 = sprite[1]
        y_0 = sprite[2]
        for y in range(len(s_tab)):
            for x in range(len(s_tab[y])):
                if 'r' not in s_tab[y][x]:
                    self.tab[y_0 + y][x_0 + x] = s_tab[y][x]

    @classmethod
    def draw_game(cls):
        print('\033[1;1H', end='')
        tab = Sprite('frame.txt').tab 

        # Dungeon view
        dungeon_frame = cls.render_dungeon()
        for y in range(len(dungeon_frame.tab)):
            for x in range(len(dungeon_frame.tab[y])):
                tab[1+y][1+x] = dungeon_frame.tab[y][x]

        #Map
        for y in range(len(Map.map.tab)):
            for x in range(len(Map.map.tab[y])):
                tab[1+y][52+x] = Map.map.tab[y][x]
        player_signs = ('v', '<', '^', '>',)
        Player = objects.Player
        tab[1+Player.player.y][52+Player.player.x] = '\u001b[35m' \
            + player_signs[Player.player.direction%4]

        for y in range(len(tab)):
            for x in range(len(tab[y])):
                print(tab[y][x], end='')
            print('')

    @classmethod
    def render_dungeon(cls):
        x,y=objects.Player.player.x, objects.Player.player.y
        board = objects.GameBoard.board
        frame = Frame()
        pos_list = None
        if objects.Player.player.direction % 4 == 0:
            pos_list = (
                (1,3,0), (-1,3,2), (0,3,1),
                (1,2,3), (-1,2,5), (0,2,4),
                (1,1,6), (-1,1,8), (0,1,7),
                (1,0,9), (-1,0,10),
            )
        elif objects.Player.player.direction % 4 == 1:
            pos_list = (
                (-3,1,0), (-3,-1,2), (-3,0,1),
                (-2,1,3), (-2,-1,5), (-2,0,4),
                (-1,1,6), (-1,-1,8), (-1,0,7),
                (0,1,9), (0,-1,10),
            )
        elif objects.Player.player.direction % 4 == 2:
            pos_list = (
                (-1,-3,0), (1,-3,2), (0,-3,1),
                (-1,-2,3), (1,-2,5), (0,-2,4),
                (-1,-1,6), (1,-1,8), (0,-1,7),
                (-1,0,9), (1,0,10),
            )
        elif objects.Player.player.direction % 4 == 3:
            pos_list = (
                (3,-1,0), (3,1,2), (3,0,1),
                (2,-1,3), (2,1,5), (2,0,4),
                (1,-1,6), (1,1,8), (1,0,7),
                (0,-1,9), (0,1,10),
            )

        for pos in pos_list:
            obj = board.get_object_at(pos[0]+x, pos[1]+y)
            Map.map.add_obj_at(obj, pos[0]+x, pos[1]+y)
            if obj is None:
                continue
            frame.add_sprite(obj.graphic_set.sprite_list[pos[2]])

        # Add weapon
        frame.add_sprite([Sprite('sword.txt', '\u001b[35m'), 36 + (cls.frame_no%2),14])

        return frame


class Map:
    def __init__(self):
        self.tab = [['\u001b[37m?' for _ in range(23)] for _ in range(13)]
        Map.map = self

    def add_obj_at(self, obj, x: int, y: int):
        try:
            if obj is None:
                self.tab[y][x] = ' '
            elif obj.type == 'wall':
                self.tab[y][x] = '\u001b[37m#'
        except IndexError:
            pass
