import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    Класс для управления ресурсами и поведением игры
    """
    def __init__(self):
        # Инициальзация pygame
        pygame.init()

        # Создание объекта класса Настройки, чтобы подтягивать их или изменения из отдельного файла а не в самом коде
        self.settings = Settings()

        # Назначение размера окна
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        # Создание экземпляра корабля
        self.ship = Ship(self)


    def run_game(self):
        """
        Запуск основного цикла игры
        """
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """
        Обрабатывает нажатия клавиш и события мыши
        """
        # Отслеживание дествий клвариатуры и мыши (итерация по всем значениям в списке действий в pygame.event.get)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #  Переместить корабль вправо
                    self.ship.rect.x += 1


    def _update_screen(self):
        # Заполенение экрана нужным цветом
        self.screen.fill(self.settings.background_color)

        # Выводит изображение корабля на экран в позиции, заданной self.rect
        self.ship.blitme()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
