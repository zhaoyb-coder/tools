import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    """显示得分信息的类"""
    def __init__(self, _settings, screen, stats):
        """初始化分数属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self._settings = _settings
        self.stats = stats
        # 设置字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # 准备初始分数图像
        self.prep_score()
        # 准备最高分数图像
        self.prep_high_score()
        # 展示等级
        self.prep_level()
        # 展示剩余飞机个数
        self.prep_ships()

    def prep_score(self):
        """将分数转为图像"""
        # 将得分显示为10的整数倍\添加用逗号表示的千位分隔符
        round_score = round(self.stats.score, -1)
        score_str = "{:,}".format(round_score)
        self.score_img = self.font.render(score_str, True, self.text_color, self._settings.bg_color)
        # 分数放置在屏幕右上角
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """将最高分数转为图像"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_img = self.font.render(high_score_str, True, self.text_color, self._settings.bg_color)
        # 分数放置在屏幕顶部中央
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.right = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转为图像"""
        self.level_img = self.font.render(str(self.stats.level), True, self.text_color, self._settings.bg_color)
        # 等级放置于分数下方
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示还剩下多少飞机"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self._settings, self.screen, 30, 30)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """屏幕显示得分和等级"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)