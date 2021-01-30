class GameStats:
    """
    Отслеживание статистики в Alien Invasion
    """
    def __init__(self, ai):
        """
        Инициализирует статистику
        """
        self.settings = ai.settings
        self.reset_stats()
        
        # Активное состояние игры (делается, чтобы завершить игру при ships_left = 0)
        self.game_active = False

    def reset_stats(self):
        """
        Инициализирует статистику, изменяющуюся в ходе игры
        """
        self.ships_left = self.settings.ship_limit
