import random
import time
from Summoner import Summoner
import yaml

from utils import clear_terminal, valid_input


def riddle_game(summoner):
    print(
        "You approach a dimly lit table where an enigmatic figure gestures you closer, a glint of mischief in their eyes."
    )
    time.sleep(3)
    print(
        "The enigmatic figure whispers, 'Invest some gold on a riddle; solve it to double your fortune. Are you game?'"
    )
    print("Your gold: " + str(summoner.gold))
    selection = input("\nType 'yes' or 'no': ")
    selection = valid_input(selection, ["yes", "no"])

    if selection == "yes":
        bet_amount = input("How much gold would you like to bet? (Max: 10 gold): ")
        bet_amount = valid_input(bet_amount, [str(i) for i in range(1, 11)])  # Validating the input to be in range 1-10
        bet_amount = int(bet_amount)

        if summoner.gold < bet_amount:
            clear_terminal()
            print("You don't have enough gold!")
            time.sleep(1)
            return

        summoner.gold -= bet_amount
        
        # Load riddles from the yaml file
        with open("Town/Tavern/riddles_past.yaml", 'r') as file:
            riddles = yaml.safe_load(file)

        print("\nAh, a brave soul! I shall weave you a riddle from the very fabric of ancient tales. Listen closely.\n")
        time.sleep(2)

        riddle_data = random.choice(riddles)
        riddle = riddle_data['riddle']
        answer = riddle_data['answer']

        print(riddle)
        tries = 3

        while tries > 0:
            guess = input(f"You have {tries} guesses left. Type your answer or 'give up': ").lower().strip()

            if " " + guess + " " in " " + answer.lower() + " ": 
                clear_terminal()
                print(f"\nImpressive! You've pierced the veil of the ancient enigma. As promised, here are your {bet_amount * 2} gold coins.\n")
                summoner.gold += bet_amount * 2  # Adding the reward to the summoner's gold
                time.sleep(3)
                return
            elif guess == "give up":
                print(f"\nChoosing to retreat? Until next time.\n")
                time.sleep(1)
                return
            else:
                tries -= 1
                if tries == 0:
                    break
                incorrect_responses = [
                    "Wrong guess, try again.",
                    "Not quite right, another attempt?",
                    "That's not it. Think deeper.",
                    "Missed the mark, adventurer.",
                    "Nope, give it another shot."
                ]
                chosen_response = random.choice(incorrect_responses)
                print("\n" + chosen_response + "\n")
                time.sleep(1)

        print(f"\nAlas, the riddle has bested you, brave traveler. The gold remains with me. \nPerhaps the fates will be kinder on your next encounter.\n")
        time.sleep(3)

    else:
        clear_terminal()
        print("\nYou walk away from the table, leaving the figure to their own devices.")
        time.sleep(1)
