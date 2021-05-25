1

class Data:
    def __init__(self, day_month_year):
        # self.day = day
        # self.month = month
        # self.year = year
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неверный год!'
            else:
                return f'Неверный месяц!'
        else:
            return f'Неверный день!'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('12 - 2 - 2002')
print(today)
print(Data.valid(12, 12, 2022))
print(today.valid(12, 14, 2007))
print(Data.extract('12 - 12 - 2012'))
print(today.extract('12 - 12 - 2020'))
print(Data.valid(2, 12, 2002))


2


class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль невозможно!")


div = DivisionByNull(50, 500)
print(DivisionByNull.divide_by_null(50, 0))
print(DivisionByNull.divide_by_null(50, 0.2))
print(div.divide_by_null(500, 0))


3


class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        # self.my_list = [int(i) for i in input('Введите значение через пробел ').split()]
        # val = int(input('Введите значение и нажмите Enter - '))
        # self.my_list.append(val)
        while True:
            try:
                val = int(input('Введите значение и нажмите Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                z_or_t = input('Попробовать еще? Z/T')

                if z_or_t == 'Z' or z_or_t == 'z':
                    print(try_except.my_input())
                elif z_or_t == 'T' or z_or_t == 't':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Error(1)
print(try_except.my_input())


6


class StoreMashines:
    def __init__(self, name, price, quantity, num_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = num_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за одну единицу': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} модель, {self.price} цена, {self.quantity} количество'

    # @classmethod
    # @staticmethod
    def reception(self):
        # print(f'Для выхода - Q, для продолжения - Enter')
        # while True:
        try:
            unit = input(f'Введите наименование: ')
            unit_p = int(input(f'Введите цену за одну единицу: '))
            unit_q = int(input(f'Введите количество: '))
            unique = {'Модель устройства': unit, 'Цена за одну единицу': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущис список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных!'

        print(f'Для выхода - Q, для продолжения - Enter')
        q = input(f'---> ')
        if q =='Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth {self.numb} times'


unit_1 = Printer('hp', 1500, 6, 12)
unit_2 = Scanner('Canon', 1000, 6, 12)
unit_3 = Copier('Xerox', 1100, 2, 20)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())


7


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма c1 и c2 равна: ')
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение c1  и c2 равно: ')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'с = {self.a} + {self.b} * i'


c_1 = ComplexNumber(2, -3)
c_2 = ComplexNumber(5, 7)
print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)






