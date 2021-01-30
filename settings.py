
class Settings:
    """
    Создание класса со всеми настройнками игры Alien Invasion
    """
    def __init__(self):
        """
        Статические настройки игры
        """
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (230, 230, 230)

        # Настройки корабля
        self.ship_limit = 3

        # Настройки выстрелов
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (220, 20, 60)
        self.bullets_allowed = 7
        
        # Настройки пришельцев
        self.fleet_drop_speed = 5

        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Динамические настройки игры
        """
        self.ship_speed = 1.25
        self.bullet_speed = 1
        self.alien_speed = 0.5
        # fleet_direction = 1 означает движение враво, -1 влево
        self.fleet_direction = 1

    def increase_speed(self):
        """
        Увеличивает настройки скорости игры
        """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale