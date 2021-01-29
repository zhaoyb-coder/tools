import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    _setting = Settings()
    screen = pygame.display.set_mode((_setting.screen_width, _setting.screen_height))
    pygame.display.set_caption("飞机大战")
    # 创建按钮
    play_button = Button(_setting, screen, "Play")
    # 创建一个统计信息
    stats = GameStats(_setting)
    # 创建飞机
    ship = Ship(_setting, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人群组
    aliens = Group()
    gf.create_fleet(_setting, screen, ship, aliens)
    # 创建记分牌
    score = Scoreboard(_setting, screen, stats)
    # 开始游戏的主循环
    while True:
        # 监控键盘和鼠标事件
        gf.check_events(_setting, screen, ship, bullets, stats, play_button, aliens, score)
        if stats.game_active:
            # 飞机持续移动
            ship.update()
            # 更新子弹
            gf.update_bullets(_setting, screen, ship, aliens, bullets, stats, score)
            # 更新外星人位置
            gf.update_aliens(_setting, stats, ship, aliens, screen, bullets, score)
        # 屏幕图像更新
        gf.update_screen(_setting, screen, aliens, ship, bullets, play_button, stats, score)


run_game()
