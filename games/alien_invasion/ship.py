import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置。"""
        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # 加载飞船图像并获取其外接矩形。
        # ship_image = pygame.image.load('images/ship.gif')
        ship_image = pygame.image.load('images/supper_ship.png')
        # 缩放
        self.image = pygame.transform.scale(ship_image, (ai_game.settings.step_width, ai_game.settings.step_height))
        self.rect = self.image.get_rect()
        # 对于每艘新飞船，都将其放在屏幕底部的中央。
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船。"""
        # 第一个参数 图片
        # 第二个参数 矩形坐标
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        # self.x = float(self.rect.x)
