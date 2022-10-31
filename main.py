import random
from game_logic import get_winner_and_return_game_round

MIN_GAMES = 3

game_data = []

OPTIONS = ['PIEDRA', 'PAPEL', 'TIJERA']

phrases_welcome = ['\u00bfCrees poder ganarle al destino? ... Prob\u00e9moslo',
                   'El destino hoy no est\u00e1 de tu lado \u00bfo si?',
                   'No hay manera de ganarme, pero intentalo...',
                   'Hoy puedes perder todo lo que apuestes \u00bfAun as\u00ed quieres apostar?  ',
                   'Comprueba si hoy es tu d\u00eda de suerte']
phrases_option = ['\u00bfBuena elecci\u00f3n? Pronto lo sabremos',
                  'Tu respuesta fue r\u00e1pida \u00bfpero inteligente?',
                  '\u00bfSeguro que era la opci\u00f3n correcta?', 'zzzz eres muy lento para elegir',
                  'Sabia decisi\u00f3n, ahora estoy temblando', 'Jajaj\u00e1 debiste escoger la otra opci\u00f3n',
                  'Est\u00e1 bien, yo elegir\u00e9 la otra opci\u00f3n']
phrases_continue = ['Okay, okay, vamos de nuevo', 'Tienes otra oportunidad \u00bfla aprovechar\u00e1s?',
                    'De acuerdo, continuemos',
                    'Despu\u00e9s del resultado como te sientes \u00bfListo para la siguiente?',
                    'Estoy at\u00f3nito por saber que pasar\u00e1']
phrases_finished = ['De acuerdo, fue un placer jugar contigo', '\u00bfTe cansaste?, espero volver a jugar contigo',
                    'Solo los cobardes huyen del campo de batalla', 'Jugaste bien baquero',
                    'Bien hecho guerrero, el valhalla te espera']


def print_welcome():
    message_welcome = ' Bienvenido a Piedra Papel o Tijera '
    print(message_welcome.center(len(message_welcome) + 50, '='))
    print(random.choice(phrases_welcome))


def print_farewell():
    message_farewell = 'Juego terminado'
    print(random.choice(phrases_finished))
    print(message_farewell.center(len(message_farewell) + 50, '='))


def print_creation_information():
    by = ' Desarrollado por Jhon Camargo '
    print('\nGracias por jugar con nosotros')
    print()
    print(''.center(len(by) + 30, '*'))
    print(f'{by}'.center(len(by) + 30, '*'))
    print(''.center(len(by) + 30, '*'))


def print_game_data():
    total_game_wom = 0
    for data in game_data:
        print(f'Juego #{data["total_games"]}\n\tFigura jugador: {data["option_user"]}\n\tFigura computador: {data["option_computer"]}\n\tFigura ganadora: {data["winner"]}\n\t\u00bfQui\u00e9n gan\u00f3?: {data["round_winner"]}')
        if data["is_user_winner"]:
            total_game_wom += 1

    print(f'\nTotal juego ganados {total_game_wom}/{len(game_data)}')


def is_user_want_continue_playing(message):
    print(f'\n{message}')
    user_choice = input('Escriba "si" o "no": ').upper()
    if user_choice != "SI":
        return False
    return True


def game_reset():
    game_data.clear()


def get_option_user():
    random.shuffle(OPTIONS)
    print(f'\nElige una de las siguientes opciones: \n1. {OPTIONS[0]} \n2. {OPTIONS[1]} \n3. {OPTIONS[2]}')
    choice = input('\u00bfCúal es tu eleccion? ')

    if not choice.isnumeric() or not 0 < int(choice) <= 3:
        print('Parece que escogiste mal, por favor...')
        return get_option_user()

    choice = int(choice)

    if choice == 1:
        choice = OPTIONS[0]
    elif choice == 2:
        choice = OPTIONS[1]
    elif choice == 3:
        choice = OPTIONS[2]
    else:
        return get_option_user()

    print(random.choice(phrases_option))

    game_data.append(get_winner_and_return_game_round(option_user=choice, games_played=len(game_data)))


def game_reload():
    games_played = 0
    while games_played < MIN_GAMES:
        if games_played > 0:
            print(random.choice(phrases_continue))
        get_option_user()
        games_played += 1
    else:
        if is_user_want_continue_playing('\u00bfQuieres seguir jugando en esta misma partida?'):
            return game_reload()
        print_game_data()
        game_reset()


if __name__ == '__main__':
    print_welcome()
    game_reload()
    continue_playing = True
    while continue_playing:
        if not is_user_want_continue_playing('\u00bfQuieres jugar una nueva partida?'):
            print_creation_information()
            break
        game_reload()
