def hangman(baseball):
    wrong_guesses = 0
    stages = ["", "________ ","|  |  ","|   ","| /|\ ","|    "]
    remaining_letters = list(word)
    letter_board = ['_']*len(word)
    win = False
    print ('Welcome to Hang Man')

while wrong_guesses < len(stages) -1:
    print('\n')
    guess = input("Guess a letter")
    if guess in remaining_letters:
        character_index = remaining_letters.index(guess)
        letter_board[character_index] = guess
        remaining_letters[character_index] = '$'
    else:
       wrong_guesses += 1
    print((' '.join(letter_board)))
    print('\n'.join(stages[0: wrong_guesses + 1]))
    if'_'not in letter_board:
        print('You win! The word was:')
        print(' '.join(letter_board))
        win= True
        break
    if not win:
        print ('\n'.join(stages[0: wrong_guesses]))
        print ('you lose! The words was {}'.format(word))

    hangman("baseball")
