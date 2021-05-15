1

my_f = open('text.101', 'w')
line = input('Введите текс \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = open('text.101', 'r')
content = my_f.readlines()
my_f.close()


2

my_file = open('text.102', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('text.102', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('text.102', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} в строке {len(content[i])} ')
my_file = open('text.102', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

3

with open('text.103', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
            sal.append(i[1])
print(f'Оклад меньше 20 000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')


4

rus = {'One': 'Один','Two': 'Два', 'Three': 'Три', 'Four': 'Четире'}
new_file = []
with open('text.104', 'r') as file_otd:
    # content = file_otd.read().split('\n')
    for i in file_otd:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
    print(new_file)
with open('text.104', 'w') as file_otd_2:
    file_otd_2.writelines(new_file)


5

def summary():
    try:
        with open('text.105', 'w+') as file_dot:
            line = input('Введите цифры через пробел \n')
            file_dot.writelines(line)
            my_num = line.split()

            print(sum(map(int, my_num)))
    except IOError:
        print('Ошибка')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода!')
summary()

6


# import json

subj = {}
with open('text.106', 'r') as input_x:
    for line in input_x:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')


7

