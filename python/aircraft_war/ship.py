import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, _settings, screen, width = 0, height = 0):
        """初始化飞机并设置初始位置"""
        super().__init__()
        self.screen = screen
        self._settings = _settings
        # 加载飞船外形并获取其外接矩形
        self.image = pygame.image.load('imgs/ship.bmp')
        if width == 0 and height == 0 :
           self.image = pygame.transform.scale(self.image,
                                               (_settings.ship_width, _settings.ship_height))
        else:
            self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将飞机置于屏幕底部中央
        self.center = float(self.screen_rect.centerx)
        self.rect.centerx = self.center
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞机的位置"""
        # 判断是否移动到屏幕之外
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self._settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self._settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞机"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
