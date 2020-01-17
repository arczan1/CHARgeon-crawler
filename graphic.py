class Sprite:
    sprites_dir = './graphics/'

    def __init__(self, path: str):
        self.tab = list()
        self.load(path)
        for line in self.tab:
            print(line)

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
                self.tab[line].append(sign)


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
        wall.sprite_list[0] = (Sprite('wall/wall0.txt'), 0, 0)
        wall.sprite_list[1] = (Sprite('wall/wall1.txt'), 0, 0)
        wall.sprite_list[2] = (Sprite('wall/wall2.txt'), 0, 0)
        wall.sprite_list[3] = (Sprite('wall/wall3.txt'), 0, 0)
        wall.sprite_list[4] = (Sprite('wall/wall4.txt'), 0, 0)
        wall.sprite_list[5] = (Sprite('wall/wall5.txt'), 0, 0)
        wall.sprite_list[6] = (Sprite('wall/wall6.txt'), 0, 0)
        wall.sprite_list[7] = (Sprite('wall/wall7.txt'), 0, 0)
        wall.sprite_list[8] = (Sprite('wall/wall8.txt'), 0, 0)
        wall.sprite_list[9] = (Sprite('wall/wall9.txt'), 0, 0)
        wall.sprite_list[10] = (Sprite('wall/wall10.txt'), 0, 0)
        cls.graphic_sets['wall'] = wall

def render_dungeon():
    x,y=3,3
