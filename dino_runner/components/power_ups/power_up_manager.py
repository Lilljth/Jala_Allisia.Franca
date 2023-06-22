import random
import pygame

from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.life import Life


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appers == score:
            self.when_appers += random.randint(200,300)
            self.num = random.randint(0,2)
            if self.num == 0:
                self.power_ups.append(Shield())
            elif self.num == 1:
                self.power_ups.append(Hammer())
            elif self.num == 2:
                self.power_ups.append(Life())

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.mask.overlap(power_up.mask,
                (power_up.rect.x - game.player.dino_rect.x, 
                 power_up.rect.y - game.player.dino_rect.y)):
                if self.num != 2:
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.has_power_up = True
                    game.player.type = power_up.type
                    game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                    self.power_ups.remove(power_up)
                elif self.num == 2:
                    if game.life < 3:
                        game.life += 1
                        self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appers = random.randint(200, 300)