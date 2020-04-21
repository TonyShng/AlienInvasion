import sys
import pygame
from alien_settings import alien_settings
from Ship import Ship
from Alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    pygame.display.set_caption("Alien Invasion")

    # 游戏设置对象
    ai_settings = alien_settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # 创建一个显示窗口

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船
    ship = Ship(ai_settings ,screen)

    # 创建一个外星人
    alien = Alien(ai_settings, screen)

    # 设置背景色
    # bg_color = (230, 230, 230)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        # 重构后的代码
        # gf.check_event(ship)
        gf.check_event(ai_settings, screen, ship, bullets)

        bullets.update()

        if stats.game_active:
            # 获取触控事件后 对飞船位置进行刷新
            ship.update()

            # 删除已消失的子弹
            # for bullet in bullets.copy():
            #     if bullet.rect.bottom <= 0:
            #         bullet.remove(bullet)
            # print(len(bullets))

            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

            ## 更新外星人的位置
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)


        # # 每次循环时都重绘屏幕
        # screen.fill(ai_settings.bg_color)
        # # 将飞船绘制到屏幕上
        # ship.blitme()
        # # 让最近绘制的屏幕可见
        # pygame.display.flip()



        #重构后的代码
        # gf.update_screen(ai_settings, screen, ship)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)



run_game()
































