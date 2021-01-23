import pygame


class Ship:
    """
    Создание класа корабль содержащий его поведение
    """

    def __init__(self, ai):
        # Инициалицируем корабль и задаем его начальную позицию
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется в центре у нижней границы экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):

        # Рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)
