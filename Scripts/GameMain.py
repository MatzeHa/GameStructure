import pygame
import os

from Scripts.Entity import Entity
from Scripts.PauseMenu import PauseMenu
from Scripts.Controls import controls_game, controls_pause

pygame.init()

if __name__ == "__main__":
    class Setup:
        def __init__(self):
            self.win = pygame.Surface((0, 0))
            self.dirtyrects = []
            self.win_w = 800
            self.win_h = 800
            self.win_size = (self.win_w, self.win_h)
            self.bgcol = (0, 0, 255)

        def update_bg(self, _win):
            self.bgcol = pause_menue.options["bgcol"]
            _win.fill(self.bgcol)
            self.win = _win.copy()

    setup = Setup()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "0, 33"
    win = pygame.display.set_mode((setup.win_w, setup.win_h))
    pygame.display.set_caption("Matzes Kneipenspiel", "MK")
    setup.win = win.copy()
    clock = pygame.time.Clock()
    run = True

    entity = Entity()
    opponents = []
    for i in range(0, 5):
        opponents.append(Entity())
    pause_menue = PauseMenu(win, setup)

    pygame.mouse.set_visible(False)
    while run:
        # EINGABE
        if pause_menue.active:
            run = controls_pause(pause_menue)

            if pause_menue.end_pause:
                setup.dirtyrects.append(pause_menue.dirtyrect)
                setup.update_bg(win)
                pause_menue.reset_pause_menue()
            else:
                setup.dirtyrects = [pause_menue.blitten()]


        else:
            run = controls_game(entity, pause_menue, setup)
            for i in opponents:
                i.random_walk()

            win.blit(win, (0, 0))
            pygame.display.update()

            # Überblitten
            entity.overblit(win, setup)
            for i in opponents:
                i.overblit(win, setup)
            setup.dirtyrects = []



            # Berechnungen

            setup.dirtyrects.append(entity.movement())
            for i in opponents:
                setup.dirtyrects.append(i.movement())

            # Blitten
            entity.blitten(win)
            for i in opponents:
                i.blitten(win)

        if not pause_menue.quit:
            clock.tick(30)
            pygame.display.update(setup.dirtyrects)
        else:
            pygame.quit()
            run = False
