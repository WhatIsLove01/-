import random

number = random.randrange(1,101)   
print('Добро пожаловать в числовую угадайку')

def is_valid(n):
    if n.isdigit():
        if 1 <= int(n) <= 100:
            return True
        else:
            return False
    else:
        return False

while True:
    num = input('Введите число от 1 до 100 - ')
    if not is_valid(num):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    num = int(num)

    if num > number:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif num < number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        break
print('Спасибо, что играли в числовую угадайку.')
    
