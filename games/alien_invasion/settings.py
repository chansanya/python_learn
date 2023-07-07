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
