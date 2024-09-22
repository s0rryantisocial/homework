first = input(print('Введите число:'))
second = input(print('Введите число:'))
third = input(print('Введите число:'))
if first == second and first == third and second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    first == second and not first == third and not second == third
    print('0')