import random as rnd

def guess(x):
    rand_num = rnd.randint(1, x)
    guess, chances = 0, 5

    while chances > 0:
        try:
            guess = int(input(f'Enter A Number Between 1 & {x}:\t'))
        except ValueError:
            print('\nEnter A Number')
        else:
            if chances == 0:
                print('You Lost!')
                break

            if guess < 1 or guess > x:
                print('\nEnter A Number Within The Given Range Please')
            elif guess == rand_num:
                print('\nCorrect!')
                break
            else:
                chances = chances - 1
                if chances == 0:
                    print('\nNo chances left! You Lost!\n')
                else:
                    print(f'\nIncorrect! {chances} chances left!')