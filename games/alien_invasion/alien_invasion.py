"""外星人入侵"""

import sys
from time import sleep
import pygame
from bullet import Bullet
from game_stats import GameStats
from alien import Alien
from button import Button
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        # 设置
        self.settings = Settings()

        # 是否全屏
        if not self.settings.is_full_scree:
            # 记录屏幕
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height

        # 设置背景色。
        self.bg_color = self.settings.bg_color
        # 设置游戏属性
        pygame.display.set_caption(self.settings.caption)

        # 创建一个用于存储游戏统计信息的实例。
        self.stats = GameStats(self)
        # 飞船
        self.ship = Ship(self)
        # 子弹
        self.bullets = pygame.sprite.Group()
        # 创建外星人
        self.aliens = pygame.sprite.Group()
        # 创建外星人编队
        self._create_fleet()

        # 创建Play按钮。
        self.play_button = Button(self, "Play")

        # 积分表
        self.sb = Scoreboard(self)

    def _create_fleet(self):
        """创建外星人群。"""
        # 创建一个外星人。
        alien = Alien(self)
        self.aliens.add(alien)

        # 外星人占用宽度
        # alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        # 计算可容纳宽度： 屏幕宽度-减去2个单位宽度
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # 计算可容纳单位： 可容纳宽度 / 单位宽度
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        # 计算可用屏幕高度
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        # 计算可容纳行数
        number_rows = available_space_y // (2 * alien_height)

        # 创建第一行外星人。
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # 创建一个外星人并将其加入当前行。
                self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number):
        """创建一个外星人并将其放在当前行。"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施。"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，并改变它们的方向。"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 设置
            self._config()

            # 检查事件
            self._check_evens()
            # 游戏活跃更新子弹和外星人信息
            if self.stats.game_active:
                # 更新外星人列表
                self._update_aliens()
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

    # 更新外星人
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人和飞船之间的碰撞。
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕底端。"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理。
                self._ship_hit()
                break

    def _ship_hit(self):
        """响应飞船被外星人撞到。"""
        if self.stats.ships_left > 0:
            # 将ships_left减1。
            self.stats.ships_left -= 1
            # 重置游戏
            self._reset_game()
            # 更新飞船数量
            self.sb.prep_ships()
            # 暂停。
            sleep(0.5)
        else:
            # 游戏介绍
            print("Game over")
            # 游戏停止
            self.stats.game_active = False
            # 显示鼠标光标
            pygame.mouse.set_visible(True)

    def _reset_game(self):
        """重置游戏"""
        # 清空余下的外星人和子弹。
        self.aliens.empty()
        self.bullets.empty()
        # 创建一群新的外星人，并将飞船放到屏幕底端的中央。
        self._create_fleet()
        self.ship.center_ship()
        # 重置得分
        self.sb.prep_score()
        # 显示等级
        self.sb.prep_level()
        # 显示剩余飞船
        self.sb.prep_ships()

    # 更新子弹数
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            # 如果子弹下边界小于0 也就是屏幕顶部
            if bullet.rect.bottom <= 0:
                # 移除此子弹
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # 检查是否有子弹击中了外星人。
        # 如果是，就删除相应的子弹和外星人。
        # 穿甲弹
        # collisions = pygame.sprite.groupcollide(
        #     self.bullets, self.aliens, False, True)
        # 普通子弹
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            # 外星人碰撞的子弹都是字典collisions中的一个键，而与每颗子弹相关的值都是一个列表，其中包含该子弹击中的外星人
            for alien in collisions.values():
                self.stats.score += self.settings.alien_points * len(alien)
            self.sb.prep_score()
            self.sb.check_high_score()

        # 检查是否灭队,灭队了生成一批新的敌人
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            # 灭队 难度提升
            self.settings.increase_speed()
            # 提高等级。
            self.stats.level += 1
            self.sb.prep_level()

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
        if not self.stats.game_active:
            # 游戏非活跃状态时
            self.play_button.draw_button()

        # 显示得分。
        self.sb.show_score()

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

                print("键盘按下")
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

                if event.key == pygame.K_p:
                    # 按P开始游戏
                    print("按P开始游戏")
                    self._start_game(True)

            # 鼠标按下
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("鼠标按下")
                # pygame.mouse.get_pos() ，
                # 它返回一个元组，其中包含玩家单击时鼠标的x坐标和y坐标
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """在玩家单击Play按钮时开始新游戏。"""
        # 检查鼠标单击位置是否在Play按钮的rect 内
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # 开始游戏
        self._start_game(button_clicked)

    def _start_game(self, flag):
        """开始游戏"""
        if flag and not self.stats.game_active:
            self.stats.game_active = True
            self.stats.reset_stats()
            self._reset_game()
            # 隐藏鼠标光标。
            pygame.mouse.set_visible(False)
            # 初始化游戏难度
            self.settings.initialize_dynamic_settings();

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中。"""
        if self.stats.game_active:
            if len(self.bullets) < self.settings.bullets_allowed:
                # 没有超出子弹上限，添加一个子弹
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)
        else:
            print("游戏未开始")


if __name__ == '__main__':
    ai = AlienInvasion()
    # 运行游戏
    ai.run_game()
