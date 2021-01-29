import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示外星人的类"""
    def __init__(self, _settings, screen):
        """初始化外星人，并设置初始位置"""
        super().__init__()
        self.screen = screen
        self._settings = _settings
        # 加载外星人图像，并设置rect属性
        self.image = pygame.image.load('imgs/alien.bmp')
        self.rect = self.image.get_rect()
        # 初始位置都在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人具体位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果外星人处于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向右移动"""
        # 将移动量设置为外星人速度和fleet_direction的乘积，让外星人向左或向右移。
        # 如果fleet_direction为1，就将外星人当前的x坐标增大alien_speed_factor，从而将外星人向右移；
        # 如果fleet_direction为-1，就将外星人当前的x坐标减去alien_speed_factor，从而将外星人向左移。
        self.x += (self._settings.alien_speed_factor * self._settings.fleet_direction)
        self.rect.x = self.x