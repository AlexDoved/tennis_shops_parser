from categories import choose_a_store


def main():
    """Основная функция (точка входа)."""
    print('1 - Ракетлон |', '2 - OZON |', '3 - Спортмастер')
    choose_a_store()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print()
        print(f'Вы завершили выполнение программы!')
