import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """
    Создание класа корабль содержащий его поведение
    """

    def __init__(self, ai):
        super().__init__()
        # Инициалицируем корабль и задаем его начальную позицию
        self.screen = ai.screen
        # Создается, чтобы его можно было использовать в update()
        self.settings = ai.settings

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Обращение к атрибуту rect отбъекта экрана с помощью метода get_rect() и присваивает его self.screen_rect
        # Это позволяет разместить корабль в нужной позиции экрана
        self.screen_rect = ai.screen.get_rect()

        # Каждый новый корабль появляется в центре у нижней границы экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля (дробные значения как 1.5) для более точного перемещения
        self.x = float(self.rect.x)

        # Флаг перемещения (для непрерывного перемещения корабля при нажатии клавиши)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Перемещает корабль, если клавиша <- / -> нажата
        """
        # Обновляет атрубиут self.x, не self.rect
        # self.rect.right возвращает координату х правого края прямоугольника корабля
        # self.rect.screen_right возвращает координату х правого угла экрана
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # 0 - координата левого угла экрана
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x (будет сохр. только целая часть, но этого достаточно)
        # для определения позиции корабля
        self.rect.x = self.x

    def blitme(self):
        """
        Вывод картинки bmp на экран
        """
        # Рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """
        Размещает корабль в центре нижней стороны экрана
        """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
