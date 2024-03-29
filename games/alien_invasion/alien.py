import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):
        super().__init__()

        """初始化飞船并设置其初始位置。"""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形。
        # ship_image = pygame.image.load('images/alien.png')
        ship_image = pygame.image.load('images/alien.png')
        # 缩放
        self.image = pygame.transform.scale(ship_image, (ai_game.settings.alien_width, ai_game.settings.alien_height))
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近。
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置。
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True。"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
