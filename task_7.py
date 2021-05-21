1


class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        mat = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                mat[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mat]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in mat]))


my_matrix = Matrix([[6, 26, 32],
                    [11, 21, 9],
                    [45, 60, 12]],
                   [[34, 3, 7],
                    [2, 4, 17],
                    [22, 9, 11]])
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print(my_matrix.__add__())


2


class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь для пальто {self.square_c}'


class Jacket(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь для костюма {self.square_j}'


coat = Coat(3, 5)
jacket = Jacket(1, 3)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(coat.get_square_c())
print(jacket.get_square_j())


3


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity
        # self.result = result

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        # self.result = Cell(self.quantity + other.quantity)
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        '''
        Выдает ошибку о том, что результат не число при вычислении
        if int(Cell(self.quantity - other.quantity)) > 0:
            return Cell(int(self.quantity - other.quantity))
        else:
            return f'Операция вычитания невозможна!'""
        '''
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

        # return Cell(int(self.quantity - other.quantity))

    def __mul__(self, other):
        # self.result = Cell(int(self.quantity * other.quantity))
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        # self.result = Cell(int(self.quantity // other.quantity))
        return Cell(int(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(17)
cells2 = Cell(8)
print(cells1)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells2.make_order(4))
print(cells1.make_order(11))
print(cells1 / cells2)


