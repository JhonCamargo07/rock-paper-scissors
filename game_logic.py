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


def get_winner_and_return_game_round(option_user, games_played):
    game_data = {}
    winner = get_figure_random()
    option_computer = get_figure_random()

    game_data.setdefault('winner', winner)
    game_data.setdefault('option_user', option_user)
    game_data.setdefault('option_computer', option_computer)
    game_data.setdefault('total_games', games_played + 1)

    print(f'Yo escojo {option_computer} y t\u00fa escogiste {option_user}\n')
    print('Y el ganador es...')
    print(f' {winner} '.center(len(winner) + 14, '*'))

    if option_user == winner == option_computer:
        print(f'Ambos ganamos')
        game_data.setdefault('round_winner', 'Ambos ganaron (computador y jugador)')
        game_data.setdefault('is_user_winner', True)
    elif option_user == winner:
        print(f'Ganaste t\u00fa')
        game_data.setdefault('round_winner', 'Gan\u00f3 jugador (usted)')
        game_data.setdefault('is_user_winner', True)
    elif option_computer == winner:
        print(f'Gan\u00e9 yo (computador)')
        game_data.setdefault('round_winner', 'Gan\u00f3 el computador')
        game_data.setdefault('is_user_winner', False)
    else:
        print(f'En esta ocasion ninguno gana')
        game_data.setdefault('round_winner', 'Ninguno gan\u00f3')
        game_data.setdefault('is_user_winner', False)
    print()

    return game_data


if __name__ == '__main__':
    for data in range(10):
        get_winner_and_return_game_round('PAPEL')
