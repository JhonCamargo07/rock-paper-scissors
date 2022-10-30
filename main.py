import random

MIN_GAMES = 3

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
    print()


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


def get_option_user():
    print(f'\nElige una de las siguientes opciones \n1. Piedra \n2. Papel \n3. Tijera')
    choice = input('¿Cúal es tu opcion? ')

    if not choice.isnumeric() or not 0 < int(choice) <= 3:
        print('Parece que escogiste mal, por favor...')
        return get_option_user()

    return choice


def is_user_want_continue_playing():
    print('\n¿Quieres jugar de nuevo?')
    user_choice = input('Escriba "si" o "no": ').upper()
    if user_choice != "SI":
        return False
    return True


def game_reload():
    games_played = 0
    while games_played < MIN_GAMES:
        if games_played > 0:
            print(random.choice(phrases_continue))
        get_option_user()
        games_played += 1


if __name__ == '__main__':
    print_welcome()
    game_reload()
    continue_playing = True
    while continue_playing:
        if not is_user_want_continue_playing():
            print_creation_information()
            break
        game_reload()
