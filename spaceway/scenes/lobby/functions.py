from sys import exit

import pygame

from .objects import PlayButton


def check_events(config, scene_buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            exit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            scene_buttons.get_by_instance(PlayButton).press()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if not scene_buttons.perform_point_collides((x, y)):
                if config['user']['color'] >= 2:
                    config['user']['color'] = 0
                else:
                    config['user']['color'] += 1

                config.save()


def update(bg, scene_buttons, caption, config):
    pygame.mixer.unpause()
    if not config['ns'].mm.get('lobby').get_num_channels():
        config['ns'].mm.get('lobby').play(-1)

    bg.blit()

    scene_buttons.draw()

    caption.update()
    caption.blit()
