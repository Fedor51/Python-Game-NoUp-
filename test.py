import pygame as pg
from objs import Object
from game import Game


class MyGame(Game):
    def __init__(self):
        # Переменные игры
        self.SIZE = (600, 500)
        self.FPS = 120

        self.bg = pg.image.load("NoUp\\resourses\\img\\bg.png")
        super().__init__(self.bg, self.SIZE)  # Game.__init__(size)

        self.draw = []

    def run(self):
        while True:
            self.clock.tick(self.FPS)  # FPS

            self.blit(self.draw)

            fps = round(self.clock.get_fps(), 2)
            pg.display.set_caption(f"FPS: {fps}")

            for ev in pg.event.get():  # Отслеживание событий
                self.close(ev)
                self.switch_pause(ev)
                
            if not self.pause:
                pass

if __name__ == "__main__":
    game = MyGame()
    game.run()
