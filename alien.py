import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    Класс, представляющий одного пришельца
    """
    def __init__(self, ai):
        """
        Инициализация пришельца и назначение начальной позиции
        """
        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings

        # Загрузка изображения и назначение атрубута rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Ширина и высота пришельца. Нужно для выставления интервала таких размеров между пришельцами.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельцев т.к. нам интересно точное горизонатльное перемещение.
        self.x = float(self.rect.x)

        # Классу Alien не нужен метод для вывода на экран:
        # self.screen_rect = ai.screen.get_rect()
        # def blit()
        # вместо него воспользуемся методом групп Pygame, который автоматически рисует все элементы группы на экране:
        # self.aliens.draw(self.screen) внутри метода _update_screen()

        # Также не нужно указывать расположение первого пришельца, т.к. по умолчанию это левый верхний угол,
        # что нам подходит.

    def check_edges(self):
        """
        Возвращает True, если пришелец находится у края экрана
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right > screen_rect.right or self.rect.left < 0:
            return True

    def update(self):
        """
        Перемещает пришельца вправо или влево
        """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
