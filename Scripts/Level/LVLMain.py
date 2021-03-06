import pygame
import random
import math

from Scripts.Util.LoadImages import ObstacleImages, LVLMainImages

from Scripts.Util.Functions import get_coords, get_max_coord, Raster, global_var
from Scripts.Util.Clock import Clock

from Scripts.Entity.Player import Player
from Scripts.Entity.Waiter import Waiter
from Scripts.Entity.Guest import Guest
from Scripts.GameModes.Order import OrderMenue
from Scripts.GameModes.Dialog import DialogMenue

from Scripts.Util.Obstacles import *

pygame.init()


class LVLMain:
    def __init__(self, win, setup):
        self.win_w, self.win_h = win.get_size()

        self.setup = setup

        self.sv = {"images": LVLMainImages(),
                   "obst_images": ObstacleImages(),
                   "win_w": self.win_w,
                   "win_h": self.win_h,
                   "wall_w": setup.wall_w,
                   "wall_h": setup.wall_h,
                   "cell_size": setup.cell_size,
                   "coord": setup.coord,
                   "max_coord": get_max_coord(setup.coord),
                   "raster": Raster(win, setup.wall_w, setup.wall_h, setup.cell_size),
                   "win_copy": win.copy()
                   }
        self.game_maxle = False
        self.g = None

    def init_main(self, win, create_char):
        # Obstacles und Interactables werden erstellt

        # create_char = CreateChar()

        filter_halo = pygame.Surface((self.win_w, self.win_h))  # the size of your rect, ist für drunkenness filter
        filter_halo.set_colorkey((255, 255, 255))  # wichtig für maskieren
        filter_halo.fill((255, 255, 255))
        surf_text = pygame.Surface((self.win_w, self.win_h))

        surf_dialog = pygame.Surface((self.sv["win_w"], self.sv["win_h"]))

        #    create_char.start_creation()
        from Scripts.Util.Functions import IncreaseI
        i = IncreaseI()

        # Fonts
        order_choose_font = pygame.font.SysFont('Courier', 33, True)
        order_choose_font.set_underline(True)

        # Obstacles und Interactables werden erstellt
        _obstacles = []
        _interactables = []

        _obstacles.append(Obstacle(i.increase(), "Walls_add", images.walls_add1, self.sv["coord"]["w"][21],
                                   self.sv["coord"]["h"][0],
                                   images.walls_add1.get_width(), images.walls_add1.get_height()))
        _obstacles.append(
            Obstacle(i.increase(), "Theke", images.img_bar, self.sv["coord"]["w"][3], self.sv["coord"]["h"][0],
                     images.img_bar.get_width(), images.img_bar.get_height(), 0, (2, 2)))
        _obstacles.append(Obstacle(i.increase(), "Schnapsregal", images.img_schnapsregal, self.sv["coord"]["w"][0],
                                   self.sv["coord"]["h"][0],
                                   images.img_schnapsregal.get_width(), images.img_schnapsregal.get_height()))

        # Tische und Stühle
        tisch_pos = {"tisch1": (9, 2), "tisch2": (10, 2), "tisch3": (17, 3), "tisch5": (18, 1), "tisch6": (22, 5),
                     "tisch7": (20, 7), "tisch9": (12, 9), "tisch10": (10, 8), "tisch11": (6, 10), "theke": (2, 4)}

        # Tisch 1
        _obstacles.append(
            Obstacle(i.increase(), "Tisch", images.img_table_31, self.sv["coord"]["w"][6], self.sv["coord"]["h"][2],
                     images.img_table_31.get_width(),
                     images.img_table_31.get_height(), 1, tisch_pos["tisch1"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][6], self.sv["coord"]["h"][1], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  180, 1, tisch_pos["tisch1"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][7], self.sv["coord"]["h"][1], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  180, 1, tisch_pos["tisch1"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][8], self.sv["coord"]["h"][1], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  180, 1, tisch_pos["tisch1"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][6], self.sv["coord"]["h"][3], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  0, 1, tisch_pos["tisch1"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][7], self.sv["coord"]["h"][3], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  0, 1, tisch_pos["tisch1"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][8], self.sv["coord"]["h"][3], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  0, 1, tisch_pos["tisch1"]))
        _interactables.append(
            Kerze(i.increase(), self.sv["coord"]["w"][7], self.sv["coord"]["h"][2], images.img_kerze[0].get_width(),
                  images.img_kerze[0].get_height(), filter_halo, 0))

        # Tisch 2
        _obstacles.append(
            Obstacle(i.increase(), "Tisch", images.img_table_11, self.sv["coord"]["w"][11],
                     self.sv["coord"]["h"][2],
                     images.img_table_11.get_width(),
                     images.img_table_11.get_height(),
                     2, tisch_pos["tisch2"]))
        _obstacles.append(
            Obstacle(i.increase(), "Tisch", images.img_table_11, self.sv["coord"]["w"][12],
                     self.sv["coord"]["h"][2],
                     images.img_table_11.get_width(),
                     images.img_table_11.get_height(), 2, tisch_pos["tisch2"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][11], self.sv["coord"]["h"][1], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  180, 2, tisch_pos["tisch2"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][11], self.sv["coord"]["h"][3], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  0, 2, tisch_pos["tisch2"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][12], self.sv["coord"]["h"][1], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  180, 2, tisch_pos["tisch2"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][12], self.sv["coord"]["h"][3], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  0, 2, tisch_pos["tisch2"]))
        _interactables.append(Kerze(i.increase(), self.sv["coord"]["w"][11], self.sv["coord"]["h"][2],
                                    images.img_kerze[0].get_width(),
                                    images.img_kerze[0].get_height(), filter_halo, 1))
        _interactables.append(Kerze(i.increase(), self.sv["coord"]["w"][12], self.sv["coord"]["h"][2],
                                    images.img_kerze[0].get_width(),
                                    images.img_kerze[0].get_height(), filter_halo, 1))

        # Tisch 3
        _obstacles.append(
            Obstacle(i.increase(), "Tisch", images.img_table_11, self.sv["coord"]["w"][16],
                     self.sv["coord"]["h"][2],
                     images.img_table_11.get_width(),
                     images.img_table_11.get_height(), 3, tisch_pos["tisch3"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][16], self.sv["coord"]["h"][1], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  180, 3, tisch_pos["tisch3"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][16], self.sv["coord"]["h"][3], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  0, 3, tisch_pos["tisch3"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][17], self.sv["coord"]["h"][2], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  90, 3, tisch_pos["tisch3"]))
        _interactables.append(Kerze(i.increase(), self.sv["coord"]["w"][16], self.sv["coord"]["h"][2],
                                    images.img_kerze[0].get_width(),
                                    images.img_kerze[0].get_height(), filter_halo, 0))
        # Tisch 5
        _obstacles.append(
            Obstacle(i.increase(), "Tisch", images.img_table_11, self.sv["coord"]["w"][19],
                     self.sv["coord"]["h"][0],
                     images.img_table_11.get_width(),
                     images.img_table_11.get_height(), 5, tisch_pos["tisch5"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][18], self.sv["coord"]["h"][0], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  270, 5, tisch_pos["tisch5"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][19], self.sv["coord"]["h"][1], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  0, 5, tisch_pos["tisch5"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][20], self.sv["coord"]["h"][0], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  90, 5, tisch_pos["tisch5"]))
        _interactables.append(Kerze(i.increase(), self.sv["coord"]["w"][19], self.sv["coord"]["h"][0],
                                    images.img_kerze[0].get_width(),
                                    images.img_kerze[0].get_height(), filter_halo, 1))

        # Tisch 6
        _obstacles.append(
            Obstacle(i.increase(), "Tisch", images.img_table_12, self.sv["coord"]["w"][22],
                     self.sv["coord"]["h"][3],
                     images.img_table_12.get_width(),
                     images.img_table_12.get_height(), 6, tisch_pos["tisch6"]))
        _interactables.append(Barstool(i.increase(), self.sv["coord"]["w"][21], self.sv["coord"]["h"][3],
                                       images.img_barstool.get_width(),
                                       images.img_barstool.get_height(), 270, 6, tisch_pos["tisch6"]))
        _interactables.append(Barstool(i.increase(), self.sv["coord"]["w"][21], self.sv["coord"]["h"][4],
                                       images.img_barstool.get_width(),
                                       images.img_barstool.get_height(), 270, 6, tisch_pos["tisch6"]))
        _interactables.append(Barstool(i.increase(), self.sv["coord"]["w"][23], self.sv["coord"]["h"][3],
                                       images.img_barstool.get_width(),
                                       images.img_barstool.get_height(), 90, 6, tisch_pos["tisch6"]))
        _interactables.append(Barstool(i.increase(), self.sv["coord"]["w"][23], self.sv["coord"]["h"][4],
                                       images.img_barstool.get_width(),
                                       images.img_barstool.get_height(), 90, 6, tisch_pos["tisch6"]))
        _interactables.append(Kerze(i.increase(), self.sv["coord"]["w"][22], self.sv["coord"]["h"][3],
                                    images.img_kerze[0].get_width(),
                                    images.img_kerze[0].get_height(), filter_halo, 0))

        # Tisch 7
        _obstacles.append(
            Obstacle(i.increase(), "Tisch", images.img_table_13, self.sv["coord"]["w"][20],
                     self.sv["coord"]["h"][8],
                     images.img_table_13.get_width(),
                     images.img_table_13.get_height(), 7, tisch_pos["tisch7"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][19], self.sv["coord"]["h"][8], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  270, 7, tisch_pos["tisch7"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][19], self.sv["coord"]["h"][9], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  270, 7, tisch_pos["tisch7"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][19], self.sv["coord"]["h"][10], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  270, 7, tisch_pos["tisch7"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][21], self.sv["coord"]["h"][8], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  90, 7, tisch_pos["tisch7"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][21], self.sv["coord"]["h"][9], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  90, 7, tisch_pos["tisch7"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][21], self.sv["coord"]["h"][10], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  90, 7, tisch_pos["tisch7"]))
        _interactables.append(Kerze(i.increase(), self.sv["coord"]["w"][20], self.sv["coord"]["h"][9],
                                    images.img_kerze[0].get_width(),
                                    images.img_kerze[0].get_height(), filter_halo, 1))

        # Tisch 9
        _obstacles.append(
            Obstacle(i.increase(), "Tisch", images.img_table_31, self.sv["coord"]["w"][13],
                     self.sv["coord"]["h"][9],
                     images.img_table_31.get_width(),
                     images.img_table_31.get_height(), 9, tisch_pos["tisch9"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][13], self.sv["coord"]["h"][8], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  180, 9, tisch_pos["tisch9"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][14], self.sv["coord"]["h"][8], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  180, 9, tisch_pos["tisch9"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][15], self.sv["coord"]["h"][8], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  180, 9, tisch_pos["tisch9"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][13], self.sv["coord"]["h"][10], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  0, 9, tisch_pos["tisch9"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][14], self.sv["coord"]["h"][10], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  0, 9, tisch_pos["tisch9"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][15], self.sv["coord"]["h"][10], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  0, 9, tisch_pos["tisch9"]))
        _interactables.append(Kerze(i.increase(), self.sv["coord"]["w"][14], self.sv["coord"]["h"][9],
                                    images.img_kerze[0].get_width(),
                                    images.img_kerze[0].get_height(), filter_halo, 0))

        # Tisch 10
        _obstacles.append(
            Obstacle(i.increase(), "Tisch", images.img_table_13, self.sv["coord"]["w"][10],
                     self.sv["coord"]["h"][9],
                     images.img_table_13.get_width(),
                     images.img_table_13.get_height(), 10, tisch_pos["tisch10"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][9], self.sv["coord"]["h"][9], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  270, 10, tisch_pos["tisch10"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][9], self.sv["coord"]["h"][10], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  270, 10, tisch_pos["tisch10"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][9], self.sv["coord"]["h"][11], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  270, 10, tisch_pos["tisch10"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][11], self.sv["coord"]["h"][9], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  90, 10, tisch_pos["tisch10"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][11], self.sv["coord"]["h"][10], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  90, 10, tisch_pos["tisch10"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][11], self.sv["coord"]["h"][11], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  90, 10, tisch_pos["tisch10"]))
        _interactables.append(Kerze(i.increase(), self.sv["coord"]["w"][10], self.sv["coord"]["h"][10],
                                    images.img_kerze[0].get_width(),
                                    images.img_kerze[0].get_height(), filter_halo, 1))

        # Tisch 11
        _obstacles.append(
            Obstacle(i.increase(), "Tisch", images.img_table_11, self.sv["coord"]["w"][7],
                     self.sv["coord"]["h"][11],
                     images.img_table_11.get_width(),
                     images.img_table_11.get_height(), 11, tisch_pos["tisch11"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][6], self.sv["coord"]["h"][11], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  270, 11, tisch_pos["tisch11"]))
        _interactables.append(
            Chair(i.increase(), self.sv["coord"]["w"][7], self.sv["coord"]["h"][10], images.img_chair.get_width(),
                  images.img_chair.get_height(),
                  180, 11, tisch_pos["tisch11"]))
        _interactables.append(Kerze(i.increase(), self.sv["coord"]["w"][7], self.sv["coord"]["h"][11],
                                    images.img_kerze[0].get_width(),
                                    images.img_kerze[0].get_height(), filter_halo, 0))

        # Thekenbestuhlung
        _interactables.append(
            Barstool(i.increase(), self.sv["coord"]["w"][6], self.sv["coord"]["h"][5], images.img_chair.get_width(),
                     images.img_chair.get_height(),
                     90, 100, tisch_pos["theke"]))
        _interactables.append(
            Barstool(i.increase(), self.sv["coord"]["w"][6], self.sv["coord"]["h"][6], images.img_chair.get_width(),
                     images.img_chair.get_height(),
                     90, 100, tisch_pos["theke"]))
        _interactables.append(
            Barstool(i.increase(), self.sv["coord"]["w"][5], self.sv["coord"]["h"][7], images.img_chair.get_width(),
                     images.img_chair.get_height(),
                     0, 100, tisch_pos["theke"]))
        _interactables.append(
            Barstool(i.increase(), self.sv["coord"]["w"][4], self.sv["coord"]["h"][7], images.img_chair.get_width(),
                     images.img_chair.get_height(),
                     0, 100, tisch_pos["theke"]))
        _interactables.append(
            Kerze(i.increase(), self.sv["coord"]["w"][5], self.sv["coord"]["h"][4], images.img_kerze[0].get_width(),
                  images.img_kerze[0].get_height(), filter_halo, 1))

        print(self.sv["coord"]["w"][7])
        # WandKerzen
        _interactables.append(
            KerzeWand(i.increase(),
                      self.sv["coord"]["w"][7],
                      self.sv["wall_h"] - 2 * self.sv["cell_size"],
                      self.sv["obst_images"].img_kerze_wand.get_width(),
                      self.sv["obst_images"].img_kerze_wand.get_height(),
                      0,
                      filter_halo))
        _interactables.append(
            KerzeWand(i.increase(), self.sv["coord"]["w"][7],
                      self.sv["win_h"] - self.sv["wall_w"] + self.sv["cell_size"],
                      images.img_kerze_wand.get_width(),
                      images.img_kerze_wand.get_height(), 180, filter_halo))
        _interactables.append(
            KerzeWand(i.increase(), self.sv["coord"]["w"][16], self.sv["wall_h"] - 2 * self.sv["cell_size"],
                      images.img_kerze_wand.get_width(),
                      images.img_kerze_wand.get_height(), 0, filter_halo))
        _interactables.append(
            KerzeWand(i.increase(), self.sv["coord"]["w"][16],
                      self.sv["win_h"] - self.sv["wall_w"] + self.sv["cell_size"],
                      images.img_kerze_wand.get_width(),
                      images.img_kerze_wand.get_height(), 180, filter_halo))
        _interactables.append(KerzeWand(i.increase(), self.sv["coord"]["w"][22], self.sv["coord"]["h"][1],
                                        images.img_kerze_wand.get_width(),
                                        images.img_kerze_wand.get_height(), 0, filter_halo))

        _interactables.append(
            Chalkboard(i.increase(), self.sv["coord"]["w"][11], self.sv["win_h"] - self.sv["wall_h"],
                       images.img_chalkboard.get_width(),
                       images.img_chalkboard.get_height(), 180))
        i = IncreaseI()
        _interactables.append(
            Door(i.increase(), self.sv["coord"]["w"][0], self.sv["coord"]["h"][12], images.img_door[0].get_width(),
                 images.img_door[0].get_height(),
                 0, self.sv["coord"], self.sv["cell_size"], "kitchen"))
        _interactables.append(
            Door(i.increase(), self.sv["coord"]["w"][25], self.sv["coord"]["h"][3], images.img_door[0].get_width(),
                 images.img_door[0].get_height(),
                 90, self.sv["coord"], self.sv["cell_size"], "outside"))
        _door_pos = []

        _interactables.append(
            Stairs(i.increase(), self.sv["coord"]["w"][13], self.sv["coord"]["h"][0], images.img_stairs.get_width(),
                   images.img_stairs.get_height(),
                   90, self.sv["coord"][self.sv["max_coord"]], self.sv["cell_size"]))
        for _i in _interactables:
            if _i.art == 'door' or _i.art == 'stairs':
                _door_pos.append(_i.serv_pos)

        _radio = Radio(i.increase(), self.sv["coord"]["w"][1], self.sv["coord"]["h"][0],
                       images.img_radio[0].get_width(),
                       images.img_radio[0].get_height())
        _interactables.append(_radio)

        # drinks: Nr. : ('Name', Preis, Alkoholgehalt. # ?Anzahl der Schlücke? #
        # hier scheint noch ein bug zu sein,
        # wenn man das zweite getränk bestellt(?) hat man mehr (doppelt so viele?) schlücke
        _drinks = {0: ("", 0, 0, 0), 1: ("Bier", 3, 10, 10), 2: ("Wein", 4, 5, 5), 3: ("Schnaps", 2, 30, 1),
                   4: ("Kaffee", 3, -3, 6)}

        _chairs = []
        _kerzen_list = []
        for _i in _interactables:
            if _i.art == 'chair':
                _chairs.append(_i)
            if _i.art == 'kerze':
                _kerzen_list.append(_i)
        random.shuffle(_chairs)

        _clock = Clock(i.increase(), 50, 500)

        _guy = Player(self.sv["coord"]["w"][8], self.sv["coord"]["h"][4], self.sv["cell_size"],
                      self.sv["cell_size"], True, create_char.new_tilemap, 64 / 4)
        _waiter = [
            Waiter(self.sv["coord"]["w"][2], self.sv["coord"]["h"][2], self.sv["cell_size"], self.sv["cell_size"],
                   _obstacles, True,
                   create_char.create_tilemap(win))]
        # gäste hinzufügen
        _guests = []
        for _i in range(0, 15):
            vel = 8
            guest = Guest(self.sv["coord"]["w"][24], self.sv["coord"]["h"][6], self.sv["cell_size"],
                          self.sv["cell_size"], vel, _chairs.pop(),
                          (random.randint(0, 0), random.randint(0, 60)), False)
            _guests.append(guest)
        # invent = Inventory()

        _order_menue = OrderMenue(_drinks)
        _dialog_menue = DialogMenue(self.win_w, self.sv["win_h"], surf_dialog, _guy)

        _halo_count = 1

        return _obstacles, _interactables, _door_pos, _radio, _drinks, _chairs, _kerzen_list, _clock, _guy, _waiter,\
            _guests, _order_menue, _dialog_menue, _halo_count, surf_text, filter_halo

    def init_draw(self, win, create_char):

        win.blit(self.sv["images"].bg, (0, 0))
        win.blit(self.sv["images"].img_ground, (self.sv["wall_w"], self.sv["wall_h"]))

        obstacles, interactables, door_pos, radio, drinks, chairs, kerzen_list, clock, guy, waiter,\
            guests, order_menue, dialog_menue, halo_count, surf_text, filter_halo = self.init_main(win, create_char)

        for obst in obstacles:
            win.blit(obst.pic, (obst.x, obst.y))

        music1 = pygame.mixer.music.load('../Sound/BlueSkies.mp3')
        sound1 = pygame.mixer.Sound('../Sound/Background_1.wav')
        sound1.set_volume(0)
        channel_bg = pygame.mixer.Channel(0)
        channel_bg.play(sound1, -1)  # ist das richtig so???

        sound_count = 0

        inventory_active = False
        text_count = 50
        win_copy = win.copy()

        for inter in interactables:
            if inter.art == 'door' or inter.art == 'radio':
                inter.draw_int(win, win_copy)
            else:
                inter.draw(win)

        clock.calc()
        clock.draw(win)
        raster = Raster(win, self.sv["wall_w"], self.sv["wall_h"], self.sv["cell_size"])
        raster.draw(win)
        self.sv["win_copy"] = win.copy()
        timer_clock = pygame.time.Clock()

        g = global_var(waiter, drinks, clock, raster, order_menue, dialog_menue, obstacles, interactables,
                       surf_text, music1, sound_count, inventory_active, text_count, sound1, radio, kerzen_list,
                       door_pos, chairs, halo_count, timer_clock, guy, guests, filter_halo)

        pygame.display.update()
        pygame.key.set_repeat()  # nochmal testen, funktioniert glaub ich noch nicht
        return win, g

    def redraw_game_window(self, win, g):
        dirtyrects = []
        # SOUND
        # Mit jedem Gast werden die Bargeräusche lauter
        volume = int(sum(i.inside for i in g.guests) / len(g.guests))
        if g.sound_count <= volume:
            g.sound_count += 0.0002
        g.sound1.set_volume(g.sound_count)

        if g.guy.ingame:
            if g.guy.start_game:
                g.win_copy_2 = win.copy()
            elif g.guy.end_game:
                win.blit(self.sv["win_copy"], (0, 0))
                dirtyrects.append(pygame.Rect(0, 0, self.win_w, self.win_h))
                g.guy.ingame = False
                g.guy.end_game = False

        dirtyrects = dirtyrects + self.del_last_blit(win, g)
        # Text

        # controls
        #_run, _kitchen = self.controls(g)

        # movement_calculation
        if g.guy.orderAction != 5 and g.guy.orderAction != 6 and g.guy.talk_action != 2 and not g.guy.ingame:
            dirtyrects = dirtyrects + self.movement_calcuation(win, g)

        # draw
        self.draw_blits(win, g)

        if g.guy.orderAction == 6:
            dirtyrects.append(g.order_menue.draw(win, g.win_copy_2, self.win_h))

        elif g.guy.talk_action == 2:
            # random choice muss hier rein!
            dirtyrects = dirtyrects + g.dialog_menue.draw(win, g.win_copy_2)
        if g.guy.ingame:
            if g.guy.start_game:

                dirtyrects = dirtyrects + [self.game_maxle.draw_init(win)]
                g.guy.start_game = False
            else:
                dirtyrects = self.game_maxle.do_turn(win)

        return dirtyrects, _run, _kitchen

    def draw_blits(self, win, g):

        _dirtyrects = []
        g.clock.draw(win)
        # characters
        g.guy.draw_char(win)
        g.waiter[0].draw_char(win)
        for guest in g.guests:
            if guest.walk_in[0] == g.clock.h_m[0] and guest.walk_in[1] <= g.clock.h_m[1] or guest.walk_in[0] < \
                    g.clock.h_m[0]:
                guest.draw_char(win)

        #           Zeichnen - Balken und Text
        g.guy.draw_display(win, g.guy.drunkenness)  # Display g.guy
        g.waiter[0].draw_display(win, g.waiter[0].angryness)  # Display g.guy
        for i in g.guests:
            if i.inside:
                _dirtyrects.append(i.draw_display(win, i.drunkenness))  # Display Waiter

        # Zeige Text an
        if g.guy.text_count < 50:
            _dirtyrects.append(g.guy.talk(win))
        if g.waiter[0].text_count < 50:
            _dirtyrects.append(g.waiter[0].talk(win))
        for i in g.guests:
            if i.text_count < 50:
                _dirtyrects.append(i.talk(win))

        # Filter für Lichteffekte
        g.halo_count += 1
        if g.halo_count >= 100:  # pi *30
            halo_count = 0
        g.filter_halo.set_alpha(round(math.sin((g.halo_count / 100) * math.pi) * 100))
        win.blit(g.filter_halo, (0, 0))

    def movement_calcuation(self, win, g):
        _dirtyrects = []
        # all interactables with own animation
        for _inter in g.interactables:
            if _inter.active:
                if isinstance(_inter, Door) or isinstance(_inter, Radio):
                    _dirtyrects.append(_inter.calc())
                    _inter.draw_int(win, self.sv["win_copy"])
        _dirtyrects.append(g.clock.calc())
        # g.guy
        _dirtyrects.append(g.guy.calc_movement(win, g))
        # Waiter
        _dirtyrects.append(g.waiter[0].calc_movement(g, self.sv["coord"][self.sv["max_coord"]],
                                                     self.sv["win_w"], self.sv["win_h"],
                                                     self.sv["wall_w"], self.sv["wall_h"],
                                                     g.door_pos, self.sv["cell_size"]))

        # Guests
        for guest in g.guests:
            if guest.walk_in[0] == g.clock.h_m[0] and guest.walk_in[1] <= g.clock.h_m[1] or guest.walk_in[0] < \
                    g.clock.h_m[0]:
                guest.calc_movement(g, self.sv["coord"][self.sv["max_coord"]],
                                    self.sv["win_w"], self.sv["win_h"],
                                    self.sv["wall_w"], self.sv["wall_h"],
                                    self.sv["cell_size"])
        # Displays
        _dirtyrects.append(g.guy.calc_display())  # Display g.guy
        _dirtyrects.append(g.waiter[0].calc_display())  # Display Waiter
        for i in g.guests:
            if i.inside:
                _dirtyrects.append(i.calc_display())  # Display Waiter
        return _dirtyrects

    def del_last_blit(self, win, setup, g):
        dirtyrects = list()

        if g.guy.ingame:
            if g.guy.start_game:
                g.win_copy_2 = win.copy()
            elif g.guy.end_game:
                win.blit(self.sv["win_copy"], (0, 0))
                dirtyrects.append(pygame.Rect(0, 0, self.setup.win_w, self.setup.win_h))
                g.guy.ingame = False
                g.guy.end_game = False
        # wenn OrderMenue aufgemacht wird, wird eine Kopie des gesamten Bildes gespeichert
        elif g.guy.orderAction == 5:
            win_copy_2 = win.copy()
            g.guy.orderAction = 6

        # wenn OrderMenue geschlossen wird, wird das Bild mit  der Kopie üüberblittet
        elif g.guy.orderAction == 7:
            win.blit(g.win_copy_2, (0, 0))
            dirtyrects.append(pygame.Rect(0, 0, win_w, win_h))
            g.guy.orderAction = 8

        # wenn Dialog Menue aufgemacht wird, wird eine Kopie des gesamten Bildes gespeichert
        elif g.guy.talk_action == 1:
            g.win_copy_2 = win.copy()
            g.guy.talk_action = 2

        # überblitten mit alter Kopie
        elif g.guy.talk_action == 2:
            win.blit(self.sv["win_copy"], (0, 0))
            dirtyrects.append(pygame.Rect(0, 0, win_w, win_h))

        # Wenn Normales In-Game Window angezeigt wird, soll alles, was sich bewegen kann, ( auch halos )
        # wieder mit Kopie ohne bewegliche sachen überblittet werden.
        else:
            dirtyrects.append(g.radio.del_blit(win, self.sv["win_copy"]))
            for i in g.kerzen_list:  # Kerzen löschen
                dirtyrects.append(i.repaint(win, self.sv["win_copy"]))
            dirtyrects.append(g.guy.del_blit(win, self.sv["win_copy"]))  # g.guy
            dirtyrects.append(g.guy.del_display(win, self.sv["win_copy"]))  # Display g.guy
            if g.guy.text_count < 51:  # Textzeile wieder überblitten
                dirtyrects.append(g.guy.del_text(win, self.sv["win_copy"]))

            dirtyrects.append(g.waiter[0].del_blit(win, self.sv["win_copy"]))  # Waiter
            dirtyrects.append(g.waiter[0].del_display(win, self.sv["win_copy"]))  # Display Waiter
            if g.waiter[0].text_count < 51:  # Textzeile wieder überblitten
                dirtyrects.append(g.waiter[0].del_text(win, self.sv["win_copy"]))

            for i in g.guests:
                dirtyrects.append(i.del_blit(win, self.sv["win_copy"]))  # Guests
                dirtyrects.append(i.del_display(win, self.sv["win_copy"]))  # Display Waiter
                if i.text_count < 51:  # Textzeile wieder überblitten
                    dirtyrects.append(i.del_text(win, self.sv["win_copy"]))
        #        # Inventar offen:
        #        if inventory_active:
        #            invent.draw(win, inventory_pic, g.guy.inventory)

        return dirtyrects


    def run_lvl(self, win, g):
        run = True
        while run:
            _dirtyrects, run, kitchen = self.redraw_game_window(win, g)
            g.timer_clock.tick(30)
            pygame.display.update(_dirtyrects)

        if kitchen:
            #            if lvl_kitchen not in locals():
            from Level.CreateKitchen import LVLKitchen
            lvl_kitchen = LVLKitchen(win)
            g.guy.x = lvl_kitchen.sv["coord"]["w"][7]
            g.guy.y = lvl_kitchen.sv["coord"]["h"][0]
            g.guy.facing = 2
            self.g = g
            lvl_kitchen.run_lvl(win, g, self)

        win.blit(self.sv["images"].game_over, (win_w / 2 - 400, win_h / 2 - 232))
        pygame.display.update()
        pygame.quit()
