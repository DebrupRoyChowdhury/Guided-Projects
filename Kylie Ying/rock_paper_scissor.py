from random import *

class game:
    def __init__(self, player_name):
        self.player_name = player_name

    def return_player_name(self):
        return self.player_name

    def new_game(self):
        no_of_rounds, prank_count, player_wins, computer_wins = 0, 0, 0, 0
        playr_name = self.return_player_name()

        print('Welcome To The Ultimate Rock, Paper, Scissors Game')
        print(f'This Match Is Between {playr_name} & The Machine')
        print('--------------------------------------------------------')
        print('Rules')
        print('\t1. Enter 0 For Rock, 1 For Paper, 2 For Scissor.')
        print('\t2. Take Fun Seriously. Entering Wrong Input 2 Times In A Single Game Will Result In An Instant Lose.')
        print('\t3. Relax.')
        print('--------------------------------------------------------')
        print('\nNow How Many Rounds Do You Want To Challenge The Machine For?\n')

        while(1):
            try:
                no_of_rounds = int(input('Enter Here: '))
            except ValueError:
                print('\nPlease Enter Valid Number Of Rounds\n')

        for round in range(no_of_rounds):
            print(f'\nRound {round + 1}\n')

            computer_choice = randint(0, 2)

            print(f'Computer Has Chosen. Now Is Your Turn {playr_name}')
            while 1:
                try:
                    player_choice = int(input('Enter Your Choice: '))
                except ValueError:
                    prank_count = prank_count + 1
                    print(f'You Now Have Only {2 - prank_count} Chances Left To Give Correct Input')

                if prank_count == 2:
                    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!YOU LOST DUDE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    return

            if (player_choice + 1) % 3 == computer_choice:
                print('Computer Wins')
                computer_wins = computer_wins + 1

            if (computer_choice + 1) % 3 == player_choice:
                print(f'{playr_name} Wins')
                player_wins = player_wins + 1

            if computer_choice == player_choice:
                print('\nIt Is A Tie. No Paints Awarded.\n')

            if player_wins > (no_of_rounds / 2):
                print(f'\n{playr_name} Has Won Due To Technical Victory!!!!!!!! Hurray!!!!!!!!!!\n')
                return

            if computer_wins > (no_of_rounds / 2):
                print(f'\nComputer Has Won Due To Technical Victory!!!!!!!! Hurray!!!!!!!!!!\n')
                return

            print(f'\nCurrent Tally: Computer {computer_wins}, {playr_name} {player_wins}.\n')

        if computer_wins > player_wins:
            print('\nComputer Has Won!!!!\n')
        elif player_wins > computer_wins:
            print(f'\n{playr_name} Has Won!!!!\n')