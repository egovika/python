1

def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Division by zero forbidden! "
    except ValueError:
        return "Value Error "


print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))


2

def personal_information(name, surname, birthday, city, email, phone):
    return f"Name - {name}; Surname - {surname}; Birthday - {birthday}; City - {city}; Email - {email}; Phone - {phone}"


print(personal_information(name='Viktoria', surname='Krainiukova', birthday='1995', city='Odessa', email='mail@mail.ru', phone='3-941-4837'))


3


def my_func(arg1, arg2, arg3):
    return sum(sorted([arg1, arg2, arg3])[1:])


print(my_func(89, 7, -3))


4


def my_func(x, y,):
    try:
        res = x ** y
    except TypeError:
        return "Enter a float and negative number: "
    return res

print(my_func(6.9, -3))


5

def sum_num():
    s = 0
    while True:
        in_list = input("Enter a number, input q for exit: ").split()
        for num in in_list:
            if num == "q":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("For exit print - 'q'")
        print(f"Sum of numbers = {s}")

print(sum_num())
