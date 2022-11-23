from random import *


class game:
    def __init__(self):
        self.player_name = input('Enter Name Please: ')
        self.__new_game()


    def __return_player_name(self):
        return self.player_name


    @staticmethod
    def __choice(num_choice):
        if num_choice == 0:
            return 'Rock'
        elif num_choice == 1:
            return 'Paper'
        else:
            return 'Scissors'


    def __new_game(self):
        no_of_rounds = 0

        print('\nWelcome To The Ultimate Rock, Paper, Scissors Game\n')

        print(f'This Match Is Between {self.__return_player_name} & La Máquina')
        print('------------------------------------------------------------------------------------------------------------')
        
        print('Rules:')
        print('\t1. Enter 0 For Rock, 1 For Paper, 2 For Scissor.')
        print('\t2. Take Fun Seriously. Entering Wrong Input Twice In A Single Game Will Result In An Instant Lose.')
        print("\t3. Relax Dude. It's Just A Game!")
        
        print('------------------------------------------------------------------------------------------------------------')
        
        print('\nNow! How Many Rounds Do You Want To Challenge The Machine For?\n')

        while(1):
            try:
                no_of_rounds = int(input('Enter Here: '))
            except ValueError:
                print('\nPlease Enter Valid Number Of Rounds\n')
            else:
                break

        print('------------------------------------------------------------------------------------------------------------')

        self.__in_match(no_of_rounds)


    def __in_match(self, no_of_rounds):
        no_of_rounds, prank_count, player_wins, computer_wins = 0, 0, 0
        playr_name = self.__return_player_name()

        for round in range(1, no_of_rounds + 1):
            computer_choice = randint(0, 2)

            print(f'\nRound {round}')
            print(f"------{'-' * round}-")
            print(f'\nLa Máquina Has Decided. Now You Decide {playr_name}!')

            while 1:
                try:
                    player_choice = int(input('Enter Your Choice: '))
                except ValueError:
                    prank_count += 1
                    print(f'You Now Have Only {2 - prank_count} Chances Left To Give Correct Input')
                else:
                    if player_choice < 0 or player_choice > 2:
                        prank_count += 1
                        print(f'You Now Have Only {2 - prank_count} Chances Left To Give Correct Input')
                        continue
                    if prank_count == 2:
                        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!YOU LOST DUDE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        return
                    break

            print(f'\n{playr_name} chose {self.__choice(player_choice)} & La Máquina chose {self.__choice(computer_choice)}\n')

            if (player_choice + 1) % 3 == computer_choice:
                print('La Máquina Wins')
                computer_wins = computer_wins + 1
            elif (computer_choice + 1) % 3 == player_choice:
                print(f'{playr_name} Wins')
                player_wins = player_wins + 1
            elif computer_choice == player_choice:
                print('\nIt Is A Tie. No Points Awarded.\n')

            if player_wins > (no_of_rounds / 2):
                print(f'\n{playr_name} Has Won Due To Technical Victory!!!!!!!! Hurray!!!!!!!!!!\n')
                return
            elif computer_wins > (no_of_rounds / 2):
                print(f'\nLa Máquina Has Won Due To Technical Victory!!!!!!!! Hurray!!!!!!!!!!\n')
                return

            print(f'\nCurrent Tally: La Máquina {computer_wins}, {playr_name} {player_wins}.\n')
            print('------------------------------------------------------------------------------------------------------------')

        if computer_wins > player_wins:
            print('\nLa Máquina Has Won!!!!\n')
        elif player_wins > computer_wins:
            print(f'\n{playr_name} Has Won!!!!\n')
        else:
            print('\nIt Is A Tie! Congratulations!! No One Wins!!')