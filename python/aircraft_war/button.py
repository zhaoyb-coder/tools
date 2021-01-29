import pygame.font


class Button():
    def __init__(self, _settings, screen, msg):
        """初始化按钮属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 设置按钮尺寸和其他属性
        self.width, self.height = 200, 50
        self.btn_color = (0, 255, 0)
        self.text_color = (255, 255,255)
        self.font = pygame.font.SysFont(None, 48)
        # 创建rect对象，并居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # 渲染按钮
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """将msg渲染为图像，并使按钮居中"""
        self.msg_img = self.font.render(msg, True, self.text_color, self.btn_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_btn(self):
        """绘制按钮"""
        self.screen.fill(self.btn_color, self.rect)
        self.screen.blit(self.msg_img,self.msg_img_rect)