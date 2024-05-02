from email import utils
from utils import print_slowly, valid_input

entry_message = ["As you step through the door of the tavern, the warm glow of the fire washes over you, chasing away the chill of the night air. The sound of raucous laughter and clinking tankards fills the air.",
"The smell of ale and roasting meat greets you as you enter the dimly lit tavern. The patrons are a mix of rough-looking adventurers and weary travelers, all seeking refuge from the dangers of the outside world.",
"The tavern is packed to the brim with patrons, their voices rising in a cacophony of sound that threatens to overwhelm you. The barkeep is a burly, bearded man who greets you with a nod and a gruff, 'What'll it be?'",
"The dimly lit tavern is filled with the sounds of clinking glasses and murmured conversations. A trio of minstrels play a lively tune in the corner, their instruments adding a touch of merriment to the otherwise dreary atmosphere.",
"The tavern is quiet when you enter, save for the soft sound of a lute being played in the corner. The barkeep is a kindly-looking man who nods at you with a smile and says, 'What can I get for you, friend?'"]

def tavern(summoner):
    print_slowly(entry_message[1], 200)
    print('\nWhat would you like to do?')
    print('\n1. Talk to the bartender')
    print('\n2. Talk to the people at the tables')
    selection = input('\nEnter a number: ')
    selection = valid_input(selection, ['1', '2'])
    if selection == '1':
        # order food or drink to heal health/mana
        summoner = bar(summoner)
    return summoner


def bar(summoner):
    print('\nYou sit down at the bar. The bartender asks you what you would like to order.')
    print('1. Food')
    print('2. Drink')
    selection = input('Enter a number: ')
    selection = valid_input(selection, ['1', '2'])
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
    selection = valid_input(selection, ['1', '2'])
    if selection == '1':
        # talk to the group
        print('\nYou sit down at the table and talk to the group.')
    elif selection == '2':
        # leave the table
        print('\nYou leave the table.')
    return summoner
