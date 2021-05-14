1

from sys import argv


def calculation():
    try:
        time, salary, bonus = map(float, argv[1:])
        print(f"Your calculation is equal {time, salary, bonus}")
    except ValueError:
        print("Enter just 3 numbers!")

calculation()



2

my_list = [76, 90, 5, 17, 300, 15, 3, 2, 18]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')

3

print(f'Числа от 20 до 240 кратный 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')


4

my_list = [3, 5, 5, 5, 9, 7, 2, 1, 9, 15, 31]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_new_list)


5


from functools import reduce

def my_f(el_p, el):
    return el_p * el


print(f'Список четных знвчений {[el for el in range(99, 101) if el % 2 == 0]}')
print(f'Результат умножения всех элементов списка {reduce(my_f, [el for el in range(99, 101) if el % 2 == 0])}')


6


from itertools import count

iterator = count(int(input('Enter a start number: ')))
print('First 10 numbers')
for i in range(10):
    print(next(iterator), end=' ')


from itertools import cycle

my_list = ['sting', 87, 346, 91, 67.98]
iterator = cycle(my_list)
for i in range(len(my_list) * 5):
    print(next(iterator), end=' ')


