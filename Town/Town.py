from utils import print_slowly, valid_input, clear_terminal
from .Tavern import tavern


def town(summoner, era):
    clear_terminal()
    if era == 'past':
        print_slowly('Welcome to the primitive town of the past!', 200)
    elif era == 'present':
        print('Welcome to the modern town of the present!')
    elif era == 'future':
        print('Welcome to the futuristic town of the future!')

    summoner = navigate(summoner)

    return summoner


def navigate(summoner):
    print_slowly('\nWhere would you like to go?', 200)
    print_slowly('\n1. Tavern', 300)
    print_slowly('\n2. Shop', 300)
    print_slowly('\n3. Inn', 300)
    print_slowly('\n4. Exit', 300)
    selection = input('Enter a number: ')
    selection = valid_input(selection, ['1', '2', '3', '4'])
    if selection == '1':
        summoner = tavern(summoner)
    elif selection == '2':
        # summoner = shop(summoner)
        return summoner
    elif selection == '3':
        # summoner = shopinn(summoner)
        return summoner
    return summoner
