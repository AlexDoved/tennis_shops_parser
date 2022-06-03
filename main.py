from categories import choose_a_store


def main():
    """Основная функция (точка входа)."""
    print('1 - Racketlon |', '2 - OZON |', '3 - Sportmaster')
    choose_a_store()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print()
        print(f'You have completed the execution of the program!')
