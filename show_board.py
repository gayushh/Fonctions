import colored, random

def show_board(info_map):
    """
    This function display a view of the board.

    Parameters
    ----------
    info_map: data structure of the board (dict)

    Return
    --------
    board : the view of the board

    Version
    --------
    specification: Marie heneffe (v.1 13/03/2020)
    implementation : Marie Heneffe (v.1 17/03/2020)

    """

    board = '🌴' * (2 * info_map['nb_cols'] + 2) + '\n'

    for row in range(info_map['nb_rows']):
        board += '🌴'

        for col in range(info_map['nb_cols']):
            board += colored.bg(random.randint(17, 45))
            board += colored.fg(random.randint(208, 229))
            if (row, col) in info_map['hubs']:
                if info_map['hubs'][(row, col)] == 'hubs1':
                    board += '🏝'
                elif info_map['hubs'][(row, col)] == 'hubs2':
                    board += '🏝'
            else:
                board += '~'
                board += colored.attr('reset')

        board += '🌴\n'

    board += '🌴' * (2 * info_map['nb_cols'] + 2)

    return board

info_map = {'nb_rows':10, 'nb_cols':20, 'hubs':{(5, 5):'hubs1', (9, 6):'hubs2'}}

print(show_board(info_map))
