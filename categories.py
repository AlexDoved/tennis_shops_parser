from rackets import (get_rackets_third_size_racketlon, names_of_rackets,
                     links_to_rackets, prices_for_rackets)
from tables import save_to_table

save_result = (
    '--- DO YOU WANT TO SAVE THE RESULT IN '
    'AN EXCEL SPREADSHEET ? (y / any character to exit) ---\n'
)


def choose_a_store():
    """Выбор магазина."""
    input_var = input('Choose a store: ')
    if input_var == '1':
        print('1 - rackets |', '2 - clothing |', '3 - equipment')
        select_a_category()
    else:
        print('The parser for this store is not implemented.')
        choose_a_store()


def select_a_category():
    """Выбор категории."""
    input_var = input('Enter a category: ')
    if input_var == '1':
        print('1 - Wilson |', '2 - Babolat |', '3 - Head')
        choose_a_brand()
    else:
        print('The parser is not implemented for this category.')
        select_a_category()


def choose_a_brand():
    """Выбор бренда."""
    input_var = input('Choose a brand of rackets: ')
    if input_var == '1':
        get_rackets_third_size_racketlon(
            url='https://racketlon.ru/tennis/racket/wilson/?features_hash=51-6199',
            brand='WILSON'
        )
        if input(f'{save_result}') == 'y':
            print('The file was created successfully!')
            save_to_table('wilson', 'rackets', names_of_rackets,
                          links_to_rackets, prices_for_rackets)
        else:
            print('The program has finished working!')

    elif input_var == '2':
        get_rackets_third_size_racketlon(
            url='https://racketlon.ru/tennis/racket/babolat/?features_hash=51-6199',
            brand='BABOLAT'
        )
        if input(f'{save_result}') == 'y':
            print('The file was created successfully!')
            save_to_table('babolat', 'rackets', names_of_rackets,
                          links_to_rackets, prices_for_rackets)
        else:
            print('The program has finished working!')

    else:
        print('The parser for this brand is not implemented.')
        choose_a_brand()
