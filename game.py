import pygame  as pg
from objs import Image

class Game:
    def __init__(self,bg, size=(400, 300)):
        self.size = size
        self.bg = bg 
        self.surface = pg.display.set_mode(size,pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.pause = False
        
    def blit(self, obj: list = [],font:list  = [],images:list = []):

        self.surface.blit(self.bg, (0, 0))  

        for img in images:
            self.surface.blit(img.surface, img.xy)
        for ft in font:
            self.surface.blit(ft.obj,ft.xy)
        for ob in obj:
            self.surface.blit(ob.skin, ob.hitbox)

        pg.display.update()

    @staticmethod
    def close(event):
        if event.type == 256:  # добавить отключение на ESC <- ДЗ
            pg.quit()
            raise SystemExit

    def switch_pause(self, event):
        if event.type == 768 and event.key == 27:
            self.pause = not self.pause
            return 'pause'

    def border(self, obj):
        if obj.hitbox.left < 0:
            obj.hitbox.left = 0
        elif obj.hitbox.right > self.size[0]:
            obj.hitbox.right = self.size[0]
        if obj.hitbox.top < 0:
            obj.hitbox.top = 0
        elif obj.hitbox.bottom > self.size[1]:
            obj.hitbox.bottom = self.size[1]
