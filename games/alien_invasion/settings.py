class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置。"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.is_full_scree = False
        # self.is_full_scree = True

        self.bg_color = (230, 230, 230)

        self.caption = '外星人入侵'

        # 移动速度
        self.step = 100
        # 大小
        self.step_width = 50
        self.step_height = 50

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)