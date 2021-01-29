class GameStats():
    """统计游戏信息"""
    def __init__(self, _settings):
        """初始化统计信息"""
        self._settings = _settings
        # 游戏最开始处于暂停状态 点击按钮之后开始游戏
        self.game_active = False
        # 最高分
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的信息"""
        self.ship_left = self._settings.ship_limit
        self.score = 0
        self.level = 1