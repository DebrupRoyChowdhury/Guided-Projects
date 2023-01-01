from random import randint

class game:
    def __init__(self, temp_player_name = ''):
        self.set_player_name(temp_player_name)

        print('Do You Want Start A New Game?')
        choice = input('Enter Y For Yes: ')
        
        if choice in ('y', 'Y'):
            self.start_new_game()


    def set_player_name(self, temp_player_name = ''):
        if temp_player_name == '':
            self.__player_name = input('Enter Your Name Please: ')
            return
        
        self.__player_name = temp_player_name


    def return_player_name(self):
        return self.__player_name


    @staticmethod
    def __choice(num_choice):
        if num_choice == 0:
            return 'Rock'
        elif num_choice == 1:
            return 'Paper'
        elif num_choice == 2:
            return 'Scissors'


    def start_new_game(self):
        line_break = '-' * 110

        print(f'''\nWelcome To The Ultimate Rock, Paper, Scissors Game\n
        \nThis Match Is Between {self.__player_name} & La Máquina
        \n{line_break}')
        \nRules:')
        \n\t1. Enter 0 For Rock, 1 For Paper, 2 For Scissor.')
        \n\t2. Take Fun Seriously. Entering Wrong Input Twice In A Single Game Will Result In An Instant Lose.')
        \n\t3. Relax Dude. It's Just A Game!")
        \n{line_break}')
        \nNow! How Many Rounds Do You Want To Challenge La Máquina For?\n''')
        
        while True:
            try:
                self.no_of_rounds = int(input('Enter Here: '))
            except ValueError:
                print('\nPlease Enter Valid Number Of Rounds\n')
            else:
                break
                
        print(f'{line_break}')

        self.__match()


    def __match(self):
        self.__prank_count, self.__player_wins, self.__computer_wins = 0, 0, 0
        playr_name = self.return_player_name()

        for round in range(1, self.no_of_rounds + 1):
            computer_choice = randint(0, 2)
            value = self.__round(computer_choice, round)

            if value == 1:
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!YOU LOST DUDE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                return
            if value == 2:
                print(f'\n{playr_name} Has Won Due To Technical Victory!!!!!!!! Hurray!!!!!!!!!!\n')
                return
            if value == 3:
                print(f'\nLa Máquina Has Won Due To Technical Victory!!!!!!!! Hurray!!!!!!!!!!\n')
                return
    
        if self.__computer_wins > self.__player_wins:
            print('\nLa Máquina Has Won!!!!\n')
        elif self.__player_wins > self.__computer_wins:
            print(f'\n{playr_name} Has Won!!!!\n')
        else:
            print('\nIt Is A Tie! Congratulations!! No One Won!!')    


    def __round(self, computer_choice, round):
        playr_name = self.return_player_name()

        print(f'\nRound {round}')
        print(f"------{'-' * round}--")
        print(f'\nLa Máquina Has Decided. Now You Decide {playr_name}!')

        player_choice = self.__choice_of_player()

        if player_choice == 3:
            return 1
        
        print(f'\n{playr_name} chose {game.__choice(player_choice)} & La Máquina chose {game.__choice(computer_choice)}\n')

        self.__judge(player_choice, computer_choice)

        if self.__player_wins > (self.no_of_rounds / 2):
            return 2
        elif self.__computer_wins > (self.no_of_rounds / 2):
            return 3

        print(f'\nCurrent Tally: La Máquina - {self.__computer_wins}, {playr_name} - {self.__player_wins}.\n')
        print('------------------------------------------------------------------------------------------------------------')
        
        return 0


    def __choice_of_player(self):
        while 1:
            if self.__prank_count == 2:
                return 3

            try:
                player_choice = int(input('Enter Your Choice: '))            
            except ValueError:
                self.__prank_count += 1
                print(f'You Now Have Only {2 - self.__prank_count} Chances Left To Give Correct Input')
            else:
                if player_choice < 0 or player_choice > 2:
                    self.__prank_count += 1
                    print(f'You Now Have Only {2 - self.__prank_count} Chances Left To Give Correct Input')
                    continue
                
                return player_choice


    def __judge(self, player_choice, computer_choice):
        if (player_choice + 1) % 3 == computer_choice:
            print('La Máquina Wins')
            self.__computer_wins += 1

        elif (computer_choice + 1) % 3 == player_choice:
            print(f'{self.__player_name} Wins')
            self.__player_wins += 1

        elif computer_choice == player_choice:
            print('\nIt Is A Tie. No Points Awarded.\n')