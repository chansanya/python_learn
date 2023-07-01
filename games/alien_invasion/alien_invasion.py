"""外星人入侵"""

import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        # 设置
        self.settings = Settings()

        if not self.settings.is_full_scree:
            # 记录屏幕
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        else:
            self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height

        # 设置背景色。
        self.bg_color = self.settings.bg_color
        # 设置游戏属性
        pygame.display.set_caption(self.settings.caption)

        # 飞船
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._config()
            self._check_evens()
            self._update_screen()

    def _config(self):
        # 设置长按的参数
        delay = 500  # 长按开始前的延迟时间（毫秒）
        interval = 100  # 连续触发间隔时间（毫秒）
        # 用于检测长按事件的计时器
        pygame.key.set_repeat(delay, interval)

    def _update_screen(self):
        """更新屏幕"""

        # 重新绘制屏幕
        self.screen.fill(self.bg_color)

        # 定位飞船位置
        self.ship.blitme()
        # 让最近绘制的屏幕可见。
        pygame.display.flip()

    def _check_evens(self):
        """监视键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("游戏关闭")
                sys.exit()

            if event.type == pygame.KEYDOWN:
                """键盘按下"""
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key == pygame.K_LEFT:
                    self.ship.rect.left -= self.settings.step
                    if self.ship.rect.left < self.ship.screen_rect.left:
                        self.ship.rect.left = self.ship.screen_rect.left

                if event.key == pygame.K_RIGHT:
                    self.ship.rect.left += self.settings.step
                    if self.ship.rect.right > self.ship.screen_rect.right:
                        self.ship.rect.right = self.ship.screen_rect.right

                if event.key == pygame.K_UP:
                    self.ship.rect.top -= self.settings.step
                    if self.ship.rect.top < self.ship.screen_rect.top:
                        self.ship.rect.top = self.ship.screen_rect.top

                if event.key == pygame.K_DOWN:
                    self.ship.rect.bottom += self.settings.step
                    if self.ship.rect.bottom > self.ship.screen_rect.bottom:
                        self.ship.rect.bottom = self.ship.screen_rect.bottom


if __name__ == '__main__':
    ai = AlienInvasion()
    # 运行游戏
    ai.run_game()
