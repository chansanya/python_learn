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
        self.step = 100

        self.step_width = 50
        self.step_height = 50
