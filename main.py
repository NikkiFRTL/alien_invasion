import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """
    Класс для управления ресурсами и поведением игры
    """
    def __init__(self):
        # Инициальзация pygame
        pygame.init()

        # Создание объекта класса Настройки, чтобы подтягивать их или изменения из отдельного файла а не в самом коде
        self.settings = Settings()

        # Назначение размера окна и имени
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        # Создание экземпляра корабля
        self.ship = Ship(self)

        # Группа для хранения всех летящих снарядов
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """
        Запуск основного цикла игры
        """
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()  # Вызывает bullet.update() для каждого снаряда в группе self.bullets
            self._update_screen()

    def _check_events(self):
        """
        Обрабатывает нажатия клавиш и события мыши
        """
        # Отслеживание дествий клвариатуры и мыши (итерация по всем значениям в списке действий в pygame.event.get)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Блок отвечающий за действие при нажатии клавиши (начать движение корабля)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Блок отвечающий за действие при отжатии клавиши (прекратить движение корабля)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """
        Реагирует на нажатие клавиш.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def _check_keyup_events(self, event):
        """
        Реагирует на отпускание клавиш.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def fire_bullet(self):
        """
        Создание нового снаряда и включение его в группу bullets
        """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        # Заполенение экрана нужным цветом
        self.screen.fill(self.settings.background_color)

        # Выводит изображение корабля на экран в позиции, заданной self.rect
        self.ship.blitme()

        # TODO
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
