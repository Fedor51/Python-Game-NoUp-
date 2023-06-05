import pygame as pg


class Object:
    def __init__(
        self,
        size=(40, 40),
        xy=(0, 0),
        color=(200, 200, 255),
        drop_speed=0,
    ):
        self.skin = pg.Surface(size)
        self.hitbox = self.skin.get_rect(topleft=xy)
        self.skin.fill(color)
        self.drop_speed = drop_speed

    def drop(self, speed_up=0.2, max_drop_speed=6):
        self.hitbox.y += self.drop_speed

        self.drop_speed += speed_up
        if self.drop_speed >= max_drop_speed:
            self.drop_speed = max_drop_speed

        return self.drop_speed


class Field:
    def __init__(self, size=(40, 40), xy=(0, 0)):
        self.hitbox = pg.Rect(xy[0], xy[1], size[0], size[1])


class Platform(Object):
    def __init__(self, size=(40, 40), xy=(0, 0), color=(200, 200, 255)):
        super(Platform, self).__init__(size, xy, color)

    def border(self, obj):
        if obj.hitbox.colliderect(self.hitbox):
            deep = {
                'left': abs(self.hitbox.left - obj.hitbox.right),
                'right': abs(self.hitbox.right - obj.hitbox.left),
                'top': abs(self.hitbox.top - obj.hitbox.bottom),
                'bottom': abs(self.hitbox.bottom - obj.hitbox.top),
            }
            sides = [s for s, v in deep.items() if v == min(deep.values())]

            if 'left' in sides:
                obj.hitbox.right = self.hitbox.left
            if 'right' in sides:
                obj.hitbox.left = self.hitbox.right
            if 'top' in sides:
                obj.hitbox.bottom = self.hitbox.top
            if 'bottom' in sides:
                obj.hitbox.top = self.hitbox.bottom

            return sides


class Player(Object):
    def __init__(
        self,
        size=(40, 40),
        xy=(0, 0),
        color=(200, 200, 255),  # Внешность и местоположение
        speed=1,
        jump_power=8,  # Характеристики
        drop_speed=0,
        hp=100,
    ):  # Дополнительные параметры
        super().__init__(size, xy, color)
        self.hp = hp
        self.speed = speed
        self.drop_speed = drop_speed
        self.jump_power = jump_power
        self.skin.blit(pg.image.load("NoUp\\resourses\\img\\ufo.png"),(0,0))

    def motion_up(self, key=119):
        self.hitbox.y -= pg.key.get_pressed()[key] * self.speed

    def motion_down(self, key=115):
        self.hitbox.y += pg.key.get_pressed()[key] * self.speed

    def motion_left(self, key=97):
        self.hitbox.x -= pg.key.get_pressed()[key] * self.speed

    def motion_right(self, key=100):
        self.hitbox.x += pg.key.get_pressed()[key] * self.speed

    def drop(self, speed_up=0.2, max_drop_speed=6):
        self.hitbox.y += self.drop_speed

        self.drop_speed += speed_up
        if self.drop_speed >= max_drop_speed:
            self.drop_speed = max_drop_speed

        return self.drop_speed

    def jump(self, key=32):
        if pg.key.get_pressed()[key]:  # То может прыгнуть
            self.drop_speed = -self.jump_power


class Bullet(Object):
    def __init__(
        self,
        size=(5, 5),
        xy=(0, 0),
        color=(0, 0, 0),
        speed=1,
        img="NoUp\\resourses\\img\\bul.png"
    ):
        super().__init__(size, xy, color)

        self.speed = speed 
        self.skin.blit(pg.image.load(img),(0,0))

    pg.init()

    def solve(self, char, pos=pg.mouse.get_pos()):
        self.bx, self.by = char
        self.tx, self.ty = pos

        self.catx = self.tx - self.bx
        self.caty = self.ty - self.by

        self.gip = (self.catx**2 + self.caty**2) ** 0.5

        self.coefx = self.catx / self.gip
        self.coefy = self.caty / self.gip

        self.sx = self.speed * self.coefx
        self.sy = self.speed * self.coefy

    def aim(self, bl, list, draw, surface):
        bl.bx += bl.sx
        bl.by += bl.sy

        bl.hitbox.x = bl.bx
        bl.hitbox.y = bl.by

        if not bl.hitbox.colliderect(surface.get_rect()):
            list.remove(bl)
            draw.remove(bl)


class Button:
    def __init__(
        self,
        size: tuple,
        xy,
        screen,
        buttonText='Button',
        onePress=False,
    ):
        self.size = size
        self.xy = xy
        self.onePress = onePress
        self.alreadyPressed = False
        self.screen = screen
        # self.fillColors = {
        #     'normal': (147, 148, 146),
        #     'hover': (102, 102, 102),
        #     'pressed': (51, 51, 51),
        # }
        # pg.Surface(size)

        self.font = pg.font.Font("NoUp\\resourses\\font\iknowaghost.ttf", 40)
        self.skin = pg.image.load('NoUp\\resourses\\img\\button_still.png')
        
        self.hitbox = self.skin.get_rect(topleft=xy)

        self.buttonSurf = self.font.render(buttonText, True, (0, 0, 0))

    def process(self):
        mousePos = pg.mouse.get_pos()
        resp = False
        # self.skin.fill(self.fillColors['normal'])
        if self.hitbox.collidepoint(mousePos):
            # self.skin.fill(self.fillColors['hover'])
            if pg.mouse.get_pressed(num_buttons=3)[0]:
                # self.skin.fill(self.fillColors['pressed'])
                if self.onePress:
                    pass
                elif not self.alreadyPressed:
                    resp = True
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.skin.blit(
            self.buttonSurf,
            [
                self.hitbox.size[0] / 2 - self.buttonSurf.get_rect().size[0] / 2,
                self.hitbox.size[1] / 2 - self.buttonSurf.get_rect().size[1] / 2,
            ],
        )
        self.screen.blit(self.skin, self.hitbox)
        return resp


class Image:
    def __init__(self,path:str,xy: tuple = (0,0)):
        self.xy = xy
        self.surface  = pg.image.load(path) 


class Obj_Image:
    def __init__(self, path:str, xy = (0,0)) -> None:
        self.xy = xy
        self.skin = pg.image.load(path)       
        self.hitbox =  self.skin.get_rect(topleft=xy)


class Font:
    def __init__(self, font, text, color = (0,0,0),xy = (0,0)) -> None:
        self.font = font
        self.color = color
        self.text = text
        self.xy = xy
        self.obj = self.font.render(text,True,self.color)

    # def update(self,t):
    #     self.obj = self.font.render(t,True,self.color)
    