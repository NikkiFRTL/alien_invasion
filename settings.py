
class Settings:
    """
    Создание класса со всеми настройнками игры Alien Invasion
    """
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed = 1.25

        # Настройки выстрелов
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (220, 20, 60)
        self.bullets_allowed = 3
