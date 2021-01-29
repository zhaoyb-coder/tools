class Settings():
    # 存储飞机大战游戏所有的设置参数
    def __init__(self):
        """ 初始化游戏设置 """
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 子弹设置
        # 宽3像素、高15像素的深灰色子弹;
        # 最多允许存在的子弹数量 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 有外星人撞到屏幕边缘时，外星人群向下移动的速度
        self.fleet_drop_speed = 10

        # 一局游戏最多拥有的飞机个数
        self.ship_limit = 3
        self.ship_width = 60
        self.ship_height = 60

        # 全局游戏节奏设置
        self.speedup_scale = 1.1
        # 外星人分数的节奏设置
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化游戏进行的设置"""
        # 一次按键飞机可以移动的像素大小
        self.ship_speed_factor = 1.5
        # 外星人移动速度
        self.alien_speed_factor = 1
        # 子弹移动速度
        self.bullet_speed_factor = 1
        # fleet_direction 1表示右移；-1表示左移
        self.fleet_direction = 1
        # 分数
        self.alien_points = 50

    def increase_speed(self):
        """提高游戏节奏"""
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
