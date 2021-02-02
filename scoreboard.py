import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """
    Класс для вывода игровой информации
    """
    def __init__(self, ai):
        """
        Атрибуты подсчета очков
        """
        self.ai = ai
        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai.settings
        self.stats = ai.stats

        # Настройка шрифта для вывода счета
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Подготовка исходного изображения очков и рекордов очков
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

        # Сообщает количество оставшихся кораблей(жизней)
        self.prep_ships()

    def prep_score(self):
        """
        Преобразует текущий счет в гарфическое изображение
        """
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.background_color)

        # Вывод счета справа сверху
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """
        Преобразует рекордный счет в гарфическое изображение
        """
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.background_color)

        # Вывод рекорда слева сверху
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """
        Преобразует номер уровня в гарфическое изображение
        """
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.background_color)

        # Вывод рекорда слева сверху
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 10
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """
        Выводит счет, рекорд, уровень и жизни корабля
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """
        Проверяет появился ли новый рекорд
        """
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_ships(self):
        """
        Сообщает количество оставшихся кораблей(жизней)
        """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
