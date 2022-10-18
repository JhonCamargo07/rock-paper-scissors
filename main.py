def print_message(turn):
    print(f'Jugador ${turn} Elige una de las siguientes opciones \n1. Piedra 2. Papel \n 3. Tijera')
    return int(input('¿Cúal es tu opcion? '))


def play(num_players, num):
    print_message(num)


NUM_MAX_PLAYERS = 7
NUM_MIN_PLAYERS = 2


def question():
    try:
        num_player = int(input('Cantidad de jugadores: '))
        if  NUM_MIN_PLAYERS <= num_player <= NUM_MAX_PLAYERS:
            contador = 0
            for num in range(num_player):
                contador += 1
                play(num_player, contador)
        else:
            print(f'Error, la cantidad de jugadores debe estar entre 2 y 7')
            question()
    except Exception as e:
        print(f'Error: ${e}')


if __name__ == '__main__':
    question()
