"""Игра крестики-нолики"""

class Game:
    "Docstring"
    def __init__(self):
        self.x_values = "abcdefdh"
        self.y_values = "12345678"

    def some_func(self):
        "Docstring"

    def some_func_2(self):
        "Docstring"

class NewGame(Game):
    "Docstring"
    def __init__(self, size):
        super().__init__()
        self.__side = 0
        self.__size = size
        self.__counter = 0
        # self.__field = [[-1] * self.__size] * self.__size
        self.__field = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

    def change_side(self):
        "Docstring"
        self.__side = (self.__side + 1) % 2

    def render(self):
        "Docstring"
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
        "Docstring"
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
                continue

            x_move = input_str[0]
            y_move = input_str[1]
            break

        try:
            y_val = self.x_values.index(x_move)
            x_val = self.y_values.index(y_move)
        except ValueError:
            print("Повторите еще раз ваш ход\n")
            return

        try:
            if self.__field[y_val][x_val] >= 0:
                raise IndexError
            self.__field[y_val][x_val] = side_val
        except IndexError:
            print("Повторите еще раз ваш ход\n")
            return

        print(f"\nВаш ход: x = {x_val + 1}, y = {y_val + 1}")
        self.__counter += 1
        return

    def move_test(self, x_val, y_val):
        "Docstring"
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
            print("Повторите еще раз ваш ход\n")
            return

        print(f"\nВаш ход: x = {x_val + 1}, y = {y_val + 1}")
        self.__counter += 1
        return

    def check_win(self):
        "Docstring"
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
    gg = NewGame(3)
    gg.render()

    while True:
        mov = gg.move()
        if mov == -1:
            break
        if mov == 0:
            print("Ничья")
            break
        gg.render()
        if gg.check_win() is True:
            print(f"\nПобеда игрока: {gg._NewGame__side}!")
            break
        gg.change_side()
