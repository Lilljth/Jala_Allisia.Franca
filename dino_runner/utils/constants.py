import pygame
import os
pygame.mixer.init()

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Cat/catrun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cat/catrun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Cat/catwool1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cat/catwool2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Cat/catdonut1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cat/catdonut2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Cat/catjump2.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Cat/catwooljump2.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Cat/catdonutjump2.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Cat/catduck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cat/catduck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Cat/catwool1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cat/catwool2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Cat/catdonutduck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cat/catdonutduck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Small1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Small2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Small3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Large1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Large2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Obstacles/Large3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/wool.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/donut.png'))

BG = [
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track2.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track3.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track4.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/Track5.png'))
]

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/heart.png'))
MUSIC = pygame.mixer.music.load("dino_runner/assets/Music/Nyan Cat.mp3")

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
