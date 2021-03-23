"""Игра крестики-нолики"""

class Game:
    def __init__(self):
        self.x_values = "abcdefdh"
        self.y_values = "12345678"


class NewGame(Game):
    def __init__(self, size):
        super().__init__()
        self.__side = 0
        self.__size = size
        self.__counter = 0
        self.__field = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

    def change_side(self):
        self.__side = (self.__side + 1) % 2

    def render(self):
        for y_val in range(self.__size):
            print(self.y_values[:self.__size][y_val], end=' ')
            for x_val in range(self.__size):
                print('O' if self.__field[y_val][x_val] == 0 else 'X' if self.__field[y_val][x_val] == 1 else '_', end=' ')
            print()
        print(' ', end=' ')
        for i in range(self.__size):
            print(self.x_values[i], end=' ')
        print()

    def move(self):
        x_move = None
        y_move = None

        if self.__counter == self.__size ** 2:
            return 0
        side_val = self.__side
        side_str = "O" if self.__side == 0 else "X" if self.__side == 1 else ValueError
        print(f"\nХод игрока: {self.__side} ({side_str})")
        while True:
            input_str = input()
            try:
                if input_str[0] == "q" or input_str[0] == "e":
                    return -1
            except IndexError:
                continue
            if len(input_str) != 2:
                print("Повторите еще раз ваш ход. Длина ввода должна содержать 2 символа. \n")
                continue

            x_move = input_str[0]
            y_move = input_str[1]
            break

        try:
            x_val = self.x_values.index(x_move)
            y_val = self.y_values.index(y_move)
            print(x_move, y_move)
            print(x_val, y_val)
        except ValueError:
            print("Повторите еще раз ваш ход. Введенное значение превышает размер поля для игры. \n")
            return -1

        try:
            if self.__field[y_val][x_val] >= 0:
                raise IndexError
            self.__field[y_val][x_val] = side_val
        except IndexError:
            print("\nПовторите еще раз ваш ход. Клетка уже занята.")
            return -1

        print(f"\nВаш ход: x = {x_val + 1}, y = {y_val + 1}")
        self.__counter += 1
        return

    def move_test(self, x_val, y_val):
        if self.__counter == self.__size ** 2:
            return 0
        side_val = self.__side
        side_str = "O" if self.__side == 0 else "X" if self.__side == 1 else ValueError
        print(f"\nХод игрока: {self.__side} ({side_str})")

        try:
            if self.__field[y_val][x_val] >= 0:
                raise IndexError
            self.__field[y_val][x_val] = side_val
        except IndexError:
            raise

        print(f"\nВаш ход: x = {y_val + 1}, y = {x_val + 1}")
        self.__counter += 1
        return

    def check_win(self):
        line_ex = [self.__side] * 3

        for i in self.__field:
            if i == line_ex:
                return True

        for i in range(self.__size):
            if [self.__field[0][i],
                self.__field[1][i],
                self.__field[2][i]] == line_ex:
                return True

        if [self.__field[0][0],
            self.__field[1][1],
            self.__field[2][2]] == line_ex:
            return True

        if [self.__field[2][0],
            self.__field[1][1],
            self.__field[0][2]] == line_ex:
            return True

        return False


if __name__ == '__main__':
    game = NewGame(3)
    print("\nПравила игры: игроки последовательно ходят на поле размерами 3x3.")
    print("Каждый ход должен состоять из двух символов, например 'a1', 'c3'.\n")
    game.render()

    while True:
        mov = game.move()
        if mov == -1:
            game.render()
            continue
        if mov == 0:
            print("Ничья")
            break
        game.render()
        if game.check_win() is True:
            print(f"\nПобеда игрока: {game._NewGame__side}!")
            break
        game.change_side()
