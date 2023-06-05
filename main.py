import pygame as pg
from functions import *
from objs import Player, Bullet, Button, Image, Obj_Image, Font, Object
from game import Game
from random import randint 


class MyGame(Game):
    def __init__(self):
        # Переменные игры
        self.SIZE = (600, 500)
        self.FPS = 120
        self.death = False

        self.bg = pg.image.load("NoUp\\resourses\\img\\bg.png")
        # "C:\\Users\\python\\PycharmProjects\\maxim_group2\\NoUp\\resourses\img\\bg.png"
        super().__init__(self.bg, self.SIZE)  # Game.__init__(size)

        # ОБЪЕКТЫ
        self.char = Player(size=(20, 20), xy=(10, 10), color=(0, 0, 0), speed=2)
        self.coin = Object((20,20),(randint(0,580),randint(0,480)),(247, 165, 0))

        self.start_but_r = False
        self.start_but = Button((180, 50), (205, 240), self.surface, "START", False)

        self.auth_but_r = False
        self.auth_but = Button((180, 50), (205, 300), self.surface, "AUTHOR", False)

        self.back_but_r = False
        self.back_but = Button((180, 50), (205, 400), self.surface, "BACK", False)

        self.close_but_r = False
        self.close_but = Button((180, 50), (205, 360), self.surface, "CLOSE", False)

        self.continue_but = Button(
            (180, 50), (205, 160), self.surface, "CONTINUE", False
        )
        self.exit_but_r = False
        self.exit_but = Button((180, 50), (205, 220), self.surface, "EXIT", False)

        self.rest_but_r = False
        self.rest_but = Button((180, 50), (205, 200), self.surface, "RESTART", False)

        self.d_exit_but_r = False
        self.d_exit_but = Button((180, 50), (205, 260), self.surface, "EXIT", False)

        self.bullets = []
        self.m_bosses = []
        self.bosses = []
        self.but_const = 5

        # Тексты
        self.font = pg.font.Font("NoUp\\resourses\\font\\iknowaghost.ttf", 40)
        # "C:\\Users\\python\\PycharmProjects\\maxim_group2\\NoUp\\resourses\\font\iknowaghost.ttf"
        self.au_text = Font(self.font, "Fedor Tarasuyk 8/05/2023", xy=(70, 200))
        self.d_time = None

        self.d_text = Font(self.font, "You've lived for ", xy=(150, 15))
        

        # timer
        self.time = [0, 0, 0]
        self.tick = 0
        self.timer = Font(self.font, gen_text(self.time))



        self.blconst = 15

        # фоточки!!!!

        self.name_img = Image("NoUp\\resourses\\img\\Name.png", (130, 0))
        # "C:\\Users\\python\\PycharmProjects\\maxim_group2\\NoUp\\resourses\\img\\Name.png"

        self.death_bg = Image("NoUp\\resourses\\img\\death_bg.jpg")
        # "C:\\Users\\python\\PycharmProjects\\maxim_group2\\NoUp\\resourses\\img\\death_bg.jpg"
        self.pause_menu = Obj_Image("NoUp\\resourses\\img\\pause.jpg", (195, 150))


        self.draw = [self.coin]  # СЮДА ПОМЕЩАЕМ ОБЪЕКТЫ ДЛЯ ОТРИСОВКИ

        self.win_border = (
            [  # СЮДА ПОМЕЩАЕМ ОБЪЕКТЫ, КОТОРЫЕ НЕ ДОЛЖНЫ ВЫХОДИТЬ ЗА ЭКРАН
                self.char,
            ]
        )
        ############

        self.immortal = False

        ############

        pg.mixer.music.load("NoUp\\resourses\\mocart-lacrimosa-dies-illa.mp3")
        pg.mixer.music.play(-1)

    def run(self):
        while True:
            # МЕНЮ
            while not self.start_but_r:
                self.but_const = 5
                while not self.start_but_r and not self.auth_but_r:  # Менюшка

                    (
                        self.back_but_r,
                        self.pause,
                        self.exit_but_r,
                        self.d_exit_but_r,
                        self.time,
                    ) = (
                        False,
                        False,
                        False,
                        False,
                        [0, 0, 0],
                    )
                    self.bullets.clear(), self.draw.clear(), self.clock.tick(
                        self.FPS
                    )  # FPS контроль

                    self.blit(
                        [
                            self.start_but,
                            self.auth_but,
                            self.close_but,
                        ],
                        images=[self.name_img],
                    )

                    fps = round(self.clock.get_fps(), 2)
                    pg.display.set_caption(f"FPS: {fps}")

                    for ev in pg.event.get():  # Отслеживание событий
                        # print(ev)
                        self.close(ev)
                        self.switch_pause(ev)

                    (
                        self.start_but_r,
                        self.auth_but_r,
                        self.close_but_r,
                    ) = (
                        self.start_but.process(),
                        self.auth_but.process(),
                        self.close_but.process(),
                    )

                    if self.close_but_r:
                        pg.quit()
                        raise SystemExit

                while not self.start_but_r and not self.back_but_r:  # Автор с датой
                    self.auth_but_r = False
                    self.clock.tick(self.FPS)

                    self.blit([self.back_but], [self.au_text])

                    fps = round(self.clock.get_fps(), 2)
                    pg.display.set_caption(f"FPS: {fps}")

                    for ev in pg.event.get():  # Отслеживание событий
                        # print(ev)
                        self.close(ev)
                        self.switch_pause(ev)
                    self.back_but_r = self.back_but.process()
            # ИГРА
            self.char.hitbox.center = pg.mouse.get_pos()

            while not self.pause and not self.d_exit_but_r:
                
                # БАЗОВЫЕ ФУНКЦИИ
                self.clock.tick(self.FPS)  # FPS контроль

                if not self.char in self.draw:
                    self.draw.append(self.char)
                
                self.timer = Font(self.font, gen_text(self.time), (0, 0, 0))

                self.blit(self.draw, [self.timer])  # Отрисовка объектов
                fps = round(self.clock.get_fps(), 2)
                pg.display.set_caption(f"FPS: {fps}")

                for ev in pg.event.get():  # Отслеживание событий
                    # print(ev)
                    self.close(ev)
                    self.switch_pause(ev)

                if not self.pause and not self.death:  # Прод. Игры
                    # ТАЙМЕР
                    self.tick = round(self.tick + 0.5, 2)
                    if round(self.tick) == 1:
                        self.tick = 0
                        self.time[2] += 1
                        self.timer.text = gen_text(self.time)
                    if self.time[2] == 100:
                        self.time[2] = 0
                        self.time[1] += 1
                        self.timer.text = gen_text(self.time)
                    if self.time[1] == 60:
                        self.time[1] = 0
                        self.time[0] += 1
                        self.timer.text = gen_text(self.time)

                    self.blconst -= 1 if self.blconst else 0

                    # УПРАВЛЯЕМ ОБЪЕКТАМИ

                    self.char.hitbox.center = pg.mouse.get_pos()

                    # <BULLETS>

                    if self.blconst <= 0:
                        rx, ry = choice(
                            rand_left(self.SIZE),
                            rand_right(self.SIZE),
                            rand_top(self.SIZE),
                            rand_bottom(self.SIZE),
                        )

                        if self.time[1] < 10:
                            self.blconst = 15
                        elif self.time[1] >= 10 and self.time[1] < 20:
                            self.blconst = 12
                        elif self.time[1] >= 20:
                            self.blconst = 9

                        c = (self.time[1] * 2) / 10
                        sp = c if c >= 1 else 1
                        bul = Bullet((5, 5), (rx, ry), (0, 0, 0), sp)
                        self.draw.append(bul)
                        self.bullets.append(bul)
                        bul.solve((rx, ry), self.char.hitbox.center)
                    # <MINI BOSS>

                    if (
                        self.time[1] % 2 == 0
                        and self.time[1] >= 2
                        and len(self.m_bosses) < 3
                    ):
                        rx, ry = choice(
                            b_rl(self.SIZE),
                            rand_right(self.SIZE),
                            b_rt(self.SIZE),
                            rand_bottom(self.SIZE),
                        )
                        m_boss = Bullet(
                            (20, 20),
                            (rx, ry),
                            (0, 0, 0),
                            1,
                            "NoUp\\resourses\\img\\m_boss.png",
                        )
                        self.draw.append(m_boss)
                        self.m_bosses.append(m_boss)
                        m_boss.solve((rx, ry), self.char.hitbox.center)
                    # <BOSS>

                    if (
                        self.time[1] % 10 == 0
                        and self.time[1] >= 10
                        and len(self.bosses) < 1
                    ):
                        rx, ry = choice(
                            bb_rl(self.SIZE),
                            rand_right(self.SIZE),
                            bb_rt(self.SIZE),
                            rand_bottom(self.SIZE),
                        )
                        boss = Bullet(
                            (50, 50),
                            (rx, ry),
                            (0, 0, 0),
                            1,
                            "NoUp\\resourses\\img\\boss.png",
                        )
                        self.draw.append(boss)
                        self.bosses.append(boss)
                        boss.solve((rx, ry), self.char.hitbox.center)


                    
                    for bl in self.bullets:
                        bl.aim(bl, self.bullets, self.draw, self.surface)
                    for mb in self.m_bosses:
                        mb.aim(mb, self.m_bosses, self.draw, self.surface)
                    for bb in self.bosses:
                        bb.aim(bb, self.bosses, self.draw, self.surface)
                    # ВЗАИМОДЕЙСВИЯ
                    for obj in self.win_border:
                        self.border(obj)  # Барьер экрана

                    for bt in self.bullets:  # Вложенные циклы ммм...
                        for btl in self.bullets:
                            if bt == btl:  # Почему все вокруг путают нас с тобой?
                                continue  # Мы один человек?
                            if bt.hitbox.colliderect(btl.hitbox):
                                if bt in self.bullets:
                                    self.bullets.remove(bt)
                                if bt in self.draw:
                                    self.draw.remove(bt)
                                self.bullets.remove(btl)
                                self.draw.remove(btl)
                            for mb in self.m_bosses:
                                if bt.hitbox.colliderect(mb.hitbox):
                                    if bt in self.bullets:
                                        self.bullets.remove(bt)
                                    if bt in self.draw:
                                        self.draw.remove(bt)
                                if btl.hitbox.colliderect(mb.hitbox):
                                    if btl in self.bullets:
                                        self.bullets.remove(btl)
                                    if btl in self.draw:
                                        self.draw.remove(btl)
                            for bb in self.bosses:
                                if bt.hitbox.colliderect(bb.hitbox):
                                    if bt in self.bullets:
                                        self.bullets.remove(bt)
                                    if bt in self.draw:
                                        self.draw.remove(bt)
                                if btl.hitbox.colliderect(bb.hitbox):
                                    self.bullets.remove(btl)
                                    self.draw.remove(btl)
                        # Смерть
                        if not self.immortal:
                            if bt.hitbox.colliderect(self.char.hitbox):
                                self.death = True
                                self.bullets.remove(bt)
                                self.draw.remove(bt)

                elif self.pause:  # Пауза
                    self.draw.append(self.pause_menu)
                    self.draw.append(self.continue_but)
                    self.draw.append(self.exit_but)

                    while self.pause and not self.exit_but_r:
                        self.clock.tick(self.FPS)  # FPS контроль

                        self.blit(self.draw, [self.timer])  # Отрисовка объектов

                        fps = round(self.clock.get_fps(), 2)
                        pg.display.set_caption(f"FPS: {fps}")

                        for ev in pg.event.get():  # Отслеживание событий
                            # print(ev)
                            self.close(ev)
                            # self.switch_pause(ev)

                        self.pause = self.continue_but.process()
                        self.exit_but_r = self.exit_but.process()

                        if not self.pause:
                            self.pause = True
                        elif self.pause:
                            self.pause = False
                        if not self.pause or self.exit_but_r:
                            self.draw.remove(self.pause_menu)
                            self.draw.remove(self.continue_but)
                            self.draw.remove(self.exit_but)

                            self.start_but_r = False
                            self.auth_but_r = False
                elif self.death:  # Смерть
                    self.bullets.clear(), self.draw.clear()
                    (
                        self.start_but_r,
                        self.rest_but_r,
                        self.d_exit_but_r,
                        self.death,
                        self.record,
                        self.time,
                        self.char.hitbox.center,
                        self.d_time,
                    ) = \
                    (
                        False,
                        False,
                        False,
                        False,
                        self.time,
                        [0, 0, 0],
                        pg.mouse.get_pos(),
                        Font(self.font, self.timer.text, (0, 0, 0), (225, 65)),
                    )

                    while not self.rest_but_r and not self.d_exit_but_r:
                        self.clock.tick(self.FPS)  # FPS контроль


                        self.blit(
                            [self.rest_but, self.d_exit_but],
                            [self.d_text, self.d_time],
                            [self.death_bg],
                        )  # Отрисовка объектов

                        fps = round(self.clock.get_fps(), 2)
                        pg.display.set_caption(f"FPS: {fps}")

                        for ev in pg.event.get():  # Отслеживание событий
                            # print(ev)
                            self.close(ev)
                            # self.switch_pause(ev)

                        self.rest_but_r = self.rest_but.process()
                        self.d_exit_but_r = self.d_exit_but.process()
