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


        portal = GraphicSet()
        portal.sprite_list[0] = (Sprite('portal/portal0.txt', '\u001b[33m'), 14, 6)
        portal.sprite_list[1] = (Sprite('portal/portal1.txt', '\u001b[33m'), 18, 6)
        portal.sprite_list[2] = (Sprite('portal/portal2.txt', '\u001b[33m'), 31, 6)
        portal.sprite_list[3] = (Sprite('portal/portal3.txt', '\u001b[33m'), 5, 5)
        portal.sprite_list[4] = (Sprite('portal/portal4.txt', '\u001b[33m'), 13, 5)
        portal.sprite_list[5] = (Sprite('portal/portal5.txt', '\u001b[33m'), 31, 5)
        portal.sprite_list[6] = (Sprite('portal/portal6.txt', '\u001b[33m'), 0, 2)
        portal.sprite_list[7] = (Sprite('portal/portal7.txt', '\u001b[33m'), 4, 2)
        portal.sprite_list[8] = (Sprite('portal/portal8.txt', '\u001b[33m'), 36, 2)
        portal.sprite_list[9] = (Sprite('portal/portal9.txt', '\u001b[33m'), 0, 0)
        portal.sprite_list[10] = (Sprite('portal/portal10.txt', '\u001b[33m'), 45, 0)
        cls.graphic_sets['portal'] = portal
        
        # Load enemy graphics
        enemy = GraphicSet()
        enemy.sprite_list[1] = (Sprite('enemy1.txt', '\u001b[31m'), 23, 8)
        enemy.sprite_list[3] = (Sprite('enemy3.txt', '\u001b[31m'), 14, 7)
        enemy.sprite_list[4] = (Sprite('enemy4.txt', '\u001b[31m'), 22, 7)
        enemy.sprite_list[5] = (Sprite('enemy5.txt', '\u001b[31m'), 33, 7)
        enemy.sprite_list[6] = (Sprite('enemy6.txt', '\u001b[31m'), 5, 5)
        enemy.sprite_list[7] = (Sprite('enemy7.txt', '\u001b[31m'), 18, 5)
        enemy.sprite_list[8] = (Sprite('enemy8.txt', '\u001b[31m'), 38, 5)
        cls.graphic_sets['enemy'] = enemy

        cls.fight_box = list()
        cls.fight_box.append(cls.load_box('fight_box/fight_box.txt'))
        cls.fight_box.append(cls.load_box('fight_box/fight_box_1.txt'))
        cls.fight_box.append(cls.load_box('fight_box/fight_box_2.txt'))
        cls.fight_box.append(cls.load_box('fight_box/fight_box_3.txt'))
         
    @classmethod
    def load_box(cls, path: str):
        box = list()
        box.append(list())
        with open(Sprite.sprites_dir + path) as file:
            sprite = file.read() 
            line = 0
            for sign in sprite:
                if sign == '\n':
                    line += 1
                    box.append(list())
                    continue
                box[line].append('\u001b[37m'+sign)
        return box


class Frame:
    def __init__(self):
        self.tab=[['\u001b[37m,' for _ in range(50)] for _ in range(20)]

    frame_no = 0

    def add_sprite(self, sprite: list):
        if sprite is None:
            return

        s_tab = sprite[0].tab 
        x_0 = sprite[1]
        y_0 = sprite[2]
        for y in range(len(s_tab)):
            for x in range(len(s_tab[y])):
                if 'r' not in s_tab[y][x]:
                    self.tab[y_0 + y][x_0 + x] = s_tab[y][x]

    @classmethod
    def draw_game(cls, bottom=None):
        print('\033[1;1H', end='')
        player = objects.Player.player
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
        Player = objects.Player
        tab[1+Player.player.y][52+Player.player.x] = '\u001b[35m' \
            + 'X'

        # Show stats
        for x in range((int)((player.hp / player.max_hp) * 21)):
            tab[16][53+x] = '\u001b[35m#'
        tab[15][69] = '\u001b[35m' + (str)(player.hp % 10)
        tab[15][68] = '\u001b[35m' + (str)((player.hp//10) % 10)
        tab[15][67] = '\u001b[35m' + (str)((player.hp//100) % 10)
        tab[15][73] = '\u001b[35m' + (str)(player.max_hp % 10)
        tab[15][72] = '\u001b[35m' + (str)((player.max_hp//10) % 10)
        tab[15][71] = '\u001b[35m' + (str)((player.max_hp//100) % 10)

        # LVL
        tab[20][73] = '\u001b[35m' + (str)(objects.GameController.lvl % 10)
        tab[20][72] = '\u001b[35m' + (str)((objects.GameController.lvl//10) % 10)
        tab[20][71] = '\u001b[35m' + (str)((objects.GameController.lvl//100) % 10)

        # GOLD
        tab[22][73] = '\u001b[33m' + (str)(Player.player.gold % 10)
        tab[22][72] = '\u001b[33m' + (str)((Player.player.gold // 10) % 10)
        tab[22][71] = '\u001b[33m' + (str)((Player.player.gold // 100) % 10)

        if bottom is not None:
            for y in range(6):
                for x in range(50):
                    tab[y+22][x+1] = bottom[y][x]

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
        frame.add_sprite([Sprite('sword.txt', '\u001b[35m'), 36 + (cls.frame_no%2),12])
        frame.add_sprite([Sprite('sword1.txt', '\u001b[33m'), 35 + (cls.frame_no%2),18])

        return frame


class Map:
    def __init__(self):
        self.tab = [['\u001b[37m?' for _ in range(23)] for _ in range(13)]
        Map.map = self

    def add_obj_at(self, obj, x: int, y: int):
        if not objects.GameBoard.board.is_in_board(x, y):
            return
        try:
            if self.can_see(x, y):
                if obj is None:
                    self.tab[y][x] = ' '
                elif obj.type == 'wall':
                    self.tab[y][x] = '\u001b[37m#'
                elif obj.type == 'enemy':
                    self.tab[y][x] = '\u001b[31m!'
                elif obj.type == 'portal':
                    self.tab[y][x] = '\u001b[33m@'
        except IndexError:
            pass

    def can_see(self, x, y):
        '''
            return True if object can be seen by player
        '''
        return True
