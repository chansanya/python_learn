class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置。"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.is_full_scree = False
        # self.is_full_scree = True

        self.bg_color = (255, 255, 255)

        self.caption = '外星人入侵'

        # 移动速度
        self.step = 10
        # 大小
        self.step_width = 50
        self.step_height = 50

        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 1

        # 子弹设置
        self.bullet_speed = 0.5
        # 子弹宽高
        self.bullet_width = 15
        self.bullet_height = 25
        # 子弹颜色
        self.bullet_color = (60, 60, 60)
        # 子弹数
        self.bullets_allowed = 3

        # 外星人宽高
        self.alien_width = 50
        self.alien_height = 50

        # 外星人设置
        self.alien_speed = 0.4
        self.fleet_drop_speed = 10
        # fleet_direction为 1表示向右移，为-1表示向左移。
        self.fleet_direction = 1

        # 加快游戏节奏的速度。
        self.speedup_scale = 1.1
        # 分数加倍
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置。"""
        # 移动速度
        self.ship_speed = 1.5
        # 子弹速度
        self.bullet_speed = 0.5
        # 外星人速度
        self.alien_speed = 0.4

        # fleet_direction为1表示向右，为-1表示向左。
        self.fleet_direction = 1
        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        # 记分
        self.alien_points = int(self.alien_points * self.score_scale)
