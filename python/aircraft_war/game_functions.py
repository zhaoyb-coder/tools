import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(_settings, screen, ship, bullets, stats, play_button, aliens, score):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydowm_events(event, _settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_btn(_settings, stats, play_button, mouse_x, mouse_y, aliens, bullets, screen, ship, score)


def check_keydowm_events(event, _settings, screen, ship, bullets):
    """键盘按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(_settings, bullets, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """键盘松开事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_btn(_setting, stats, play_button, mouse_x, mouse_y, aliens, bullets, screen, ship, score):
    """单击Play按钮时开始游戏"""
    btn_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if btn_clicked and not stats.game_active:
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏节奏
        _setting.initialize_dynamic_settings()
        # 重置游戏信息
        stats.reset_stats()
        stats.game_active = True
        # 重新绘制分数
        score.prep_score()
        score.prep_high_score()
        score.prep_level()
        score.prep_ships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建新的外星人，并让飞船居中
        create_fleet(_setting, screen, ship, aliens)
        ship.center_ship()


def update_screen(_setting, screen, aliens, ship, bullets, play_button, stats, score):
    """更新屏幕图像，并切换到新图像"""
    # 设置背景色
    screen.fill(_setting.bg_color)
    # 显示分数
    score.show_score()
    if not stats.game_active:
        play_button.draw_btn()
    # 在飞船和敌方后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_buller()
    # # 初始化飞船
    ship.blitme()
    # # 初始化外星人
    aliens.draw(screen)
    # 屏幕可见
    pygame.display.flip()


def update_bullets(_settings, screen, ship, aliens, bullets, stats, score):
    # 子弹位置更新
    bullets.update()
    # 检查是否有子弹击中了外星人，如果有，则删除子弹和外星人
    check_bullet_alien_collisions(_settings, screen, ship, bullets, aliens, stats, score)
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def check_bullet_alien_collisions(_settings, screen, ship, bullets, aliens, stats, score):
    """响应子弹与外星人的碰撞"""
    # 删除发生碰撞的外星人和子弹
    # 要模拟能够穿行到屏幕顶端的高能子弹——消灭它击中的每个外星人，
    # 可将第一个布尔实参设置为False，并让第二个布尔实参为True。
    # 这样被击中的外星人将消失，但所有的子弹都始终有效，直到抵达屏幕顶端后消失
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 击中外星人，增加分数
    if collisions:
        for aliens in collisions.values():
            stats.score += _settings.alien_points * len(aliens)
            score.prep_score()
        check_high_score(stats, score)
    if len(aliens) == 0:
        # 外星人已经被全部消灭，删除现有的子弹并新增外星人
        bullets.empty()
        # 加快游戏节奏
        _settings.increase_speed()
        # 提高等级
        stats.level += 1
        score.prep_level()
        create_fleet(_settings, screen, ship, aliens)


def check_fleet_edges(_settings, aliens):
    """当有外星人到达边缘时采取的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(_settings, aliens)
            break


def change_fleet_direction(_settings, aliens):
    """将整群外星人整体下移，并改变方向"""
    for alien in aliens.sprites():
        alien.rect.y +=  _settings.fleet_drop_speed
    _settings.fleet_direction *= -1


def update_aliens(_settings, stats, ship, aliens, screen, bullets, score):
    """更新外星人群中所有外星人位置"""
    # 检查是否有外星人到达底部
    check_aliens_bottom(_settings, stats, screen, ship, aliens, bullets, score)
    check_fleet_edges(_settings, aliens)
    aliens.update()
    # 检测外星人和飞机的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(_settings, stats, screen, ship, aliens, bullets, score)


def fire_bullet(_settings, bullets, screen, ship):
    """如果子弹没有达到上限就发射一颗子弹"""
    # 创建一个子弹，并将其加入编组
    if len(bullets) < _settings.bullet_allowed:
        new_bullet = Bullet(_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(_settings, alien_width):
    """计算可容纳多少个外星人"""
    # 计算可用于放置外星人的水平空间
    available_space_x = _settings.screen_width - 2 * alien_width
    # 可容纳多少个外星人
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并加入当前行"""
    alien = Alien(_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(_settings, ship_height, alien_height):
    """计算屏幕能容纳多少行外星人"""
    available_space_y = (_settings.screen_height -
                         3 * alien_height - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_fleet(_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少外星人，
    # 外星人间距为外星人宽度
    alien = Alien(_settings, screen)
    number_aliens_x = get_number_aliens_x(_settings, alien.rect.width)
    number_rows = get_number_rows(_settings, ship.rect.height, alien.rect.height)
    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(_settings, screen, aliens, alien_number, row_number)


def ship_hit(_settings, stats, screen, ship, aliens, bullets, score):
    """响应被外星人碰到的飞船"""
    if stats.ship_left > 0:
        # 将ship_limit 减少 1
        stats.ship_left -= 1
        # 更新记分牌->飞机减少1
        score.prep_ships()
        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建新的外星人并把飞船放到屏幕底部中央
        create_fleet(_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        # 展示光标
        pygame.mouse.set_visible(True)


def check_aliens_bottom(_settings, stats, screen, ship, aliens, bullets, score):
    """检查是否有外星人到达屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(_settings, stats, screen, ship, aliens, bullets, score)
            break


def check_high_score(stats, score):
    """检查是否诞生了最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.prep_high_score()
