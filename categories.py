from rackets import (get_rackets_third_size_racketlon, names_of_rackets,
                     links_to_rackets, prices_for_rackets)
from tables import save_to_table

save_result = ('--- ХОТИТЕ СОХРАНИТЬ РЕЗУЛЬТАТ В '
               'ТАБЛИЦУ EXCEL ? (y / любой символ для выхода) ---\n')


def choose_a_store():
    """Выбор магазина."""
    input_var = input('Выберите магазин: ')
    if input_var == '1':
        print('1 - ракетки |', '2 - одежда |', '3 - снаряжение')
        select_a_category()
    else:
        print('Парсер для данного магазина не реализован.')
        choose_a_store()


def select_a_category():
    """Выбор категории."""
    input_var = input('Введите номер категории: ')
    if input_var == '1':
        print('1 - Wilson |', '2 - Babolat |', '3 - Head')
        choose_a_brand()
    else:
        print('Парсер для данной категории не реализован.')
        select_a_category()


def choose_a_brand():
    """Выбор бренда."""
    input_var = input('Выберите бренд ракеток: ')
    if input_var == '1':
        get_rackets_third_size_racketlon(
            url='https://racketlon.ru/tennis/racket/wilson/?features_hash=51-6199',
            brand='WILSON'
        )
        if input(f'{save_result}') == 'y':
            print('Файл успешно создан!')
            save_to_table('wilson', 'rackets', names_of_rackets,
                          links_to_rackets, prices_for_rackets)
        else:
            print('Программа закончила работу!')

    elif input_var == '2':
        get_rackets_third_size_racketlon(
            url='https://racketlon.ru/tennis/racket/babolat/?features_hash=51-6199',
            brand='BABOLAT'
        )
        if input(f'{save_result}') == 'y':
            print('Файл успешно создан!')
            save_to_table('babolat', 'rackets', names_of_rackets,
                          links_to_rackets, prices_for_rackets)
        else:
            print('Программа закончила работу!')

    else:
        print('Парсер для данного бренда не реализован.')
        choose_a_brand()
