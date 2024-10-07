# try:
#     i = 0
#     print(10 / i)
#     print('Сделано')
# except (ZeroDivisionError, NameError) as exe:
#     print(f'Нельзя делить на НОЛЬ ')
# else:
#     print(Если ошибок не было{exe.args})
# finally:
#     print('Выполнять всегда')

def add_everything_up(a, b):
    try:
        a + b
    except TypeError as exe:
        return str(a) + str(b)
    else:
        return a + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))