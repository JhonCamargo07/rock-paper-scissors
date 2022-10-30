import random


def get_figure_random():
    NUM_MAX_RANDOM = random.randint(5, 20)

    figures = []

    for figure in range(NUM_MAX_RANDOM):
        figures.append('PAPEL')
        figures.append('TIJERA')
        figures.append('PIEDRA')
        random.shuffle(figures)

    random.shuffle(figures)
    return random.choice(figures)


def get_winner(option_user):
    winner = get_figure_random()
    option_computer = get_figure_random()

    print(f'Yo escojo {option_computer} y t\u00fa escogiste {option_user}\n')
    print('Y el ganador es...')
    print(f' {winner} '.center(len(winner) + 14, '*'))

    if option_user == winner == option_computer:
        print(f'Ambos ganamos')
    elif option_user == winner:
        print(f'Ganaste t\u00fa')
    elif option_computer == winner:
        print(f'Gan\u00e9 yo (computador)')
    else:
        print(f'En esta ocasion ninguno gana')
    print()


if __name__ == '__main__':
    for data in range(10):
        get_winner('PAPEL')
