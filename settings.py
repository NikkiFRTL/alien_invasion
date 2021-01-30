
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
        self.ship_limit = 3

        # Настройки выстрелов
        self.bullet_speed = 1
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (220, 20, 60)
        self.bullets_allowed = 3
        
        # Настройки пришельцев
        self.alien_speed = 0.5
        self.fleet_drop_speed = 20
        # fleet_direction = 1 означает движение враво, -1 влево
        self.fleet_direction = 1
