class Game:
    def __init__(self):
        self.x_values = "abcdefdh"
        self.y_values = "12345678"
        pass

class NewGame(Game):
    def __init__(self, size):
        super().__init__()
        self.__side = 0
        self.__size = size
        self.__counter = 0
        # self.__field = [[-1] * self.__size] * self.__size
        self.__field = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

    def change_side(self):
        self.__side = (self.__side + 1) % 2

    def render(self):
        for y in range(self.__size):
            print(self.y_values[:self.__size][y], end=' ')
            for x in range(self.__size):
                print('O' if self.__field[y][x] == 0 else 'X' if self.__field[y][x] == 1 else '_', end=' ')
            print()
        print(' ', end=' ')
        for i in range(self.__size):
            print(self.x_values[i], end=' ')
        print()

    def move(self):
        move_x = None
        move_y = None

        if self.__counter == self.__size ** 2:
            return 0
        side_val = self.__side
        side_str = "O" if self.__side == 0 else "X" if self.__side == 1 else ValueError
        print(f"\nХод игрока: {self.__side} ({side_str})")
        while(True):
            str = input()
            try:
                if str[0] == "q" or str[0] == "e":
                    return -1
            except IndexError:
                continue
            if len(str) != 2:
                continue
            else:
                move_x = str[0]
                move_y = str[1]
                break

        try:
            x = self.x_values.index(move_x)
            y = self.y_values.index(move_y)
        except ValueError:
            print("Повторите еще раз ваш ход\n")
            return

        try:
            if self.__field[y][x] >= 0:
                raise IndexError
            self.__field[y][x] = side_val
        except IndexError:
            print("Повторите еще раз ваш ход\n")
            return

        print(f"\nВаш ход: x = {x + 1}, y = {y + 1}")
        self.__counter += 1
        return

    def move_test(self, x, y):
        if self.__counter == self.__size ** 2:
            return 0
        side_val = self.__side
        side_str = "O" if self.__side == 0 else "X" if self.__side == 1 else ValueError
        print(f"\nХод игрока: {self.__side} ({side_str})")

        try:
            if self.__field[y][x] >= 0:
                raise IndexError
            self.__field[y][x] = side_val
        except IndexError:
            print("Повторите еще раз ваш ход\n")
            return

        print(f"\nВаш ход: x = {x + 1}, y = {y + 1}")
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
    gg = NewGame(3)
    gg.render()

    while(True):
        mov = gg.move()
        if mov == -1:
            break
        if mov == 0:
            print("Ничья")
            break
        gg.render()
        if gg.check_win() == True:
            print(f"\nПобеда игрока: {gg._NewGame__side}!")
            break
        gg.change_side()