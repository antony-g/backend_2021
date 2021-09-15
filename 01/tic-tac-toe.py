"""Игра крестики-нолики"""


class Game:
    """Parent class, e.g. for chess of some other game"""

    def __init__(self):
        """Base class constructor method"""
        self.x_values = "abcdefghi"
        self.y_values = "1234567890"

    def some_method_1(self):
        """Some method for pylint check"""

    def some_method_2(self):
        """Some method for pylint check"""


class DuplicateError(BaseException):  # Отд. файл
    """Custom exception case"""


class NewGame(Game):
    """New XO game"""
    def __init__(self, size):
        """Constructor method"""
        super().__init__()
        self.__side = 0
        self.__size = size
        self.__counter = 0
        self.__field = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        # Не исп. приватные методы

    def change_side(self):
        """Changing side"""
        self.__side = (self.__side + 1) % 2

    def show_board(self):
        """Rendering the board"""
        for y_val in range(self.__size):
            print(self.y_values[:self.__size][y_val], end=' ')
            for x_val in range(self.__size):
                print('O' if self.__field[y_val][x_val] == 0 else
                      'X' if self.__field[y_val][x_val] == 1 else '_', end=' ')
            print()
        print(' ', end=' ')
        for i in range(self.__size):
            print(self.x_values[i], end=' ')
        print()

    def validate_input(self, input_str=None):
        """Validate of the input string"""
        if self.__counter == self.__size ** 2:
            return # Raise / True / False
        side_str = "X" if self.__side == 1 else "O" if self.__side == 0 else ValueError
        while True:
            print(f"\nХод игрока {self.__side} ({side_str}):")
            input_str = input() if input_str is None else input_str
            if input_str[0:2] == "qu" or input_str[0:2] == "ex":
                return
            if len(input_str) != 2:
                print("Повторите еще раз ваш ход. Длина ввода должна содержать 2 символа.\na1")
                input_str = None
                game.show_board()
                continue
            try:
                x_val = self.x_values.index(input_str[0])
                y_val = self.y_values.index(input_str[1])
                return x_val, y_val
            except ValueError:
                return -1, -1  # try isdigit(input_st) except ValueError / try: ... except IndexError
            # Не возвр. кортеж, возвр. True/False

    def move(self, x_val, y_val):
        """Making move based on the input values"""
        # print(f"Ваш ход: x = {x_val + 1}, y = {y_val + 1}")
        if x_val == -1 and y_val == -1:
            print("Повторите еще раз ваш ход. Введенное значение превышает размер поля для игры.\n")
            return -1  #return IndexError("some_text"), except MyCustomValidation
        side_val = self.__side
        try:
            if self.__field[y_val][x_val] >= 0:
                raise DuplicateError
        except IndexError:
            print("Повторите еще раз ваш ход. Введенное значение превышает размер поля для игры.\n")
            return -1  # except MyCustomValidation2 # False
        except DuplicateError:
            print("Повторите еще раз ваш ход. Клетка уже занята.\n")
            return -1  # except MyCustomValidation3 # False
        if (x_val > 2) or (y_val > 2) or (y_val < 0):
            return -1  # except MyCustomValidation4 # False
        print()
        self.__field[y_val][x_val] = side_val
        self.__counter += 1
        self.change_side()
        return 0 # True

    def check_win(self):
        """Check of each winner lines"""
        line_win = [(self.__side + 1) % 2] * 3
        # print(f"{self.__side}!!!")

        for i in self.__field:
            if i == line_win:
                return True

        for i in range(self.__size):
            if [self.__field[0][i],
                self.__field[1][i],
                self.__field[2][i]] == line_win:
                return True

        if [self.__field[0][0],
            self.__field[1][1],
            self.__field[2][2]] == line_win:
            return True

        if [self.__field[2][0],
            self.__field[1][1],
            self.__field[0][2]] == line_win:
            return True

        return False


if __name__ == '__main__':
    game = NewGame(3)
    print("\nПравила игры: игроки последовательно ходят на поле размерами 3x3\n\
Каждый ход должен состоять из двух символов, например 'a1', 'c3'.\n")
    game.show_board()

    while True:
        try:
            x, y = game.validate_input() # check_draw, True / False
        except TypeError:
            print("Ничья!")
            break
        MOVE = game.move(x, y)
        if MOVE == -1:
            game.show_board()
            continue
        game.show_board()
        if game.check_win() is True:
            print(f"\nПобеда игрока: {abs(game._NewGame__side - 1)}!")
            break
