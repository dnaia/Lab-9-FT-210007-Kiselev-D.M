import random
import logging

logging.basicConfig(level=logging.INFO, filename='logs_test22_Lab_9_FT_210007_Kiselev_D_M.txt', filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")

counter1 = 0  # Вспомогательный счетчик
while counter1 != 1:  # Проверка, чтобы ввели число.
    # | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        number = int(input('Введите положительное число, которое загадывает компьютер: '))
        logging.info('Вводят число, которое загадывает компьютер')
        while number <= 0:  # Проверка, чтобы ввели положительное число
            print("Введите положительное число!")
            logging.warning('Ввели число, меньшее единицы')
            number = int(input('Введите положительное число, которое загадывает компьютер: '))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
        logging.error('Ввели не число!')
    else:
        counter1 += 1
        logging.info('Ввели корректное число({})'.format(number))

counter2 = 0  # Вспомогательный счетчик
while counter2 != 1:  # Проверка, чтобы ввели число.
    # | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        attempt = int(input('Введите число попыток отгадать число: '))
        logging.info('Вводят число попыток, за которое пользователь может отгадать число')
        while attempt <= 0:  # Проверка, чтобы ввели положительное число
            print("Число попыток не может быть 0 или меньше нуля!")
            logging.warning('Ввели число, меньшее единицы')
            attempt = int(input('Введите число попыток отгадать число: '))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
        logging.error('Ввели не число!')
    else:
        counter2 += 1
        logging.info('Ввели корректное число попыток({})'.format(attempt))

i = 1  # Вспомогат данные(попытка)
while i != attempt + 1:  # Попытки отгадать число
    print('Попытка номер:', i)
    logging.info('Попытка отгадать число №({})'.format(i))
    counter3 = 0  # Вспомогательный счетчик
    while counter3 != 1:  # Проверка, чтобы ввели число.
        # | Диалоговый режим с пользователем и обработкой ошибок ввода
        try:
            answer = int(input('Как вы думаете, какое число загадал компьютер? '))
            logging.info('Вводят предполагаемое число, которое загадал компьютер')
        except ValueError:
            print('Вы ввели не число!\nПробуйте снова\n')
            logging.error('Ввели не число!')
        else:
            counter3 += 1
            logging.info('Ввели корректное предполагаемое число, которое загадал компьютер({})'.format(answer))

    if answer > number:  # Загаданное число меньше введенного значения
        print('Загаданное число меньше того, чем вы ввели!\n')
        logging.info('Предпологаемое число меньше числа, которое загадал компьютер')
    elif answer < number:  # Загаданное число больше введенного значения
        print('Загаданное число больше того, чем вы ввели!\n')
        logging.info('Предпологаемое число больше числа, которое загадал компьютер')
    elif answer == number:  # Загаданное число равно введенному значению
        logging.info('Предпологаемое число равно числу, которое загадал компьютер')
        print('Вы отгадали!\nКомпьютер загадал число:', number)
        break
    i += 1

if i == attempt + 1:
    print('Вы так и не отгадали число!\nКомпьютер загадал число:', number)
    logging.info('Загаданное число не было отгадано')
