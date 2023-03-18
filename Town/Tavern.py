from email import utils


def tavern(summoner):
    print('\nYou enter the tavern. It is dimly lit and slimy.')
    print('You see several tables with people sitting at them. They all turn to look at you.')
    print('What would you like to do?')
    print('1. Talk to the bartender')
    print('2. Talk to the people at the tables')
    selection = input('Enter a number: ')
    selection = utils.valid_input(selection, ['1', '2'])
    if selection == '1':
        # order food or drink to heal health/mana
        summoner = bar(summoner)
    return summoner


def bar(summoner):
    print('\nYou sit down at the bar. The bartender asks you what you would like to order.')
    print('1. Food')
    print('2. Drink')
    selection = input('Enter a number: ')
    selection = utils.valid_input(selection, ['1', '2'])
    if selection == '1':
        # order food to heal health
        print('\nYou order some food.')
    elif selection == '2':
        # order drink to heal mana
        print('\nYou order some drink.')
    return summoner


def tables(summoner):
    print('\nYou sit down at a table. You see a group of people sitting at the table.')
    print('What would you like to do?')
    print('1. Talk to the group')
    print('2. Leave the table')
    selection = input('Enter a number: ')
    selection = utils.valid_input(selection, ['1', '2'])
    if selection == '1':
        # talk to the group
        print('\nYou sit down at the table and talk to the group.')
    elif selection == '2':
        # leave the table
        print('\nYou leave the table.')
    return summoner
