import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, HEART
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
FONT_STYLE = 'freesansbold.ttf'


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.life = 3
        self.death_count = 0
        self.bg_color = 255
        self.text_color = 0

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def reset(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        self.life = 3
        self.bg_color = 255
        self.text_color = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self)
        if self.score >= 200 and self.score <= 600:
            if self.bg_color != 0:
                self.bg_color -= 15
                self.text_color +=15


    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 1

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((self.bg_color, self.bg_color, self.bg_color))
        self.draw_background()
        self.draw_score()
        self.draw_life()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        self.draw_image(BG[0], 380)
        if self.score >= 601 and self.score <= 900:
            self.screen.blit(BG[1], (0,0))
        elif self.score >=901 and self.score <= 1300:
            self.screen.blit(BG[2], (0,0))
        elif self.score >= 1301 and self.score <= 1600:
            self.screen.blit(BG[3], (0,0))
        elif self.score >= 1601 and self.score <= 1900:
            self.screen.blit(BG[4], (0,0))
        elif self.score >= 1901:
            self.screen.blit(BG[5], (0,0))

    def draw_image(self, image, y):
        image_width = image.get_width()
        self.screen.blit(image, (self.x_pos_bg, y))
        self.screen.blit(image, (image_width + self.x_pos_bg, y))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(image, (image_width + self.x_pos_bg, y))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        self.text(f'Score: {self.score}', (1000, 50))

    def draw_life(self):
        for i in range(1, self.life +1):
            self.screen.blit(HEART, (50*i,50))

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000,2)
            if time_to_show >= 0:
                self.text(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                    (500, 50)
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
                    

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.player = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def text(self, texto, posicao):
        font = pygame.font.Font(FONT_STYLE, 22)
        self.texto = font.render(texto, True, (self.text_color, self.text_color, self.text_color))
        self.posicao = self.texto.get_rect()
        self.posicao.center = posicao 
        self.screen.blit(self.texto, self.posicao)


    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.screen.fill((255,255,255))
            self.text("Press any key to start", (half_screen_width, half_screen_height))
            
        else:
            self.screen.blit(ICON, (half_screen_width -80, half_screen_height - 140))
            self.text("Press any key to start", (half_screen_width, half_screen_height))
            self.text(f"Death Count: {self.death_count}", (half_screen_width, half_screen_height + 30))
            self.text(f"Score: {self.score}", (half_screen_width, half_screen_height + 60))


        pygame.display.update()

        self.handle_events_on_menu()