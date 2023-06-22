import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus, Large_Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SHIELD_TYPE, HAMMER_TYPE


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        self.result = random.randint(0,2)

        if len(self.obstacles) == 0:
            if self.result == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif self.result == 1:
                self.obstacles.append(Large_Cactus(LARGE_CACTUS))
            elif self.result == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed,self.obstacles)
            if game.player.mask.overlap(obstacle.mask,
                (obstacle.rect.x - game.player.dino_rect.x, 
                 obstacle.rect.y - game.player.dino_rect.y)):
                if not game.player.has_power_up and game.life > 1:
                    game.life -= 1
                    self.obstacles.remove(obstacle)
                elif not game.player.has_power_up and game.life <= 1:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    if game.player.type == HAMMER_TYPE:
                        self.obstacles.remove(obstacle)
                    else:
                        ...

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    