import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


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

        # Создание экземпляра для хранения игровой статистики
        self.stats = GameStats(self)

        # Создание экземпляра корабля
        self.ship = Ship(self)

        # Группа для хранения всех летящих снарядов
        self.bullets = pygame.sprite.Group()

        # Группа для хранения всех пришельцев
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Создание кнопки Play
        self.play_button = Button(self, 'Play')

    def run_game(self):
        """
        Запуск основного цикла игры
        """
        while True:
            self._check_events()

            # Отделим части игры, которые должны выподлняться только при активной игре (game_active = True)
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """
        Запускает новую игру при нажатии кнопки Play
        """
        # Проверяет находится ли точка щелчка в пределах прямоугольника Play
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True

    def _check_keydown_events(self, event):
        """
        Реагирует на нажатие клавиш.
        """
        # Действия при нажатии клавиш перемещения -> <-
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        # Добпавление действия при нажатии кнопки пробела
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
        # Сначала проверим, что количество уже летящих на экране снарядов не болшье разрешенного значения (3)
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """
        Обновляет позиции срарядов и удаляет старые снаряды
        """
        # Вызываем bullet.update() для каждого снаряда в группе self.bullets
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана. Иначе они существуют за его пределами и потребляют память
        # Сам список bullets в цикле изменять нельзя, пожтому изменять будет его копию .copy()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """
        Обработка коллизий снарядов с пришельцами
        """
        # Проверка попадений в пришельцев (коллизий) с помощью sprite.groupcollide()
        # True, True обозначает, что нужно удалять каждый объект после столкновения
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)

        # Удаление существующих снарядов после поражения последнего пришельца и создание нового флота
        # Метод empty() удаляет все спрайты(объекты группы) из группы
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """
        Создание флота вторжения
        """
        # Создание пришельца и вычисление допустимого количества пришельцев в ряду
        # Интервал между пришельцами равен ширине пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height

        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        available_space_y = self.settings.screen_height - (2 * alien_height) - ship_height * 4
        number_rows = available_space_y // (2 * alien_height)

        # Создание первого ряда пришельцев
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x - 1):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """
        Создание пришельца и размещение его в ряду, добавление его в группу Sprite
        """
        alien = Alien(self)
        # Атрибут size содержит коржтеж из значений ширины и высоты rect
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """
        Реагирует на достижение пришельцем края экрана
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """
        Опускает весь флот и меняет его направление движения
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """
        Проверяет достиг ли флот края экрана и обновляет позиции всех пришельцев во флоте
        """
        self._check_fleet_edges()
        # Вызываем aliens.update() для каждого снаряда в группе self.aliens
        self.aliens.update()

        # Проверка коллизий корабль - пришелец
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Проверяет добрались ли пришельцы до нижнего края экрана
        self._check_aliens_bottom()

    def _ship_hit(self):
        """
        Обрабатывает столкнокение корабля с пришельцем
        """
        if self.stats.ships_left > 0:
            # Уменьшение количества жизней на 1
            self.stats.ships_left -= 1

            # Очистка кораблей и снарядов
            self.bullets.empty()
            self.aliens.empty()

            # Создание нового флота и размещение корабля в центре
            self._create_fleet()
            self.ship.center_ship()

            # Пауза
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """
        Проверяет добрались ли пришельцы до нижнего края экрана
        """
        if self.stats.ships_left > 0:
            screen_rect = self.screen.get_rect()
            for alien in self.aliens.sprites():
                if alien.rect.bottom >= screen_rect.bottom:
                    # Происхоит тоже, что при столкновении с кораблем
                    self._ship_hit()
                    break
        else:
            self.stats.game_active = False

    def _update_screen(self):
        # Заполенение экрана нужным цветом
        self.screen.fill(self.settings.background_color)

        # Выводит изображение корабля на экран в позиции, заданной self.rect
        self.ship.blitme()

        # Перебор всех bullet в спрайте(группы) bullets и прорисовка каждой
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Специальный метод pygame для вывода всей группы на поверхность(получаемый аргумент)
        self.aliens.draw(self.screen)

        # Кнопка Play отображается только когда игра не активна
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
