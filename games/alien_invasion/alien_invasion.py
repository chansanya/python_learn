"""外星人入侵"""

import sys
import pygame

from bullet import Bullet
from alien import Alien
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
        # 子弹
        self.bullets = pygame.sprite.Group()
        # 创建外星人
        self.aliens = pygame.sprite.Group()
        # 创建外星人编队
        self._create_fleet()


    def _create_fleet(self):
        """创建外星人群。"""
        # 创建一个外星人。
        alien = Alien(self)
        self.aliens.add(alien)

        alien_width = alien.rect.width
        # 计算可容纳宽度： 屏幕宽度-减去2个单位宽度
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # 计算可容纳单位： 可容纳宽度 / 单位宽度
        number_aliens_x = available_space_x // (2 * alien_width)
        # 创建第一行外星人。
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行。
            alien = Alien(self)
            # 计算起始位置: 边距 + （单位+外边距）* 单位序列
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 设置
            self._config()
            # 检查事件
            self._check_evens()
            # 更新子弹列表
            self._update_bullets()
            # 重新绘制屏幕
            self._update_screen()

    def _config(self):
        # 设置长按的参数
        delay = 500  # 长按开始前的延迟时间（毫秒）
        interval = 100  # 连续触发间隔时间（毫秒）
        # 用于检测长按事件的计时器
        pygame.key.set_repeat(delay, interval)

    # 更新子弹数
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            # 如果子弹下边界小于0 也就是屏幕顶部
            if bullet.rect.bottom <= 0:
                # 移除此子弹
                self.bullets.remove(bullet)

    # 更新屏幕信息
    def _update_screen(self):
        """更新屏幕"""
        # 重新绘制屏幕
        self.screen.fill(self.bg_color)
        # 定位飞船位置
        self.ship.blitme()

        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 绘制外星人
        self.aliens.draw(self.screen)

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

                if event.key == pygame.K_SPACE:
                    # 发射子弹
                    self._fire_bullet()

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中。"""
        if len(self.bullets) < self.settings.bullets_allowed:
            # 没有超出子弹上限，添加一个子弹
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


if __name__ == '__main__':
    ai = AlienInvasion()
    # 运行游戏
    ai.run_game()

