import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    """飞船子弹管理"""
    def __init__(self, _settings, screen, ship):
        """在飞机的初始位置创建一个子弹"""
        super().__init__()
        self.sceern = screen
        # 先创建子弹的矩形，然后再设置具体位置
        self.rect = pygame.Rect(0, 0, _settings.bullet_width, _settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 用小数表示子弹位置
        self.y = float(self.rect.y)
        self.color = _settings.bullet_color
        self.speed_factor = _settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数
        self.y -= self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_buller(self):
        """屏幕上绘制子弹"""
        pygame.draw.rect(self.sceern,self.color,self.rect)